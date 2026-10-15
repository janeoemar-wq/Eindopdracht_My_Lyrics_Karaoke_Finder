import json
import requests
import musicbrainzngs

from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from M04_Config import EMAIL

console = Console()
#API identificatie instellen
musicbrainzngs.set_useragent(
    "My Lyrics Finder",
    "1.0",
    EMAIL
)
# keuze 1 zoek artiest
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

    resultaat = zoek_artiest(artiest_naam)

    if resultaat is None:
        return

    tabel = Table(
        title="Zoekresultaten",
        border_style="bright_yellow"
    )

    tabel.add_column("Nr", justify="right", style="bright_yellow")
    tabel.add_column("Naam", style="white")
    tabel.add_column("Land", style="white")
    tabel.add_column("Type", style="white")

    artiesten = resultaat["artist-list"]
    if len(artiesten) == 0:
        console.print(
            "[bold red]Geen artiesten gevonden.[/bold red]"
        )
        return

    for nummer, artiest in enumerate(artiesten[:10], start=1):
        naam = artiest.get("name", "Onbekend")
        land = artiest.get("country", "-")
        soort = artiest.get("type", "-")

        tabel.add_row(
            str(nummer),
            naam,
            land,
            soort
        )

    console.print(tabel)

if __name__ == "__main__":

    while True:

        artiest = console.input(
            "\n[bold yellow]Naam artiest (0 = stoppen): [/bold yellow]"
        )

        if artiest == "0":
            break

        toon_artiesten(artiest)

        console.input(
            "\n[bold cyan]Druk op Enter om verder te gaan...[/bold cyan]"
        )