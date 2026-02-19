# DMATH-CODE — SW 01: Wahrscheinlichkeit

> **Modul:** DMATH-CODE, HSLU | **Dozent:** Dr. Reto Berger | **Semester:** Frühlingssemester 25

---

## 🎯 Lernziele

1. **Zufallsexperiment verstehen** — Sie wissen, was ein Zufallsexperiment ist und können seinen Ergebnisraum $\Omega$ beschreiben.
2. **Wahrscheinlichkeitsfunktionen berechnen** — Sie können Wahrscheinlichkeitsfunktionen aufstellen und verstehen den Begriff *uniform*.
3. **Wahrscheinlichkeiten für Ereignisse berechnen** — Sie können Ereignisse als Teilmengen von $\Omega$ modellieren und deren Wahrscheinlichkeiten berechnen (inkl. Vereinigung, Schnitt, Komplement).

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---------|-----------|
| **Zufallsexperiment** | Ein Vorgang, der beliebig oft unter gleichen Bedingungen wiederholt werden kann und dessen Ergebnis nicht mit Sicherheit vorhergesagt werden kann. |
| **Ergebnismenge** $\Omega$ | Die Menge aller möglichen Ergebnisse eines Zufallsexperiments. |
| **Ergebnis** $\omega$ | Ein einzelnes Element aus $\Omega$. |
| **Wahrscheinlichkeitsfunktion** $P$ | Ordnet jedem Ergebnis $\omega \in \Omega$ eine reelle Zahl von 0 bis 1 zu, sodass $\sum_{\omega \in \Omega} P(\omega) = 1$. |
| **Uniform** | Eine Wahrscheinlichkeitsfunktion heisst *uniform*, wenn alle Ergebnisse die gleiche Wahrscheinlichkeit haben: $P(\omega_1) = P(\omega_2) = \ldots = P(\omega_n) = \frac{1}{n}$. |
| **Ereignis** $E$ | Jede Teilmenge $E \subseteq \Omega$ der Ergebnismenge. |
| **Sicheres Ereignis** | $\Omega$ selbst — tritt immer ein, $P(\Omega) = 1$. |
| **Unmögliches Ereignis** | Die leere Menge $\{\}$ — tritt nie ein, $P(\{\}) = 0$. |
| **Gegenereignis** $\overline{A}$ | Komplement von $A$: alle Ergebnisse, die **nicht** in $A$ liegen. |
| **Laplace-Experiment** | Zufallsexperiment mit uniformer Wahrscheinlichkeitsfunktion (alle Ergebnisse gleichwahrscheinlich). |

---

## 📐 Definitionen, Sätze & Beweise

### Definition 1: Zufallsexperiment

> Ein **Zufallsexperiment** ist ein Vorgang, der
> - beliebig oft unter gleichen Bedingungen wiederholt werden kann **und**
> - dessen Ergebnis nicht mit Sicherheit vorhergesagt werden kann.

Die Menge $\Omega$ aller möglichen Ergebnisse heisst **Ergebnismenge**.

**Beispiel:** Einen Würfel einmal werfen → $\Omega = \{1, 2, 3, 4, 5, 6\}$

---

### Definition 2: Wahrscheinlichkeitsfunktion

> Sei $\Omega = \{\omega_1, \omega_2, \ldots, \omega_n\}$ die Ergebnismenge eines Zufallsexperiments. Eine **Wahrscheinlichkeitsfunktion** $P$ ordnet jedem Ergebnis $\omega \in \Omega$ genau eine *reelle Zahl von 0 bis 1* zu, so dass:
>
> $$\sum_{\omega \in \Omega} P(\omega) = P(\omega_1) + P(\omega_2) + \ldots + P(\omega_n) = 1$$

**Uniform:** $P(\omega_1) = P(\omega_2) = \ldots = P(\omega_n) = \frac{1}{|\Omega|}$

**Beispiel (fairer Würfel):**
$$P(1) = P(2) = P(3) = P(4) = P(5) = P(6) = \frac{1}{6}$$

**Intuition:** Die Wahrscheinlichkeitsfunktion verteilt eine «Gesamtmasse» von 1 auf alle Ergebnisse. Bei uniformer Verteilung bekommt jedes Ergebnis den gleichen Anteil.

---

### Definition 3: Ereignis

