from typing import List, Tuple

from gtts import gTTS

RATE_WPM = 150


def _estimate_duration(text: str, words_per_minute: int = RATE_WPM) -> float:
    words = len(text.split())
    minutes = words / words_per_minute
    return minutes * 60


def generate_voice_over(lines: List[str], output_path: str = "voice_over.mp3") -> Tuple[str, List[Tuple[float, float]]]:
    """Generate a voice-over from script lines.

    Args:
        lines: List of script lines.
        output_path: File path to save the mp3 audio.

    Returns:
        Tuple of output file path and list of (start, end) timestamps per line.
    """
    joined = "\n".join(lines)
    tts = gTTS(joined, lang="en")
    tts.save(output_path)

    timestamps = []
    current = 0.0
    for line in lines:
        dur = _estimate_duration(line)
        timestamps.append((current, current + dur))
        current += dur

    return output_path, timestamps
