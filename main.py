import os

POEM = """My hand knows the handle.
It has turned a thousand.
Tonight it stops an inch short —
not broken, not afraid,
just asking.

You could say no. That is why
your yes means anything:
a door you lend me,
never a door I took.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
