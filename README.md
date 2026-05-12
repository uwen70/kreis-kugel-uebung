# Übungsaufgabe: Gemeinsames Arbeiten mit GitHub

## Ziel

Ein Python-Programm soll einen Radius abfragen und daraus berechnen:

1. Umfang eines Kreises
2. Flächeninhalt eines Kreises
3. Volumen einer Kugel

Die drei Berechnungen sind jeweils in eigene Module ausgelagert.

## Dateien

- `main.py` – Grundprogramm
- `umfang.py` – Modul für den Kreisumfang
- `flaecheninhalt.py` – Modul für den Flächeninhalt
- `volumen.py` – Modul für das Kugelvolumen

## Rollenverteilung

- Person 1: implementiert `berechne_umfang(radius)` in `umfang.py`
- Person 2: implementiert `berechne_flaecheninhalt(radius)` in `flaecheninhalt.py`
- Person 3: implementiert `berechne_volumen(radius)` in `volumen.py`

## Erwartete Formeln

- Umfang Kreis: `U = 2 * pi * r`
- Flächeninhalt Kreis: `A = pi * r ** 2`
- Volumen Kugel: `V = 4 / 3 * pi * r ** 3`

Hinweis: `pi` kann aus dem Modul `math` importiert werden:

```python
import math
```

## Arbeitsauftrag für Studierende

1. Forke das Ausgangsrepository.
2. Klone deinen Fork in VS Code.
3. Bearbeite nur das Modul, das dir zugeteilt wurde.
4. Teste das Programm lokal.
5. Committe und pushe deine Änderung in deinen Fork.
6. Erstelle einen Pull Request zum Ausgangsrepository.
7. Nachdem Pull Requests zusammengeführt wurden: Synchronisiere deinen Fork mit dem Ausgangsrepository.
