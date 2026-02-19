# 🤖 DMATH.CODE Wochen-Zusammenfassung – Prompt-Template

> **Zweck:** Diesen Prompt bei jeder neuen Semesterwoche verwenden, damit der Agent automatisch eine optimale Prüfungszusammenfassung für **Diskrete Mathematik (DMATH.CODE, HSLU)** erstellt.

---

## Prompt (Copy-Paste für jede neue Woche)

```
Erstelle eine umfassende Prüfungszusammenfassung für die aktuelle Semesterwoche (SW XX) des Moduls "Diskrete Mathematik" (DMATH.CODE, HSLU).

Das Ausgabeformat ist ein Markdown-File namens ZUSAMMENFASSUNG_SWXX.md im entsprechenden SW-Ordner.

### Quelldateien im Wochenordner:
- **DMATH-CODE-SerieXX.pdf** → Aufgabenstellung (Übungsserie)
- **DMATH-CODE-SerieXX-final.pdf** → Lösung / Musterlösung
- **DMATH-CODE-SerieXX.ipynb** → Jupyter Notebook (falls vorhanden)

Alle drei Dateitypen durchlesen und Inhalte integrieren.

### Struktur & Inhalt (in dieser Reihenfolge):

1. **Header**: Modulname (DMATH.CODE), Wochennummer (SW XX), Thema
2. **🎯 Lernziele**: Aus den Aufgabenstellungen und Lösungen abgeleitete Lernziele
3. **📖 Wichtigste Begriffe**: Tabelle mit Begriff + Definition aller neuen mathematischen Konzepte
4. **📐 Definitionen, Sätze & Beweise**: Alle zentralen Definitionen und Sätze der Woche:
   - Formale mathematische Notation
   - Intuitive Erklärung in eigenen Worten
   - Beweisideen / Beweisschemata (wo relevant)
   - Schritt-für-Schritt Beispielrechnungen
5. **� Formeln & Rechenregeln**: Kompakte Übersicht aller relevanten Formeln:
   - Wahrscheinlichkeitsformeln, algebraische Identitäten, Algorithmen-Schritte
   - Jede Formel mit kurzer Erklärung der Variablen
   - Randfall-Hinweise (z.B. Division durch 0, leere Mengen)
6. **📊 Vergleiche & Klassifizierungen**: Tabellen die Verfahren, Algorithmen oder Konzepte gegenüberstellen
7. **💻 Code-Beispiele (Python)**: Alle relevanten Implementierungen aus den Notebooks und Lösungen:
   - Kommentare auf Deutsch
   - Erklärung des mathematischen Hintergrunds vor dem Code
   - Code aus den Musterlösungen (final.pdf / .ipynb) bevorzugen
   - NumPy / SciPy Funktionen erklären wenn verwendet
8. **✏️ Übungsaufgaben-Zusammenfassung**: Tabelle aller Aufgaben mit:
   - Aufgabennummer
   - Thema / Konzept
   - Lösungsansatz (Kurzform)
   - Typische Stolpersteine
9. **⚠️ Prüfungsrelevante Hinweise**:
   - Typische Aufgabentypen und wie man sie erkennt
   - Häufige Fehlerquellen und Fallstricke
   - Merkregeln und Eselsbrücken
   - Formeln die man auswendig wissen muss
10. **🔗 Verbindung zu vorherigen/folgenden Wochen**: Rückbezug und Vorausschau:
    - Wie baut der Stoff auf?
    - Welche Konzepte werden später wieder gebraucht?

### Wichtige Regeln:
- **Sprache:** Deutsch (mathematische Fachbegriffe dürfen Englisch/Latein bleiben)
- **Code:** Ausschliesslich Python (NumPy, SciPy, SymPy wo relevant)
- **Quellen:** Alle Dateien im SW-Ordner durchlesen (Serie-PDF, Final-PDF, .ipynb)
- **Mathematische Notation:** LaTeX-Syntax in Markdown verwenden ($..$ für inline, $$...$$ für Blöcke)
- **Formeln** immer mit konkretem Zahlenbeispiel ergänzen
- **Emojis** als Section-Icons verwenden für schnelles Scannen
- **Tabellen** bevorzugen für Vergleiche und Übersichten
- **Beweise** mindestens als Beweisskizze darstellen, nicht weglassen
- Das File soll so vollständig sein, dass man damit alleine die Prüfung bestehen kann
- **Schlüsselformeln** (z.B. Satz von Bayes, totale Wahrscheinlichkeit, Euklids Algorithmus) immer hervorheben
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für Querverweise
```

