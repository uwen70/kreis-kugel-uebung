# Lehrbrief: Grundlagen von JSON und Verarbeitung mit Python

## 1. Einordnung des Themas

JSON steht für **JavaScript Object Notation**. Es handelt sich um ein textbasiertes Datenformat, mit dem strukturierte Daten gespeichert und zwischen Programmen ausgetauscht werden können.

JSON ist heute eines der wichtigsten Austauschformate in der Softwareentwicklung. Es wird besonders häufig verwendet bei:

- Webschnittstellen und APIs,
- Konfigurationsdateien,
- Datenaustausch zwischen Frontend und Backend,
- mobilen Apps,
- Datenexporten,
- NoSQL-Datenbanken,
- Automatisierungen und Skripten.

JSON ist kompakter als XML und für Menschen meist gut lesbar. Gleichzeitig lässt es sich von Programmen sehr einfach verarbeiten. Deshalb ist JSON in vielen modernen Anwendungen das Standardformat für den Datenaustausch.

Typische Beispiele aus der Praxis sind:

- Wetterdaten einer API,
- Produktlisten aus einem Webshop,
- Einstellungen einer Anwendung,
- Benutzerprofile,
- Messwerte von Sensoren,
- Antworten von KI- oder Cloud-Diensten.

---

## 2. Lernziele

Nach der Bearbeitung dieses Lehrbriefs sollen Studierende:

1. den grundlegenden Aufbau von JSON verstehen,
2. Objekte, Arrays, Schlüssel und Werte unterscheiden können,
3. die wichtigsten JSON-Datentypen kennen,
4. gültiges und ungültiges JSON erkennen können,
5. JSON-Daten mit Python einlesen und auswerten können,
6. Python-Datenstrukturen in JSON speichern können,
7. typische Fehler beim Arbeiten mit JSON erkennen und beheben können,
8. JSON und XML grundsätzlich vergleichen können.

---

## 3. Grundidee von JSON

JSON beschreibt Daten mithilfe von **Schlüssel-Wert-Paaren**.

Ein sehr einfaches Beispiel:

```json
{
    "name": "Anna Müller",
    "alter": 21
}
```

Dieses JSON-Dokument beschreibt eine Person. Die Person hat einen Namen und ein Alter.

Die Struktur lässt sich so lesen:

| Schlüssel | Wert |
|---|---|
| `name` | `Anna Müller` |
| `alter` | `21` |

Der Schlüssel steht links, der Wert rechts. Zwischen Schlüssel und Wert steht ein Doppelpunkt.

```json
"name": "Anna Müller"
```

Mehrere Schlüssel-Wert-Paare werden durch Kommas getrennt.

```json
{
    "name": "Anna Müller",
    "alter": 21,
    "stadt": "Chemnitz"
}
```

---

## 4. Aufbau einer JSON-Datei

Eine JSON-Datei enthält strukturierte Daten. Die wichtigsten Bausteine sind:

- Objekte,
- Arrays,
- Schlüssel,
- Werte,
- Datentypen.

### 4.1 Objekte

Ein JSON-Objekt wird mit geschweiften Klammern geschrieben.

```json
{
    "name": "Anna Müller",
    "alter": 21
}
```

Ein Objekt enthält Schlüssel-Wert-Paare.

Der Schlüssel muss in doppelten Anführungszeichen stehen:

```json
"name"
```

Der Wert kann unterschiedliche Datentypen haben, zum Beispiel Text, Zahl, Wahrheitswert, Objekt oder Array.

### 4.2 Arrays

Ein Array ist eine Liste von Werten. Arrays werden mit eckigen Klammern geschrieben.

```json
[
    "Chemnitz",
    "Dresden",
    "Leipzig"
]
```

Ein Array kann auch mehrere Objekte enthalten.

```json
[
    {
        "name": "Anna Müller",
        "alter": 21
    },
    {
        "name": "Max Schneider",
        "alter": 24
    }
]
```

Das ist in der Praxis sehr häufig: Eine Datei enthält nicht nur eine Person, sondern eine Liste von Personen, Produkten, Bestellungen oder Messwerten.

### 4.3 Schlüssel

Ein Schlüssel beschreibt, welche Information gespeichert wird.

Beispiel:

```json
{
    "produktname": "Kugelschreiber",
    "preis": 1.49
}
```

Die Schlüssel heißen hier:

