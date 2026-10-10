from csv import writer
from datetime import date, timedelta
from math import sin
from pathlib import Path


def main() -> None:
    output = Path("data/sample/prices.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as handle:
        rows = writer(handle)
        rows.writerow(["date", "open", "high", "low", "close", "volume"])
        start = date(2024, 1, 1)
        for index in range(80):
            close = 100 + 2 * sin(index / 4) + 0.03 * index
            rows.writerow(
                [
                    start + timedelta(days=index),
                    close,
                    close + 1,
                    close - 1,
                    close,
                    1000 + index,
                ]
            )


if __name__ == "__main__":
    main()
