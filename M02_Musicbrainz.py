
import musicbrainzngs
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
    artiesten = resultaat["artist-list"]



#len = tel hoeveel artiesten er zijn, als er geen artiest gevonden is, print in rood
    if len(artiesten) == 0:
        console.print(
            "[bold red]Geen artiesten gevonden.[/bold red]"
        )
        return # FUNCTIE def toon_artiesten STOPPEN, onderstaande tabel wordt niet gemaakt.


#1Tabel: opmaken zodat het resultaat netjes verwerkt wordt
#Rich tabel leeg tabel aanmaken en opmaken
    linker_tabel = Table(
        border_style="bright_yellow"
    )
    rechter_tabel = Table(
        border_style="bright_yellow"
    )


# 2 Kolommen: in tabel voor headers van bovenstaanse tabel aanmaken (headers)
    linker_tabel.add_column("Nr")
    linker_tabel.add_column("Naam")
    linker_tabel.add_column("Type")
    linker_tabel.add_column("Beschrijving")

    rechter_tabel.add_column("Nr")
    rechter_tabel.add_column("Naam")
    rechter_tabel.add_column("Type")
    rechter_tabel.add_column("Beschrijving")

#3 rijen: eerste 10 artiesten toevoegen
#enumerate=voeg automatisch nummers toe,begin bij 1
    for nummer, artiest_musicbrainz in enumerate(
            artiesten[:5],
            start=1
    ):
        linker_tabel.add_row(
            str(nummer),
            artiest_musicbrainz.get("name", "-"),
            artiest_musicbrainz.get("type", "-"),
            artiest_musicbrainz.get("disambiguation", "-")
        )

    for nummer, artiest_musicbrainz in enumerate(
            artiesten[5:10],
            start=6
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

        actie = toon_nummers_van_artiest(
            artist_id,
            artiest_naam
        )
        console.print(actie)
        # if actie == "terug":
        #     return
        #
        # if actie == "hoofdmenu":
        #     return "hoofdmenu"

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

        linker_tabel = Table(
            border_style="bright_yellow"
        )
        linker_tabel.add_column(
            "Nr",
            justify="center"
        )
        linker_tabel.add_column(
            "Titel"
        )

        rechter_tabel = Table(
            border_style="bright_yellow"
        )
        rechter_tabel.add_column(
            "Nr",
            justify="center"
        )
        rechter_tabel.add_column(
            "Titel"
        )

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
                    expand=True
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
            return


        elif keuze.upper() == "S":
            return


        else:

            console.print(

                "[red]Ongeldige keuze[/red]"

            )