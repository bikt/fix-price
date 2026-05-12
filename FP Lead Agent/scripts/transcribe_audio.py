from __future__ import annotations

import argparse
import json
from pathlib import Path

from faster_whisper import WhisperModel


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_path")
    parser.add_argument("--model", default="small")
    parser.add_argument("--language", default="ru")
    parser.add_argument("--output-dir", default="transcripts")
    args = parser.parse_args()

    audio_path = Path(args.audio_path)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(audio_path),
        language=args.language,
        vad_filter=True,
        beam_size=5,
    )

    collected = []
    text_parts = []

    for segment in segments:
        text = segment.text.strip()
        if not text:
            continue
        collected.append(
            {
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": text,
            }
        )
        text_parts.append(text)

    stem = audio_path.stem
    txt_path = output_dir / f"{stem}.txt"
    json_path = output_dir / f"{stem}.json"

    txt_path.write_text("\n".join(text_parts), encoding="utf-8")
    json_path.write_text(
        json.dumps(
            {
                "audio": str(audio_path),
                "language": info.language,
                "language_probability": info.language_probability,
                "duration": info.duration,
                "segments": collected,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"TXT={txt_path}")
    print(f"JSON={json_path}")
    print(f"LANG={info.language}")
    print(f"PROB={info.language_probability:.4f}")
    print(f"DURATION={info.duration:.2f}")
    print("---TRANSCRIPT---")
    print("\n".join(text_parts))


if __name__ == "__main__":
    main()
