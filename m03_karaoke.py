from m00_imports import *
from m04_config import YOUTUBE_SEARCH_URL
from m05_utils import (
    vraag_artiest_en_titel,
    maak_menu_tabel,
    toon_foutmelding

)

def toon_karaoke_menu():
    while True:
        console.clear()
        submenu = maak_menu_tabel(50)

        submenu.add_row("1", "Zoek karaokevideo")
        submenu.add_row("2", "Karaokefavorieten")
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

            if artiest == "" or titel == "":
                toon_foutmelding(
                    "Voer een artiest en titel in."
                )
                continue
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
            # Vraag of de gebruiker de karaokezoekopdracht wil opslaan als favoriet.
            opslag = console.input(
                "\nOpslaan als karaokefavoriet? (j/n): "
            ).strip().lower()

            if opslag == "j":
                sla_karaoke_favoriet_op(
                    artiest,
                    titel,
                    youtube_url
                )

                console.print(
                    "[green]Karaokefavoriet opgeslagen.[/green]"
                )
            continue

# SUBMENU KEUZE 2:
# Open YouTube-resultaten voor alle karaokevideo's van een artiest.
        elif submenu_keuze == "2":

            try:
                with open(
                    "m07_karaoke_favorieten.txt",
                    "r",
                    encoding="utf-8"
                ) as bestand:
                    favorieten = bestand.readlines()

            except FileNotFoundError:
                toon_foutmelding(
                    "Geen karaokefavorieten gevonden."
                )
                continue

            tabel = maak_menu_tabel(80)

            for nummer, favoriet in enumerate(
                favorieten,
                start=1
            ):
                omschrijving, url = (
                    favoriet.strip().split("|")
                )

                tabel.add_row(
                    str(nummer),
                    omschrijving
                )

            console.print(
                Panel(
                    tabel,
                    title="Karaokefavorieten",
                    border_style="bright_yellow"
                )
            )

            keuze = console.input(
                "\nKies een favoriet (0 = terug): "
            ).strip()

            if keuze == "0":
                continue

            if not keuze.isdigit():
                toon_foutmelding(
                    "Ongeldige keuze."
                )
                continue

            keuze = int(keuze)

            if keuze < 1 or keuze > len(favorieten):
                toon_foutmelding(
                    "Ongeldige keuze."
                )
                continue

            omschrijving, url = (
                favorieten[keuze - 1]
                .strip()
                .split("|")
            )

            webbrowser.open(url)

            console.print(
                f"[green]YouTube geopend voor {omschrijving}[/green]"
            )

            console.input(
                "\nDruk op Enter om verder te gaan..."
            )

            continue


# Sla een karaokefavoriet op in het bestand met opgeslagen karaokevideo's.
def sla_karaoke_favoriet_op(
    artiest,
    titel,
    url
):
    with open(
        "m07_karaoke_favorieten.txt",
        "a",
        encoding="utf-8"
    ) as bestand:
        bestand.write(
            f"{artiest} - {titel}|{url}\n"
        )

