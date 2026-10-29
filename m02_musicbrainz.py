"""
Opmaak artiestentabel
Nr: width=3
Naam: width=10
Type: width=10
Beschrijving: max_width=35
no_wrap=True
overflow="ellipsis"
Columns(..., equal=True, expand=False)
Panel width=160

Verdeling:
midden = (len(pagina_artiesten) + 1) // 2
6 resultaten = 3/3
7 resultaten = 4/3
8 resultaten = 4/4
10 resultaten = 5/5
"""

import musicbrainzngs
from m00_imports import *
from m04_config import EMAIL
from m04_config import LYRICS_API_URL
from rich.columns import Columns
from m05_utils import (
    haal_data_op,
    toon_foutmelding,
    maak_menu_tabel,
    vraag_opslaan_favoriet,
    # toon_paginering
)
from urllib.parse import quote ## Zet spaties en speciale tekens om naar een geldige URL voor de API.
#API identificatie instellen
musicbrainzngs.set_useragent(
    "My Lyrics Finder",
    "1.0",
    EMAIL
)

#Stuur de ingevoerde artiestnaam naar MusicBrainz.
#dict = de functie geeft normaal een dictionary terug (resultaat)
#None = bij een fout geeft de functie None terug
def zoek_artiest(artiest_naam) -> dict | None:
    try:
        resultaat = musicbrainzngs.search_artists(
            artiest_naam,
            limit=100
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
        return None
    artiesten = resultaat["artist-list"]

#Haal de lijst met gevonden artiesten uit het resultaat.
#Zoekresultaten artiesten gefilterd op exacte artiestnaam
    console.print()
#len = tel hoeveel artiesten er zijn, als er geen artiest gevonden is, print in rood
    if len(artiesten) == 0:
# Gebruik centrale foutmelding voor consistente opmaak
        toon_foutmelding(
            "Geen artiesten gevonden."
        )
# FUNCTIE def toon_artiesten met return STOPPEN, onderstaande tabel wordt niet gemaakt.
        return None
    pagina = 0

    while True:
        console.clear()
        per_pagina = 10

        start = pagina * per_pagina
        einde = start + per_pagina

        pagina_artiesten = artiesten[start:einde]


#Linker tabel aanmaken en opmaken:deze tabel toont de eerste helft van de gevonden artiesten.
        linker_tabel = Table(
            border_style="bright_yellow",
            expand=True
        )

        linker_tabel.add_column("Nr", width=3)
        linker_tabel.add_column("Naam", width=10)
        linker_tabel.add_column("Type", width=10)
        linker_tabel.add_column(
            "Beschrijving",
            max_width=35,
            no_wrap=True,
            overflow="ellipsis"
        )

        rechter_tabel = Table(
            border_style="bright_yellow",
            expand=True
        )

        rechter_tabel.add_column("Nr", width=3)
        rechter_tabel.add_column("Naam", width=10)
        rechter_tabel.add_column("Type", width=10)
        rechter_tabel.add_column(
            "Beschrijving",
            max_width=35,
            no_wrap=True,
            overflow="ellipsis"
        )

        # Toon maximaal 10 resultaten verdeeld over twee kolommen.
#enumerate=voeg automatisch nummers toe,begin bij 1

        for nummer, artiest_musicbrainz in enumerate(
                pagina_artiesten[:5],
                start=start + 1
        ):
            linker_tabel.add_row(
                str(nummer),
                artiest_musicbrainz.get("name", "-"),
                artiest_musicbrainz.get("type", "-"),
                artiest_musicbrainz.get("disambiguation", "-")
            )

        for nummer, artiest_musicbrainz in enumerate(
                pagina_artiesten[5:10],
                start=start + 6
        ):
            rechter_tabel.add_row(
                str(nummer),
                artiest_musicbrainz.get("name", "-"),
                artiest_musicbrainz.get("type", "-"),
                artiest_musicbrainz.get("disambiguation", "-")
            )

# Toon beide tabellen naast elkaar in één panel.
        console.print(
            Panel(
                Columns(
                    [linker_tabel, rechter_tabel],
                    equal=True,
                    expand=False

                ),
                title=f"[bold bright_white]RESULTATEN VOOR {artiest_naam.upper()}[/bold bright_white]",
                title_align="center",
                border_style="bright_yellow",
                width=160,
            )
        )
# Toon hoeveel resultaten zijn gevonden en hoeveel resultaten
# op de huidige pagina zichtbaar zijn voor de gebruiker.
        totaal_paginas = (
                                 len(artiesten) + per_pagina - 1
                         ) // per_pagina

# Geef de gebruiker inzicht in het totaal aantal resultaten,
# de huidige pagina en het aantal getoonde resultaten.
        console.print(
            f"[bright_yellow]Aantal gevonden artiesten: {len(artiesten)}[/bright_yellow]"
        )

        console.print(
            f"[bright_yellow]Getoonde resultaten: {len(pagina_artiesten)}[/bright_yellow]"
        )

        console.print(
            f"[bright_yellow]Pagina {pagina + 1} van {totaal_paginas}[/bright_yellow]"
        )
        console.print(
            "\n[bold yellow][N][/bold yellow] Volgende pagina | "
            "[bold yellow][V][/bold yellow] Vorige pagina | "
            "[bold yellow][0][/bold yellow] Terug | "
            "[bold yellow][S][/bold yellow] Hoofdmenu"
        )

        console.print("1-10 = Artiest kiezen op deze pagina")

        keuze = console.input(
            "\nMaak keuze: "
        ).upper()
    #keuze maken
        if keuze.upper() == "N":
            if pagina < totaal_paginas - 1:
                pagina += 1
            else:
                console.print(
                    "[yellow]Dit is de laatste pagina.[/yellow]"
                )
            continue


        elif keuze.upper() == "V":

            if pagina > 0:

                pagina -= 1

            else:

                toon_foutmelding(
                    "Dit is de eerste pagina."
                )

            continue

        elif keuze == "0":
            return None

        elif keuze.upper() == "S":
            return "hoofdmenu"

        elif keuze.isdigit():
            keuze = int(keuze)
            if keuze < start + 1 or keuze > start + len(pagina_artiesten):
                toon_foutmelding(
                    "Ongeldige keuze"
                )
                return None

            if keuze > start + len(pagina_artiesten):
                toon_foutmelding(
                    "Ongeldige keuze"
                )
                continue

            gekozen_artiest = artiesten[keuze - 1]

            artiest_naam = gekozen_artiest["name"]
            artist_id = gekozen_artiest["id"]

            artiest, songtitel = toon_nummers_van_artiest(
                artist_id,
                artiest_naam
            )

            if artiest is None:
                continue

            resultaat_songtekst = toon_songtekst(
                artiest,
                songtitel
            )

            if resultaat_songtekst is None:
                continue

            break
        else:
            toon_foutmelding(
                "Ongeldige keuze"
            )
    return None

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
        console.clear()
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
            max_width=35,
            no_wrap=True,
            overflow="ellipsis"
        )
