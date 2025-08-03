import calendar
from rich.console import Console
from rich.table import Table

def colorfull_calendar(year):
    console = Console()
    cal = calendar.Calendar()

    for month in range(1, 13):
        month_name = calendar.month_name[month]
        table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

        # Add weekday headers
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            style = "red" if day in ["Sat", "Sun"] else "green"
            table.add_column(day, justify="center", style=style)

        # Add days
        month_days = cal.monthdayscalendar(year, month)
        for week in month_days:
            table.add_row(*[str(day) if day != 0 else "" for day in week])

        console.print(table)
        console.print("\n")

# Example usage
colorfull_calendar(2025)
