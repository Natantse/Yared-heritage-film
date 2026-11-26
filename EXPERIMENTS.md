# EXPERIMENTS.md

# Production Experiments and Findings

This document records experiments conducted while producing the Saint Yared Heritage Short.

The results below reflect the production decisions and feedback observed during development.

## Experiment 1 — Visual Realism

**Hypothesis:** A photorealistic historical style would create a stronger sense of authenticity.

**Change:** Used AI-generated cinematic historical imagery rather than cartoon-style visuals.

**Result:** The more realistic visual direction was preferred.

## Experiment 2 — Character Consistency

**Hypothesis:** Using a consistent reference portrait would improve continuity.

**Change:** Created an approved reference portrait of Saint Yared and used it to guide the visual design.

**Result:** The portrait provided a consistent visual reference, although generated scenes did not always preserve every detail.

## Experiment 3 — Video Model Selection

**Hypothesis:** A smaller video-generation model could produce usable scenes within the available GPU resources.

**Change:** Used Wan 2.1 T2V 1.3B GGUF.

**Result:** The model generated short scenes within the available hardware constraints. Some results required additional review and selection.

## Experiment 4 — Scene Duration

**Hypothesis:** Short scenes would make the film easier to assemble and keep visually engaging.

**Change:** Generated short clips of approximately three to four seconds.

**Result:** The clips were suitable for a short cinematic sequence.

## Experiment 5 — Narration Voice

**Hypothesis:** A deeper, slower Amharic voice would better suit the historical subject.

**Change:** Tested voice speed, pitch, and volume using Microsoft Edge TTS.

**Result:** The selected voice used a lower pitch and slower delivery.

## Experiment 6 — Narration Pacing

**Hypothesis:** Adjusting pauses and phrase delivery would make the narration more natural.

**Change:** Revised the ending delivery, including the questioning tone of "ያ ሰው?" and the final phrase.

**Result:** The revised delivery was preferred during listening review.

## Experiment 7 — Instrumental Music

**Hypothesis:** A begena-inspired instrumental would support the Ethiopian heritage theme.

**Change:** Tested different MusicGen prompts and instrumental directions.

**Result:** The selected version used a deep, solemn begena-inspired sound. Other added instruments and choir elements were rejected.

## Experiment 8 — Music and Narration Balance

**Hypothesis:** Lower background music would make the narration easier to understand.

**Change:** Mixed the soundtrack beneath the spoken narration.

**Result:** The narration remained the primary audio focus.

## Experiment 9 — Subtitle Presentation

**Hypothesis:** Smaller, two-line English subtitles would be easier to read.

**Change:** Revised subtitle size and line breaks.

**Result:** A smaller subtitle style was selected for the film.

## Experiment 10 — Export and Video Formats

**Hypothesis:** Separate vertical and horizontal exports would support different viewing platforms.

**Change:** Created vertical and horizontal video versions and checked their resolution and audio streams.

**Result:** Both formats were exported successfully. An additional subtitle-only radio cut was also created.

## Lessons Learned

- Visual consistency requires careful review of generated scenes.
- Audio quality and narration pacing are essential to storytelling.
- Smaller models can be useful when hardware resources are limited.
- Subtitle timing and readability need manual checking.
- Testing different prompts is important when generating music.
- Exported videos should be checked for both video and audio streams.

## Limitations

These experiments were qualitative production tests, not controlled scientific experiments. Numerical performance measurements and audience-test results were not collected for every experiment.