> Sei $\Omega$ die Ergebnismenge und $P$ eine Wahrscheinlichkeitsfunktion:
> - Jede **Teilmenge** $E = \{\omega_1, \omega_2, \ldots, \omega_k\}$ von $\Omega$ heisst ein **Ereignis**.
> - Die Wahrscheinlichkeit $P(E)$ für das Ereignis $E = \{\omega_1, \omega_2, \ldots, \omega_k\}$ ist:
>
> $$P(E) = \sum_{\omega \in E} P(\omega) = P(\omega_1) + P(\omega_2) + \ldots + P(\omega_k)$$

**Beispiel (Roulette):** $\Omega = \{0, 1, 2, \ldots, 36\}$, uniform mit $P(\omega) = \frac{1}{37}$

| Ereignis | Beschreibung | \|E\| | P(E) |
|----------|-------------|:-----:|:----:|
| 1–18 | 1, 2, 3, …, 18 | 18 | 18/37 |
| even | 2, 4, 6, 8, …, 36 | 18 | 18/37 |
| 1st 12 | 1, 2, 3, …, 12 | 12 | 12/37 |
| black | 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35 | 18 | 18/37 |
| red | 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 | 18 | 18/37 |
| odd | 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35 | 18 | 18/37 |
| 2 to 1 A | 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34 | 12 | 12/37 |
| 2 to 1 B | 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35 | 12 | 12/37 |
| 2 to 1 C | 3, 6, 9, 12, 15, 18, 21, 24, 27, 33, 36 | 12 | 12/37 |

---

### Satz 1: Rechenregeln für Wahrscheinlichkeiten

> Sei $P$ eine Wahrscheinlichkeitsfunktion und $A$, $B$ beliebige Ereignisse:

| Regel | Formel | Erklärung |
|-------|--------|-----------|
| **Sicheres Ereignis** | $P(\Omega) = 1$ | Trifft immer zu |
| **Unmögliches Ereignis** | $P(\{\}) = 0$ | Tritt nie ein |
| **Gegenereignis** | $P(\overline{A}) = 1 - P(A)$ | Komplement |
| **Vereinigung** (Inklusion-Exklusion) | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Doppelzählung korrigieren |

**Beweisskizze (Gegenereignis):**
- $A$ und $\overline{A}$ sind disjunkt: $A \cap \overline{A} = \{\}$
- $A \cup \overline{A} = \Omega$
- Also: $P(A) + P(\overline{A}) = P(\Omega) = 1$ → $P(\overline{A}) = 1 - P(A)$ ∎

**Beweisskizze (Vereinigung / Inklusion-Exklusion):**
- Wenn man $P(A) + P(B)$ rechnet, werden die Ergebnisse in $A \cap B$ doppelt gezählt.
- Daher muss $P(A \cap B)$ einmal abgezogen werden. ∎

**Zahlenbeispiel (Roulette):**

$P(\text{odd} \cup \text{red}) = P(\text{odd}) + P(\text{red}) - P(\text{odd} \cap \text{red}) = \frac{18}{38} + \frac{18}{38} - \frac{10}{38} = \frac{26}{38}$

$P(\text{odd}) = 1 - P(\text{odd}) = 1 - \frac{18}{38} = \frac{20}{38}$

---

## 📝 Formeln & Rechenregeln

### Kernformeln dieser Woche

| # | Formel | Beschreibung | Variablen |
|---|--------|-------------|-----------|
| 1 | $P(\omega) = \frac{1}{|\Omega|}$ | Uniform (Laplace) | $\omega$: Ergebnis, $|\Omega|$: Anzahl Ergebnisse |
| 2 | $\sum_{\omega \in \Omega} P(\omega) = 1$ | Normierungsbedingung | Summe über alle Ergebnisse = 1 |
| 3 | $P(E) = \frac{|E|}{|\Omega|}$ | Laplace-Wahrscheinlichkeit | $|E|$: Anzahl günstige, $|\Omega|$: Anzahl mögliche |
| 4 | $P(\overline{A}) = 1 - P(A)$ | Gegenereignis | Nützlich wenn $P(\overline{A})$ einfacher zu berechnen |
| 5 | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Inklusion-Exklusion | Doppelzählung korrigieren |

### Wichtige Zählprinzipien

| Situation | Formel | Beispiel |
|-----------|--------|---------|
| Geordnete Auswahl **mit** Zurücklegen | $|\Omega| = n^k$ | $k$ Würfe eines $n$-seitigen Würfels |
| Geordnete Auswahl **ohne** Zurücklegen | $|\Omega| = \frac{n!}{(n-k)!}$ | $k$ aus $n$ Elementen wählen (Reihenfolge zählt) |
| Ungeordnete Auswahl **ohne** Zurücklegen | $|\Omega| = \binom{n}{k} = \frac{n!}{k!(n-k)!}$ | $k$ aus $n$ Elementen wählen (Reihenfolge egal) |

