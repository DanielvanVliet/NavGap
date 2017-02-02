NavGap Indoors Navigatiesysteem

Het programma maakt gebruik van linux commando's en een linux os is dus vereist

De volgende python modules zijn vereist en moeten geïnstalleerd worden op de pi:
tkinter
subprocess

Op de pi moet git staan en het project moet worden gecloned naar de pi.
Ook is er een scherm / vnc vereist om de tkinter gui te weergeven (als het op de pi gedraaid wordt)

Om het navigatiesysteem op te stellen moet het volgende gebeuren:
Indien er met database gewerkt wordt moet de database aangesloten zijn op de navgapapp; hostname en username en password moeten ingevoerd worden in de navgapapp.
Er moeten nodes geplaatst worden op de locatie en de afstanden tussen andere nodes moeten overeenkomen met de gegevens in de navgapapp.
De nodes moeten ieder een eigen wifi-ssid uitzenden.

Om de applicatie te starten zonder database moet navgapapp_v6.py afgespeeld worden.
Om de applicatie te starten met database moet navgapapp_v7.py afgespeeld worden. (Hierbij moet wel de database aangesloten zijn en er moet data in staan)
