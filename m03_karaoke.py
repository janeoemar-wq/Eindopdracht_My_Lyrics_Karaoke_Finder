from m00_imports import *
from m04_config import YOUTUBE_SEARCH_URL
from m05_utils import (
    vraag_artiest_en_titel,
    maak_menu_tabel,
    toon_foutmelding,
    vraag_opslaan_favoriet,
    lees_bestand

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
# Gebruik een herbruikbare hulpfunctie voor de J/N-vraag,
# zodat dezelfde code niet meerdere keren geschreven hoeft te worden.
            if vraag_opslaan_favoriet(
                    "Opslaan als karaokefavoriet?"
            ):
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
            beheer_karaoke_favorieten()

            continue
def beheer_karaoke_favorieten():

    while True:
        console.clear()

        menu = maak_menu_tabel(50)
        menu.add_row("1", "Favorieten bekijken")
        menu.add_row("2", "Favoriet verwijderen")
        menu.add_row("0", "Terug")

        console.print(
            Panel(
                menu,
                title="KARAOKEFAVORIETEN",
                border_style="bright_yellow",
                width=50
            )
        )

        keuze = console.input(
            "\nMaak een keuze (0-2): "
        ).strip()

        if keuze == "0":
            break

        elif keuze == "1":

            favorieten = lees_bestand(
                "m07_karaoke_favorieten.txt"
            )

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

            keuze_favoriet = console.input(
                "\nKies een favoriet (0 = terug): "
            ).strip()

            if keuze_favoriet == "0":
                continue

            if not keuze_favoriet.isdigit():
                toon_foutmelding(
                    "Ongeldige keuze."
                )
                continue
            keuze_favoriet = int(
                keuze_favoriet
            )

            if (
                    keuze_favoriet < 1
                    or keuze_favoriet > len(favorieten)
            ):
                toon_foutmelding(
                    "Ongeldige keuze."
                )

                continue

            omschrijving, url = (
                favorieten[
                    keuze_favoriet - 1
                    ]
                .strip()
                .split("|")
            )

            webbrowser.open(url)

            console.print(
                f"[green]YouTube geopend voor {omschrijving}[/green]"
            )


        elif keuze == "2":

            with open(

                    "m07_karaoke_favorieten.txt",

                    "r",

                    encoding="utf-8"

            ) as bestand:

                favorieten = bestand.readlines()

            if not favorieten:
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

                    title="Karaokefavorieten verwijderen",

                    border_style="red"

                )

            )

            keuze_verwijderen = console.input(

                "\nNummer verwijderen (0 = terug): "

            ).strip()

            if keuze_verwijderen == "0":
                continue

            if not keuze_verwijderen.isdigit():
                toon_foutmelding(

                    "Ongeldige keuze."

                )

                continue

            keuze_verwijderen = int(

                keuze_verwijderen

            )

            if (

                    keuze_verwijderen < 1

                    or keuze_verwijderen > len(favorieten)

            ):
                toon_foutmelding(

                    "Ongeldige keuze."

                )

                continue

            del favorieten[

                keuze_verwijderen - 1

                ]

            with open(

                    "m07_karaoke_favorieten.txt",

                    "w",

                    encoding="utf-8"

            ) as bestand:

                bestand.writelines(

                    favorieten

                )

            console.print(

                "[green]Favoriet verwijderd.[/green]"

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

