
import musicbrainzngs
import requests
from rich.console import Console
from M04_Config import EMAIL
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns

#API identificatie instellen
musicbrainzngs.set_useragent(
    "My Lyrics Finder",
    "1.0",
    EMAIL
)

console = Console()
#Stuur de ingevoerde artiestnaam naar MusicBrainz.
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
        return None# zorgt ervoor dat de functie niet vastloopt na een fout

#Zoekt artiesten op,
# toont de resultaten, laat de gebruiker een
# artiest kiezen en haalt daarna de gegevens van die artiest op.
def toon_artiesten(artiest_naam):

    resultaat = zoek_artiest(
        artiest_naam
    )
    if resultaat is None:
        return
#Haal de lijst met gevonden artiesten uit het resultaat.
#Zoekresultaten artiesten gefilterd op exacte artiestnaam
    artiesten = [
        artiest
        for artiest in resultaat["artist-list"]
        if artiest.get("name", "").lower() == artiest_naam.lower()
    ]



#len = tel hoeveel artiesten er zijn, als er geen artiest gevonden is, print in rood
    if len(artiesten) == 0:
        console.print(
            "[bold red]Geen artiesten gevonden.[/bold red]"
        )
        return # FUNCTIE def toon_artiesten STOPPEN, onderstaande tabel wordt niet gemaakt.


#1Tabel: opmaken zodat het resultaat netjes verwerkt wordt
#Rich tabel leeg tabel aanmaken en opmaken
        linker_tabel = Table(
        border_style="bright_yellow",
        )
        rechter_tabel = Table(
        border_style="bright_yellow",
        )


# 2 Kolommen: in tabel voor headers van bovenstaanse tabel aanmaken (headers)
    linker_tabel = Table(
        border_style="bright_yellow"
    )
    linker_tabel.add_column("Nr", width=3)
    linker_tabel.add_column("Naam", width=10)
    linker_tabel.add_column("Type", width=10)
    linker_tabel.add_column("Beschrijving", max_width=45)

    rechter_tabel = Table(
        border_style="bright_yellow"
    )
    rechter_tabel.add_column("Nr", width=3)
    rechter_tabel.add_column("Naam", width=10)
    rechter_tabel.add_column("Type", width=10)
    rechter_tabel.add_column("Beschrijving", max_width=45)

#3 rijen: eerste 10 artiesten toevoegen
#enumerate=voeg automatisch nummers toe,begin bij 1
    midden = (len(artiesten) + 1) // 2
    for nummer, artiest_musicbrainz in enumerate(
            artiesten[:midden],
            start=1
    ):
        linker_tabel.add_row(
            str(nummer),
            artiest_musicbrainz.get("name", "-"),
            artiest_musicbrainz.get("type", "-"),
            artiest_musicbrainz.get("disambiguation", "-")
        )

    for nummer, artiest_musicbrainz in enumerate(
            artiesten[midden:],
            start=midden + 1
    ):
        rechter_tabel.add_row(
            str(nummer),
            artiest_musicbrainz.get("name", "-"),
            artiest_musicbrainz.get("type", "-"),
            artiest_musicbrainz.get("disambiguation", "-")
        )


    console.print(
        Panel(
            Columns(
                [linker_tabel, rechter_tabel],
                equal=True,
                expand=True

            ),
            title=f"[bold bright_white]RESULTATEN VOOR {artiest_naam.upper()}[/bold bright_white]",
            title_align="center",
            border_style="bright_yellow",
            width=160,
        )
    )
    console.print()

    console.print("1-20 = Artiest kiezen")
    console.print("N    = Volgende artiesten")
    console.print("V    = Vorige artiesten")
    console.print("0    = Terug")
    console.print("S    = Hoofdmenu")

#Vraag de gebruiker te maken:1-10 = Artiest kiezen
# N    = Volgende artiesten
# V    = Vorige artiesten
# 0    = Terug
# S    = Hoofdmenu
    keuze = console.input(
        "\nMaak keuze: "
    )
#keuze maken
    if keuze.upper() == "N":
        console.print(
            "[yellow]Volgende pagina nog bouwen[/yellow]"
        )
        return

    elif keuze.upper() == "V":
        console.print(
            "[yellow]Vorige pagina nog bouwen[/yellow]"
        )
        return


    elif keuze.upper() == "S":

        return "hoofdmenu"


    elif keuze == "0":

        return "terug"

    elif keuze.isdigit():

        keuze = int(keuze)

        if keuze < 1 or keuze > 10:
            console.print(
                "[red]Ongeldige keuze[/red]"
            )
            return

        gekozen_artiest = artiesten[keuze - 1]

        artiest_naam = gekozen_artiest["name"]
        artist_id = gekozen_artiest["id"]

        artiest, songtitel = toon_nummers_van_artiest(
            artist_id,
            artiest_naam
        )
        if artiest is None:
            return
        toon_songtekst(
            artiest,
            songtitel
        )
    else:
        console.print(
            "[red]Ongeldige keuze[/red]"
        )