### ⚠️ Randfälle

- **Division durch 0:** Nicht möglich, da $|\Omega| \geq 1$ (mindestens ein Ergebnis)
- **Leere Menge:** $P(\{\}) = 0$ — das unmögliche Ereignis hat Wahrscheinlichkeit 0
- **Ergebnismenge:** $P(\Omega) = 1$ — immer!
- **Summenbedingung prüfen:** Verteilung ist nur gültig, wenn $\sum P(\omega_i) = 1$

---

## 📊 Vergleiche & Klassifizierungen

### Uniforme vs. nicht-uniforme Verteilungen

| Eigenschaft | Uniform (Laplace) | Nicht-uniform |
|-------------|-------------------|---------------|
| $P(\omega)$ | $\frac{1}{|\Omega|}$ für alle $\omega$ | Unterschiedlich pro $\omega$ |
| Berechnung $P(E)$ | $\frac{|E|}{|\Omega|}$ (Abzählen reicht) | $\sum_{\omega \in E} P(\omega)$ (jedes $\omega$ einzeln) |
| Beispiel | Fairer Würfel | Gezinkter Würfel |
| Vorteil | Einfach zu berechnen | Flexibler |

### Gegenereignis vs. direkte Berechnung

| Ansatz | Wann verwenden | Beispiel |
|--------|---------------|---------|
| **Direkt:** $P(E)$ berechnen | Wenn $|E|$ klein / einfach abzählbar | «Genau eine 6 in 4 Würfen» |
| **Über Gegenereignis:** $P(E) = 1 - P(\overline{E})$ | Wenn $|\overline{E}|$ viel einfacher zu bestimmen | «Mindestens eine 6» → $1 - P(\text{keine 6})$ |

### Varianten eines Zufallsgenerators (Aufgabe 2d)

| Variante | Methode | $|\Omega|$ | Verteilung |
|----------|---------|---------|-----------|
| **Variante 1** | 3 Bits → Binärzahl → Dezimal (0–7) | $2^3 = 8$ | **uniform**: $P(k) = \frac{1}{8}$ für $k \in \{0,\ldots,7\}$ |
| **Variante 2** | 7 Bits → Anzahl Nullen zählen (0–7) | $2^7 = 128$ | **nicht-uniform**: $P(k) = \binom{7}{k} \cdot \frac{1}{2^7}$ |

---

## 💻 Code-Beispiele (Python)

### Würfelsimulation — Ist `randint` fair?

**Mathematischer Hintergrund:** Ein fairer Würfel ist ein Laplace-Experiment mit $P(k) = \frac{1}{6}$ für $k \in \{1,...,6\}$. Durch Simulation mit vielen Würfen kann man prüfen, ob die relativen Häufigkeiten gegen $\frac{1}{6} \approx 0.1667$ konvergieren (**Gesetz der grossen Zahlen**).

```python
import numpy as np
import random as rd

# Einen einzelnen Wurf simulieren
rd.randint(1, 6)  # Gibt zufällig 1, 2, 3, 4, 5 oder 6 zurück

# 5'000'000 Würfe simulieren und relative Häufigkeiten bestimmen
Augenzahlen = np.array([0, 0, 0, 0, 0, 0])  # Zähler für jede Augenzahl
Anzahl_Spiele = 5_000_000

for _ in range(Anzahl_Spiele):
    Wurf = rd.randint(1, 6)       # Zufälliger Wurf (1..6)
    Augenzahlen[Wurf - 1] += 1    # Zähler für diese Augenzahl erhöhen

# Relative Häufigkeiten berechnen (sollten alle ≈ 0.1667 sein)
relative_haeufigkeiten = np.round(Augenzahlen / Anzahl_Spiele, decimals=4)
print(relative_haeufigkeiten)
# Beispielausgabe: [0.1665 0.1669 0.1666 0.1667 0.1665 0.1669]
```

> **`np.round(array, decimals=4)`** — Rundet jedes Element auf 4 Dezimalstellen.  
> **`rd.randint(a, b)`** — Gibt eine zufällige ganze Zahl $n$ mit $a \leq n \leq b$ zurück (inklusive beider Grenzen).

---

### Chevalier de Méré — Simulation der zwei Spiele

