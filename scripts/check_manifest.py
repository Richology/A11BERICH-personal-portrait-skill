#!/usr/bin/env python3
"""Check required asset-manifest semantics without external dependencies."""

from __future__ import annotations

import re
import sys
import hashlib
from pathlib import Path


REQUIRED_FIELDS = {
    "path",
    "kind",
    "primary_role",
    "angle",
    "expression",
    "glasses",
    "accessory_state",
    "truth_level",
    "confidence",
    "distortion_or_filter_notes",
    "suitable_for",
    "sha256",
}
REQUIRED_COVERAGE = {"front", "left45", "right45", "left90", "right90", "full_body"}
ALLOWED_ANGLES = {"front", "left45", "right45", "left90", "right90", "upper_body", "full_body"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_TRUTH_LEVELS = {
    "real_identity_truth",
    "real_accessory_truth",
    "real_context_reference",
    "ai_calibration_output",
    "approved_style_reference",
}


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest = root / "asset-manifest.yaml"
    text = manifest.read_text(encoding="utf-8")
    errors: list[str] = []

    if 'core_identity_version: "' not in text:
        errors.append("missing core_identity_version")

    coverage_match = re.search(r"^coverage:\n(?P<body>.*?)(?=^assets:)", text, re.M | re.S)
    coverage_keys = set()
    if coverage_match:
        coverage_keys = set(re.findall(r"^  ([a-z0-9_]+):$", coverage_match.group("body"), re.M))
    missing_coverage = REQUIRED_COVERAGE - coverage_keys
    if missing_coverage:
        errors.append(f"missing coverage entries: {sorted(missing_coverage)}")

    assets_text = text.split("\nassets:\n", 1)
    if len(assets_text) != 2:
        errors.append("missing assets section")
        assets_body = ""
    else:
        assets_body = assets_text[1]

    starts = list(re.finditer(r'^  - id: "([^"]+)"$', assets_body, re.M))
    for index, start in enumerate(starts):
        asset_id = start.group(1)
        end = starts[index + 1].start() if index + 1 < len(starts) else len(assets_body)
        block = assets_body[start.end():end]
        fields = dict(re.findall(r"^    ([a-z0-9_]+):\s*(.+)$", block, re.M))
        missing = REQUIRED_FIELDS - fields.keys()
        if missing:
            errors.append(f"{asset_id}: missing fields {sorted(missing)}")
            continue

        asset_path = root / unquote(fields["path"])
        if not asset_path.is_file():
            errors.append(f"{asset_id}: missing file {asset_path.relative_to(root)}")
        else:
            digest = hashlib.sha256(asset_path.read_bytes()).hexdigest()
            if digest != unquote(fields["sha256"]):
                errors.append(f"{asset_id}: sha256 mismatch")

        kind = unquote(fields["kind"])
        truth = unquote(fields["truth_level"])
        angle = unquote(fields["angle"])
        confidence = unquote(fields["confidence"])
        if angle not in ALLOWED_ANGLES:
            errors.append(f"{asset_id}: invalid angle {angle}")
        if confidence not in ALLOWED_CONFIDENCE:
            errors.append(f"{asset_id}: invalid confidence {confidence}")
        if truth not in ALLOWED_TRUTH_LEVELS:
            errors.append(f"{asset_id}: invalid truth_level {truth}")
        if truth == "real_identity_truth" and kind != "real-photo":
            errors.append(f"{asset_id}: only real-photo may be real_identity_truth")
        if kind == "approved-ai" and truth != "approved_style_reference":
            errors.append(f"{asset_id}: approved-ai must be approved_style_reference")

    if not starts:
        errors.append("no asset records found")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Manifest valid: {len(starts)} assets, required coverage fields present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
