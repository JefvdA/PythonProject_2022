# Wat is dit project?
Dit project is gemaakt voor een schoolopdracht (2021-2022) voor AP Hogeschool. Opleidingsonderdeel "Python development"
Het is een app die de werking van de velo-fietsjes in Antwerpen nabootst.

# Hoe uitvoeren?
De app kan gestart worden door het python script "main.py" in de directory "app" te runnen.

Er kunnen ook volgende command-line arguments meegegeven worden:
- **-s [multiplier]**  : dit zal direct een simulatie starten, zonder eerst het hele menu te tonen. [multiplier] is optional, hiermee kan de snelheid van de simulatie gekozen worden, default zal dit 1 zijn.

# Features:
De state van de app wordt ook opgeslagen zodat het bij volgend gebruik terug geladen kan worden indien gewenst.

De app is uitgerust met een cli interface, waardoor de gebruiker makkelijk via menu's acties in de app kan ondernemen.

## Acties als user
Een user kan:
- Een fiets uit een station halen
- Een fiets terugbrengen naar een station

## Acties als transporteur
Een transporteur kan:
- Een fiets uit een station halen
- Een fiets terugbrengen naar een station

Het verschil is dat een transporteur een maximum van 10 fietsen kan bijhouden, vergeleken met een user die er maar 1 kan bijhouden.

## Genereren van logs
Doorheen de app worden logs bijgehouden van verschillende acties, zoals ophalen en terugbrengen van een fiets.

De gebruiker kan er ook voor kiezen een static site te genereren die deze logs mooi zal laten zien.

De static site houd in:
- lijst van alle stations
- per station een lijst met alle logs die voor dit station bijgehouden zijn

## Simuleren van de applicatie
Indien de gebruiker niet alles manueel wilt ingeven, kan er ook een simulatie gestart worden.
De gebruiker kan dan kiezen aan welke snelheid deze simulatie moet runnen.

De simulatie houd in:
- Elke 5 seconden zal een user een fiets gaan halen / terugbrengen uit een station
- Elke 10 seconden zal een transporteur een station gaan legen of vullen, dit hangt af van hoe vol een station zit.

**De simulatie kan ook gestart worden met volgend command-line argument: "-s [multiplier]" , met [multiplier] zijnde de snelheid van de simulatie**

# Keuzes
Doorheen het project heb ik keuze's moeten maken.
Zoals je in de "app" folder kan zien is het project in heel veel files onderverdeeld, op deze manier was het makkelijk te weten waar een function zich zal bevinden indien ik deze moest veranderen, ook is de app nu makkelijk uit te breiden.
Zo is de app state bijgehouden in de class VeloApp, dit is dan ook de class die gepickled wordt om de state van de applicatie bij te houden.
Ik heb ook gekozen om "repositories" te maken, dit is een python class die een list bevat (BV "Users" voor "User"), maar deze class heeft ook functions die de list kan aanpassen. Zo heeft de Users class bijvoorbeeld een function om nieuwe users te genereren, op deze manier zijn er weer heel wat functions die we uit de VeloApp klasse kunnen weghouden.

# Werking
## Menu's
Menu's werken in mijn applicatie op volgende manier:

Eerst is er een "tool" die ik heb toegevoegd genoemd "menu_generator" deze bevat een class Menu, die door simpel een list van strings met verschillende options, heel snel een Menu generated, op deze manier is het dus heel makkelijk een nieuw menu scherm te maken, aangezien heel wat boilerplate code niet meer geschreven moet worden.

In de "screens" directory worden de verschillende menu's bijgehouden. Elke menu heeft dus een list van strings met verschillende options, en gebruikt dus de "menu_generator" om snel een menu te maken. Het is dan deze menu zelf die de input van de user gaat verwerken en weet wat er moet gebeuren bij verschillende user inputs.

## Tool's
Zoals al eerder aangekaart is er een "menu_generator" maar er zijn ook andere "tools"

Deze worden bijgehouden in de dirtory "tools":
- cli_tools : bevat functions zoals "clear", wat platform-independant de console zal clearen, en "wait_for_enter" wat gewoon zal wachten tot de user enter, of een andere toets heeft ingedrukt. Ook is er een method "get_user_input" die voegt " >>>" toe aan een message, aangezien dat in mijn applicatie een universele manier is om aan te tonen dat de app input verwacht (>>>)
- html_generator : bevat "generator", deze heeft een function "generate_html_file" die html als string ontvangt, en een file met deze html aanmaakt. In de "views" directory zitten dan weer de files die verantwoordelijk zijn om verschillende soorten html string te genereren, zo is er eentje voor stations_lists (homepage van de static site) en eentje voor (station_log) die de log van een bepaald station toont.
- logger : deze klasse is verantwoordelijk voor het bijhouden van de logs. Hij houd ook rekening met de tijd wanneer de log plaatsvond, en past deze ook aan wanneer de simulatie runt.
- menu_generator : Dit is al uitgelegd onder het puntje Menu's
- name_generator : Deze "tool" bevat in de file "generator" heel wat functions die het mogelijk maken om namen te genereren. Het haalt heel wat voornamen en achternamen uit JSON files en mixt deze om een groot aanbod van namen te geven. De reden dat deze file zoveel ongebruikte functions heeft is omdat ik aan het experimenteren was met een package te uploaden naar pypi, en ik wou dus ook wat extra functionaliteit meegeven, buiten enkel het genereren van volledige namen (voornaam + achternaam)