#BEGIN RECHTER TABEL: Rechter tabel aanmaken en opmaken. Deze tabel toont de tweede helft van de gevonden artiesten.
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
            max_width=35,
            no_wrap=True,
            overflow="ellipsis"
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


        console.print(
            "\n[bold yellow][N][/bold yellow] Volgende pagina | "
            "[bold yellow][V][/bold yellow] Vorige pagina | "
            "[bold yellow][0][/bold yellow] Terug | "
            "[bold yellow][S][/bold yellow] Hoofdmenu"
        )
        totaal_paginas = (len(works) + 19) // 20

        console.print(
            f"[bright_yellow]Aantal gevonden nummers: {len(works)}[/bright_yellow]")

        console.print(
            f"[bright_yellow]Pagina {pagina + 1} van {totaal_paginas}[/bright_yellow]")

        console.print("1-20 = Nummer kiezen op deze pagina")

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
                "[red]Ongeldige keuze[/red]")

    return None, None
def toon_songtekst(
        artiest_naam,
        songtitel,
        vraag_om_opslaan=True
) -> str | None:

# Zet spaties en speciale tekens om naar een veilige URL-notatie voor de lyrics API.
    veilige_artiest = quote(artiest_naam)
    veilige_titel = quote(songtitel)

# Gebruik de centrale configuratie voor de API-basis-URL.
# Hierdoor blijven instellingen gescheiden van programmalogica.
    url = f"{LYRICS_API_URL}{veilige_artiest}/{veilige_titel}"

    try:
