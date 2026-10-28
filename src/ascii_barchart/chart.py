
from rich.console import Console
from rich.text import Text

def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values):
    console = Console()

    if not values:
        console.print("No data available.")
        return

    maximum = max(value for label, value in values)

    colors = ["green", "blue", "yellow", "magenta"]

    for i, (label, value) in enumerate(values):
        bar_length = scale_bar(value, maximum)

        bar = Text("█" * bar_length, style=colors[i % len(colors)])

        console.print(f"{label}: ", end="")
        console.print(bar, end="")
        console.print(f" {value:.2f}")


if __name__ == "__main__":
    values = [
        ("A", 2.16),
        ("B", 4.33),
        ("C", 6.57),
        ("D", 8.71),
    ]

    render_bar_chart(values)