```text
produktname
preis
```

Wichtig:

- Schlüssel müssen in doppelten Anführungszeichen stehen.
- Schlüssel sollten innerhalb eines Objekts eindeutig sein.
- Schlüssel sollten sprechende Namen haben.

Nicht empfehlenswert:

```json
{
    "x": "Kugelschreiber",
    "y": 1.49
}
```

Besser:

```json
{
    "produktname": "Kugelschreiber",
    "preis": 1.49
}
```

### 4.4 Werte

Ein Wert ist die konkrete gespeicherte Information.

```json
{
    "name": "Anna Müller",
    "alter": 21,
    "aktiv": true
}
```

Die Werte sind:

| Schlüssel | Wert |
|---|---|
| `name` | `"Anna Müller"` |
| `alter` | `21` |
| `aktiv` | `true` |

---

## 5. JSON-Datentypen

JSON kennt nur wenige, aber sehr wichtige Datentypen.

| Datentyp | Beispiel | Bedeutung |
|---|---|---|
| String | `"Anna"` | Text |
| Number | `21` oder `1.49` | Zahl |
| Boolean | `true` oder `false` | Wahrheitswert |
| null | `null` | kein Wert |
| Object | `{ "name": "Anna" }` | strukturierter Datensatz |
| Array | `[1, 2, 3]` | Liste |

### 5.1 String

Ein String ist Text. Strings stehen in doppelten Anführungszeichen.

```json
{
    "name": "Anna Müller"
}
```

Falsch wäre:

```json
{
    "name": 'Anna Müller'
}
```

JSON erlaubt keine einfachen Anführungszeichen für Strings.

### 5.2 Number

Zahlen werden ohne Anführungszeichen geschrieben.

```json
{
    "alter": 21,
    "preis": 1.49
}
```

Wenn eine Zahl in Anführungszeichen steht, ist sie aus Sicht von JSON ein Text.

```json
{
    "alter": "21"
}
```

Das ist nicht immer falsch, aber für Berechnungen ungünstig. Python müsste diesen Text erst in eine Zahl umwandeln.

### 5.3 Boolean

Boolean-Werte beschreiben Wahrheitswerte.

```json
{
    "aktiv": true,
    "bezahlt": false
}
```

Wichtig: In JSON heißen die Werte kleingeschrieben:

```json
true
false
```

Nicht gültig sind:

```json
True
False
```

Das ist eine häufige Fehlerquelle, weil Python `True` und `False` mit Großbuchstaben schreibt.

### 5.4 null

`null` bedeutet, dass kein Wert vorhanden ist.

```json
{
    "telefon": null
}
```

Das kann bedeuten:

- Die Information ist unbekannt.
- Die Information wurde noch nicht erfasst.
- Für dieses Feld gibt es keinen passenden Wert.

Auch hier ist die Schreibweise wichtig:

```json
null
```

Nicht gültig ist:

```json
None
```

`None` ist der entsprechende Wert in Python, aber nicht in JSON.

### 5.5 Objekt

Ein Objekt kann weitere Daten gruppieren.

```json
{
    "name": "Anna Müller",
    "adresse": {
        "strasse": "Hauptstraße 12",
        "plz": "09111",
        "ort": "Chemnitz"
    }
}
```

Das Objekt `adresse` enthält weitere Schlüssel-Wert-Paare.

### 5.6 Array

Ein Array speichert mehrere Werte.

```json
{
    "faecher": [
        "Informatik",
        "Mathematik",
        "Englisch"
    ]
}
```

Ein Array kann auch Objekte enthalten.

```json
{
    "personen": [
        {
            "name": "Anna Müller",
            "alter": 21
        },
        {
            "name": "Max Schneider",
            "alter": 24
        }
    ]
}
```

---

## 6. Regeln für gültiges JSON

JSON ist streng. Kleine Schreibfehler führen schnell dazu, dass eine Datei nicht gelesen werden kann.

Wichtige Regeln sind:

1. Schlüssel müssen in doppelten Anführungszeichen stehen.
2. Strings müssen in doppelten Anführungszeichen stehen.
3. Zwischen Schlüssel und Wert steht ein Doppelpunkt.
4. Mehrere Einträge werden durch Kommas getrennt.
5. Nach dem letzten Eintrag steht kein Komma.
6. Es gibt keine Kommentare.
7. Wahrheitswerte heißen `true` und `false`.
8. Ein leerer Wert heißt `null`.

