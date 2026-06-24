# Lehrbrief: Grundlagen von XML und Verarbeitung mit Python

## 1. Einordnung des Themas

XML steht für **Extensible Markup Language**. Es handelt sich um eine Auszeichnungssprache, mit der strukturierte Daten in Textform beschrieben werden können.

XML wird genutzt, um Daten zwischen Programmen, Systemen oder Organisationen auszutauschen. Auch wenn heute häufig JSON verwendet wird, spielt XML weiterhin eine wichtige Rolle, zum Beispiel bei:

- Schnittstellen zwischen Unternehmen
- Konfigurationsdateien
- Rechnungs- und Austauschformaten
- Webservices
- Dokumentenformaten
- Industrie- und Behördenstandards

Beispiele für XML-nahe oder XML-basierte Formate sind unter anderem:

- XRechnung
- SVG
- XHTML
- RSS-Feeds
- Office-Dokumente wie `.docx` oder `.xlsx`
- viele technische Konfigurationsdateien

XML ist besonders dann nützlich, wenn Daten klar strukturiert, prüfbar und langfristig lesbar gespeichert werden sollen.

---

## 2. Lernziele

Nach der Bearbeitung dieses Lehrbriefs sollen Studierende:

1. den grundlegenden Aufbau einer XML-Datei verstehen,
2. Elemente, Attribute, Textinhalte und Verschachtelungen unterscheiden können,
3. wohlgeformtes XML erkennen und einfache Fehler finden,
4. den Zweck von XML-Schemata erklären können,
5. XML-Daten mit Python einlesen und auswerten können,
6. verschiedene XML-Parser grundsätzlich vergleichen können,
7. einfache XML-Dateien selbst erzeugen und verarbeiten können.

---

## 3. Grundidee von XML

XML beschreibt Daten mithilfe sogenannter **Tags**. Tags markieren den Anfang und das Ende eines Elements.

Ein sehr einfaches Beispiel:

```xml
<person>
    <name>Anna Müller</name>
    <alter>21</alter>
</person>
```

Dieses XML-Dokument beschreibt eine Person. Die Person hat einen Namen und ein Alter.

Die Struktur ähnelt einem Baum:

```text
person
├── name
└── alter
```

Das oberste Element heißt **Wurzelelement**. In diesem Beispiel ist das:

```xml
<person>
```

Jedes XML-Dokument darf genau **ein Wurzelelement** besitzen.

---

## 4. Aufbau einer XML-Datei

Eine XML-Datei besteht typischerweise aus folgenden Bestandteilen:

### 4.1 XML-Deklaration

Am Anfang einer XML-Datei kann eine XML-Deklaration stehen:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

Sie gibt an:

- welche XML-Version verwendet wird,
- welche Zeichenkodierung genutzt wird.

Die Zeichenkodierung `UTF-8` ist heute üblich und empfehlenswert, da sie Umlaute und Sonderzeichen unterstützt.

### 4.2 Elemente

Elemente sind die wichtigsten Bausteine in XML.

Beispiel:

```xml
<produkt>
    <name>Kugelschreiber</name>
    <preis>1.49</preis>
</produkt>
```

Hier gibt es die Elemente:

```text
produkt
name
preis
```

Ein Element besteht meistens aus:

```xml
<starttag>Inhalt</endtag>
```

Beispiel:

```xml
<name>Kugelschreiber</name>
```

Das Starttag ist:

```xml
<name>
```

Das Endtag ist:

```xml
</name>
```

Der Inhalt ist:

```text
Kugelschreiber
```

### 4.3 Verschachtelung von Elementen

XML erlaubt verschachtelte Strukturen:

```xml
<kunde>
    <name>Anna Müller</name>
    <adresse>
        <strasse>Hauptstraße 12</strasse>
        <plz>09111</plz>
        <ort>Chemnitz</ort>
    </adresse>
</kunde>
```

