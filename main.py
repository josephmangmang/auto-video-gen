"""Example command-line utility to generate a short inspirational video."""
import argparse
import os
from pathlib import Path
from typing import List

from auto_video_gen import (
    compile_video,
    find_gifs,
    generate_script,
    generate_srt,
    generate_voice_over,
)


def run(topic: str, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)

    lines = generate_script(topic)
    audio_path, timestamps = generate_voice_over(lines, os.path.join(output_dir, "voice.mp3"))
    gif_urls = find_gifs(lines)

    gif_paths: List[str] = []
    for i, url in enumerate(gif_urls):
        if not url:
            gif_paths.append(None)
            continue
        path = os.path.join(output_dir, f"gif_{i}.mp4")
        try:
            import requests

            r = requests.get(url, timeout=10)
            with open(path, "wb") as f:
                f.write(r.content)
            gif_paths.append(path)
        except Exception:
            gif_paths.append(None)

    srt_path = generate_srt(lines, timestamps, os.path.join(output_dir, "captions.srt"))
    final_video = compile_video(gif_paths, audio_path, lines, timestamps, os.path.join(output_dir, "final.mp4"))
    return {
        "script": lines,
        "audio": audio_path,
        "gifs": gif_paths,
        "srt": srt_path,
        "video": final_video,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an inspirational short video")
    parser.add_argument("topic", help="Topic or keyword")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()
    result = run(args.topic, args.output)
    print(result)
