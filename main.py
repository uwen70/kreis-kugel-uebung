"""
Grundprogramm: Kreis- und Kugelberechnungen

Aufgabe:
- Radius über input() abfragen
- Umfang des Kreises berechnen
- Flächeninhalt des Kreises berechnen
- Volumen der Kugel berechnen

Die drei Berechnungen sind in eigene Module ausgelagert.
Die Funktionen in den Modulen sind absichtlich noch nicht implementiert.
"""

from umfang import berechne_umfang
from flaecheninhalt import berechne_flaecheninhalt
from volumen import berechne_volumen


def main():
    radius = float(input("Bitte Radius eingeben: "))

    umfang = berechne_umfang(radius)
    flaeche = berechne_flaecheninhalt(radius)
    volumen = berechne_volumen(radius)

    print()
    print("--- Ergebnis ---")
    print(f"Radius: {radius}")
    print(f"Umfang des Kreises: {umfang}")
    print(f"Flächeninhalt des Kreises: {flaeche}")
    print(f"Volumen der Kugel: {volumen}")


if __name__ == "__main__":
    main()
