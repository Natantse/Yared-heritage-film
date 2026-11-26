# ARCHITECTURE.md

# AI Film Production Architecture

## 1. Overview

The Saint Yared Heritage Short was created through a multi-stage AI-assisted production workflow.

The workflow combines research, script development, visual generation, narration, music generation, subtitles, and final video editing.

## 2. Production Pipeline

The production process follows these stages:

1. **Research and script:** Develop the story and narration about Saint Yared.
2. **Storyboarding:** Plan the sequence and purpose of each scene.
3. **Visual generation:** Create historical-style images and short video scenes using AI tools.
4. **Narration:** Generate Amharic narration using Microsoft Edge Text-to-Speech.
5. **Music generation:** Create an instrumental soundtrack using Meta MusicGen, guided by a begena-inspired prompt.
6. **Subtitles:** Prepare English subtitles in SRT format.
7. **Assembly:** Combine the scenes, narration, music, and subtitles using FFmpeg.
8. **Export:** Produce vertical and horizontal film versions and the radio cut.

## 3. Tools and Technologies

| Tool | Purpose |
|---|---|
| Gemini | Script and text assistance |
| FLUX.1 schnell | Historical-style portrait generation |
| Wan 2.1 T2V 1.3B GGUF | AI video scene generation |
| Microsoft Edge TTS | Amharic narration |
| Meta MusicGen | Instrumental music generation |
| FFmpeg | Audio and video processing |
| Python | Automation and media processing |
| Kaggle | GPU-based generation and editing |
| GitHub | Source code, documentation, and deliverables |

## 4. Media Organization

The production materials are organized into separate folders:

- `keyframes/` — generated reference images.
- `motion/` — generated video scenes.
- `music/` — soundtrack files.
- `narration/` — narration files.
- `subtitles/` — subtitle files.
- `exports/` — final video outputs.

## 5. Audio and Video Assembly

The final film combines the generated scenes with the Amharic narration and instrumental soundtrack.

The music is mixed beneath the narration so the spoken words remain clear.

English subtitles are added to improve accessibility for international viewers.

The project produces:
- A vertical short film.
- A horizontal short film.
- A radio cut with English subtitles on a black background.

## 6. Model and Workflow Limitations

The smaller Wan 2.1 model was selected because of available GPU memory and storage constraints.

AI-generated historical imagery is interpretive rather than documentary evidence.

MusicGen produces an AI-generated instrumental inspired by the begena; it does not guarantee an authentic traditional instrument recording.

Some production stages were completed manually in Kaggle rather than through a single automated command.

## 7. Reproducibility

The project uses Python scripts and documented production steps.

Generated media, model versions, prompts, and processing settings should be recorded where available so that the workflow can be reviewed and repeated.

## 8. Future Architecture Improvements

Future versions could include:
- A fully automated end-to-end pipeline.
- Automatic subtitle alignment using speech recognition.
- More systematic logging of model parameters and execution time.
- Automated output validation.
- Improved caching and recovery after failed generation stages.