Das Element `adresse` enthält weitere Elemente. Dadurch können komplexe Daten sauber dargestellt werden.

Wichtig ist: Elemente müssen korrekt geschlossen werden.

Richtig:

```xml
<name>Anna Müller</name>
```

Falsch:

```xml
<name>Anna Müller
```

Auch die Verschachtelung muss stimmen.

Richtig:

```xml
<kunde>
    <name>Anna Müller</name>
</kunde>
```

Falsch:

```xml
<kunde>
    <name>Anna Müller</kunde>
</name>
```

Das zweite Beispiel ist fehlerhaft, weil `name` zuerst geöffnet, aber nicht zuerst geschlossen wurde.

### 4.4 Attribute

Elemente können Attribute besitzen. Attribute stehen im Starttag.

Beispiel:

```xml
<produkt artikelnummer="A1001">
    <name>Kugelschreiber</name>
    <preis>1.49</preis>
</produkt>
```

Das Element `produkt` hat das Attribut:

```xml
artikelnummer="A1001"
```

Attribute eignen sich gut für kurze Zusatzinformationen oder Identifikatoren.

Ein weiteres Beispiel:

```xml
<kunde kundennummer="K4711">
    <name>Anna Müller</name>
</kunde>
```

Hier ist `kundennummer` ein Attribut.

### 4.5 Elemente oder Attribute?

Eine typische Frage lautet: Soll eine Information als Element oder als Attribut gespeichert werden?

Beide Varianten sind technisch möglich.

Variante mit Attribut:

```xml
<kunde kundennummer="K4711">
    <name>Anna Müller</name>
</kunde>
```

Variante mit Element:

```xml
<kunde>
    <kundennummer>K4711</kundennummer>
    <name>Anna Müller</name>
</kunde>
```

Eine einfache Orientierung:

| Information | Eher geeignet als |
|---|---|
| Identifikationsnummer | Attribut oder Element |
| längerer Text | Element |
| mehrfach vorkommende Werte | Element |
| strukturierte Daten | Element |
| kurze Zusatzinformation | Attribut |

Für Anfänger ist es oft einfacher, wichtige fachliche Daten als Elemente zu speichern. Attribute sollten gezielt verwendet werden.

---

## 5. Regeln für wohlgeformtes XML

Eine XML-Datei ist **wohlgeformt**, wenn sie die grundlegenden XML-Regeln einhält.

Wichtige Regeln sind:

1. Es gibt genau ein Wurzelelement.
2. Jedes geöffnete Element wird wieder geschlossen.
3. Elemente sind korrekt verschachtelt.
4. Attributwerte stehen in Anführungszeichen.
5. Groß- und Kleinschreibung wird beachtet.

### 5.1 Groß- und Kleinschreibung

XML unterscheidet zwischen Groß- und Kleinschreibung.

Diese beiden Elemente sind verschieden:

```xml
<Name>Anna</Name>
<name>Anna</name>
```

Das folgende Beispiel ist fehlerhaft:

```xml
<Name>Anna</name>
```

Das Starttag heißt `Name`, das Endtag aber `name`.

### 5.2 Attributwerte mit Anführungszeichen

Richtig:

```xml
<produkt artikelnummer="A1001">
```

Falsch:

```xml
<produkt artikelnummer=A1001>
```

Attributwerte müssen in Anführungszeichen stehen.

### 5.3 Sonderzeichen in XML

Einige Zeichen haben in XML eine besondere Bedeutung. Deshalb müssen sie ersetzt werden.

| Zeichen | Ersatz in XML |
|---|---|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| `'` | `&apos;` |

Beispiel:

```xml
<beschreibung>Preis kleiner als 10 &amp; sofort lieferbar</beschreibung>
```

Das Zeichen `&` wird als `&amp;` geschrieben.

---

## 6. Beispiel einer vollständigen XML-Datei