# Main application files
- main.py : Dit is het script dat de gebruiker moet runnen. Dit zorgt dat de juiste menu's getoond worden, checkt voor command-line arguments, en creert ook de VeloApp class.
- velo_app.py : Dit is eigenlijk het hoofd van de applicatie, hier wordt ook de state bijgehouden. De klasse is zelf verantwoordelijk voor het inlezen van starterdata ("initialize()") en het uitlezen van opgeslagen data uit de pickle file ("load_data()"), alsook het opslagen naar een pickle file ("save_data()")
- constants.py : Dit is gewoon een file die heel wat constanten bevat die op meerdere plekken nodig zijn. Op het moment zijn dit enkel paths die nodig zijn. Door "os.path.join(dirname" wordt er op een mooie manier met paths gewerkt, dit werkt ook op zowel windows als unix systemen.
- simulator.py : Kijk bij volgend puntje "Simulator"

# Simulator
Dit is de simulator klasse, die is verantwoordelijk voor het simuleren van acties binnen de VeloApp.

De klasse maakt gebruikt van threading, aangezien met behulp van "sleep" gewerkt wordt, en we ook nog steeds moeten luisteren naar user input.
De klasse heeft een function "start()" die de thread start, en wacht op een input van de user vooraleer deze weer te stoppen.

De function "run_simulation" zal elke "cycle" van de simulatie voorstellen, bij default zal er 1 seconde gewacht worden tussen cycles, voor real-time voor te stellen. Maar dit kan aangepast worden door de meegegeven snelheid.

## User actions
User actions in de simulatie werken als volgt, elke 5 seconden:

Er is 50 / 50 kans dat er een fiets wordt teruggebracht, of een fiets wordt weggenomen.
Daarna wordt er een random user opgehaald, met of zonder fiets, naargelang de action die uitgevoerd moet worden.
Tot slot zal de user de fiets terugbrengen, of wegnemen uit het station.

## Transporteur actions
Transporteur actions in de simulatie werken als volgt, elke 10 seconden:

Het percentage fietsen wordt opgehaald voor een random station. Nu zijn er twee mogelijkheden:
1. Als er meer dan 75% volle slots zijn, en het max aantal transporteurs (4) nog niet overschreden is, dan zal deze transporteur de helft van de fietsen (of zoveel hij kan) meenemen uit het station.
2. Als er minder dan 25% volle slots zijn, en er een actieve transporteur (een die fietsen heeft) beschikbaar is, dan zal deze transporteur de helft van zijn fietsen (of minstens 8) wegzetten bij het station.

## Resultaten simulatie
Wanneer ik de simulatie laat draaien voor heel wat tijd, +- 2u (in simulatie tijd), geeft dit toch al een heel realistisch beeld.

De transporteurs doen denk ik ook zeker hun job goed, aangezien alle stations ongeveer gelijk verdeeld lijken.

# Moeilijkheden
Een probleem waar ik wel tegen viel, en wat ik ook niet heb kunnen oplossen is de tijd van logs bijhouden wanneer een simulatie geweest is.

Wanneer je op het moment de simulatie 3u laat draaien (in simulatie tijd) en daarna manuele acties gaat uitvoeren, dan zullen de logs van deze manuele acties nog steeds de echte tijd (datetime.now()) weergeven, en voer je dus eigenlijk de acties "in het verleden" uit.
Eerst wou ik proberen ervoor te zorgen dat wanneer een simulatie geweest is, je ook vanaf de zogezegde tijd na de simulatie verder gaat loggen bij manuele acties, maar dit nam heel veel tijd in beslag omdat alles in heel veel files is bijgehouden.

# Conclusie
Ik denk dat ik soms ook gewoon teveel files heb aangemaakt, en dat ik teveel probeerde te programmeren zoals in andere talen en me meer moest aanpassen aan python.
Ik denk wel dat als ik dit project opnieuw zou maken dit al heel wat beter zal gaan, aangezien het me echt wel veel heeft bijgeleerd.

Met andere woorden was het dus een leuk project om te maken!











