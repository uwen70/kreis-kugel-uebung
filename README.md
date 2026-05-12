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

---

# Vorbereitung in VS Code

## 1. Git installieren

VS Code hat zwar eine eingebaute Oberfläche für Quellcodeverwaltung, benötigt aber ein installiertes Git auf dem Rechner.

### Windows

1. Git herunterladen und installieren: https://git-scm.com/download/win
2. Während der Installation können die Standardoptionen übernommen werden.
3. Danach VS Code vollständig schließen und neu öffnen.
4. Prüfung im Terminal:

```bash
git --version
```

Wenn eine Versionsnummer erscheint, ist Git korrekt installiert.

## ⚠️ Ergänzung: 🔹 Git ohne Adminrechte (Pool-PCs)

Falls keine Installation möglich ist:

### Option 1: Portable Git (empfohlen)

1. Download: https://git-scm.com/download/win  
2. ZIP-Datei entpacken, z. B. nach:

    C:\Users\Schueler\Tools\Git

3. VS Code öffnen  
4. Test im Terminal:

    git --version

Falls Git nicht erkannt wird, kann es direkt gestartet werden über:

    ...\Git\cmd\git.exe

### Option 2: GitHub-Weboberfläche (Notlösung)

Falls Git lokal nicht funktioniert:

- Dateien direkt im Browser bearbeiten  
- Änderungen committen  
- Pull Request erstellen  

⚠️ Einschränkung:  
- kein lokales Arbeiten mit Git möglich  
- nur eingeschränkt für die Übung geeignet

---
## 2. Benötigte VS-Code-Erweiterungen installieren

Öffne in VS Code links den Bereich **Extensions / Erweiterungen** oder drücke:

```text
Strg + Shift + X
```

Installiere folgende Erweiterungen:

### Pflicht

1. **Python**  
   Herausgeber: Microsoft  
   Zweck: Python-Dateien ausführen, Syntaxhervorhebung, Interpreter-Auswahl

2. **GitHub Pull Requests**  
   Herausgeber: GitHub / Microsoft  
   Zweck: Anmeldung bei GitHub, Pull Requests ansehen und bearbeiten

### Optional, aber hilfreich

3. **Git Graph**  
   Zweck: Grafische Darstellung von Branches und Commits

4. **GitLens**  
   Zweck: Bessere Übersicht über Änderungen, Autorinnen/Autoren und Historie

## 3. Bei GitHub in VS Code anmelden

1. In VS Code links auf das GitHub-Symbol klicken.
2. Auf **Sign in** klicken.
3. Anmeldung im Browser bestätigen.
4. Danach zurück zu VS Code wechseln.

---

# Eigenen Fork als neues Projekt in VS Code einbinden

## Schritt 1: Repository auf GitHub forken

1. Öffne das Ausgangsrepository des Dozenten auf GitHub.
2. Klicke oben rechts auf **Fork**.
3. Erstelle den Fork in deinem eigenen GitHub-Konto.

Danach besitzt du eine eigene Kopie des Repositories.

## Schritt 2: URL des eigenen Forks kopieren

1. Öffne deinen Fork auf GitHub.
2. Klicke auf den grünen Button **Code**.
3. Wähle **HTTPS**.
4. Kopiere die URL.

Beispiel:

```text
https://github.com/dein-benutzername/kreis-kugel-uebung.git
```

## Schritt 3: Repository in VS Code klonen

1. Öffne VS Code.
2. Drücke:

```text
Strg + Shift + P
```

3. Suche nach:

```text
Git: Clone
```

4. Füge die kopierte GitHub-URL ein.
5. Wähle einen lokalen Ordner aus, z. B.:

```text
Dokumente/PythonKurs
```

6. Wenn VS Code fragt, ob das geklonte Repository geöffnet werden soll: **Open** wählen.

Jetzt ist der Fork als neues Projekt in VS Code geöffnet.

## Schritt 4: Python-Datei testen

Öffne das Terminal in VS Code:

```text
Terminal > New Terminal
```

Starte das Programm:

```bash
python main.py
```

Falls `python` nicht funktioniert, versuche:

```bash
py main.py
```

## Schritt 5: Eigene Aufgabe bearbeiten

Bearbeite nur die Datei, die dir zugeteilt wurde:

- Person 1: `umfang.py`
- Person 2: `flaecheninhalt.py`
- Person 3: `volumen.py`

Beispiel für eine Implementierung:

```python
import math

def berechne_umfang(radius):
    return 2 * math.pi * radius
```

## Schritt 6: Änderungen speichern, committen und pushen

1. Datei speichern.
2. Links in VS Code auf **Source Control / Quellcodeverwaltung** klicken.
3. Geänderte Datei mit **+** vormerken.
4. Commit-Nachricht eintragen, z. B.:

```text
Implementiere Umfangberechnung
```

5. Auf **Commit** klicken.
6. Danach auf **Sync Changes** oder **Push** klicken.

## Schritt 7: Pull Request auf GitHub erstellen

1. Öffne deinen Fork auf GitHub.
2. Klicke auf **Compare & pull request**.
3. Beschreibe kurz deine Änderung.
4. Klicke auf **Create pull request**.

Der Dozent kann deinen Pull Request prüfen und zusammenführen.

---

# Fork nach dem Zusammenführen synchronisieren

Nachdem Pull Requests im Ausgangsrepository zusammengeführt wurden, muss der eigene Fork aktualisiert werden.

## Variante über GitHub-Webseite

1. Öffne deinen Fork auf GitHub.
2. Klicke auf **Sync fork**.
3. Klicke auf **Update branch**.

## Danach in VS Code aktualisieren

1. Öffne dein Projekt in VS Code.
2. Öffne das Terminal.
3. Führe aus:

```bash
git pull
```

Jetzt enthält dein lokales Projekt die neuen Änderungen aus deinem Fork.

---

# Häufige Fehler

## Fehler: VS Code zeigt keine Git-Funktionen

Mögliche Ursachen:

- Git ist nicht installiert.
- VS Code wurde nach der Git-Installation nicht neu gestartet.
- Der Projektordner ist kein Git-Repository.
- Es wurde nur ein ZIP entpackt, aber kein Repository geklont.

## Fehler: Änderungen können nicht gepusht werden

Mögliche Ursachen:

- Du arbeitest im Ausgangsrepository statt in deinem Fork.
- Du bist nicht bei GitHub angemeldet.
- Du hast keine Berechtigung für das Repository.

## Fehler: Programm gibt `None` aus

Ursache:

- Eine Funktion enthält noch `pass`.
- Die Funktion berechnet noch keinen Wert mit `return`.
