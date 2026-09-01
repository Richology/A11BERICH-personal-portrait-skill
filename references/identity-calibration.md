# Identity calibration

Calibration measures whether the active real-photo identity set can reproduce A11BERICH at each angle. It does not manufacture new identity truth.

## Minimum angle-matched sets

| Task | Identity inputs |
| --- | --- |
| Front portrait | One high-confidence front real photo |
| Left/right 45° | One high-confidence front real photo + one real photo from the same 45° direction |
| Left/right 90° | One real photo from the same 90° direction + optional high-confidence front photo |
| Full body | One high-confidence face real photo + one high-confidence full-body real photo + the target reference |

Never load every identity image by default. Never substitute the opposite direction. A target reference supplies only labeled wardrobe, pose, scene, light, and composition; it supplies no identity, face, hair, body, eyewear, text, UI, logo, sign, plate, or bystander.

Each calibration angle starts fresh from matching-angle original photos. Do not rotate a front photo, edit a previous calibration output, or feed an AI calibration image into a later attempt. Save any generated calibration image as `ai_calibration_output` in a new version; it can expose a gap but cannot auto-promote to identity truth.

## Owner scoring

The owner scores each result from 0–10 after side-by-side comparison with the matching real photo.

| Check | What to compare |
| --- | --- |
| Face geometry | Face width/length and midface length |
| Eyes/brows | Eye distance, eye shape, brow thickness, arch, and spacing |
| Nose | Bridge width/height, tip, nostrils, and alar width |
| Mouth | Lip thickness, mouth width, corners, teeth, and smile behavior |
| Jaw | Chin length/width/projection and mandibular angle |
| Side landmarks | Ear size/position and cheek/jaw contour |
| Hair | Hairline, short spiky black top, and close-cut sides |
| Body | Head-to-shoulder ratio, shoulder width, 180 cm / 75 kg lean-athletic build, torso and true limb proportions |

Production thresholds:

- Front: owner score `>= 8`.
- Left45 and right45: each `>= 8`.
- Left90 and right90: each `>= 7`.
- Full-body proportions: `>= 8`.

An angle below its threshold, without a score, or without matching real coverage is not `stable_production`. Report it as pending or missing and request a sharp matching-angle original photo before likeness-critical production.

## Identity versioning

- The manifest names one active core identity version and retains prior versions for rollback.
- Random one-off defects do not change core identity. Promote a new version only after the same identity drift recurs across different scenes/outputs, the correction is supported by real photos, and the owner approves it.
- Record the evidence, affected traits, decision, date, and prior version. Never encode one failed AI face or one accidental expression as identity.