**Mathematischer Hintergrund:**
- **Spiel 1:** 4× ein Würfel werfen → Gewinn bei mindestens einer 6  
  $P(\text{Gewinn}) = 1 - P(\text{keine 6}) = 1 - \left(\frac{5}{6}\right)^4 \approx 0.5177$
- **Spiel 2:** 24× zwei Würfel werfen → Gewinn bei mindestens einer Doppelsechs  
  $P(\text{Gewinn}) = 1 - P(\text{keine 66}) = 1 - \left(\frac{35}{36}\right)^{24} \approx 0.4914$

```python
import numpy as np
import random as rd

Gewinne_Spiel_1 = 0
Gewinne_Spiel_2 = 0
Anzahl_Spiele = 500_000

# Spiel 1: 4-mal würfeln, Gewinn bei mindestens einer 6
for _ in range(Anzahl_Spiele):
    Spielresultat = [rd.randint(1, 6) for _ in range(4)]  # 4 Würfe
    if 6 in Spielresultat:
        Gewinne_Spiel_1 += 1

# Spiel 2: 24-mal zwei Würfel werfen, Gewinn bei mindestens einer Doppelsechs
for _ in range(Anzahl_Spiele):
    Spielresultat = [(rd.randint(1, 6), rd.randint(1, 6)) for _ in range(24)]
    if (6, 6) in Spielresultat:
        Gewinne_Spiel_2 += 1

# Gewinnwahrscheinlichkeiten ausgeben
ergebnis = np.round(
    np.array([Gewinne_Spiel_1, Gewinne_Spiel_2]) / Anzahl_Spiele, decimals=4
)
print(ergebnis)
# Beispielausgabe: [0.5178 0.4917]
# → Spiel 1 ist tatsächlich vorteilhafter als Spiel 2!
```

> **`[... for _ in range(n)]`** — List Comprehension: erzeugt eine Liste mit $n$ Elementen.  
> **`(6,6) in list`** — Prüft, ob das Tupel `(6,6)` in der Liste vorkommt.  
> **Erkenntnis:** Die Spiele kompensieren sich **nicht** — Spiel 1 hat eine leicht höhere Gewinnwahrscheinlichkeit (~51.8% vs. ~49.1%).

---

### Laplace-Wahrscheinlichkeit berechnen (nützliche Muster)

```python
import math
from math import comb, factorial

# --- Aufgabe 3: P(mind. eine 1 in 8-Bit-Datenwort) ---
# Ω = {0,1}^8 → |Ω| = 2^8 = 256
# Gegenereignis: keine 1 → nur ω = 00000000 → 1 Ergebnis
P_mind_eine_1 = 1 - 1 / 2**8  # = 1 - 1/256
print(f"P(mind. eine 1 in 8 Bit) = {P_mind_eine_1:.10f}")
# → 0.99609375

# --- Aufgabe 4: P(durch 2 oder 5 teilbar bei Zahl 1..100) ---
# Inklusion-Exklusion: P(A∪B) = P(A) + P(B) - P(A∩B)
P_durch_2_oder_5 = 50/100 + 20/100 - 10/100
print(f"P(durch 2 oder 5 teilbar) = {P_durch_2_oder_5}")
# → 0.6

# --- Aufgabe 5: Chevalier de Méré (exakt) ---
P_spiel1 = 1 - (5/6)**4
P_spiel2 = 1 - (35/36)**24
print(f"Spiel 1: P = {P_spiel1:.6f}")  # 0.517747
print(f"Spiel 2: P = {P_spiel2:.6f}")  # 0.491404

# --- Aufgabe 6: Kein Treffer bei Fixpunkt-Problem ---
# Ω = {0,1,2,3,4}^5, |Ω| = 5^5
# Kein Treffer: Position i ≠ i → an jeder Stelle 4 Möglichkeiten
P_kein_treffer = 4**5 / 5**5
print(f"P(kein Treffer) = {P_kein_treffer:.5f}")
# → 0.32768

# --- Aufgabe 7: Gleich viele Frauen und Männer in jeder Gruppe ---
# Team: 6 Frauen + 6 Männer → 12 Personen, in 2 Gruppen à 6
# |Ω| = C(12,6) = 924
# Günstig: C(6,3) * C(6,3) = 20 * 20 = 400
P_gleich = comb(6,3) * comb(6,3) / comb(12,6)
print(f"P(gleich viele ♀ und ♂) = {P_gleich:.4f}")
# → 0.4329

# --- Aufgabe 8: Geburtstagsparadoxon (Ziffern-Variante) ---
# 5 Personen, Ziffern 0-9, P(mind. 2 gleich)
# Gegenereignis: alle verschieden → 10·9·8·7·6 Möglichkeiten
P_mind_2_gleich = 1 - (10 * 9 * 8 * 7 * 6) / 10**5
print(f"P(mind. 2 gleiche Ziffern) = {P_mind_2_gleich:.4f}")
# → 0.6976

# --- Aufgabe 9: 15 Jobs auf 20 Server, jeder Server genau 1 Job ---
# |Ω| = 20^15 (jeder Job wählt uniform einen Server)
# Günstig: 20!/(20-15)! = 20!/5! (geordnete Auswahl ohne Zurücklegen)
P_alle_verschieden = factorial(20) // factorial(5) / 20**15
print(f"P(15 Server je 1 Job) = {P_alle_verschieden:.7f}")
# → 0.0006187...
```

