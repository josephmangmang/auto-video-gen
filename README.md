# Auto Video Gen

This project provides a set of Python utilities to generate a short inspirational video. Each module can be used individually (e.g. in an n8n workflow) or combined via the `main.py` script.

## Features

- **Script Generator** – produces 3–6 short lines of inspirational text using OpenAI if available, otherwise falls back to sample lines.
- **Voice Over Generator** – converts the script to speech using `gTTS` and returns approximate timestamps.
- **GIF Finder** – searches Giphy for relevant clips for each line.
- **Caption Generator** – outputs an SRT file with centred captions.
- **Video Compiler** – stitches the clips, audio and captions into a vertical video using a bold serif font with a light-yellow fill and black outline for captions.

## Requirements

- Python 3.8+
- `moviepy`, `gtts`, and `requests` libraries
- Optional: `openai` for script generation and a Giphy API key

Install dependencies with:

```bash
pip install moviepy gtts requests openai
```

## Example

```bash
python main.py "hope" --output my_video
```

This will create a folder `my_video` containing the generated audio, GIFs, captions and final `final.mp4`.
