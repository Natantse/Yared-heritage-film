# Pipeline Architecture

## Overview
The project uses a Python pipeline controlled by a storyboard written in JSON.

## Pipeline Stages

1. **Storyboard:** `storyboard.json` contains the film scenes, narration, subtitles, and prompts.
2. **Validation:** `pipeline.py` checks the storyboard using `schema/storyboard.schema.json`.
3. **Keyframes:** Visual prompts are used to generate consistent scene images.
4. **Motion:** Keyframes are developed into moving video shots.
5. **Music:** An original score is created for the film.
6. **Narration:** Amharic narration is generated and checked.
7. **Assembly:** Video, narration, subtitles, and music are combined into final exports.

## Technical Design
- Python manages the pipeline.
- JSON stores the storyboard.
- JSON Schema checks the storyboard structure.
- FFmpeg is planned for video and audio assembly.
- Generated assets will be stored in the `outputs/` directory.

## Reproducibility
The pipeline will use documented settings and run logs. Generated assets and model parameters will be recorded so another person can understand how the film was produced.

## Current Implementation Status
The storyboard validation and shot-list printing are implemented. Media generation and final video assembly are planned but not yet implemented.