---

## ✏️ Übungsaufgaben-Zusammenfassung

| Nr. | Thema / Konzept | Lösungsansatz | Typische Stolpersteine |
|-----|----------------|---------------|----------------------|
| **1** | Ergebnismengen bestimmen | a) $\Omega = \{1,...,6\}^2$ (36 Paare) b) Münzen: Kreuzprodukt c) Tennisturnier: Spielverläufe auflisten | Ergebnismenge muss **alle** möglichen Ausgänge enthalten, nicht nur die «interessanten» |
| **2a** | Wahrscheinlichkeit Münzwurf | $P(\text{Zahl}) = 1 - P(\text{Kopf}) = 1 - 0.3 = 0.7$ | Gegenereignis nicht vergessen |
| **2b** | Uniforme Verteilung | 1a: $P(\omega)=\frac{1}{36}$, 1b: $P(\omega)=\frac{1}{8}$, 1c: $P(\omega)=\frac{1}{10}$ | $|\Omega|$ korrekt bestimmen (bei 1c sind es 10 Spielverläufe) |
| **2c** | Nicht-uniforme Verteilung | Geometrische Reihe: $x + 1.1x + 1.1^2x + \ldots = 1$ lösen | Normierungsbedingung $\sum P = 1$ aufstellen |
| **2d** | Zufallsgenerator-Varianten | Var. 1: $P = \frac{1}{8}$ uniform; Var. 2: Binomialkoeffizienten $\binom{7}{k} \cdot \frac{1}{128}$ | Var. 2 ist **nicht** uniform! |
| **3** | Mind. eine 1 in 8 Bits | $P = 1 - \frac{1}{2^8} = 0.99609375$ | Gegenereignis (= keine 1 → nur `00000000`) nutzen |
| **4** | Teilbarkeit durch 2 oder 5 | Inklusion-Exklusion: $P = \frac{50+20-10}{100} = 0.6$ | Durch 10 teilbare Zahlen werden doppelt gezählt! |
| **5** | Chevalier de Méré | $P_1 = 1-(5/6)^4 \approx 0.5177$; $P_2 = 1-(35/36)^{24} \approx 0.4914$ | Erfolgs-WS pro Wurf und Anzahl Würfe kompensieren sich **nicht** |
| **6** | Fixpunkt-Problem | $P(\text{kein Treffer}) = (4/5)^5 = 0.32768$ | Jede Position hat **unabhängig** 4 von 5 «Nicht-Treffer»-Werten |
| **7** | Gruppenaufteilung | $P = \frac{\binom{6}{3}\binom{6}{3}}{\binom{12}{6}} = \frac{400}{924} \approx 0.4329$ | Binomialkoeffizienten korrekt anwenden |
| **8** | Geburtstagsparadoxon (Ziffern) | $P = 1 - \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{10^5} = 0.6976$ | Gegenereignis «alle verschieden» ist einfacher |
| **9** | Jobs auf Server verteilen | $P = \frac{20!}{5! \cdot 20^{15}} \approx 0.0006187$ | Sehr klein! Fast sicher teilen sich Server einen Job |
| **10** | Hashing / Linear Probing (optional) | Ergebnismenge durchgehen, benachbarte Positionen zählen | Zyklische Nachbarschaft (Index 5 und 0 sind benachbart) |

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Aufgabentypen

