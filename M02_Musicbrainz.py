
import musicbrainzngs
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
import musicbrainzngs

from rich.console import Console
from rich.table import Table

from M04_Config import EMAIL

console = Console()

musicbrainzngs.set_useragent(
    "My Lyrics Finder",
    "1.0",
    EMAIL
)


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

    tabel.add_column("Naam")
    tabel.add_column("Land")
    tabel.add_column("Type")

    for artiest in artiesten[:10]:

        tabel.add_row(
            artiest.get("name", "-"),
            artiest.get("country", "-"),
            artiest.get("type", "-")
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