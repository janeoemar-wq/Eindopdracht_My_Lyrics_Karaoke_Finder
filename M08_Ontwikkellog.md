# Ontwikkellog My Lyrics & Karaoke Finder
## Projectbestanden
### M01_Main.py
### M02_Musicbrainz.py
### M03_Karaoke.py
### M04_Config.py
### M05_requirements.txt
### M06_opgeslagen_songteksten.json
### M07_fouten.log
### M08_Ontwikkellog.md

✅ Klaar
❌ Niet klaar
⬜ Nog doen
☑ Afgerond
☐ Openstaand

# Ontwikkellog My Lyrics & Karaoke Finder
## Datum: 14-10-2026
✅ M01_Main.py	Console()	Rich Console toegevoegd	Rich-opmaak gebruiken
✅ M01_Main.py	Keuze-validatie	Ongeldige invoer afgevangen	Voldoen aan foutafhandeling
✅ Project	Structuur
✅ .gitignore/Configuratie/.venv, cache en Config uitgesloten/M05_requirements.txt	Packages
✅Benodigde bibliotheken geinstalleerd(requests, musicbrainzngs en rich).

✅ Git repository geïnitialiseerd

✅ Eerste commit gemaakt
   • Dag 1 - Projectopstart, structuur bedacht

✅ Eerste tag gemaakt
   • 2026-10-14_opstart

✅ GitHub repository aangemaakt
   • janeoemar-wq/Eindopdracht_My_Lyrics_Karaoke_Finder

⬜ GitHub gekoppeld

⬜ Eerste push uitgevoerd
==================================================
TODO - VOLGENDE WERKDAG
==================================================
⬜ MusicBrainz koppelen
⬜ M04_Config.py koppelen aan M02_Musicbrainz.py
⬜ User-Agent instellen
⬜ Functie muziek_zoeken() aanmaken
⬜ Artiest invoeren
⬜ MusicBrainz API aanroepen
⬜ Gevonden artiesten ophalen
⬜ Gevonden artiesten tonen in Rich Table
⬜ Artiest laten kiezen
⬜ Keuze valideren
⬜ Gekozen artiest tonen in Rich Panel
⬜ Testen op foutieve invoer
⬜ Wijzigingen toevoegen aan ontwikkellog

En als alles meezit, kun je daarna beginnen aan:

==================================================
TODO - DAARNA
==================================================
⬜ Titel zoeken
⬜ Songtekst ophalen via LRCLIB
⬜ Songtekst tonen in Rich Panel 
⬜ Songtekst opslaan in JSON
⬜ Opgeslagen nummers bekijken
⬜ Karaokefunctie bouwen


16 oktober:

Queen gekozen
↓
Panel: NUMMERS VAN QUEEN
↓
10 nummers tonen
↓
1 t/m 10 = nummer kiezen
N = volgende 10
V = vorige 10
T = terug

20 okt:
Bestand: M02_Musicbrainz.py
Functie: toon_artiesten()
Aangepast:Zoekopdrachten zoals 'Queen' toonden ook artiesten met 'queen' in een bijnaam of beschrijving, zoals Madonna ('Queen of Pop').
Resultaten van MusicBrainz worden nu gefilterd op exacte overeenkomst met de ingevoerde artiestnaam. 
Hierdoor worden bij zoekopdrachten zoals 'Queen' geen artiesten meer getoond die het woord 'queen' alleen in 
een bijnaam of beschrijving hebben.

# OPmaak 2 kolommen tekst verdeeld 

RESULTATEN VOOR ...
NUMMERS VAN ...
toekomstige LYRICS
toekomstige FAVORIETEN

border_style="bright_yellow"
Nr = vaste breedte 3- width=3
Naam = vaste breedte 10- width=10
Type = vaste breedte 10- width=10

Beschrijving = maximaal 20 tekens - max_width=20
Titel:max_width=35
Columns(
    [linker_tabel, rechter_tabel],
    equal=True,
    expand=True)

Panel
title_align="center"
border_style="bright_yellow"
width=160

Verdeling links/rechts: midden = (len(resultaten) + 1) // 2
daardoor:
Linker en rechter tabel even breed
Tabellen verdeeld over de volledige panelbreedte
6 resultaten → 3 links / 3 rechts
7 resultaten → 4 links / 3 rechts
8 resultaten → 4 links / 4 rechts
10 resultaten → 5 links / 5 rechts 

Fase: Songtekst ophalen

Stap/Onderdeel: Lyrics API gekoppeld

Functie/codeblok: toon_songtekst()

Aanpassing: Tweede webrequest toegevoegd met Lyrics.ovh. De gekozen artiest en songtitel worden gebruikt om automatisch de bijbehorende songtekst op te halen en weer te geven in een Rich Panel. De API gebruikt het endpoint https://api.lyrics.ovh/v1/{artist}/{title}.

Waarom: Om na het kiezen van een nummer direct de songtekst te kunnen tonen.

Resultaat: De songtekst van het gekozen nummer wordt succesvol opgehaald en weergegeven.

Status: het werkt!!!!

Stap/Onderdeel:
Favorieten opslaan

Functie/codeblok:
sla_favoriet_op()

Aanpassing:
Gekozen artiest en songtitel worden opgeslagen in favorieten.txt.

Waarom:
Voldoen aan de opdracht-eis om gegevens op te slaan in een lokaal bestand.

Resultaat:
Na het kiezen van "J" wordt het nummer toegevoegd aan favorieten.txt.

Status:
Werkend