import requests
import musicbrainzngs
from rich.console import Console
from M04_Config import EMAIL
from rich.table import Table
from rich.panel import Panel

#API identificatie instellen
musicbrainzngs.set_useragent(
    "My Lyrics Finder",
    "1.0",
    EMAIL
)
from M04_Config import EMAIL

console = Console()

def zoek_artiest(artiest_naam):

    try:

        resultaat = musicbrainzngs.search_artists(
            artiest_naam
        )

        return resultaat

    except Exception as fout:

        console.print(
            f"[bold red]Fout:[/bold red] {fout}"
        )

        return None


def toon_artiesten(artiest_naam):

    resultaat = zoek_artiest(
        artiest_naam
    )
    if resultaat is None:
        return

    artiesten = resultaat["artist-list"]


    if len(artiesten) == 0:
        console.print(
            "[bold red]Geen artiesten gevonden.[/bold red]"
        )
        return
    tabel = Table(
        border_style="bright_yellow"
    )

    tabel.add_column("Nr")
    tabel.add_column("Naam")
    tabel.add_column("Land")
    tabel.add_column("Type")

    for nummer, artiest in enumerate(
            artiesten[:10],
            start=1
    ):
        tabel.add_row(
            str(nummer),
            artiest.get("name", "-"),
            artiest.get("country", "-"),
            artiest.get("type", "-")
        )

    console.print(
        Panel(
            tabel,
            title="[bold bright_white]ZOEKRESULTATEN[/bold bright_white]",
            title_align="center",
            border_style="bright_yellow",
            width=50,
        )
    )
    keuze = console.input(
        "\nKies artiestnummer: "
    )
    if not keuze.isdigit():
        return
    keuze = int(keuze)
    if keuze < 1 or keuze > len(artiesten[:10]):
        return
    gekozen_artiest = artiesten[keuze - 1]
    naam = gekozen_artiest.get("name", "Onbekend")
    land = gekozen_artiest.get("country", "-")
    soort = gekozen_artiest.get("type", "-")



    console.print()
    console.print(f"[bold yellow]Naam:[/bold yellow] {naam}")
    console.print(f"[bold yellow]Land:[/bold yellow] {land}")
    console.print(f"[bold yellow]Type:[/bold yellow] {soort}")

#TOON NUMMERS VAN ARTIEST
    artist_id = gekozen_artiest["id"]
    console.print(
        f"[green]Artist ID gevonden:[/green] {artist_id}"
    )

    toon_nummers_van_artiest(artist_id)

def toon_nummers_van_artiest(artist_id):
    resultaat = musicbrainzngs.browse_recordings(
        artist=artist_id,
        limit=20,
        offset = 0
    )
    nummers = resultaat["recording-list"]
    for nummer, lied in enumerate(nummers, start=1):
        console.print(
            f"{nummer}. {lied['title']}"
        )
       #
    # unieke_nummers = []
    #
    # for lied in nummers:
    #     console.print(lied["title"])
    #     titel = lied["title"]
    #
    #     if titel not in unieke_nummers:
    #         unieke_nummers.append(titel)
    #
    # for nummer, titel in enumerate(unieke_nummers, start=1):
    #
    #     console.print(
    #         f"{nummer}. {lied['title']}"
    #     )

    # hoofdprogramma
if __name__ == "__main__":

    while True:

        artiest = console.input(
            "\n[bold yellow]Naam artiest (0 = stoppen): [/bold yellow]"
        )

        if artiest == "0":
            break

        toon_artiesten(artiest)