```xml
<?xml version="1.0" encoding="UTF-8"?>
<artikel>
    <produkt artikelnummer="A1001">
        <name>Kugelschreiber</name>
        <kategorie>Bürobedarf</kategorie>
        <preis>1.49</preis>
        <lagerbestand>250</lagerbestand>
    </produkt>
    <produkt artikelnummer="A1002">
        <name>Notizbuch</name>
        <kategorie>Bürobedarf</kategorie>
        <preis>3.99</preis>
        <lagerbestand>120</lagerbestand>
    </produkt>
</artikel>
```

Dieses Dokument enthält mehrere Produkte. Das Wurzelelement ist:

```xml
<artikel>
```

Jedes Produkt besitzt:

- eine Artikelnummer als Attribut,
- einen Namen,
- eine Kategorie,
- einen Preis,
- einen Lagerbestand.

---

## 7. XML-Schemata

### 7.1 Warum braucht man Schemata?

XML beschreibt zunächst nur eine Struktur. Es sagt aber noch nicht automatisch, welche Elemente erlaubt sind oder welche Datentypen verwendet werden sollen.

Ein Schema legt Regeln für eine XML-Datei fest.

Beispielsweise kann ein Schema definieren:

- Welche Elemente dürfen vorkommen?
- In welcher Reihenfolge müssen sie stehen?
- Welche Elemente sind Pflicht?
- Welche Elemente sind optional?
- Welche Datentypen sind erlaubt?
- Welche Attribute sind erlaubt?
- Wie oft darf ein Element vorkommen?

Ohne Schema könnte eine XML-Datei formal korrekt sein, aber fachlich trotzdem falsch.

Beispiel:

```xml
<produkt>
    <name>Kugelschreiber</name>
    <preis>teuer</preis>
</produkt>
```

Diese XML-Datei kann wohlgeformt sein. Fachlich ist sie aber problematisch, weil `preis` vermutlich eine Zahl sein sollte.

Ein Schema könnte festlegen:

```text
preis muss eine Dezimalzahl sein.
```

### 7.2 DTD

DTD steht für **Document Type Definition**. DTD ist eine ältere Möglichkeit, Regeln für XML-Dokumente zu definieren.

Ein sehr einfaches DTD-Beispiel:

```xml
<!ELEMENT produkt (name, preis)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT preis (#PCDATA)>
```

Das bedeutet:

- Ein `produkt` besteht aus `name` und `preis`.
- `name` enthält Text.
- `preis` enthält Text.

DTD ist relativ einfach, aber im Vergleich zu moderneren Schemaformen eingeschränkt. Zum Beispiel lassen sich Datentypen nur begrenzt prüfen.

### 7.3 XML Schema Definition, kurz XSD

XSD ist eine häufig verwendete und mächtigere Form zur Beschreibung von XML-Strukturen.

Ein einfaches XSD-Beispiel:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <xs:element name="produkt">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="preis" type="xs:decimal"/>
            </xs:sequence>
            <xs:attribute name="artikelnummer" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

</xs:schema>
```

Dieses Schema beschreibt ein Produkt mit:

- einem Element `name` vom Typ `xs:string`,
- einem Element `preis` vom Typ `xs:decimal`,
- einem Pflichtattribut `artikelnummer`.

Eine dazu passende XML-Datei wäre:

```xml
<produkt artikelnummer="A1001">
    <name>Kugelschreiber</name>
    <preis>1.49</preis>
</produkt>
```

Eine nicht passende XML-Datei wäre:

```xml
<produkt>
    <name>Kugelschreiber</name>
    <preis>teuer</preis>
