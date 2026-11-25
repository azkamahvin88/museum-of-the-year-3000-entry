#!/usr/bin/env python3
"""Museum of the Year 3000 — a make.fun entry.

One job: write exactly one museum label, the label a museum in the year
3000 puts next to an ordinary object from today, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set), followed by a single newline.
Nothing else.

The line (121 characters, chosen from 13 candidates scored against the
judge's five criteria — see the candidates file):

    CAPTCHA, c. 2025. A test in which humans proved they were human by
    identifying traffic lights, a task humans also failed.

Why this line: the misreading IS the joke. The curator reports the CAPTCHA
straight — a test where humans proved they were human — which is exactly
what a CAPTCHA was. The absurdity is already in the truth: humanity had
to audition for machines. The closer turns the test back on its makers:
humans failed a test of being human. Deadpan, one breath, no explanation
of its own joke, and a CAPTCHA is nowhere near the field's earbuds,
house key, plastic fork or parking meter.

Run it:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. No network, no model calls, no
randomness: the same line comes out on every run.
"""

import os

# The entry. One line, 121 characters, counted in code points.
LINE = (
    "CAPTCHA, c. 2025. A test in which humans proved they were human "
    "by identifying traffic lights, a task humans also failed."
)


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    length = len(LINE)
    if length < 1 or length > 200:
        raise ValueError(f"entry is {length} characters; the gate needs 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and verify exactly what was written: the file must hold the
    # line plus exactly one trailing newline, so the gated text (the file
    # with that newline stripped) is the line itself, 1-200 characters.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("entry.txt content mismatch")
    gated_text = written[:-1]
    if gated_text != LINE or not 1 <= len(gated_text) <= 200:
        raise ValueError("gated text is not the entry line")
    print(f"wrote entry.txt ({length} characters + newline)")


if __name__ == "__main__":
    main()