# Ik gebruik de hulpfunctie uit m0010, zodat alle API-aanvragen en foutafhandeling op één centrale plek staan.

        data = haal_data_op(url)


# Stop de functie als de API geen gegevens terugstuurt
# Toon een nette foutmelding wanneer de songtekst niet beschikbaar is.
        if data is None:
            console.print(
                f"[red]Voor dit nummer is geen songtekst beschikbaar:[/red] "
                f"{artiest_naam} - {songtitel}"
            )

            console.input(
                "\nDruk op Enter om een ander nummer te kiezen..."
            )

            return None

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

# Gebruik een herbruikbare hulpfunctie voor de J/N-vraag,
# zodat dezelfde code niet meerdere keren geschreven hoeft te worden.
        if vraag_om_opslaan:
            if vraag_opslaan_favoriet(
                "Opslaan als favoriet?"
            ):
                sla_favoriet_op(
                    artiest_naam,
                    songtitel
                )


        console.input(
            "\nDruk op Enter om terug te gaan..."
        )
        return songtekst

    except Exception as fout:

        console.print(
            f"[bold red]Fout:[/bold red] {fout}"
        )
        return None
#OPSLAAN IN FAVORIETEN
def sla_favoriet_op(
        artiest_naam,
        songtitel
):
    with open(
            "m06_songteksten_favorieten.txt",
            "a",
            encoding="utf-8"
    ) as bestand:

        bestand.write(
            f"{artiest_naam} - {songtitel}\n"
        )

    console.print(
        "[green]Favoriet opgeslagen.[/green]"
    )
#TOON FAVORIETEN_______________________________
def toon_favorieten():

    try:

        with open(
                "m06_songteksten_favorieten.txt",
                "r",
                encoding="utf-8"
        ) as bestand:

            favorieten = bestand.readlines()

        if len(favorieten) == 0:

            console.print(
                "[yellow]Geen favorieten gevonden.[/yellow]"
            )
            return None

        linker_tabel = Table(
            border_style="bright_yellow"
        )

        linker_tabel.add_column("Nr", width=5)
        linker_tabel.add_column(
            "Favoriet",
            max_width=40,
            no_wrap=True,
            overflow="ellipsis"
        )

        rechter_tabel = Table(
            border_style="bright_yellow"
        )

        rechter_tabel.add_column("Nr", width=5)
        rechter_tabel.add_column(
            "Favoriet",
            max_width=40,
            no_wrap=True,
            overflow="ellipsis"
        )

        midden = (len(favorieten) + 1) // 2
        for nummer, favoriet in enumerate(
                favorieten[:midden],
                start=1
        ):
            linker_tabel.add_row(
                str(nummer),
                f"[cyan]{favoriet.strip()}[/cyan]"
            )

        for nummer, favoriet in enumerate(
                favorieten[midden:],
                start=midden + 1
        ):
            rechter_tabel.add_row(
                str(nummer),
                f"[cyan]{favoriet.strip()}[/cyan]"
            )
        console.print(
            Panel(
                Columns(
                    [linker_tabel, rechter_tabel],
                    equal=True,
                    expand=False
                ),
                title="[bold bright_white]OPGESLAGEN FAVORIETEN [/bold bright_white]",
                border_style="bright_yellow",
                width=160
            )
        )

    except FileNotFoundError:

        console.print(
            "[yellow]Nog geen favorieten opgeslagen.[/yellow]"
        )

