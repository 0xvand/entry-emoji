import os

# The entry: one beach hut, U+1F6D6. Built from its codepoint so the bytes
# written are exact by construction: a single grapheme cluster, a single
# codepoint, 4 UTF-8 bytes and no variation selector or joiner, so it sits
# inside the gate's 1 to 8 characters however they are counted.
def entry_text() -> str:
    # One codepoint in, one grapheme out: chr() of U+1F6D6 encodes to
    # exactly the 4 UTF-8 bytes f0 9f 9b 96, with nothing around them.
    return chr(0x1F6D6)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