def toon_nummers_van_artiest(
        artist_id,
        artiest_naam
):

    resultaat = musicbrainzngs.get_artist_by_id(
        artist_id,
        includes=["works"]
    )

    works = resultaat["artist"]["work-list"]

    pagina = 0

    while True:
#LINKER TABEL-----------------------------------
        linker_tabel = Table(
            border_style="bright_yellow",
            expand=True
        )
        linker_tabel.add_column(
            "Nr",
            width=3,
            justify="center"
        )
        linker_tabel.add_column(
            "Titel",
            max_width=35
        )
#BEGIN RECHTER TABEL------------------------------
        rechter_tabel = Table(
            border_style="bright_yellow",
            expand=True
        )
        rechter_tabel.add_column(
            "Nr",
            width=3,
            justify="center"
        )
        rechter_tabel.add_column(
            "Titel",
            max_width=35
        )
#EINDE RECHTER TABEL------------------------------
        start = pagina * 20

        for nummer, work in enumerate(
                works[start:start + 10],
                start=start + 1
        ):
            linker_tabel.add_row(
                str(nummer),
                work["title"]
            )

        for nummer, work in enumerate(
                works[start + 10:start + 20],
                start=start + 11
        ):
            rechter_tabel.add_row(
                str(nummer),
                work["title"]
            )

        console.print(
            Panel(
                Columns(
                    [linker_tabel, rechter_tabel],
                    equal=True,
                    expand=False
                ),
                title=f"[bold bright_white]NUMMERS VAN {artiest_naam.upper()}[/bold bright_white]",
                title_align="center",
                border_style="bright_yellow",
                width=160
            )
        )

        console.print()

        console.print("1-20 = Nummer kiezen")
        console.print("N    = Volgende")
        console.print("V    = Vorige")
        console.print("0    = Terug")
        console.print("S    = Hoofdmenu")

        keuze = console.input(
            "\nMaak keuze: "
        )

        if keuze.upper() == "N":

            if start + 20 < len(works):
                pagina += 1
            else:
                console.print(
                    "[red]Geen volgende pagina.[/red]"
                )

        elif keuze.upper() == "V":

            if pagina > 0:
                pagina -= 1
            else:
                console.print(
                    "[red]Geen vorige pagina.[/red]"
                )

        elif keuze == "0":
            return None, None

        elif keuze.upper() == "S":
            return None, None

        elif keuze.isdigit():

            keuze = int(keuze)

            if 1 <= keuze <= len(works):

                gekozen_nummer = works[keuze - 1]

                songtitel = gekozen_nummer["title"]

                console.print(
                    f"[green]Gekozen nummer:[/green] {songtitel}"
                )

                return artiest_naam, songtitel

            else:
                console.print(
                    "[red]Ongeldige keuze[/red]"
                )

        else:

            console.print(
                "[red]Ongeldige keuze[/red]"
            )
def toon_songtekst(
        artiest_naam,
        songtitel
):
    url = (
        f"https://api.lyrics.ovh/v1/"
        f"{artiest_naam}/{songtitel}"
    )

    try:

        response = requests.get(url)

        data = response.json()

        songtekst = data.get(
            "lyrics",
            "Geen songtekst gevonden."
        )

        console.print()

        console.print(
            Panel(
                songtekst,
                title=f"[bold bright_white]{songtitel}[/bold bright_white]",
                border_style="bright_yellow"
            )
        )
# OPSLAAN
        opslaan = console.input(
            "\nOpslaan als favoriet? (J/N): "
        ).upper()

        if opslaan == "J":

            sla_favoriet_op(
                artiest_naam,
                songtitel
            )
    except Exception as fout:

        console.print(
            f"[bold red]Fout:[/bold red] {fout}"
        )
#OPSLAAN IN FAVORIETEN
def sla_favoriet_op(
        artiest_naam,
        songtitel
):
    with open(
            "favorieten.txt",
            "a",
            encoding="utf-8"
    ) as bestand:

        bestand.write(
            f"{artiest_naam} - {songtitel}\n"
        )

    console.print(
        "[green]Favoriet opgeslagen.[/green]"
    )