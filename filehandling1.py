from pathlib import Path


def read_file(path: Path) -> str:
    """Read and return the contents of a text file."""
    with path.open('r', encoding='utf-8') as file:
        return file.read()


def append_line(path: Path, text: str) -> None:
    """Append a single line of text to a file."""
    with path.open('a', encoding='utf-8') as file:
        file.write(text + '\n')


def main() -> None:
    file_path = Path(r"C:\Users\SANJIV NEUPANE\Downloads\pyfile.txt")

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    print("Original file contents:")
    print(read_file(file_path))

    append_line(file_path, "I study in Asian school of management and technology")

    print("\nUpdated file contents:")
    print(read_file(file_path))


if __name__ == '__main__':
    main()
