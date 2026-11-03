# Ontwikkellog My Lyrics & Karaoke Finder

## Datum: 14-10-2026
⬜ M01_Main.py	Console()	Rich Console toegevoegd	Rich-opmaak gebruiken<br>
⬜ M01_Main.py	Keuze-validatie	Ongeldige invoer afgevangen, voldoen aan foutafhandeling<br>
⬜ Project	Structuur<br>
⬜ .gitignore/Configuratie/.venv, cache en Config uitgesloten<br>
⬜ Benodigde bibliotheken geinstalleerd(requests, musicbrainzngs en rich)<br>
⬜ Git repository geïnitialiseerd<br>
⬜ Eerste commit gemaakt: Dag 1 - Projectopstart, structuur bedacht <br>
⬜ Eerste tag gemaakt: 2026-10-14_opstart<br>
⬜ GitHub repository aangemaakt: janeoemar-wq/Eindopdracht_My_Lyrics_Karaoke_Finder<br>
⬜ GitHub gekoppeld<br>
⬜ Eerste push uitgevoerd<br>
 
## Datum: 15-10-2026

⬜ MusicBrainz koppelen<br>
⬜ M04_Config.py koppelen aan M02_Musicbrainz.py<br>
⬜ User-Agent instellen<br>
⬜ Functie muziek_zoeken() aanmaken<br>
⬜ Artiest invoeren<br>
⬜ MusicBrainz API aanroepen<br>
⬜ Gevonden artiesten ophalen<br>
⬜ Gevonden artiesten tonen in Rich Table<br>
⬜ Artiest laten kiezen<br>
⬜ Keuze valideren<br>
⬜ Gekozen artiest tonen in Rich Panel<br>
⬜ Testen op foutieve invoer<br>
⬜ Wijzigingen toevoegen aan ontwikkellog<br>

## Datum: 16-10-2026

⬜ Titel zoeken<br>
⬜ Songtekst ophalen via LRCLIB<br>
⬜ Songtekst tonen in Rich Panel <br>
⬜ Songtekst opslaan in JSON<br>
⬜ Opgeslagen nummers bekijken <br>
⬜ Karaokefunctie bouwen  <br>
⬜ Testen: Queen gekozen-> Panel: NUMMERS VAN -> 10 nummers tonen-> 1 t/m 10 = nummer kiezen  <br>
N = volgende 10 <br>
V = vorige 10  <br>
T = terug <br>

## Datum: 20-10-2026
Bestand: M02_Musicbrainz.py: Functie: toon_artiesten() <br>
⬜ Aangepast:Zoekopdrachten zoals 'Queen' toonden ook artiesten met 'queen' in een 
bijnaam of beschrijving, zoals Madonna ('Queen of Pop').<br>
⬜ Resultaten van MusicBrainz worden nu gefilterd op exacte overeenkomst met de 
ingevoerde artiestnaam. <br>
Hierdoor worden bij zoekopdrachten zoals 'Queen' geen artiesten meer getoond die het 
woord 'queen' alleen in een bijnaam of beschrijving hebben. <br>
⬜ Opmaak 2 kolommen tekst verdeeld <br>
* RESULTATEN VOOR ...<br>
* NUMMERS VAN ...<br>
* toekomstige LYRICS <br>
* toekomstige FAVORIETEN <br>

border_style="bright_yellow" <br>
Nr = vaste breedte 3- width=3 <br>
Naam = vaste breedte 10- width=10 <br>
Type = vaste breedte 10- width=10 <br>
Beschrijving = maximaal 20 tekens - max_width=20 <br>

Titel:max_width=35 <br>
Columns(<br>
    [linker_tabel, rechter_tabel],<br>
    equal=True,<br>
    expand=True)<br>

Panel<br>
title_align="center" <br>
border_style="bright_yellow" <br>
width=160 <br>

Verdeling links/rechts: midden = (len(artiesten) + 1) // 2
Opmaak:<br>
Linker en rechter tabel even breed <br>
Tabellen verdeeld over de volledige panelbreedte <br>
6 resultaten → 3 links / 3 rechts <br>
7 resultaten → 4 links / 3 rechts <br>
8 resultaten → 4 links / 4 rechts <br>
10 resultaten → 5 links / 5 rechts <br>

