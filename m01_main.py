from rich.align import Align
from m00_imports import *
from m02_musicbrainz import toon_muziek_menu, toon_favorieten_menu
from m03_karaoke import toon_karaoke_menu
from m05_utils import maak_menu_tabel

# Toon het applicatielogo en de projectinformatie.
def toon_logo():
    console.print(
        Panel(
            Align.center(
                "[bold bright_white]My Lyrics & Karaoke Finder[/bold bright_white]"
            ),
            title="[bold bright_white]2026 NOVI Eindopdracht[/bold bright_white]",
            title_align="center",
            border_style="bold yellow",
            width=50,
        ),
    )

    console.print()
toon_logo()

# Bouw en toon het hoofdmenu met de beschikbare functionaliteiten.
def toon_hoofdmenu():
    console.clear()
    tabel = maak_menu_tabel(45)

    tabel.add_row("1", "Muziek en songteksten zoeken")
    tabel.add_row("2", "Favorieten beheren")
    tabel.add_row("3", "Karaokevideo's zoeken")
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

# Centrale programmalus die actief blijft totdat de gebruiker ervoor kiest de applicatie af te sluiten.
while True:

    toon_hoofdmenu()
# Vraag de gebruiker om een keuze te maken uit het HOOFDMENU.
    keuze = console.input(
        "[bold]Maak een keuze "
        "[bold yellow][0][/bold yellow] t/m "
        "[bold yellow][3][/bold yellow]: [/bold]"
    ).strip()
# Controleer of de invoer overeenkomt met een beschikbare menuoptie.
    if keuze not in ["0", "1", "2", "3"]:
        logging.error(f"Ongeldige menukeuze ingevoerd: {keuze}")
# Informeer de gebruiker dat een ongeldige menuoptie is ingevoerd.
        console.print(
            "[bold red]Ongeldige keuze. Kies 0 t/m 3.[/bold red]"
        )
        continue

# Open het SUBMENU voor keuze 1 "Muziek en songteksten zoeken".
    if keuze == "1":
        toon_muziek_menu()
# Open het SUBMENU voor keuze 2 "Favorieten beheren".
    elif keuze == "2":
        toon_favorieten_menu()
# Open het SUBMENU voor keuze 3 "Karaokevideo's zoeken.
    elif keuze == "3":
        toon_karaoke_menu()

    elif keuze == "0":

        console.print(
            "[bold red]Programma afgesloten[/bold red]"
        )
# Beëindig de programmalus en sluit de applicatie af.
        break





