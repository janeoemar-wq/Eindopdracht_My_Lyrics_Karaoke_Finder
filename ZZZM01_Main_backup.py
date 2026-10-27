
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from m02_musicbrainz import toon_artiesten, toon_favorieten, verwijder_favoriet

console = Console()
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
    tabel = Table(
        border_style="bright_yellow",
        width=45
    )

    tabel.add_column("Keuze", justify="center")
    tabel.add_column("Actie")

    tabel.add_row("1", "Muziek en songteksten zoeken")
    tabel.add_row("2", "Opgeslagen nummers bekijken")
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

toon_hoofdmenu()
#EINDE TOON HOOFDMENU

while True:
    keuze = console.input("[bold]Maak een keuze (0-3):[/bold]").strip()
    if keuze in ["0", "1", "2", "3"]:
        break
    console.print("[bold red]Ongeldige invoer! Kies 0, 1, 2, 3[/bold red]")

#keuze validatie(1,2,3, en 0)

if keuze == "1":

    submenu = Table(
    border_style="bright_yellow",
    width=45
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
    )
    )

    artiest_naam = console.input(
        "\n[bold white]Voer artiestnaam in: [/bold white]"
    )

    actie = toon_artiesten(
        artiest_naam
    )

    if actie == "hoofdmenu":
        toon_hoofdmenu()

elif keuze == "2":

    while True:

        console.clear()

        submenu = Table(
            border_style="bright_yellow",
            width=50
        )

        submenu.add_column("Keuze", justify="center")
        submenu.add_column("Actie")

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

        elif keuze == "3":

            submenu = Table(
                border_style="bright_yellow",
                width=50
            )

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

        elif submenu_keuze == "0":
            break