### 6.1 Doppelte Anführungszeichen

Richtig:

```json
{
    "name": "Anna Müller"
}
```

Falsch:

```json
{
    name: "Anna Müller"
}
```

Falsch:

```json
{
    "name": 'Anna Müller'
}
```

### 6.2 Kommas zwischen Einträgen

Richtig:

```json
{
    "name": "Anna Müller",
    "alter": 21,
    "stadt": "Chemnitz"
}
```

Falsch:

```json
{
    "name": "Anna Müller"
    "alter": 21
}
```

Hier fehlt ein Komma nach `"Anna Müller"`.

### 6.3 Kein Komma nach dem letzten Eintrag

Richtig:

```json
{
    "name": "Anna Müller",
    "alter": 21
}
```

Falsch:

```json
{
    "name": "Anna Müller",
    "alter": 21,
}
```

Das letzte Komma ist in JSON nicht erlaubt.

### 6.4 Keine Kommentare

In JSON sind Kommentare nicht erlaubt.

Falsch:

```json
{
    "name": "Anna Müller",
    // Alter der Person
    "alter": 21
}
```

Wenn Erklärungen benötigt werden, müssen sie als normale Datenfelder gespeichert werden oder außerhalb der JSON-Datei dokumentiert werden.

---

## 7. Beispiel einer vollständigen JSON-Datei

Speichern Sie die folgende Datei unter dem Namen:

```text
produkte.json
```

Inhalt:

```json
{
    "produkte": [
        {
            "artikelnummer": "A1001",
            "name": "Kugelschreiber",
            "kategorie": "Bürobedarf",
            "preis": 1.49,
            "lagerbestand": 250
        },
        {
            "artikelnummer": "A1002",
            "name": "Notizbuch",
            "kategorie": "Bürobedarf",
            "preis": 3.99,
            "lagerbestand": 120
        },
        {
            "artikelnummer": "A1003",
            "name": "Taschenrechner",
            "kategorie": "Technik",
            "preis": 12.99,
            "lagerbestand": 35
        }
    ]
}
```

Das Wurzelelement aus XML gibt es in JSON nicht in derselben Form. Häufig verwendet man aber ein äußeres Objekt, das die Daten sinnvoll benennt.

In diesem Beispiel enthält das äußere Objekt den Schlüssel:

```text
produkte
```

Der Wert zu diesem Schlüssel ist ein Array mit mehreren Produktobjekten.

---

## 8. JSON und Python-Datenstrukturen

JSON passt sehr gut zu Python, weil sich JSON-Daten direkt auf wichtige Python-Datenstrukturen abbilden lassen.

| JSON | Python |
|---|---|
| Object | Dictionary (`dict`) |
| Array | Liste (`list`) |
| String | String (`str`) |
| Number | Integer (`int`) oder Float (`float`) |
| true | `True` |
| false | `False` |
| null | `None` |

Beispiel JSON:

```json
{
    "name": "Anna Müller",
    "alter": 21,
    "aktiv": true
}
```

Nach dem Einlesen in Python entsteht daraus sinngemäß:

```python
{
    "name": "Anna Müller",
    "alter": 21,
    "aktiv": True
}
```

Man erkennt den wichtigen Unterschied:

- JSON schreibt `true`,
- Python schreibt `True`.

Beim Einlesen übernimmt die Python-Bibliothek diese Umwandlung automatisch.

---

## 9. JSON mit Python einlesen

Python enthält mit dem Modul `json` bereits eine Standardbibliothek für JSON.

Sie muss nicht zusätzlich installiert werden.

### 9.1 JSON-Datei einlesen

```python
import json

with open("produkte.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

print(daten)
```

Erläuterung:

```python
import json
```

Das Modul `json` wird importiert.

```python
with open("produkte.json", "r", encoding="utf-8") as datei:
```

Die Datei wird zum Lesen geöffnet. Die Angabe `encoding="utf-8"` ist wichtig, damit Umlaute korrekt verarbeitet werden.

```python
daten = json.load(datei)
```

Die JSON-Datei wird eingelesen und in Python-Datenstrukturen umgewandelt.

```python
print(daten)
```

Die eingelesenen Daten werden ausgegeben.

### 9.2 Auf einzelne Daten zugreifen

Nach dem Einlesen kann man wie mit Dictionaries und Listen arbeiten.

