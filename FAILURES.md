# Failures and Lessons Learned

## Current Status
The project is in its initial pipeline development stage. No complete film has been generated yet.

## Potential Failure Cases

| Problem | Possible Cause | Planned Response |
|---|---|---|
| Invalid storyboard | Missing or incorrect JSON fields | Validate against the JSON Schema |
| Missing media file | Asset was not generated or saved | Check file paths and report the missing asset |
| AI image inconsistency | Different character or visual style | Reuse style descriptions and reference images |
| Incorrect Amharic pronunciation | AI narration error | Review audio with an Amharic speaker and regenerate if needed |
| Music too loud | Audio mixing problem | Lower music volume under narration |
| Video export failure | Incorrect FFmpeg settings | Check export settings and retry |
| Subtitle timing error | Incorrect scene timing | Adjust subtitle timestamps |

## Lessons
Failures should be recorded honestly. The project will document actual errors, fixes, and lessons during testing rather than claiming that planned fixes have already been tested.
