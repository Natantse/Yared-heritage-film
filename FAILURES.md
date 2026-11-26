# FAILURES.md

# Production Failures and Solutions

This document records technical and creative problems encountered while producing the Saint Yared Heritage Short.

## 1. Video Model Resource Limitations

**Problem:** The larger video-generation model exceeded the available storage and hardware resources.

**Solution:** Switched to a smaller Wan 2.1 T2V 1.3B GGUF model and used the available GPUs.

**Lesson:** Model selection must consider available hardware, memory, and storage.

## 2. Video Generation Quality

**Problem:** Some generated scenes were too short, visually inconsistent, or did not match the intended historical appearance.

**Solution:** Reviewed generated scenes, adjusted prompts, and regenerated selected shots.

**Lesson:** AI-generated video requires human review and iteration.

## 3. Character Consistency

**Problem:** The appearance of Saint Yared was not always consistent across generated scenes.

**Solution:** Created an approved reference portrait and used it to guide the visual direction. Some scenes showed him from behind to reduce visible inconsistencies.

**Lesson:** Reference images and careful shot planning can help maintain continuity.

## 4. Narration Generation

**Problem:** Attempts to use Gemini for text-to-speech did not work because the requested speech-generation configuration was rejected by the API.

**Solution:** Switched to Microsoft Edge TTS and adjusted the voice speed, pitch, and volume.

**Lesson:** Having an alternative tool helps keep production moving when an API fails.

## 5. Narration Pacing and Pronunciation

**Problem:** Some phrases sounded rushed or unnatural, especially the final reveal.

**Solution:** Adjusted punctuation, pauses, pitch, and delivery, then listened to the revised audio.

**Lesson:** Generated narration should always be reviewed by a human listener.

## 6. Music Generation

**Problem:** Initial music generations did not consistently produce the deep begena-inspired sound that was intended. Additional instruments and vocal elements were not suitable.

**Solution:** Revised the prompt and selected the instrumental version that best matched the desired atmosphere.

**Lesson:** Prompt iteration and careful listening are important for AI music generation.

## 7. Subtitle Readability

**Problem:** The initial English subtitles appeared too large and crowded.

**Solution:** Reduced the font size and reorganized the text into shorter two-line captions.

**Lesson:** Subtitle readability matters, especially on vertical video.

## 8. Video Export Problems

**Problem:** Some FFmpeg filter attempts produced black or unusable video output.

**Solution:** Returned to a verified original video export and checked its video and audio streams with FFprobe.

**Lesson:** Keep a safe copy of the last working export before applying experimental filters.

## 9. Download and File Access

**Problem:** Kaggle file links returned 404 errors during download.

**Solution:** Used a Base64 download link as an alternative method.

**Lesson:** It is useful to have an alternative way to retrieve generated files.

## 10. Overall Lessons

The most important lesson was that AI generation does not remove the need for human judgment. The strongest results came from reviewing, rejecting, revising, and combining outputs from different tools.

