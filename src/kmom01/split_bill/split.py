# Fösta push
x = int(input("Vad är summan på notan?\n"))
y = int(input("Hur många personer ska dela på nota?\n"))

if y <= 0:
    print("Varning! Antal personer måste vara minst 1.")
else:
    z = x/y
    print(f"Varje person ska betala {z}")
