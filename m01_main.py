from m00_imports import *
from m02_musicbrainz import (
    toon_muziek_menu,
    toon_favorieten_menu
)
from m03_karaoke import toon_karaoke_menu

from m10_utils import (
    maak_menu_tabel
)
# begin applicatielogo

def toon_logo():
    console.print(
        Panel(
            "[center][bold bright_white]My Lyrics & Karaoke Finder[/bold bright_white][/center]",
            title="[bold bright_white]2026 NOVI Eindopdracht[/bold bright_white]",
            title_align="center",
            border_style="bold yellow",
            width=50,
        ),
        justify="left"
    )

    console.print()


toon_logo()


#begin hoofmenu
def toon_hoofdmenu():
    tabel = maak_menu_tabel(45)

    tabel.add_row("1", "Muziek en songtekst zoeken")
    tabel.add_row("2", "Favorieten bekijken")
    tabel.add_row("3", "Karaoke zoeken")
    tabel.add_row("0", "Afsluiten")

    console.print(
        Panel(
            tabel,
            title="[bold bright_white]HOOFDMENU[/bold bright_white]",
            title_align="center",
            border_style="bright_yellow",
            width=50
        )
    )

#ombouwen van hoofdmenu naar centrale lus
while True:

    toon_hoofdmenu()

    keuze = console.input(
        "[bold]Maak een keuze "
        "[bold yellow][0][/bold yellow] t/m "
        "[bold yellow][3][/bold yellow]: [/bold]"
    ).strip()

    if keuze not in ["0", "1", "2", "3"]:
        # Log ongeldige invoer van de gebruiker.
        logging.error(f"Ongeldige menukeuze ingevoerd: {keuze}")

        console.print(
            "[bold red]Ongeldige keuze. Kies 0 t/m 3.[/bold red]"
        )
        continue

#keuze validatie(1,2,3, en 0)
    if keuze == "1":
        toon_muziek_menu()

    elif keuze == "2":
        toon_favorieten_menu()

    elif keuze == "3":
        toon_karaoke_menu()

    elif keuze == "0":

        console.print(
            "[bold red]Programma afgesloten[/bold red]"
        )

        break





