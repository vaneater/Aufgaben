# Diese Funktion macht nichts und muss abgebrochen werden,
# ich komme leider nicht darauf wieso.

def binary(k):
    # Liste initialisieren
    bits= []

    # Solange die Zahl über 1 liegt...
    while k > 1:
        # die Zahl halbieren
        b = k/2
        # prüfen, ob b+1 = k ist
        if b*2+1 == k:
            # "1" in die Liste hinzufügen
            bits.append(1)
        elif b*2 == k:
            # "0" in die Liste hinzufügen
            bits.append(0)
    k = k/2

    # Liste spiegeln, da die Reihenfolge sonst falsch ist
    bits.reverse()

    # Liste ausgeben
    print("Die Zahl " + k + "in Binär ist ")
    for x in bits(len(a)):
        print
        a[x]

    # Anzahl der Bits ausgeben
    print("Die Zahl " + k + "hat " + len(bits) + "Bits. ")