---

## Themenübersicht pro Woche

| Woche | Thema | Schlüsselkonzepte |
|-------|-------|-------------------|
| SW 01 | Wahrscheinlichkeit | Grundbegriffe, Laplace, Mengenoperationen |
| SW 02 | Bedingte Wahrscheinlichkeit | P(A\|B), Unabhängigkeit, Multiplikationssatz |
| SW 03 | Satz von Bayes | Bayes-Theorem, totale Wahrscheinlichkeit, Baumdiagramme |
| SW 04 | Zufallsvariablen | Verteilungen, Erwartungswert, Varianz |
| SW 05 | Randomisierte Algorithmen | Monte-Carlo, Las Vegas, Probabilistische Analyse |
| SW 06 | Markov-Ketten | Übergangsmatrizen, stationäre Verteilung, Absorbierende Zustände |
| SW 07 | Matrizenalgebra | Matrizenmultiplikation, Inverse, Determinante |
| SW 08 | Modulare Arithmetik | Kongruenzen, mod-Rechnung, Restklassen |
| SW 09 | Primzahlen | Sieb des Eratosthenes, Primzahltests, Faktorisierung |
| SW 10 | Euklids Algorithmus | ggT, erweiterter Euklid, Bézout-Koeffizienten |
| SW 11 | Chinesischer Restsatz | CRT, simultane Kongruenzen, Anwendungen |
| SW 12 | Endliche Gruppen | Gruppenaxiome, Ordnung, Untergruppen, Lagrange |
| SW 13 | Endliche Körper | Körperaxiome, GF(p), GF(p^n), Anwendungen (Krypto) |

---

## Ordnerstruktur-Erwartung

```
DMATH.CODE/
├── Unterrichtsserien fuer beide Kohorten/
│   ├── SW 01 Wahrscheinlichkeit/
│   │   ├── DMATH-CODE-Serie01.pdf          (Aufgaben)
│   │   ├── DMATH-CODE-Serie01-final.pdf    (Lösung)
│   │   ├── DMATH-CODE-Serie01.ipynb        (Notebook, falls vorhanden)
│   │   └── ZUSAMMENFASSUNG_SW01.md         ← Output
│   ├── SW 02 Bedingte Wahrscheinlichkeit/
│   │   ├── DMATH-CODE-Serie02.pdf
│   │   ├── DMATH-CODE-Serie02-final.pdf
│   │   ├── DMATH-CODE-Serie02.ipynb
│   │   └── ZUSAMMENFASSUNG_SW02.md         ← Output
│   ├── ...
│   └── SW 13 Endliche Koerper/
│       ├── DMATH-CODE-Serie13.pdf
│       ├── DMATH-CODE-Serie13-final.pdf
│       └── ZUSAMMENFASSUNG_SW13.md         ← Output
├── Admin/
├── Pruefungsvorbereitung.zip
├── Literatur zur Diskreten Mathematik.zip
└── Prompt.md  ← Diese Datei
```

---

## Hinweise für den Agent

- Zuerst den **SW-Ordner** der aktuellen Woche im Pfad `Unterrichtsserien fuer beide Kohorten/` auslesen
- **PDFs** direkt lesen (Serie-PDF = Aufgaben, Final-PDF = Lösungen)
- **Jupyter Notebooks** (.ipynb) direkt lesen und Code-Zellen extrahieren
- ZUSAMMENFASSUNG aus vorherigen Wochen lesen für **Querverweise**
- Bei Wochen ohne .ipynb: Code-Beispiele aus den Final-PDFs extrahieren
- **Mathematische Beweise** nicht kürzen — lieber als Beweisskizze komprimieren
- **Jede Formel** mit mindestens einem durchgerechneten Zahlenbeispiel belegen
