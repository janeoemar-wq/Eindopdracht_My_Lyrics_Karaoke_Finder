"""
zelfde breedte
zelfde kleur
gecentreerd
titel in bovenste rand
direct onder het logo
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

#EINDE LOGO

#begin hoofmenu
def toon_hoofdmenu():
    tabel = Table(
        border_style="bright_yellow",
        width=46
    )

    tabel.add_column("Keuze", justify="center")
    tabel.add_column("Actie")

    tabel.add_row("1", "Muziek en songtekst zoeken")
    tabel.add_row("2", "Opgeslagen nummers bekijken")
    tabel.add_row("3", "Karaoke zoeken")
    tabel.add_row("0", "Afsluiten")

    console.print(
        Panel(
            tabel,
            title="[bold bright_white]HOOFDMENU[/bold bright_white]",
            title_align="center",
            border_style="bright_yellow",
            width=50,
        ),
        justify="center"
    )
toon_hoofdmenu()
#EINDE TOON HOOFDMENU

while True:
    keuze = console.input("[bold]Maak een keuze (0-3):[/bold]").strip()
    if keuze in ["0", "1", "2", "3"]:
        break
    console.print("[bold red]Ongeldige invoer! Kies 0, 1, 2, 3[/bold red]")

#keuze validatie(1,2,3, en 0)
if keuze == "1":
    console.clear()
    # begin LOGO
    console.print(
        Panel(
            "[bold bright_white]My Lyrics & Karaoke Finder[/bold bright_white]",
            subtitle="[bright_yellow]2026 NOVI Eindopdracht[/bright_yellow]",
            border_style="bold yellow",
            width=50,
        ),
        justify="center"
    )

    console.print()

    submenu = Table(
        border_style="bright_yellow",
        width=46
    )

    submenu.add_column("Keuze", justify="center")
    submenu.add_column("Actie")

    submenu.add_row("1", "Zoek artiest")
    submenu.add_row("2", "Zoek nummer")
    submenu.add_row("0", "Terug")

    console.print(
        Panel(
            submenu,
            title="[bold bright_white]MUZIEK & SONGTEKST[/bold bright_white]",
            title_align="center",
            border_style="bright_yellow",
            width=50,
        ),
        justify="center"
    )
elif keuze == "2":
    # begin LOGO
    console.print(
        Panel(
            "[bold bright_white]My Lyrics & Karaoke Finder[/bold bright_white]",
            subtitle="[bright_yellow]2026 NOVI Eindopdracht[/bright_yellow]",
            border_style="bold yellow",
            width=50,
        ),
        justify="center"
    )

    submenu = Table(
        title="[bold bright_white]OPGESLAGEN NUMMERS[/bold bright_white]",
        border_style="bright_yellow",
        width=40
    )

    submenu.add_column("Keuze", justify="center")
    submenu.add_column("Actie")

    submenu.add_row("1", "Favorieten bekijken")
    submenu.add_row("2", "Favoriet verwijderen")
    submenu.add_row("0", "Terug")

    console.print(submenu)

elif keuze == "3":
    # begin LOGO
    console.print(
        Panel(
            "[bold bright_white]My Lyrics & Karaoke Finder[/bold bright_white]",
            subtitle="[bright_yellow]2026 NOVI Eindopdracht[/bright_yellow]",
            border_style="bold yellow",
            width=50,
        ),
        justify="center"
    )
    submenu = Table(
        title="[bold bright_white]KARAOKE[/bold bright_white]",
        border_style="bright_yellow"
    )

    submenu.add_column("Keuze", justify="center")
    submenu.add_column("Actie")

    submenu.add_row("1", "Zoek karaokevideo")
    submenu.add_row("2", "Open YouTube-resultaten")
    submenu.add_row("0", "Terug")

    console.print(
        Panel(
            submenu,
            title="[bold bright_white]MUZIEK & SONGTEKST[/bold bright_white]",
            title_align="center",
            border_style="bright_yellow",
            width=50
        ),
        justify="center"
    )

elif keuze == "0":
    console.print("[bold red]Programma afgesloten[/bold red]")






