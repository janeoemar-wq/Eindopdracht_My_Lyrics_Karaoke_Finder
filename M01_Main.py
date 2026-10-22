from M00_Imports import *
from M02_Musicbrainz import toon_artiesten, toon_favorieten, verwijder_favoriet
from M03_Karaoke import toon_karaoke_menu
from M10_Helpersfunctie import (
    vraag_artiest_en_titel,
    maak_menu_tabel
)
import requests
import webbrowser
from urllib.parse import quote_plus

# begin LOGO
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
#EINDE LOGO

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
        "[bold]Maak een keuze (0-3):[/bold]"
    ).strip()

    if keuze not in ["0", "1", "2", "3"]:

        console.print(
            "[bold red]Ongeldige invoer! Kies 0, 1, 2, 3[/bold red]"
        )

        continue

#keuze validatie(1,2,3, en 0)

    if keuze == "1":
        while True:
            submenu = maak_menu_tabel(45)

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
            )
            )
            submenu_keuze = console.input(
                "\nMaak een keuze (0-2): "
            ).strip()

            if submenu_keuze == "0":
                break

            if submenu_keuze == "1":
                artiest_naam = console.input(
                        "\n[bold white]Voer artiestnaam in (0 = Terug, S = Hoofdmenu): [/bold white]"
                )

                if artiest_naam == "0":
                    break

                if artiest_naam.upper() == "S":
                    break

                actie = toon_artiesten(
                    artiest_naam
                )

                if actie == "hoofdmenu":
                    continue  # hiermee kom je weer in het hoofdmenu


            elif submenu_keuze == "2":
                console.print(
                    "[yellow]Zoek nummer wordt later gebouwd[/yellow]"
                )
                continue

            else:
                console.print(
                    "[red]Ongeldige keuze[/red]"
                )
                continue

    elif keuze == "2":

        while True:

            console.clear()
            submenu = maak_menu_tabel(50)

            submenu.add_row("1", "Favorieten bekijken")
            submenu.add_row("2", "Favoriet verwijderen")
            submenu.add_row("0", "Terug")

            console.print(
                Panel(
                    submenu,
                    title="[bold bright_white]OPGESLAGEN NUMMERS[/bold bright_white]",
                    title_align="center",
                    border_style="bright_yellow",
                    width=50,
                )
            )

            submenu_keuze = console.input(
                "\n[bold white]Maak een keuze (0-2): [/bold white]"
            ).strip()

            if submenu_keuze == "1":

                toon_favorieten()

                console.input(
                    "\nDruk op Enter om verder te gaan..."
                )
                continue




            elif submenu_keuze == "2":

                actie = verwijder_favoriet()

                if actie == "hoofdmenu":
                    break

                continue



            elif submenu_keuze == "0":

                break



            if submenu_keuze == "0":

                break
            elif submenu_keuze == "1":

                console.print(
                    "[yellow]Zoek karaokevideo wordt later gebouwd[/yellow]"
                )

                continue
            elif submenu_keuze == "2":

                console.print(
                    "[yellow]Open YouTube-resultaten wordt later gebouwd[/yellow]"
                )

                continue
    elif keuze == "3":
        toon_karaoke_menu()

    elif keuze == "0":

        console.print(
            "[bold red]Programma afgesloten[/bold red]"
        )

        break