</produkt>
```

Hier fehlen zwei Dinge:

1. Das Pflichtattribut `artikelnummer`.
2. Der Preis ist keine Dezimalzahl.

### 7.4 DTD und XSD im Vergleich

| Kriterium | DTD | XSD |
|---|---|---|
| Alter | älter | moderner |
| Syntax | eigene Syntax | XML-Syntax |
| Datentypen | eingeschränkt | umfangreich |
| Pflichtfelder | möglich | möglich |
| Wertebereiche | eingeschränkt | besser möglich |
| Lesbarkeit für Anfänger | teilweise einfacher | ausführlicher, aber präziser |
| Praxisrelevanz | noch vorhanden | sehr verbreitet |

Für moderne Anwendungen ist XSD meist geeigneter, weil es genauer prüfen kann, ob Daten fachlich korrekt aufgebaut sind.

---

## 8. XML-Parser

### 8.1 Was ist ein Parser?

Ein Parser ist ein Programm oder eine Bibliothek, die eine Datei einliest und deren Struktur interpretiert.

Ein XML-Parser liest XML-Daten und stellt sie dem Programm in einer verarbeitbaren Form zur Verfügung.

Mit einem Parser kann man zum Beispiel:

- XML-Dateien einlesen,
- Elemente suchen,
- Attribute auslesen,
- Inhalte verändern,
- neue XML-Dateien erzeugen,
- XML gegen ein Schema prüfen.

### 8.2 Parser-Arten im Vergleich

#### 8.2.1 DOM-Parser

DOM steht für **Document Object Model**.

Bei einem DOM-Parser wird das gesamte XML-Dokument in den Arbeitsspeicher geladen und als Baumstruktur dargestellt.

Vorteile:

- einfache Navigation im Dokument,
- Zugriff auf beliebige Stellen möglich,
- gut geeignet für kleinere und mittlere XML-Dateien.

Nachteile:

- benötigt mehr Speicher,
- bei sehr großen XML-Dateien weniger geeignet.

Typische Verwendung:

```text
kleine Konfigurationsdateien
überschaubare Datenlisten
XML-Dateien, die vollständig bearbeitet werden sollen
```

#### 8.2.2 SAX-Parser

SAX steht für **Simple API for XML**.

Ein SAX-Parser liest das XML-Dokument schrittweise von oben nach unten. Dabei reagiert er auf Ereignisse, zum Beispiel:

- Start eines Elements,
- Ende eines Elements,
- Textinhalt.

Vorteile:

- speicherschonend,
- gut für große XML-Dateien.

Nachteile:

- komplexer zu programmieren,
- kein einfacher Rücksprung im Dokument möglich,
- weniger intuitiv für Anfänger.

Typische Verwendung:

```text
sehr große XML-Dateien
Streaming-Verarbeitung
Importprozesse mit vielen Datensätzen
```

#### 8.2.3 Pull-Parser

Ein Pull-Parser liest XML ebenfalls schrittweise. Der Unterschied zu SAX besteht darin, dass das Programm aktiv das nächste Ereignis abruft.

Vorteile:

- speicherschonend,
- bessere Kontrolle durch das Programm,
- geeignet für große Dateien.

Nachteile:

- etwas anspruchsvoller als DOM,
- mehr Programmierlogik erforderlich.

#### 8.2.4 ElementTree in Python

Python bringt mit `xml.etree.ElementTree` bereits eine XML-Bibliothek mit.

Sie ist für Anfänger gut geeignet, weil sie relativ einfach zu verwenden ist.

Typische Möglichkeiten:

- XML-Dateien einlesen,
- Elemente suchen,
- Attribute auslesen,
- Elemente ändern,
- neue XML-Dateien schreiben.

Für den Einstieg ist `ElementTree` eine sehr gute Wahl.

#### 8.2.5 lxml

`lxml` ist eine externe Python-Bibliothek. Sie ist leistungsfähiger als `ElementTree`, muss aber zusätzlich installiert werden.

Installation:

```bash
pip install lxml
```

Vorteile:

- sehr leistungsfähig,
- unterstützt XPath umfangreicher,
- kann XML gegen XSD validieren,
- gut geeignet für professionelle XML-Verarbeitung.

Nachteile:

- zusätzliche Installation erforderlich,
- für Anfänger etwas komplexer.

### 8.3 Vergleich wichtiger Parser in Python

| Parser / Bibliothek | Art | Vorteil | Nachteil | Geeignet für |
|---|---|---|---|---|
| `xml.etree.ElementTree` | Baumorientiert | in Python enthalten, einfach | weniger leistungsfähig | Einstieg, kleine bis mittlere Dateien |
| `xml.dom.minidom` | DOM | anschauliche Baumstruktur | umständlicher, speicherintensiv | Lehrzwecke |
| `xml.sax` | SAX | speicherschonend | komplexer | große XML-Dateien |
| `lxml` | leistungsfähiger Baumparser | XSD, XPath, Geschwindigkeit | externe Installation | professionelle Anwendungen |
| `BeautifulSoup` | toleranter Parser | gut bei fehlerhaftem XML/HTML | nicht primär XML-Standardprüfung | unsaubere Datenquellen |

Für diese Vorlesung empfiehlt sich zunächst:

```python
xml.etree.ElementTree
```

Für fortgeschrittene Themen kann anschließend `lxml` eingeführt werden.

---

## 9. Einfache Python-Beispiele

### 9.1 Beispiel-XML-Datei

Speichern Sie die folgende Datei unter dem Namen:

```text
produkte.xml
```

Inhalt:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<artikel>
    <produkt artikelnummer="A1001">
        <name>Kugelschreiber</name>
        <kategorie>Bürobedarf</kategorie>
        <preis>1.49</preis>
        <lagerbestand>250</lagerbestand>
    </produkt>
    <produkt artikelnummer="A1002">
        <name>Notizbuch</name>
        <kategorie>Bürobedarf</kategorie>
        <preis>3.99</preis>
        <lagerbestand>120</lagerbestand>
    </produkt>
    <produkt artikelnummer="A1003">
        <name>Taschenrechner</name>
        <kategorie>Technik</kategorie>
        <preis>12.99</preis>
        <lagerbestand>35</lagerbestand>
    </produkt>
</artikel>
```