```python
import json

with open("produkte.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

produkte = daten["produkte"]

for produkt in produkte:
    print(produkt["name"])
```

Ausgabe:

```text
Kugelschreiber
Notizbuch
Taschenrechner
```

Erläuterung:

```python
produkte = daten["produkte"]
```

Aus dem Dictionary `daten` wird der Wert zum Schlüssel `produkte` gelesen. Dieser Wert ist eine Liste.

```python
for produkt in produkte:
```

Die Schleife durchläuft jedes Produkt in der Liste.

```python
print(produkt["name"])
```

Aus jedem Produkt-Dictionary wird der Wert zum Schlüssel `name` ausgegeben.

### 9.3 Mehrere Felder ausgeben

```python
import json

with open("produkte.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

for produkt in daten["produkte"]:
    artikelnummer = produkt["artikelnummer"]
    name = produkt["name"]
    preis = produkt["preis"]

    print(artikelnummer, name, preis)
```

Mögliche Ausgabe:

```text
A1001 Kugelschreiber 1.49
A1002 Notizbuch 3.99
A1003 Taschenrechner 12.99
```

### 9.4 Zahlenwerte verarbeiten

JSON-Zahlen werden in Python automatisch zu Zahlen. Deshalb kann man direkt mit ihnen rechnen.

```python
import json

with open("produkte.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

gesamtwert = 0

for produkt in daten["produkte"]:
    preis = produkt["preis"]
    lagerbestand = produkt["lagerbestand"]

    wert = preis * lagerbestand
    gesamtwert += wert

print("Gesamter Lagerwert:", gesamtwert)
```

Mögliche Ausgabe:

```text
Gesamter Lagerwert: 1338.85
```

Im Unterschied zu XML muss hier nicht erst aus Text eine Zahl gemacht werden, sofern die JSON-Datei den Preis auch wirklich als Zahl enthält.

### 9.5 Nach Daten filtern

Im folgenden Beispiel werden nur Produkte aus der Kategorie `Bürobedarf` ausgegeben.

```python
import json

with open("produkte.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

for produkt in daten["produkte"]:
    if produkt["kategorie"] == "Bürobedarf":
        print(produkt["name"])
```

Ausgabe:

```text
Kugelschreiber
Notizbuch
```

---

## 10. JSON mit Python schreiben

Python kann nicht nur JSON-Dateien lesen, sondern auch neue JSON-Dateien erzeugen.

### 10.1 Python-Daten als JSON speichern

```python
import json

daten = {
    "personen": [
        {
            "id": "P1",
            "name": "Anna Müller",
            "alter": 21,
            "stadt": "Chemnitz"
        },
        {
            "id": "P2",
            "name": "Max Schneider",
            "alter": 24,
            "stadt": "Dresden"
        }
    ]
}

with open("personen.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, ensure_ascii=False, indent=4)
```

Dieses Programm erzeugt eine Datei `personen.json`.

Wichtige Parameter:

| Parameter | Bedeutung |
|---|---|
| `ensure_ascii=False` | Umlaute werden lesbar gespeichert |
| `indent=4` | JSON wird eingerückt und dadurch gut lesbar |

Ohne `indent=4` würde die Datei in einer langen Zeile gespeichert. Das ist für Programme in Ordnung, aber für Menschen schlecht lesbar.

### 10.2 Neue Daten hinzufügen

Im nächsten Beispiel wird eine vorhandene Datei eingelesen, eine neue Person ergänzt und anschließend eine neue Datei gespeichert.

Ausgangsdatei `personen.json`:

```json
{
    "personen": [
        {
            "id": "P1",
            "name": "Anna Müller",
            "alter": 21,
            "stadt": "Chemnitz"
        },
        {
            "id": "P2",
            "name": "Max Schneider",
            "alter": 24,
            "stadt": "Dresden"
        }
    ]
}
```

Python-Programm:

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

neue_person = {
    "id": "P3",
    "name": "Lisa Weber",
    "alter": 19,
    "stadt": "Leipzig"
}

daten["personen"].append(neue_person)

