"""
m05_utils.py

Bevat herbruikbare hulpfuncties die door meerdere modules
worden gebruikt.

Door deze functies centraal op te slaan wordt dubbele code
voorkomen en blijft het project overzichtelijk en eenvoudiger
te onderhouden.

Voorbeelden:
- API-gegevens ophalen
- Foutmeldingen tonen
- Menu-tabellen maken
- Invoer van artiest en titel verwerken
- Bestanden inlezen
- Favorieten opslaan
"""
from m00_imports import *
import logging

# Configureer logging zodat technische fouten automatisch
# worden opgeslagen in het logbestand temp.log.
logging.basicConfig(
    filename="temp.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Vraag de gebruiker om een artiest en titel.
def vraag_artiest_en_titel():
    artiest = console.input("Artiest: ").strip()
    titel = console.input("Titel: ").strip()

    return artiest, titel

# Haal gegevens op via een API en verwerk eventuele fouten centraal.
def haal_data_op(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as fout:
# Sla technische fouten permanent op in het logbestand.
        logging.error(f"Fout bij ophalen van URL: {url} | {fout}")
        return None

# Toon een foutmelding in een rood Rich-panel voor een consistente opmaak.
def toon_foutmelding(tekst):
    console.print(
        Panel(
            tekst,
            title="Fout",
            border_style="red"
        )
    )

# voor de tabellen en panels gebruik ik dezelfde opmaak in:
# Hoofdmenu
# Muziek & Songteksten
# Favorieten beheren
# Karaoke
def maak_menu_tabel(breedte=50):

    tabel = Table(
        border_style="bright_yellow",
        width=breedte
    )

    tabel.add_column(
        "Keuze",
        justify="center"
    )

    tabel.add_column(
        "Actie"
    )

    return tabel

# Gebruik één centrale functie voor de J/N-vraag bij het opslaan
# van songtekst- en karaokefavorieten. Hiermee wordt dubbele code voorkomen.
def vraag_opslaan_favoriet(tekst):
    return console.input(
        f"\n{tekst} (J/N): "
    ).strip().upper() == "J"

# Lees alle regels uit een bestand en geef deze terug als lijst,
# zodat dezelfde bestandsinleescode niet herhaald hoeft te worden.
def lees_bestand(bestandsnaam):
    with open(
        bestandsnaam,
        "r",
        encoding="utf-8"
    ) as bestand:
        return bestand.readlines()