### 9.2 XML-Datei mit Python einlesen

```python
import xml.etree.ElementTree as ET

baum = ET.parse("produkte.xml")
wurzel = baum.getroot()

print(wurzel.tag)
```

Ausgabe:

```text
artikel
```

Erläuterung:

```python
import xml.etree.ElementTree as ET
```

Die Bibliothek `ElementTree` wird importiert. Der Kurzname `ET` macht den späteren Code kürzer.

```python
baum = ET.parse("produkte.xml")
```

Die XML-Datei wird eingelesen.

```python
wurzel = baum.getroot()
```

Das Wurzelelement wird ermittelt.

```python
print(wurzel.tag)
```

Der Name des Wurzelelements wird ausgegeben.

### 9.3 Alle Produkte ausgeben

```python
import xml.etree.ElementTree as ET

baum = ET.parse("produkte.xml")
wurzel = baum.getroot()

for produkt in wurzel.findall("produkt"):
    name = produkt.find("name").text
    preis = produkt.find("preis").text

    print(name, preis)
```

Mögliche Ausgabe:

```text
Kugelschreiber 1.49
Notizbuch 3.99
Taschenrechner 12.99
```

Erläuterung:

```python
for produkt in wurzel.findall("produkt"):
```

Die Schleife geht alle `produkt`-Elemente durch.

```python
name = produkt.find("name").text
```

Das Unterelement `name` wird gesucht. Mit `.text` wird sein Textinhalt gelesen.

```python
preis = produkt.find("preis").text
```

Der Preis wird ausgelesen.

### 9.4 Attribute auslesen

```python
import xml.etree.ElementTree as ET

baum = ET.parse("produkte.xml")
wurzel = baum.getroot()

for produkt in wurzel.findall("produkt"):
    artikelnummer = produkt.get("artikelnummer")
    name = produkt.find("name").text

    print(artikelnummer, name)
```

Ausgabe:

