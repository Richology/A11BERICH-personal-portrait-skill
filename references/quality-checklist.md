# Quality checklist

Reject or rebuild any image that fails a critical identity or anatomy check.

## Identity and face

- Face matches real-photo truths, not an earlier AI image.
- Face reads immediately as A11BERICH rather than a generic similar East Asian man; compare the output side by side with the selected real truth at the same approximate angle.
- Eyebrow shape and spacing remain consistent.
- Mouth, lips, teeth, and smile remain plausible and identity-consistent.
- Chin and jawline are stable; no widening, shrinking, doubling, or carved edge.
- Reject a longer/narrower midface, hollow cheeks, deep-set eyes, narrower nose, thinner lips, longer/pointed chin, or older/gaunter appearance than the real truth.
- Short spiky black hair, hairline, and side length remain consistent.
- Retouching is light; skin retains natural texture without wax, relief, worm-like patterns, repeated pores, or smeared facial hair.

## Body and anatomy

- 180 cm / 75 kg lean-muscular proportions read naturally; head size, torso length, and limb length agree.
- Full-body outputs retain believable athletic shoulder width and head scale; do not inherit a slimmer target model's body.
- Shoulder line is continuous and anatomically plausible; no sloped, doubled, fused, or detached shoulder.
- Arms match the real muscularity without inflation, asymmetry, or broken elbows.
- Both hands are appropriate to the action; count fingers, inspect joints, nails, grip, and contact with props.
- Crops are intentional and do not accidentally amputate hands, fingers, feet, hair, or chin.

## Accessories and wardrobe

- Eyewear follows the selected mode or explicit request; both frames and lenses are symmetric, aligned, and transparent/tinted as specified.
- Necklace matches its reference and sits naturally around the neck; it does not fuse with skin or collar.
- Right-wrist bracelet and left-wrist silver square watch with black woven band are correct when visible.
- Clothing structure is coherent: collar, lapels, sleeves, seams, fasteners, hems, folds, and layers connect correctly.
- No abnormal fabric embossing, insect/worm patterns, melted texture, duplicate seams, fake logos, or accidental wardrobe carryover.

## Scene and delivery

- Background perspective, horizon, furniture, screens, and floor/wall junctions agree.
- The action belongs in the selected scene and does not repeat the same stock pose/expression across a series.
- Unrequested text, UI chrome, watermarks, logos, people, and background elements from references are absent.
- Requested text/logo is present only when authorized, spelled verbatim, and visually correct; otherwise omit it.
- Lighting direction, reflections, shadows, eyewear reflections, and subject/background color temperature agree.
- Output ratio and safe area suit avatar (`1:1`), vertical portrait/social (`3:4`), or horizontal key-visual (`16:9`) use; vertical output is natively `3:4`, never `9:16` or `4:5`.

## Edit stopping rule

If face, chin, hands, shoulders, or skin/clothing texture drifts, do not patch again. Return to the real identity truths and create a fresh generation. Never perform a second local edit on an AI-generated or already edited AI image.