| Aufgabentyp | Erkennungsmerkmal | Lösungsstrategie |
|-------------|-------------------|-----------------|
| Ergebnismenge bestimmen | «Beschreiben Sie $\Omega$» | Alle möglichen Ergebnisse systematisch auflisten; bei mehrfachen Experimenten Kreuzprodukt verwenden |
| Wahrscheinlichkeit berechnen (Laplace) | «Uniform», «fairer Würfel», «zufällig» | $P(E) = \frac{|E|}{|\Omega|}$ — günstige durch mögliche |
| «Mindestens»-Aufgaben | «mindestens eine...», «mindestens zwei...» | **Gegenereignis!** $P(\text{mind.}) = 1 - P(\text{keine/r/s})$ |
| Vereinigung/Schnitt | «oder», «und», Überlappung | Inklusion-Exklusion: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Zählprobleme | «Wie viele Möglichkeiten», Gruppenaufteilung | Binomialkoeffizienten, Fakultäten, Kreuzprodukte |

### 🚨 Häufige Fehlerquellen

1. **Ergebnismenge zu klein:** Alle Möglichkeiten aufschreiben, nicht nur die offensichtlichen.
2. **Uniform verwechselt:** Prüfen ob wirklich **alle** Ergebnisse gleich wahrscheinlich sind (z.B. zwei Würfel: Summe 7 ist wahrscheinlicher als Summe 2).
3. **Gegenereignis vergessen:** Bei «mindestens»-Aufgaben fast immer einfacher über $1 - P(\overline{E})$.
4. **Doppelzählung bei $\cup$:** Immer $P(A \cap B)$ abziehen!
5. **$|\Omega|$ falsch:** Bei $k$ Würfen mit $n$-seitigem Würfel ist $|\Omega| = n^k$ (mit Zurücklegen).

### 🧠 Merkregeln & Eselsbrücken

- **«Mindestens → Gegenereignis»**: Sobald «mindestens» vorkommt → $1 - P(\text{nichts davon})$
- **«Oder → Plus Minus»**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Uniform → Abzählen reicht**: Günstige / Mögliche
- **Chevalier de Méré**: $\frac{1/6}{1/36} = 6$ und $\frac{24}{4} = 6$ → sieht gleich aus, **ist es aber nicht**, weil $(1-p)^n$ nicht linear in $p$ ist!
- **Geburtstagsparadoxon**: Schon bei wenigen Personen/Objekten ist die Wahrscheinlichkeit für Kollisionen überraschend hoch.

### 📌 Formeln zum Auswendiglernen

$$\boxed{P(E) = \frac{|E|}{|\Omega|}}$$

$$\boxed{P(\overline{A}) = 1 - P(A)}$$

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

$$\boxed{\sum_{\omega \in \Omega} P(\omega) = 1}$$

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

### Vorausschau

| Folgewoche | Thema | Bezug zu SW 01 |
|-----------|-------|---------------|
| **SW 02** | Bedingte Wahrscheinlichkeit | Baut auf $P(A \cap B)$ auf → Einführung von $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |
| **SW 03** | Satz von Bayes | Nutzt bedingte WS aus SW 02 + Inklusion-Exklusion aus SW 01 |
| **SW 04** | Zufallsvariablen | Ergebnismengen $\Omega$ werden zu Zahlen abgebildet → baut direkt auf SW 01 |
| **SW 05** | Randomisierte Algorithmen | Verwendet Wahrscheinlichkeitsmodelle aus SW 01–03 für Algorithmenanalyse |

### Wie baut der Stoff auf?

```
SW 01: Wahrscheinlichkeit (Grundlagen)
  │
  ├── Ergebnismenge Ω, Wahrscheinlichkeitsfunktion P
  │   → Basis für ALLE folgenden Wochen
  │
  ├── Mengenoperationen (∪, ∩, Komplement)
  │   → SW 02: Bedingte WS nutzt P(A∩B)
  │   → SW 03: Totale WS, Bayes braucht Partitionen von Ω
  │
  └── Zählprinzipien (n^k, n!, C(n,k))
      → SW 04: Verteilungen (Binomial, etc.)
      → SW 08-10: Kombinatorik in modularer Arithmetik
```

### Wichtigste Konzepte für später

- **$\Omega$ und $P$** sind die Grundlage für alles — ohne sie geht nichts.
- **Inklusion-Exklusion** kommt in SW 02 und SW 03 wieder.
- **Gegenereignis-Trick** wird in jeder Woche mit Wahrscheinlichkeiten gebraucht.
- **Zählprinzipien** ($n^k$, $\binom{n}{k}$) kommen in SW 04 (Binomialverteilung) und SW 08–13 (Kombinatorik, Algebra) wieder.

---

> **Quellen:** DMATH-CODE-Serie01.pdf, DMATH-CODE-Serie01-final.pdf, DMATH-CODE-Serie01.ipynb
