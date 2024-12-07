def parse(file: str) -> list[str]:
    with open(file) as input:
        lines = input.read().splitlines()

    return lines