### Stap/Onderdeel: Songtekst ophalen
⬜ Stap/Onderdeel: Lyrics API gekoppeld
⬜ Functie/codeblok: toon_songtekst()
Aanpassing: Tweede webrequest toegevoegd met Lyrics.ovh. <br>
De gekozen artiest en songtitel worden gebruikt om automatisch de bijbehorende songtekst 
op te halen en weer te geven in een Rich Panel. <br>
De API gebruikt het endpoint https://api.lyrics.ovh/v1/{artist}/{title}.<br>
Reden: Om na het kiezen van een nummer direct de songtekst te kunnen tonen.
Resultaat: De songtekst van het gekozen nummer wordt succesvol opgehaald en weergegeven.

FAVORIETEN:
Stap 1A - Favorietenbestand aanmaken .txt <br>
Stap 1B - Testen <br>
Stap 1C - Functie aanroepen <br>

### Stap/Onderdeel:Favorieten opslaan <br>
Functie/codeblok: sla_favoriet_op() <br>
Aanpassing: gekozen artiest en songtitel worden opgeslagen in favorieten.txt.
Reden: om te voldoen aan de opdracht-eis om gegevens op te slaan in een lokaal bestand.
Resultaat: na het kiezen van "J" wordt het nummer toegevoegd aan favorieten.txt.

## Datum: 21-10-2026
### Hoofdmenu ombouwen
Hoofdmenu-> 2 -> 0 -> Programma stopt  NAAR:<br>
Hoofdmenu-> 2 -> Opgeslagen nummers-> 0 -> terug naar while -> Hoofdmenu opnieuw tonen <br>
ombouwen keuze 2 <br>
ombouwen keuze 1 <br>

⬜ Ja-pad voor opslaan favoriet opgenomen in flowchart<br>
⬜ Noteren wanneer ik dubbele codes programmeer<br>
Opletten voor dubbele code tussen Functionaliteit 1 (songtekst zoeken) en Functionaliteit 3 <br>
(karaoke zoeken) <br>


## Datum: 22-10-2026
⬜ Hernoemen van bestanden, consistent zijn in gebruik van functienamen, nummering, opmaak <br>
⬜ in de verschillende modules bepaalde imports ondergebracht naar M00_Imports.py <br>
(door te renamen worden wijzigingen overal doorgevoerd) <br>
⬜ M10_Helpers.py aangemaakt <br>
⬜ Verplaatsen van dubbele codes naar helperfuncties <br>
⬜ Begonnen met de karaokefunctie <br>

## Datum: 23-10-2026
⬜ Herstel en refactor van de MusicBrainz-module.Functie/codeblok <br>
toon_artiesten()                                                                      <br>
toon_nummers_van_artiest()                                                            <br>
zoek_artiest()                                                                        <br>

### Probleem en aanpassing                                                           <br>
⬜ Verkeerde inspringingen (if, elif, else) hersteld.                                <br>
⬜ Ontbrekende return-statements toegevoegd.                                         <br>
⬜ while True teruggeplaatst in toon_nummers_van_artiest().                          <br>
⬜ Foutieve else-structuren gecorrigeerd.                                            <br>
⬜ Meerdere syntaxfouten opgezocht en opgelost, bij elk wijzingn direct de errors 
begrijpen en oplossen:                                                              <br>
Unexpected indent                                                                    <br>
Py:ELSE_KEYWORD                                                                     <br>
Py:DEDENT                                                                            <br>
Missing return statement                                                              <br>
⬜ Nieuwe Git-commit en tag aangemaakt als herstelpunt.                              <br>
⬜ Dagelijks committen een een tag aanmaken wanneer code werkte                       <br>

## Datum: 26-10-2026
### Opmaak:
⬜ Gebruikersinterface consistent gemaakt door overal dezelfde notatie voor toetsen en 
keuzes toe te passen.                                                               <br>
⬜ Navigatieopties gewijzigd van ronde haakjes ( ) naar vierkante haakjes [ ] voor een 
uniforme uitstraling.                                                               <br>
⬜ Gele markering toegevoegd aan invoertoetsen zoals [0], [S], [N] en [V] zodat 
acties beter zichtbaar zijn.                                                        <br>
⬜ Invoerscherm voor artiesten aangepast naar een duidelijkere opmaak met aparte 
navigatieregels:                                                                    <br>
[0] Terug |                                                             <br>
[S] Hoofdmenu                                                           <br>