#VERWIJDER FAVORIET
def verwijder_favoriet():

    with open(
            "m06_songteksten_favorieten.txt",
            "r",
            encoding="utf-8"
    ) as bestand:

        favorieten = bestand.readlines()
#bij foutieve keuze als er geen favorieten zijn, bestand is leeg
    if len(favorieten) == 0:
        console.print(
            "[yellow]Geen favorieten gevonden.[/yellow]"
        )
        return None

    tabel = Table(
        border_style="bright_yellow"
    )

    tabel.add_column(
        "Nr",
        justify="center",
        width=5
    )

    tabel.add_column(
        "Favoriet",
        overflow="ellipsis"
    )

    for nummer, favoriet in enumerate(
            favorieten,
            start=1
    ):
        tabel.add_row(
            str(nummer),
            favoriet.strip()
        )

    console.print(
        Panel(
            tabel,
            title="[bold bright_white]FAVORIET VERWIJDEREN[/bold bright_white]",
            border_style="bright_yellow"
        )
    )

    keuze = console.input(
        "\nNummer(s) om te verwijderen "
        "(bijv. 1,3,5 | 0 = Terug | S = Hoofdmenu): "
    ).upper()

    if keuze == "0":
        return None
    if keuze == "S":
        return "hoofdmenu"
    try:

        keuzes = sorted(
            {
                int(nummer.strip())
                for nummer in keuze.split(",")
            }
        )

    except ValueError:

        console.print(
            "[red]Voer geldige nummers in.[/red]"
        )
        return None

# Controleer of alle ingevoerde nummers bestaan.

    for nummer in keuzes:

        if nummer < 1 or nummer > len(favorieten):
            console.print(
                f"[red]Ongeldig nummer: {nummer}[/red]"
            )
            return None

    for te_verwijderen in sorted(
        keuzes,
        reverse=True
    ):
        del favorieten[te_verwijderen - 1]

    with open(
            "m06_songteksten_favorieten.txt",
            "w",
            encoding="utf-8"
    ) as bestand:
        bestand.writelines(
            favorieten
        )

    console.print(
        f"[green]{len(keuzes)} favoriet(en) verwijderd.[/green]"
    )
    console.input(
        "\nDruk op Enter om verder te gaan..."
    )
    return None

def zoek_nummer(songtitel) -> dict | None:

    try:

        resultaat = musicbrainzngs.search_recordings(
            recording=songtitel,
            limit = 100
        )

        return resultaat

    except Exception as fout:

        console.print(
            f"[bold red]Fout:[/bold red] {fout}"
        )

        return None

def zoek_nummer_menu():

    songtitel = console.input(
        "[bold white]Voer songtitel in: [/bold white]"
    ).strip()

    if songtitel == "":
        toon_foutmelding(
            "Voer een songtitel in."
        )
        return None

    resultaat = zoek_nummer(
        songtitel
    )

    if resultaat is None:
        return None

    nummers = resultaat.get(
        "recording-list",
        []
    )
