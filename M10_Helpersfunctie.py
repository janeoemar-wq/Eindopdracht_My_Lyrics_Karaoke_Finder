"""Om dubbele codes  te voorkomen heb ik deze functie gemaakt en worden ze door gebruikt om een songtekst en karaoke voeo te zoeken
console
"""
from M00_Imports import *



def vraag_artiest_en_titel():
    artiest = console.input("Artiest: ").strip()
    titel = console.input("Titel: ").strip()

    return artiest, titel


def haal_data_op(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        return None


def toon_foutmelding(tekst):
    console.print(
        Panel(
            tekst,
            title="Fout",
            border_style="red"
        )
    )

