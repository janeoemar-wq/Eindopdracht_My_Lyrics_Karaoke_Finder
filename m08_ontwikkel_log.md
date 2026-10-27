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

Verdeling links/rechts: midden = (len(artiesten) + 1) // 2
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

FAVORIETYN:
Stap 1A - Favorietenbestand aanmaken txt
Stap 1B - Testen
Stap 1C - Functie aanroepen

Hoofdmenu ombouwen op 21 okt van:
Hoofdmenu
↓
2
↓
0
↓
Programma stopt
                  NAAR:
Hoofdmenu
↓
2
↓
Opgeslagen nummers
↓
0
↓
terug naar while
↓
Hoofdmenu opnieuw tonen

ombouwen keuze 2
ombouwen keuze 1

Voor het bouwen van de functioanleit , rekeneninggehouden met advies docent:
Voor je ontwikkellog kun je noteren

Feedback docent:

GO ontvangen op ontwerp.
Ja-pad voor opslaan favoriet explicieter opnemen in flowchart.
Opletten voor dubbele code tussen Functionaliteit 1 (songtekst zoeken) en Functionaliteit 3 (karaoke zoeken).
Waar mogelijk functies hergebruiken.

Mijn advies: die tip over dubbele code gaan we straks echt gebruiken wanneer we Karaoke bouwen. Dan kunnen we bestaande zoekfuncties hergebruiken in plaats van alles opnieuw te programmeren. Dat scoort meestal ook beter op het beoordelingspunt efficiënte code / functies gebruiken

22 oktober:
✅ Hernoem bestanden
✅ Laat programma weer starten
✅ Vul M00_Imports.py
✅ Maak M10_Helpers.py
✅ Verplaats dubbele code naar helperfuncties
✅ Daarna verder met de karaokefunctie

23 okt
Herstel en refactor van de MusicBrainz-module.Functie/codeblok
toon_artiesten()
toon_nummers_van_artiest()
zoek_artiest()

Aanpassing en waarom
Verkeerde inspringingen (if, elif, else) hersteld.
Ontbrekende return-statements toegevoegd.
while True teruggeplaatst in toon_nummers_van_artiest().
Foutieve else-structuren gecorrigeerd.
Twee kolommen voor artiestresultaten behouden tijdens de refactor.
Meerdere syntaxfouten opgelost waardoor PyCharm meldingen gaf zoals:
Unexpected indent
Py:ELSE_KEYWORD
Py:DEDENT
Missing return statement
Code opnieuw geformatteerd en getest.
Nieuwe Git-commit en tag aangemaakt als herstelpunt.

26-10

Voor je ontwikkellog kun je dit kort en professioneel noteren:

Gebruikersinterface consistent gemaakt door overal dezelfde notatie voor toetsen en keuzes toe te passen.
Navigatieopties gewijzigd van ronde haakjes ( ) naar vierkante haakjes [ ] voor een uniforme uitstraling.
Gele markering toegevoegd aan invoertoetsen zoals [0], [S], [N] en [V] zodat beschikbare acties beter zichtbaar zijn.
Invoerscherm voor artiesten aangepast naar een duidelijkere opmaak met aparte navigatieregels:
[0] Terug | [S] Hoofdmenu
Voer artiestnaam in:
Zoekresultaten van artiesten verdeeld over pagina's voor een betere leesbaarheid.
Paginering toegevoegd met opties voor volgende en vorige pagina.

Extra gebruikersinformatie toegevoegd:
totaal aantal gevonden resultaten;
aantal getoonde resultaten;
huidige pagina.


Zoekresultaten overzichtelijk weergegeven in twee kolommen om meer gegevens tegelijk zichtbaar te maken.

Navigatieteksten verduidelijkt met beschrijvingen zoals:
1-10 = Artiest kiezen op deze pagina
1-20 = Nummer kiezen op deze pagina
Dubbele codeblokken en foutieve inspringingen verwijderd tijdens het opschonen van m01_main.py.
Menustructuur gecontroleerd en hersteld zodat submenu's correct terugkeren naar het juiste scherm.

Functie Zoek nummer uitgebreid met:

zoeken op songtitel via MusicBrainz;
tonen van de gevonden resultaten in een tabel;
weergeven van de bijbehorende artiest;
kiezen van een nummer uit de resultatenlijst;
automatisch ophalen van de songtekst via Lyrics.ovh;
mogelijkheid om de gekozen songtekst op te slaan als favoriet

Gebruiksvriendelijkheid verbeterd door een consistente opmaak en navigatie in de gehele applicatie toe te passen.

Datum: 27-10-2026
Fase flowchart:
Hoofdmenu / Navigatie
Stap/Onderdeel:
Refactor hoofdmenu
Functie/codeblok:
toon_muziek_menu()
toon_favorieten_menu()
toon_karaoke_menu()
Aanpassing:
Submenu's uit m01_main.py verplaatst naar aparte functies in modules.
Bestandsnamen gestandaardiseerd naar m00 t/m m10 structuur.
Waarom:
Verbetering van de architectuur, onderhoudbaarheid en scheiding van verantwoordelijkheden.