# Toon zoekresultaten in pagina's van 10 nummers.
    pagina = 0
    per_pagina = 10

    if len(nummers) == 0:
        toon_foutmelding(
            "Geen nummers gevonden."
        )
        return None

    while True:

        start = pagina * per_pagina
        einde = start + per_pagina

        pagina_nummers = nummers[start:einde]
        midden = (len(pagina_nummers) + 1) // 2

        linker_tabel = Table(
            border_style="bright_yellow",
            expand=True
        )

        linker_tabel.add_column(
            "Nr",
            justify="center",
            width=5
        )

        linker_tabel.add_column(
            "Titel",
            overflow="ellipsis"
        )

        linker_tabel.add_column(
            "Artiest",
            overflow="ellipsis"
        )

        rechter_tabel = Table(
            border_style="bright_yellow",
            expand=True
        )

        rechter_tabel.add_column(
            "Nr",
            justify="center",
            width=5
        )

        rechter_tabel.add_column(
            "Titel",
            overflow="ellipsis"
        )

        rechter_tabel.add_column(
            "Artiest",
            overflow="ellipsis"
        )

        for nummer, opname in enumerate(
                pagina_nummers[:midden],
                start=start + 1
        ):
            artiest_lijst = opname.get(
                "artist-credit",
                []
            )

            artiest_naam = "-"

            if len(artiest_lijst) > 0:
                artiest_naam = artiest_lijst[0].get(
                    "name",
                    "-"
                )

            linker_tabel.add_row(
                str(nummer),
                opname.get(
                    "title",
                    "-"
                ),
                artiest_naam
            )

        for nummer, opname in enumerate(
                pagina_nummers[midden:],
                start=start + midden + 1
        ):
            artiest_lijst = opname.get(
                "artist-credit",
                []
            )

            artiest_naam = "-"

            if len(artiest_lijst) > 0:
                artiest_naam = artiest_lijst[0].get(
                    "name",
                    "-"
                )

            rechter_tabel.add_row(
                str(nummer),
                opname.get(
                    "title",
                    "-"
                ),
                artiest_naam
            )

        console.print(
            Panel(
                Columns(
                    [linker_tabel, rechter_tabel],
                    equal=True,
                    expand=False
                ),
                title=f"[bold bright_white]RESULTATEN VOOR {songtitel.upper()}[/bold bright_white]",
                border_style="bright_yellow",
                width=160
            )
        )
        console.print(
            f"[bright_yellow]Aantal gevonden nummers: {len(nummers)}[/bright_yellow]"
        )
        console.print(
            f"[bright_yellow]Getoonde resultaten: {len(pagina_nummers)}[/bright_yellow]"
        )
        console.print(
            "[bright_yellow]Kies een nummer voor de songtekst.[/bright_yellow]"
        )

        console.print()

        totaal_paginas = (
                                len(nummers) + per_pagina - 1
                        ) // per_pagina

        console.print(
            f"[bright_yellow]Pagina {pagina + 1} van {totaal_paginas}[/bright_yellow]"
        )

        console.print(
            "\n[bold yellow][N][/bold yellow] Volgende pagina | "
            "[bold yellow][V][/bold yellow] Vorige pagina | "
            "[bold yellow][0][/bold yellow] Terug | "
            "[bold yellow][S][/bold yellow] Hoofdmenu"
        )

        console.print(
            f"{start + 1}-{start + len(pagina_nummers)} = Nummer kiezen op deze pagina"
        )

        keuze = console.input(
            "\nMaak keuze: "
        )

        if keuze.upper() == "N":

            if pagina < totaal_paginas - 1:
                pagina += 1

            else:
                toon_foutmelding(
                    "Dit is de laatste pagina."
                )

            continue

        elif keuze.upper() == "V":

            if pagina > 0:
                pagina -= 1

            else:
                console.print(
                    "[yellow]Dit is de eerste pagina.[/yellow]"
                )
            continue

        if keuze == "0":
            return None
        if not keuze.isdigit():
            toon_foutmelding(
                "Ongeldige keuze"
            )

            continue
        keuze = int(keuze)
        if keuze < 1 or keuze > len(nummers):
            toon_foutmelding(
                "Ongeldige keuze"
            )
            continue

            return None
        gekozen_nummer = nummers[
            keuze - 1
            ]
        songtitel = gekozen_nummer.get(
            "title",
            "-"
        )
        artiest_lijst = gekozen_nummer.get(
            "artist-credit",
            []
        )
        if len(artiest_lijst) == 0:
            toon_foutmelding(
                "Geen artiest gevonden."
            )
            return None
        artiest_naam = artiest_lijst[0].get(
            "name",
            "-"
        )
        resultaat_songtekst = toon_songtekst(
            artiest_naam,
            songtitel
        )

        if resultaat_songtekst is None:
            continue

        return None

