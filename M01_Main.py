from rich import console
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

console.print(
    Panel(
        "[bold bright_white]My Lyrics & Karaoke Finder[/bold bright_white]",
        subtitle="[yellow]2026 NOVI Eindopdracht[/yellow]",
        border_style="bright_yellow",
        width=50,
    ),
    justify="center"
)

tabel = Table(
    title="[bold bright_white]HOOFDMENU[/bold bright_white]",
    border_style="bright_yellow"
)

tabel.add_column("Keuze", justify="center", style="white")
tabel.add_column("Actie", style="white")

tabel.add_row("1", "Muziek en songtekst zoeken")
tabel.add_row("2", "Opgeslagen nummers bekijken")
tabel.add_row("3", "Karaoke zoeken")
tabel.add_row("0", "Afsluiten")

console.print(tabel)

while True:
    keuze = input("Maak een keuze (0-3): ").strip()
    if keuze in ["0", "1", "2", "3"]:
        break
    console.print("[bold red]Ongeldige invoer! Kies 0, 1, 2, 3, 4[/bold red]")

#keuze validatie(1,2,3, en 0)
if keuze == "1":
    console.print("[bright yellow]Muziek en songtekst zoeken gekozen[/bright yellow]")
elif keuze == "2":
    console.print("[bright yellow]Opgeslagen nummers bekijken gekozen[/bright yellow]")

elif keuze == "3":
    console.print("[bright yellow]Karaoke zoeken gekozen[/bright yellow]")

elif keuze == "0":
    console.print("[bold red]Programma afgesloten[/bold red]")





