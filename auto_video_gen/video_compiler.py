import os
from typing import List, Optional

# MoviePy reorganised modules in version 2+. Importing from ``moviepy.editor``
# no longer works, so import the classes/functions directly from ``moviepy``
from moviepy import (
    AudioFileClip,
    CompositeVideoClip,
    TextClip,
    VideoFileClip,
    concatenate_videoclips,
)


DEFAULT_SIZE = (1080, 1920)
FONT_SIZE = 70


def compile_video(video_paths: List[Optional[str]],
                  audio_path: str,
                  captions: List[str],
                  timestamps: List[tuple],
                  output_path: str = "final.mp4") -> str:
    """Compile gifs/clips, audio, and captions into a final video."""
    clips = []
    for path, (start, end), text in zip(video_paths, timestamps, captions):
        duration = end - start
        if path and os.path.exists(path):
            clip = VideoFileClip(path).subclip(0, min(duration, VideoFileClip(path).duration))
        else:
            clip = TextClip("", size=DEFAULT_SIZE, color="black", duration=duration)
        clip = clip.set_duration(duration).resize(height=DEFAULT_SIZE[1]).resize(width=DEFAULT_SIZE[0])

        caption = (TextClip(text, fontsize=FONT_SIZE, color="white", stroke_color="black", stroke_width=2)
                   .set_position("center")
                   .set_duration(duration))
        clips.append(CompositeVideoClip([clip, caption]))

    video = concatenate_videoclips(clips)
    audio = AudioFileClip(audio_path)
    final = video.set_audio(audio)
    final = final.set_fps(24)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
