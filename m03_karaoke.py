from m00_imports import *
from m04_config import YOUTUBE_SEARCH_URL
from m10_utils import (
    vraag_artiest_en_titel,
    maak_menu_tabel
)

def toon_karaoke_menu():
    while True:
        submenu = maak_menu_tabel(50)

        submenu.add_column("Keuze", justify="center")
        submenu.add_column("Actie")

        submenu.add_row("1", "Zoek karaokevideo")
        submenu.add_row("2", "Open YouTube-resultaten")
        submenu.add_row("0", "Terug")

        console.print(
            Panel(
                submenu,
                title="[bold bright_white]KARAOKE[/bold bright_white]",
                title_align="center",
                border_style="bright_yellow",
                width=50,
            )
        )

        submenu_keuze = console.input(
            "\nMaak een keuze (0-2): "
        ).strip()

        if submenu_keuze == "0":

            break

# SUB MENU KEUZE 1
        elif submenu_keuze == "1":

            artiest, titel = vraag_artiest_en_titel()

            zoekopdracht = (

                f"{artiest} {titel} karaoke"

            )
# Bouw de zoek-URL op met een configurabele basis-URL.
# Dit vergemakkelijkt onderhoud en toekomstige wijzigingen.

            youtube_url = (

                    YOUTUBE_SEARCH_URL

                    + quote_plus(zoekopdracht)

            )

            webbrowser.open(youtube_url)

            console.print(

                Panel(

                    f"YouTube geopend voor:\n{artiest} - {titel}",

                    title="Karaoke",

                    border_style="green"

                )

            )

            continue

# SUBMENU KEUZE 2:
# Open YouTube-resultaten voor alle karaokevideo's van een artiest.
        elif submenu_keuze == "2":

            artiest = console.input(
                "Artiest: "
            ).strip()

            youtube_url = (
                    YOUTUBE_SEARCH_URL
                    + quote_plus(f"{artiest} karaoke")
            )

            webbrowser.open(youtube_url)

            console.print(
                Panel(
                    f"Karaoke-resultaten geopend voor:\n{artiest}",
                    title="YouTube",
                    border_style="green"
                )
            )

            continue
