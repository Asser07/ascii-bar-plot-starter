# Hints – ASCII horizontal bar chart

Nutze diese Datei nur, wenn ihr weitere Tipps braucht. Der Schwerpunkt des
Praktikums ist **Projektstruktur, Environment, Dependencies, Imports und Git/GitHub**.
Der Plot selbst soll bewusst überschaubar bleiben.

## 1. Zielstruktur

```text
.
├── .gitignore
├── pyproject.toml
├── uv.lock
├── data/
│   └── points.csv
└── src/
    └── ascii_barchart/
        ├── __init__.py
        ├── io.py
        ├── analysis.py
        ├── chart.py
        └── cli.py
```

## 2. uv-Projekt

Im Repository-Root im VS-Code-Terminal:

```bash
uv init --lib --name ascii-barchart
uv venv
uv add rich
```

Danach in VS Code ggf. `Ctrl/Cmd+Shift+P` → **Python: Select Interpreter** →
Interpreter aus `.venv` auswählen.

## 3. Minimale `.gitignore`

```gitignore
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.DS_Store
```

## 4. CSV laden – `io.py`

```python
import csv
import os


def load_rows(csv_path):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(csv_path)

    rows = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(
                (
                    row["type"],
                    float(row["value1"]),
                    float(row["value2"]),
                )
            )

    return rows
```

## 5. Mittelwerte – `analysis.py`

```python
def average_value1_by_type(rows):
    sums = {}
    counts = {}

    for point_type, value1, _value2 in rows:
        sums[point_type] = sums.get(point_type, 0.0) + value1
        counts[point_type] = counts.get(point_type, 0) + 1

    result = []
    for point_type in sorted(sums):
        average = sums[point_type] / counts[point_type]
        result.append((... add your code ...))

    return result
```

## 6. Balkenlänge

Der größte Mittelwert soll einen Balken mit `width` Zeichen bekommen.

```python
def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return ... add your code ...
```

## 7. Rich-Grundidee – `chart.py`

```python
from rich.console import Console
from rich.text import Text

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}

console = Console()
line = Text("A | ")
line.append("█" * 20, style=STYLES["A"])
line.append(" 2.16")
console.print(line)
```

## 8. CLI – `cli.py`

```python
import os
import sys

from .analysis import average_value1_by_type
from .chart import render_bar_chart
from .io import load_rows


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m ascii_barchart.cli <csv-file>")
        raise SystemExit(1)

    csv_path = os.path.abspath(sys.argv[1])

    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        raise SystemExit(1)

    rows = load_rows(csv_path)
    averages = average_value1_by_type(rows)
    render_bar_chart(averages)


if __name__ == "__main__":
    main()
```

Ausführen:

```bash
uv run python -m ascii_barchart.cli data/points.csv
```

## 9. Erwartete Mittelwerte

Damit ihr euch auf Projektstruktur statt Fehlersuche in der Mathematik konzentrieren könnt:

```text
A ≈ 2.16
B ≈ 4.33
C ≈ 6.57
D ≈ 8.71
```