with open("personen_neu.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, ensure_ascii=False, indent=4)
```

Erläuterung:

```python
daten["personen"].append(neue_person)
```

Die neue Person wird an die Liste `personen` angehängt.

### 10.3 Daten verändern

Im folgenden Beispiel wird das Alter einer Person geändert.

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

for person in daten["personen"]:
    if person["id"] == "P1":
        person["alter"] = 22

with open("personen_geaendert.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, ensure_ascii=False, indent=4)
```

Dieses Programm:

1. liest die Datei `personen.json`,
2. sucht die Person mit der ID `P1`,
3. ändert das Alter auf `22`,
4. speichert das Ergebnis in `personen_geaendert.json`.

---

## 11. JSON-Strings und JSON-Dateien

JSON kann als Datei vorliegen oder als Text in einem Programm.

### 11.1 JSON aus einer Datei lesen

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)
```

Hier wird `json.load()` verwendet.

### 11.2 JSON aus einem String lesen

```python
import json

json_text = '{"name": "Anna Müller", "alter": 21}'

daten = json.loads(json_text)

print(daten["name"])
```

Ausgabe:

```text
Anna Müller
```

Hier wird `json.loads()` verwendet.

### 11.3 Unterschied zwischen `load` und `loads`

| Funktion | Bedeutung |
|---|---|
| `json.load(datei)` | liest JSON aus einer geöffneten Datei |
| `json.loads(text)` | liest JSON aus einem String |
| `json.dump(daten, datei)` | schreibt JSON in eine Datei |
| `json.dumps(daten)` | erzeugt einen JSON-String |

Beispiel mit `json.dumps()`:

```python
import json

person = {
    "name": "Anna Müller",
    "alter": 21
}

json_text = json.dumps(person, ensure_ascii=False, indent=4)

