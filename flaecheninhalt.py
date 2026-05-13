



import math

"""
Modul für die Berechnung des Flächeninhalts eines Kreises.

Formel:
A = pi * r²
"""

def berechne_flaecheninhalt(radius):
    if radius < 0:
        raise ValueError("Der Radius kann nicht negativ sein.")
    
    return math.pi * (radius ** 2)


if __name__ == "__main__":
    try:
        eingabe = input("Welchen Radius hat dein Kreis? ")
        r = float(eingabe)
        
        ergebnis = berechne_flaecheninhalt(r)
        
        print(f"Der Flächeninhalt eines Kreises mit Radius {r} beträgt: {ergebnis:.2f}")
        
    except ValueError as e:
        if "negativ" in str(e):
            print("Fehler: Ein Kreis kann keinen negativen Radius haben.")
        else:
            print("Fehler: Bitte gib eine gültige Zahl ein.")



       
        
    