```text
A1001 Kugelschreiber
A1002 Notizbuch
A1003 Taschenrechner
```

Mit:

```python
produkt.get("artikelnummer")
```

wird das Attribut `artikelnummer` ausgelesen.

### 9.5 Zahlenwerte verarbeiten

XML speichert Inhalte zunächst als Text. Wenn mit Zahlen gerechnet werden soll, müssen sie umgewandelt werden.

```python
import xml.etree.ElementTree as ET

baum = ET.parse("produkte.xml")
wurzel = baum.getroot()

gesamtwert = 0

for produkt in wurzel.findall("produkt"):
    preis = float(produkt.find("preis").text)
    lagerbestand = int(produkt.find("lagerbestand").text)

    wert = preis * lagerbestand
    gesamtwert += wert

print("Gesamter Lagerwert:", gesamtwert)
```

Mögliche Ausgabe:

```text
Gesamter Lagerwert: 1338.85
```

Wichtig:

```python
float(...)
```

wandelt einen Text in eine Kommazahl um.

```python
int(...)
```

wandelt einen Text in eine ganze Zahl um.

### 9.6 XML-Daten verändern

Im nächsten Beispiel wird der Preis eines Produkts verändert.

```python
import xml.etree.ElementTree as ET

baum = ET.parse("produkte.xml")
wurzel = baum.getroot()

for produkt in wurzel.findall("produkt"):
    artikelnummer = produkt.get("artikelnummer")

    if artikelnummer == "A1001":
        produkt.find("preis").text = "1.79"

baum.write("produkte_geaendert.xml", encoding="UTF-8", xml_declaration=True)
```

Dieses Programm:

1. liest die Datei `produkte.xml`,
2. sucht das Produkt mit der Artikelnummer `A1001`,
3. ändert den Preis,
4. schreibt eine neue Datei `produkte_geaendert.xml`.

### 9.7 Neue XML-Datei mit Python erzeugen

```python
import xml.etree.ElementTree as ET

wurzel = ET.Element("artikel")

produkt = ET.SubElement(wurzel, "produkt")
produkt.set("artikelnummer", "A2001")

name = ET.SubElement(produkt, "name")
name.text = "Lineal"

kategorie = ET.SubElement(produkt, "kategorie")
kategorie.text = "Bürobedarf"

preis = ET.SubElement(produkt, "preis")
preis.text = "2.49"

lagerbestand = ET.SubElement(produkt, "lagerbestand")
lagerbestand.text = "80"

baum = ET.ElementTree(wurzel)
baum.write("neue_produkte.xml", encoding="UTF-8", xml_declaration=True)
```

Dieses Programm erstellt eine neue XML-Datei.

Die erzeugte Datei sieht ungefähr so aus:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<artikel>
    <produkt artikelnummer="A2001">
        <name>Lineal</name>
        <kategorie>Bürobedarf</kategorie>
        <preis>2.49</preis>
        <lagerbestand>80</lagerbestand>
    </produkt>
</artikel>
```

Je nach Python-Version kann die Formatierung etwas anders aussehen. Fachlich ist das aber kein Problem.

---

## 10. Typische Fehler beim Arbeiten mit XML

### Fehler 1: Datei nicht gefunden

```python
baum = ET.parse("produkte.xml")
```

Wenn die Datei nicht im gleichen Ordner liegt wie das Python-Programm, entsteht ein Fehler.

Mögliche Lösung:

- Datei in den richtigen Ordner legen,
- Dateinamen prüfen,
- Pfad korrekt angeben.

### Fehler 2: Element existiert nicht

```python
preis = produkt.find("preis").text
```

Wenn das Element `preis` fehlt, kann Python einen Fehler melden.

Robustere Variante:

```python
preis_element = produkt.find("preis")

if preis_element is not None:
    print(preis_element.text)
else:
    print("Kein Preis vorhanden")
