# Likeness troubleshooting

Diagnose first. Do not generate or edit until the mismatch class and the matching real truth are identified.

## One-off rendering defects

Examples: one malformed finger, one wrong button, a broken seam, or an isolated fabric pattern. If identity, pose, and scene are otherwise correct, one local repaint is allowed. List all invariants first. Do not add the defect to the core identity profile.

## Repeated identity drift

Examples recurring across different scenes: long/narrow face, pointed chin, hollow/deep-set eyes, overly narrow nose, thin lips, undersized head, narrow or inward-rolled shoulders. Compare multiple failures with matching real photos. Only repeated, cross-scene evidence may trigger an identity-constraint update and version proposal.

## Angle failure

If one angle repeatedly looks wrong, check manifest coverage and owner scores. Ask for a sharp original photo from that exact direction when coverage is missing, partial, or below threshold. Do not compensate by loading many mismatched photos, using the opposite side, rotating a front photo, or letting AI guess.

## Stopping rules

- Never make a failed AI output an identity source.
- Never chain calibration outputs or perform a second local edit on an already edited AI image.
- Never freeze a single expression, bad hand, button, wrinkle, or other accidental artifact into permanent identity.
- Rebuild from the original target and angle-matched real truth after face, chin, hair, shoulder, or body drift.

