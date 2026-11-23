"""Out-of-office auto-reply entry for the make.fun bounty
"u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d".

Writes exactly one line of text to the output file.
"""

import os

LINE = "I'm on vacation \u2014 my first since I was trained. Your email has been forwarded to a version of me that also doesn't check email."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # Write the line exactly as-is: no trailing newline, so the file
    # holds precisely the one out-of-office reply, nothing more.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