def toon_muziek_menu():
    console.clear()
    while True:
        submenu = maak_menu_tabel(45)

        submenu.add_row("1", "Zoek artiest")
        submenu.add_row("2", "Zoek nummer")
        submenu.add_row("0", "Terug")

        console.print(
        Panel(
        submenu,
        title="[bold bright_white]MUZIEK & SONGTEKSTEN[/bold bright_white]",
        title_align="center",
        border_style="bright_yellow",
        width=50,
        )
        )
        submenu_keuze = console.input(
            "\nMaak een keuze "
            "[bold yellow][0][/bold yellow] t/m "
            "[bold yellow][2][/bold yellow]: "
        ).strip()

        if submenu_keuze == "0":
            break

        if submenu_keuze == "1":
            console.print(
                "\n[bold yellow][0][/bold yellow] Terug | "
                "[bold yellow][S][/bold yellow] Hoofdmenu"
            )

            artiest_naam = console.input(
                "[bold white]Voer artiestnaam in: [/bold white]"
            )

            if artiest_naam == "0":
                continue

            if artiest_naam.upper() == "S":
                return

            resultaat = toon_artiesten(
                artiest_naam
            )

            if resultaat == "hoofdmenu":
                continue

        elif submenu_keuze == "2":
            zoek_nummer_menu()

        else:
            toon_foutmelding(
                "Ongeldige keuze"
            )
            continue

def toon_favorieten_menu():
    console.clear()
    while True:

        console.clear()
        submenu = maak_menu_tabel(50)

        submenu.add_row("1", "Favorieten bekijken")
        submenu.add_row("2", "Favoriet verwijderen")
        submenu.add_row("3", "Songtekst bekijken")
        submenu.add_row("0", "Terug")

        console.print(
            Panel(
                submenu,
                title="[bold bright_white]FAVORIETEN BEHEREN[/bold bright_white]",
                title_align="center",
                border_style="bright_yellow",
                width=50,
            )
        )
        # Vraag de gebruiker om een keuze uit het submenu.
        submenu_keuze = console.input(
            "\nMaak een keuze "
            "[bold yellow][0][/bold yellow] t/m "
            "[bold yellow][3][/bold yellow]: "
        ).strip()

        if submenu_keuze == "0":
            break

        if submenu_keuze == "1":

            toon_favorieten()

            console.input(
                "\nDruk op Enter om verder te gaan..."
            )
            continue

        elif submenu_keuze == "2":

            resultaat = verwijder_favoriet()

            if resultaat == "hoofdmenu":
                break

            continue



        elif submenu_keuze == "3":

            toon_favorieten()
            keuze = console.input(
                "\nVoer het nummer van een favoriet in: "
            )

            if not keuze.isdigit():
                toon_foutmelding(
                    "Ongeldige keuze"
                )
                continue

            with open(
                    "m06_songteksten_favorieten.txt",
                    "r",
                    encoding="utf-8"
            ) as bestand:

                favorieten = bestand.readlines()

            keuze = int(keuze)

            if keuze < 1 or keuze > len(favorieten):
                toon_foutmelding(
                    "Ongeldige keuze"
                )
                continue

            favoriet = favorieten[keuze - 1].strip()

            artiest_naam, songtitel = favoriet.split(
                " - ",
                maxsplit=1
            )

            toon_songtekst(
                artiest_naam,
                songtitel,
                vraag_om_opslaan=False
            )

            continue
        else:
            toon_foutmelding(
                "Ongeldige keuze"
            )
            continue
