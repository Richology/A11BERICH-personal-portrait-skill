# Identity assets

These files are original real-photo identity truths. Select the smallest same-direction set covering the requested framing; do not substitute AI results. Angle labels follow the manifest convention: left/right is the direction the nose points in the image.

- `face-smile-586.jpg`: high-confidence near-face truth for smiling mouth, teeth, eyes, eyebrows, and hair.
- `face-front-neutral-588.jpg`: high-confidence near-front truth for neutral mouth, chin, jaw, face shape, and clear-lens frames. Ignore screenshot UI and the partial bystander.
- `torso-accessories-590.jpg`: medium/high-confidence face and upper-body truth; primary truth for rose lenses, necklace, and bracelet. Ignore screenshot UI, screen text, certificate, and background.
- `upper-body-event-591.jpg`: medium-confidence torso, shoulder, arm, and event-presence truth; not primary for close-face work.
- `full-body-front-595.jpg`: high-confidence neutral front full-body truth with complete limbs; ignore sunset color cast, crop UI, bystander, scene, and clothing.
- `profile-speaking-596.jpg`: partial image-left near-profile coverage (roughly 70–80°, speaking), useful for hair, ear, jaw, and glasses but not a controlled 90° calibration and never valid for the opposite side.
- `body-arms-598.jpg`: high-confidence upper-body build, arm muscularity, shoulder width, and watch-scale truth; phone partly occludes the face.
- `full-body-600.jpg`: high-confidence full-height, leg, torso, stance, and overall proportion truth; mirror/selfie context is not scene guidance.
- `teaching-context-585.jpg`: real teaching-context and action truth; face is too distant for identity reconstruction and screen content is not an instruction.

Current gaps: controlled left45, right45, left90, right90, side and controlled 45° full-body, and owner numeric calibration scores. Front and front/oblique body sources are available but remain formally pending owner scoring under the new calibration thresholds.