### Voer artiestnaam in:                                                                <br>
⬜ Zoekresultaten van artiesten verdeeld over pagina's voor een betere leesbaarheid. <br>
⬜ Paginering toegevoegd met opties voor volgende en vorige pagina.<br>
⬜ Extra gebruikersinformatie toegevoegd: <br>
totaal aantal gevonden resultaten; <br>
aantal getoonde resultaten; <br>
huidige pagina.<br>
⬜ Zoekresultaten overzichtelijk weergegeven in twee kolommen om meer gegevens 
tegelijk zichtbaar te maken.<br>
⬜ Navigatieteksten verduidelijkt met beschrijvingen zoals: <br>
1-10 = Artiest kiezen op deze pagina <br>
1-20 = Nummer kiezen op deze pagina <br>
⬜ Dubbele codeblokken en foutieve inspringingen verwijderd tijdens het opschonen 
van m01_main.py. <br>
⬜ Menustructuur gecontroleerd en hersteld zodat submenu's correct terugkeren naar het 
juiste scherm.<br>

### Functie Zoek nummer uitgebreid met:
⬜ zoeken op songtitel via MusicBrainz; <br>
⬜ tonen van de gevonden resultaten in een tabel;<br>
⬜ weergeven van de bijbehorende artiest;<br>
⬜ kiezen van een nummer uit de resultatenlijst;<br>
⬜ automatisch ophalen van de songtekst via Lyrics.ovh;<br>
⬜ mogelijkheid om de gekozen songtekst op te slaan als favoriet<br>
⬜ Gebruiksvriendelijkheid verbeterd door een consistente opmaak en navigatie in de 
gehele applicatie toe te passen.<br>

## Datum: 27-10-2026
### Hoofdmenu / Navigatie:
### Stap/Onderdeel: Refactor hoofdmenu
⬜ Functie/codeblok:             <br>
toon_muziek_menu()              <br>
toon_favorieten_menu()          <br>
toon_karaoke_menu()             <br>
Aanpassing:                     <br>
⬜ Submenu's uit m01_main.py verplaatst naar aparte functies in modules.<br>
⬜ Bestandsnamen gestandaardiseerd naar m00 t/m m10 structuur. Ter verbetering van de 
architectuur en onderhoudbaarheid.<br>
⬜ Uitbreiding favorietenbeheer <br>
⬜ Zoek nummer afgerond met artiestselectie
⬜ Zoek nummer afgerond
⬜ Zoek nummer resultatenlijst toegevoegd
⬜ Hoofdmenu refactor en bestandsnamen 
⬜ Herstel inspringing en return-statements MusicBrainz module
⬜ Herstel inspringing en return-statements MusicBrainz module
⬜ Rich tabelopmaak verbeterd

## Datum: 28-10-2026 
⬜ zoeken naar app om verantwoordingsvideo te maken <br>
⬜ keuze: clipcharm (onbekend ermee, tutorials gevolgd) <br>
⬜ Fix crashes bij favorietenbeheer en invoervalidatie
⬜ Karaoke module toegevoegd

## Datum: 29-10-2026
⬜ nieuw toegevoegd: karaoke_favorieten_bekijken
⬜ nieuw karaoke_favorieten_openen
⬜ utils_refactor (was helpersfunctie)

## Datum: 30-10-2026
### Projectbestanden definitief: naamgeving en nummering
* m01_main.py<br>
* m02_musicbrainz.py
* m03_karaoke.py
* m04_config.py
* m05_utils
* m06_songteksten_favorieten.txt
* m07_karaoke_favorieten.txt
* m08_opgeslagen_songteksten
* m09_fouten.log
* m10 requirements.txt
* m11_ontwikkellog.md

## Datum: 01-11-2026 
* m11_ontwikkellog.md bijgewerkt, opgemaakt en structuur aangbracht.

## Datum: 02-11-2026 
⬜ eerste video's opgenomen in clipchamp
⬜ 

## Datum: 03-11-2026 
⬜ 
## Datum: 04-11-2026 
⬜ 
## Datum: 05-11-2026 
⬜ 
## Datum: 06-11-2026 
⬜ 