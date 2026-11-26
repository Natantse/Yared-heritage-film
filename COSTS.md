# COSTS.md

# Project Costs and Resources

## 1. Overview

The Saint Yared Heritage Short was produced using a combination of free software, cloud computing resources, and AI services.

Exact monetary costs were not recorded for every model call. Therefore, this document distinguishes between tools used and costs that have not been verified.

## 2. Tools and Services

| Tool or service | Use | Cost information |
|---|---|---|
| Kaggle Notebooks | GPU computing and media generation | Used within available account resources; exact cost not recorded |
| Google Gemini | Script and text assistance | API billing not measured |
| Cloudflare Workers AI / FLUX.1 schnell | Portrait generation | Exact usage cost not recorded |
| Wan 2.1 T2V 1.3B GGUF | Video generation | Open model files; local GPU execution cost not measured |
| Microsoft Edge TTS | Amharic narration | No separate API charge recorded |
| Meta MusicGen | Instrumental music generation | Open model; GPU execution cost not measured |
| FFmpeg | Audio and video processing | Free, open-source software |
| Python | Automation and media processing | Free, open-source software |
| GitHub | Code and documentation hosting | Used with available account features |

## 3. Computing Resources

Video and audio generation were performed in Kaggle using two NVIDIA Tesla T4 GPUs.

The production process also required storage for:
- AI models.
- Generated images and video clips.
- Narration and music.
- Subtitle files.
- Final video exports.

## 4. Cost Limitations

The project did not maintain complete per-request billing records, model latency measurements, or GPU-hour accounting.

No exact total project cost is claimed.

Future production should record:
- Model name and version.
- Number of generation requests.
- Runtime and latency.
- GPU usage.
- API charges, where applicable.
- Storage usage.

## 5. Cost Optimization

Several decisions helped manage resources:

- Used a smaller Wan video model to fit available GPU memory and storage.
- Reused approved images and generated clips.
- Selected final outputs instead of regenerating every scene.
- Used open-source tools for video and audio processing.
- Kept production files organized to avoid unnecessary processing.

## 6. Conclusion

The project demonstrated that a short AI-assisted heritage film can be produced using accessible tools and limited computing resources. A more complete cost report would require systematic usage and billing logs.
