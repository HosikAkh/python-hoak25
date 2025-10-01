"""
Loopar:
1. For loop, fortsätter utföra ett arbete tills villkoren är uppfylld. While-loop, fortsätter så länge villkoren stämmer.
2. Den fortsätter att utföras om och om igen.
3. Det går, och huvud loop skall fortsätta upprepa eller köra loopen inom sig.
4. Break avbryter processen när villkoret är uppfylld, medan continue hoppar över loopen beroende på villkoren.
5. Ja, 

Exempel:
min_lista = ["äpple", "banan", "körsbär"]
for frukt in min_lista:
    print(frukt)

Felhantering:
1. Exception är en felhanterings funktion som körs vid ett villkort exempelvis ValueError.
2. Att med try-except kan man utföra annan jobb om koden stöter på ett problem, medan i vanliga fall den avbryts och skickar error.

Pseudokod:
1. Det används och är språk för att förklara logiken och algoritmer som inte följer programmeringspråkets specifika syntax.
2. Nej, samma svar som i fråga ett.

Hur kod funkar:
1.  range(5) -> 0,1,2,3,4
    range(1,5) -> 1,2,3,4
2. Beror på, den kan fånga alla fel och error som koden stöter på, och oftast blir det svårt att identifiera specifika för oss problemet. 
Ibland kan den även fortsätta köras oavsett error eller likt.

Tolka kod:
1. Output: 2 4 6 8
2. Output:  0: h
            0: e
            0: j
            1: h
            1: e
            1: j
Första for loopen kör den 0, 1, två gången. Loop i loopen kör igenom varje bokstav i texten.
3. e funkar som variabel för felmedellandet som skall skrivas ut tillsammans med felet.
4. 
    1. Slutvärde blir 6
    2. Villkoret är inte uppfylld, och värdet är mindre än 0.
    3. första omgång 10, andra omgång 3, tredje omgång 7, sist men inte minst fjärde omgång 6
"""
import random

print(f"\nUPPGIFTER: \nFörsta uppgift:\n")
print(f"Välkommen till gissa talet. Du har 8 försök på dig att gissa slumpmässiga talet.")

slump = random.randint(0, 100) #slumpmässigt tal mellan 0 till 100.
antal_försök = 0
max_försök = 8
gissning = None

while gissning != slump and antal_försök < max_försök:
    try:
        gissning = int(input("Ange ett tal mellan 0 till 100: "))
        antal_försök += 1

        print(f"Antal försök kvar: {max_försök - antal_försök}")

        if gissning < slump:
            print("För lågt!")
        elif gissning > slump:
            print("För högt!")
        else:
            print(f"Grattis! Du har gissat rätt på {antal_försök} försök!")
    except ValueError:
        print("Fel: Skriv in ett heltal snälla!")

if gissning != slump:
    print("Tyvärr du har slut på försök.")