```

### Fehler 3: Text kann nicht in Zahl umgewandelt werden

```python
preis = float(produkt.find("preis").text)
```

Wenn in der XML-Datei steht:

```xml
<preis>teuer</preis>
```

kann Python daraus keine Zahl machen.

Dann entsteht ein Fehler.

Eine einfache Absicherung:

```python
text = produkt.find("preis").text

try:
    preis = float(text)
    print(preis)
except ValueError:
    print("Der Preis ist keine gültige Zahl:", text)
```

---

## 11. Kurzer Einblick: XML und XPath

XPath ist eine Sprache, mit der gezielt Elemente in XML-Dokumenten gesucht werden können.

Ein einfaches Beispiel mit `ElementTree`:

```python
import xml.etree.ElementTree as ET

baum = ET.parse("produkte.xml")
wurzel = baum.getroot()

for name in wurzel.findall("./produkt/name"):
    print(name.text)
```

Die Angabe:

```python
./produkt/name
```

bedeutet:

```text
Suche vom aktuellen Element aus alle produkt-Elemente und darin jeweils das Element name.
```

XPath ist besonders nützlich, wenn XML-Dateien tief verschachtelt sind.

---

## 12. Übungsaufgaben

### Aufgabe 1: XML lesen

Erstellen Sie die Datei `personen.xml` mit folgendem Inhalt:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<personen>
    <person id="P1">
        <name>Anna Müller</name>
        <alter>21</alter>
        <stadt>Chemnitz</stadt>
    </person>
    <person id="P2">
        <name>Max Schneider</name>
        <alter>24</alter>
        <stadt>Dresden</stadt>
    </person>
    <person id="P3">
        <name>Lisa Weber</name>
        <alter>19</alter>
        <stadt>Leipzig</stadt>
    </person>
</personen>
```

Schreiben Sie ein Python-Programm, das alle Namen ausgibt.

Erwartete Ausgabe:

```text
Anna Müller
Max Schneider
Lisa Weber
```

### Aufgabe 2: Attribute auslesen

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
alter = int(person.find("alter").text)
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
personen_neu.xml
```

### Aufgabe 6: XML selbst entwerfen

Entwerfen Sie eine XML-Datei für eine kleine Bibliothek.

Die Datei soll mindestens drei Bücher enthalten.

Jedes Buch soll enthalten:

- ISBN
- Titel
- Autor
- Erscheinungsjahr
- Kategorie

Beispielstruktur:

```xml
<bibliothek>
    <buch isbn="...">
        <titel>...</titel>
        <autor>...</autor>
        <jahr>...</jahr>
        <kategorie>...</kategorie>
    </buch>
</bibliothek>
```

### Aufgabe 7: Bücher auswerten

Lesen Sie die XML-Datei aus Aufgabe 6 mit Python ein und geben Sie alle Bücher aus.

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
jahr = int(buch.find("jahr").text)
```

### Aufgabe 9: Fehlerhafte XML-Datei untersuchen

Die folgende XML-Datei ist fehlerhaft:

```xml
<personen>
    <person id=P1>
        <name>Anna Müller</name>
        <alter>21</alter>
    </person>
    <person id="P2">
        <name>Max Schneider</alter>
        <alter>24</alter>
    </person>
</personen>
```

Finden Sie die Fehler und korrigieren Sie die Datei.

Hinweise:

- Prüfen Sie Attribute.
- Prüfen Sie Start- und Endtags.
- Prüfen Sie die Verschachtelung.

### Aufgabe 10: Schemaüberlegung

Überlegen Sie für die Bibliotheksdatei aus Aufgabe 6:

1. Welche Elemente sollten Pflichtfelder sein?
2. Welche Elemente könnten optional sein?
3. Welche Datentypen wären sinnvoll?
4. Sollte die ISBN als Attribut oder als Element gespeichert werden?

Begründen Sie Ihre Entscheidung kurz.

---

## 13. Musterlösungen zu ausgewählten Aufgaben

