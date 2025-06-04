from typing import List, Tuple


def format_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace('.', ',')


def generate_srt(lines: List[str], timestamps: List[Tuple[float, float]], output_path: str = "captions.srt") -> str:
    """Generate an SRT caption file.

    Args:
        lines: Script lines.
        timestamps: List of (start, end) timestamps in seconds.
        output_path: Where to save the SRT file.
    Returns:
        Path to generated SRT file.
    """
    entries = []
    for i, (text, (start, end)) in enumerate(zip(lines, timestamps), 1):
        start_str = format_timestamp(start)
        end_str = format_timestamp(end)
        entries.append(f"{i}\n{start_str} --> {end_str}\n{text}\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(entries))

    return output_path
