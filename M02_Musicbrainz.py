
import musicbrainzngs
from rich.console import Console
from M04_Config import EMAIL
from rich.table import Table

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
        title="Zoekresultaten"
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

    console.print(tabel)
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


if __name__ == "__main__":

    while True:

        artiest = console.input(
            "\n[bold yellow]Naam artiest (0 = stoppen): [/bold yellow]"
        )

        if artiest == "0":
            break

        toon_artiesten(artiest)