### Musterlösung zu Aufgabe 1

```python
import xml.etree.ElementTree as ET

baum = ET.parse("personen.xml")
wurzel = baum.getroot()

for person in wurzel.findall("person"):
    name = person.find("name").text
    print(name)
```

### Musterlösung zu Aufgabe 2

```python
import xml.etree.ElementTree as ET

baum = ET.parse("personen.xml")
wurzel = baum.getroot()

for person in wurzel.findall("person"):
    personen_id = person.get("id")
    name = person.find("name").text

    print(personen_id, name)
```

### Musterlösung zu Aufgabe 3

```python
import xml.etree.ElementTree as ET

baum = ET.parse("personen.xml")
wurzel = baum.getroot()

summe = 0
anzahl = 0

for person in wurzel.findall("person"):
    alter = int(person.find("alter").text)
    summe += alter
    anzahl += 1

durchschnitt = summe / anzahl

print("Durchschnittsalter:", round(durchschnitt, 1))
```

### Musterlösung zu Aufgabe 4

```python
import xml.etree.ElementTree as ET

baum = ET.parse("personen.xml")
wurzel = baum.getroot()

for person in wurzel.findall("person"):
    name = person.find("name").text
    stadt = person.find("stadt").text

    if stadt == "Chemnitz":
        print(name, "wohnt in Chemnitz.")
```

### Musterlösung zu Aufgabe 5

```python
import xml.etree.ElementTree as ET

baum = ET.parse("personen.xml")
wurzel = baum.getroot()

neue_person = ET.SubElement(wurzel, "person")
neue_person.set("id", "P4")

name = ET.SubElement(neue_person, "name")
name.text = "Tom Fischer"

alter = ET.SubElement(neue_person, "alter")
alter.text = "22"

stadt = ET.SubElement(neue_person, "stadt")
stadt.text = "Zwickau"

baum.write("personen_neu.xml", encoding="UTF-8", xml_declaration=True)
```

---

## 14. Didaktischer Vorschlag für die Vorlesung

Eine mögliche Reihenfolge für eine 90-minütige Einheit wäre:

| Phase | Inhalt | Zeit |
|---|---:|---:|
| Einstieg | Warum XML? Beispiele aus der Praxis | 10 min |
| Theorie | Aufbau von XML | 20 min |
| Theorie | Wohlgeformtheit und Schemata | 15 min |
| Demonstration | XML mit Python einlesen | 15 min |
| Übung | Personen- oder Produktdatei auswerten | 20 min |
| Sicherung | Fehleranalyse und kurze Reflexion | 10 min |

Für eine vertiefende zweite Einheit können folgende Themen ergänzt werden:

- XML-Dateien erzeugen
- XML-Dateien verändern
- XPath
- XSD-Validierung mit `lxml`
- Vergleich XML und JSON

---

## 15. Zusammenfassung

XML ist eine Auszeichnungssprache zur strukturierten Darstellung von Daten. Eine XML-Datei besteht aus Elementen, Attributen und Textinhalten. Damit eine XML-Datei korrekt verarbeitet werden kann, muss sie wohlgeformt sein. Schemata wie DTD oder XSD können zusätzlich festlegen, welche Struktur und welche Datentypen erlaubt sind.

Python bietet mit `xml.etree.ElementTree` eine gut geeignete Standardbibliothek für den Einstieg in die XML-Verarbeitung. Damit können XML-Dateien eingelesen, durchsucht, verändert und neu erzeugt werden.

Für Anfänger ist XML ein gutes Thema, weil es mehrere grundlegende Programmierkonzepte verbindet:

- Dateien lesen und schreiben,
- Datenstrukturen verstehen,
- Schleifen verwenden,
- Bedingungen einsetzen,
- Texte und Zahlen verarbeiten,
- Fehler erkennen und beheben.

Damit eignet sich XML sehr gut als Brücke zwischen Datenmodellierung und praktischer Programmierung mit Python.
