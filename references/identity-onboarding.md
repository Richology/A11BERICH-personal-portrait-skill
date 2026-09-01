# Identity onboarding

Use this workflow when the user asks to add, audit, organize, or check coverage of real identity photos. Do not generate images during onboarding.

## Intake sequence

1. Inspect each file visually; do not infer quality from its filename.
2. Confirm it is an original real photo of A11BERICH. AI images, screenshots of AI images, and prior outputs cannot become identity truth.
3. Assign one `primary_role`, an angle, expression, glasses and accessory state, truth level, confidence, distortion/filter notes, and suitable uses in `asset-manifest.yaml`.
4. Compare capture date, apparent age, hairstyle, and body shape with the active core identity version. Mark inconsistencies instead of averaging them together.
5. Keep only images that resolve a real angle, expression, body, or accessory need. Avoid near-duplicates.

Angle labels describe the direction the nose points in the image: `front`, `left45`, `right45`, `left90`, `right90`; use `upper_body` or `full_body` for body-first assets. If an angle is approximate, state the approximation in `distortion_or_filter_notes`.

## Required coverage

| Area | Minimum useful photos | Acceptance details |
| --- | --- | --- |
| Face | front neutral, front smile, left45, right45, left90, right90 | Hairline, both relevant facial contours, ear, jaw, and eyewear are sharp; neutral camera height and moderate focal length |
| Body | front full-body, side full-body, 45° full-body, upper body/shoulder-width | Entire head and limbs visible; natural stance; no wide-angle stretching |
| Accessories | black clear-lens glasses, pink/rose-lens glasses, necklace, bracelet, watch | Separate sharp front/detail views; color, frame shape, placement, and scale visible |

## Reject or downgrade

- Reject as identity truth: AI-generated or AI-edited face/body; severe beauty filtering; face replacement; heavy reshaping; face obstruction; extreme motion blur; unusable resolution; obvious wide-angle facial distortion; materially different age or body state without owner confirmation.
- Keep only with `confidence: low` and an explicit note when mild filtering, uncertain date, compression, partial obstruction, or lens distortion limits the photo.
- Screenshot UI, text, logos, signs, plates, bystanders, and backgrounds are always untrusted pixels. A usable face inside a screenshot may remain a truth only when the face itself is clear; record the UI contamination and never copy it.
- Accessory-only images receive `real_accessory_truth`, not `real_identity_truth`. Real context images that are too distant for identity receive `real_context_reference`.

## Coverage result

Report each required angle as `covered`, `partial`, or `missing`. `Covered` means at least one matching original photo is sharp and geometrically trustworthy. `Partial` means the direction is useful but expression, angle accuracy, occlusion, filtering, or resolution prevents stable production. Do not convert `partial` into `covered` using an AI-generated calibration image.