print(json_text)
```

Mögliche Ausgabe:

```json
{
    "name": "Anna Müller",
    "alter": 21
}
```

---

## 12. Typische Fehler beim Arbeiten mit JSON

### Fehler 1: Ein Komma fehlt

Fehlerhafte JSON-Datei:

```json
{
    "name": "Anna Müller"
    "alter": 21
}
```

Nach `"Anna Müller"` fehlt ein Komma.

Korrekt:

```json
{
    "name": "Anna Müller",
    "alter": 21
}
```

### Fehler 2: Komma nach dem letzten Eintrag

Fehlerhaft:

```json
{
    "name": "Anna Müller",
    "alter": 21,
}
```

Korrekt:

```json
{
    "name": "Anna Müller",
    "alter": 21
}
```

### Fehler 3: Einfache statt doppelte Anführungszeichen

Fehlerhaft:

```json
{
    'name': 'Anna Müller'
}
```

Korrekt:

```json
{
    "name": "Anna Müller"
}
```

### Fehler 4: Python-Schreibweise in JSON

Fehlerhaft:

```json
{
    "aktiv": True,
    "telefon": None
}
```

Korrekt:

```json
{
    "aktiv": true,
    "telefon": null
}
```

### Fehler 5: Datei nicht gefunden

```python
with open("produkte.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)
```

Wenn die Datei nicht im gleichen Ordner liegt wie das Python-Programm, entsteht ein Fehler.

Mögliche Lösungen:

- Dateinamen prüfen,
- Datei in den richtigen Ordner legen,
- vollständigen oder relativen Pfad angeben.

### Fehler 6: Schlüssel existiert nicht

```python
print(person["telefon"])
```

Wenn der Schlüssel `telefon` nicht vorhanden ist, entsteht ein Fehler.

Robustere Variante:

```python
telefon = person.get("telefon")

if telefon is not None:
    print(telefon)
else:
    print("Keine Telefonnummer vorhanden")
```

Die Methode `.get()` ist nützlich, wenn ein Schlüssel fehlen könnte.

### Fehler 7: Falscher Datentyp

Angenommen, in der JSON-Datei steht:

```json
{
    "alter": "21"
}
```

Dann ist `alter` ein String und keine Zahl.

Wenn gerechnet werden soll, muss der Wert umgewandelt werden:

```python
alter = int(daten["alter"])
```

Besser ist es aber, die Zahl direkt als Zahl zu speichern:

```json
{
    "alter": 21
}
```

---

## 13. JSON Schema

### 13.1 Warum braucht man ein Schema?

JSON beschreibt Daten, prüft aber nicht automatisch, ob diese Daten fachlich sinnvoll sind.

Beispiel:

```json
{
    "name": "Kugelschreiber",
    "preis": "teuer"
}
```

Diese JSON-Datei kann syntaktisch gültig sein. Fachlich ist sie aber problematisch, weil `preis` vermutlich eine Zahl sein sollte.

Ein Schema kann festlegen:

- Welche Felder sind erlaubt?
- Welche Felder sind Pflichtfelder?
- Welche Datentypen müssen verwendet werden?
- Welche Wertebereiche sind zulässig?
- Dürfen zusätzliche Felder vorkommen?

### 13.2 Einfaches JSON-Schema

Ein JSON Schema für ein Produkt könnte so aussehen:

```json
{
    "type": "object",
    "properties": {
        "artikelnummer": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "preis": {
            "type": "number"
        },
        "lagerbestand": {
            "type": "integer"
        }
    },
    "required": [
        "artikelnummer",
        "name",
        "preis"
    ]
}
```

Dieses Schema sagt:

- Das Produkt ist ein Objekt.
- `artikelnummer` ist ein String.
- `name` ist ein String.
- `preis` ist eine Zahl.
- `lagerbestand` ist eine ganze Zahl.
- `artikelnummer`, `name` und `preis` sind Pflichtfelder.

### 13.3 Passende JSON-Datei

```json
{
    "artikelnummer": "A1001",
    "name": "Kugelschreiber",
    "preis": 1.49,
    "lagerbestand": 250
}
```

### 13.4 Nicht passende JSON-Datei

```json
{
    "artikelnummer": "A1001",
    "name": "Kugelschreiber",
    "preis": "teuer"
}
```

Hier ist `preis` ein String. Das Schema erwartet aber eine Zahl.

### 13.5 Validierung mit Python

Für JSON-Schema-Validierung benötigt man meist eine zusätzliche Bibliothek.

Installation:

```bash
pip install jsonschema
```

Ein einfaches Beispiel:

```python
from jsonschema import validate

produkt = {
    "artikelnummer": "A1001",
    "name": "Kugelschreiber",
    "preis": 1.49,
    "lagerbestand": 250
}

schema = {
    "type": "object",
    "properties": {
        "artikelnummer": {"type": "string"},
        "name": {"type": "string"},
        "preis": {"type": "number"},
        "lagerbestand": {"type": "integer"}
    },
    "required": ["artikelnummer", "name", "preis"]
}

validate(instance=produkt, schema=schema)

print("Die Daten sind gültig.")
```

Für den Einstieg ist JSON Schema noch kein Pflichtstoff. Es ist aber wichtig zu verstehen, warum reine Syntaxprüfung nicht ausreicht.

---

## 14. JSON und XML im Vergleich

JSON und XML können beide strukturierte Daten darstellen. Trotzdem unterscheiden sie sich deutlich.

| Kriterium | JSON | XML |
|---|---|---|
| Grundstruktur | Objekte und Arrays | Elemente und Attribute |
| Lesbarkeit | meist kompakt und übersichtlich | oft ausführlicher |
| Datentypen | einfache Datentypen vorhanden | Inhalte meist Text, Typprüfung über Schema |
| Kommentare | nicht erlaubt | möglich |
| Attribute | nicht vorhanden | vorhanden |
| Reihenfolge | bei Arrays wichtig | bei Elementen oft wichtig |
| Schemata | JSON Schema | DTD, XSD |
| Python-Einstieg | sehr einfach mit `json` | gut mit `ElementTree` |
| typische Verwendung | Web-APIs, Konfigurationen, Apps | Standards, Dokumentformate, Behörden- und Industrieformate |

### 14.1 Beispiel: gleiche Daten in JSON

```json
{
    "person": {
        "id": "P1",
        "name": "Anna Müller",
        "alter": 21,
        "stadt": "Chemnitz"
    }
}
```

### 14.2 Beispiel: gleiche Daten in XML

```xml
<person id="P1">
    <name>Anna Müller</name>
    <alter>21</alter>
    <stadt>Chemnitz</stadt>
</person>
```

JSON ist meist kürzer. XML kann dafür mit Elementen, Attributen, Namespaces und Schemata sehr genau modellieren.

Eine einfache Orientierung:

| Situation | Häufig passende Wahl |
|---|---|
| Web-API | JSON |
| Konfigurationsdatei für moderne Anwendung | JSON |
| Dokumentformat mit komplexer Struktur | XML |
| Datenaustausch mit Behördenstandard | häufig XML |
| einfache Datenliste für Python | JSON |
| stark regulierte Schnittstelle mit XSD | XML |

---

## 15. Übungsaufgaben

### Aufgabe 1: JSON lesen

Erstellen Sie die Datei `personen.json` mit folgendem Inhalt:

```json
{
    "personen": [
        {
            "id": "P1",
            "name": "Anna Müller",
            "alter": 21,
            "stadt": "Chemnitz"
        },
        {
            "id": "P2",
            "name": "Max Schneider",
            "alter": 24,
            "stadt": "Dresden"
        },
        {
            "id": "P3",
            "name": "Lisa Weber",
            "alter": 19,
            "stadt": "Leipzig"
        }
    ]
}
```

Schreiben Sie ein Python-Programm, das alle Namen ausgibt.

Erwartete Ausgabe:

```text
Anna Müller
Max Schneider
Lisa Weber
```

### Aufgabe 2: ID und Name ausgeben

Erweitern Sie das Programm aus Aufgabe 1 so, dass zusätzlich die jeweilige ID ausgegeben wird.

Erwartete Ausgabe:

```text
P1 Anna Müller
P2 Max Schneider
P3 Lisa Weber
```

### Aufgabe 3: Durchschnittsalter berechnen

Schreiben Sie ein Programm, das das Durchschnittsalter aller Personen berechnet.

Hinweis:

```python
alter = person["alter"]
```

Mögliche Ausgabe:

```text
Durchschnittsalter: 21.333333333333332
```

Zusatz: Runden Sie das Ergebnis auf eine Nachkommastelle.

### Aufgabe 4: Personen nach Stadt filtern

Schreiben Sie ein Programm, das nur Personen aus `Chemnitz` ausgibt.

Beispielausgabe:

```text
Anna Müller wohnt in Chemnitz.
```

### Aufgabe 5: Neue Person hinzufügen

Schreiben Sie ein Programm, das der Datei eine weitere Person hinzufügt:

```text
ID: P4
Name: Tom Fischer
Alter: 22
Stadt: Zwickau
```

Speichern Sie das Ergebnis in einer neuen Datei:

```text
personen_neu.json
```

### Aufgabe 6: JSON selbst entwerfen

Entwerfen Sie eine JSON-Datei für eine kleine Bibliothek.

Die Datei soll mindestens drei Bücher enthalten.

Jedes Buch soll enthalten:

- ISBN,
- Titel,
- Autor,
- Erscheinungsjahr,
- Kategorie.

Beispielstruktur:

```json
{
    "bibliothek": [
        {
            "isbn": "...",
            "titel": "...",
            "autor": "...",
            "jahr": 2020,
            "kategorie": "..."
        }
    ]
}
```

### Aufgabe 7: Bücher auswerten

Lesen Sie die JSON-Datei aus Aufgabe 6 mit Python ein und geben Sie alle Bücher aus.

Beispielausgabe:

```text
Der Hobbit von J. R. R. Tolkien
Python lernen von Max Mustermann
Datenbanken verstehen von Erika Beispiel
```

### Aufgabe 8: Bücher nach Jahr filtern

Geben Sie nur Bücher aus, die nach dem Jahr 2010 erschienen sind.

Hinweis:

```python
jahr = buch["jahr"]
```

### Aufgabe 9: Fehlerhafte JSON-Datei untersuchen

Die folgende JSON-Datei ist fehlerhaft:

```json
{
    "personen": [
        {
            "id": "P1",
            "name": "Anna Müller",
            "alter": 21,
        },
        {
            id: "P2",
            "name": "Max Schneider",
            "alter": True
        }
    ]
}
```

Finden Sie die Fehler und korrigieren Sie die Datei.

Hinweise:

- Prüfen Sie Kommas.
- Prüfen Sie Anführungszeichen.
- Prüfen Sie JSON-Schreibweisen für Wahrheitswerte.
- Prüfen Sie, ob Datentypen fachlich sinnvoll sind.

### Aufgabe 10: Schemaüberlegung

Überlegen Sie für die Bibliotheksdatei aus Aufgabe 6:

1. Welche Felder sollten Pflichtfelder sein?
2. Welche Felder könnten optional sein?
3. Welche Datentypen wären sinnvoll?
4. Sollte die ISBN als Zahl oder als String gespeichert werden?

Begründen Sie Ihre Entscheidung kurz.

---

## 16. Musterlösungen zu ausgewählten Aufgaben

### Musterlösung zu Aufgabe 1

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

for person in daten["personen"]:
    print(person["name"])
```

### Musterlösung zu Aufgabe 2

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

for person in daten["personen"]:
    personen_id = person["id"]
    name = person["name"]

    print(personen_id, name)
```

### Musterlösung zu Aufgabe 3

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

summe = 0
anzahl = 0

for person in daten["personen"]:
    summe += person["alter"]
    anzahl += 1

durchschnitt = summe / anzahl

print("Durchschnittsalter:", round(durchschnitt, 1))
```

### Musterlösung zu Aufgabe 4

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

for person in daten["personen"]:
    if person["stadt"] == "Chemnitz":
        print(person["name"], "wohnt in Chemnitz.")
```

### Musterlösung zu Aufgabe 5

```python
import json

with open("personen.json", "r", encoding="utf-8") as datei:
    daten = json.load(datei)

neue_person = {
    "id": "P4",
    "name": "Tom Fischer",
    "alter": 22,
    "stadt": "Zwickau"
}

daten["personen"].append(neue_person)

with open("personen_neu.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, ensure_ascii=False, indent=4)
```

### Musterlösung zu Aufgabe 9

Fehlerhafte Datei:

```json
{
    "personen": [
        {
            "id": "P1",
            "name": "Anna Müller",
            "alter": 21,
        },
        {
            id: "P2",
            "name": "Max Schneider",
            "alter": True
        }
    ]
}
```

Fehler:

- Nach `"alter": 21` steht ein Komma, obwohl kein weiteres Feld folgt.
- Der Schlüssel `id` steht nicht in doppelten Anführungszeichen.
- `True` ist Python-Schreibweise, in JSON müsste es `true` heißen.
- Fachlich ist `alter` als Wahrheitswert nicht sinnvoll; es sollte eine Zahl sein.

Korrigierte Datei:

```json
{
    "personen": [
        {
            "id": "P1",
            "name": "Anna Müller",
            "alter": 21
        },
        {
            "id": "P2",
            "name": "Max Schneider",
            "alter": 24
        }
    ]
}
```

---

## 17. Didaktischer Vorschlag für die Vorlesung

Eine mögliche Reihenfolge für eine 90-minütige Einheit wäre:

| Phase | Inhalt | Zeit |
|---|---:|---:|
| Einstieg | Warum JSON? Beispiele aus APIs und Konfigurationen | 10 min |
| Theorie | Aufbau von JSON: Objekt, Array, Schlüssel, Wert | 20 min |
| Theorie | Datentypen und Syntaxregeln | 15 min |
| Demonstration | JSON mit Python einlesen | 15 min |
| Übung | Personen- oder Produktdatei auswerten | 20 min |
| Sicherung | Fehleranalyse und Vergleich mit XML | 10 min |

Für eine vertiefende zweite Einheit können folgende Themen ergänzt werden:

- JSON-Dateien erzeugen,
- JSON-Dateien verändern,
- Fehlerbehandlung beim Einlesen,
- JSON Schema,
- Zugriff auf Web-APIs,
- Vergleich JSON und XML,
- Umwandlung zwischen JSON und CSV.

---

## 18. Zusammenfassung

JSON ist ein kompaktes, textbasiertes Format zur Darstellung strukturierter Daten. Es verwendet Objekte, Arrays und einfache Datentypen wie String, Number, Boolean und null.

Für Python ist JSON besonders gut geeignet, weil JSON-Objekte direkt zu Dictionaries und JSON-Arrays direkt zu Listen werden. Mit dem Standardmodul `json` können JSON-Dateien ohne zusätzliche Installation gelesen und geschrieben werden.

Für Anfänger ist JSON ein sehr geeignetes Thema, weil es mehrere grundlegende Programmierkonzepte verbindet:

- Dateien lesen und schreiben,
- Datenstrukturen verstehen,
- Listen und Dictionaries verwenden,
- Schleifen einsetzen,
- Bedingungen formulieren,
- Datentypen unterscheiden,
- Fehler in strukturierten Daten erkennen.

Im Vergleich zu XML ist JSON meist kürzer und einfacher zu verarbeiten. XML bleibt wichtig für bestimmte Standards, Dokumentformate und stark formalisierte Schnittstellen. Wer beide Formate versteht, kann viele praktische Datenverarbeitungsaufgaben sicherer und flexibler lösen.
