# DMATH.CODE – SW 05: Randomisierte Algorithmen

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Semesterwoche:** SW 05
> **Thema:** Randomisierte Algorithmen
> **Dozent:** Dr. Reto Berger · HSLU · Frühlingssemester 25

---

## 🎯 Lernziele

1. **Erwartete Berechnungskomplexität** einfacher Algorithmen berechnen können.
2. Den **Unterschied zwischen Las Vegas und Monte Carlo Algorithmen** kennen und ihre Vor- und Nachteile verstehen.
3. Den **Code randomisierter Algorithmen** korrekt lesen und interpretieren können.
4. **Probabilistische Analyse** auf konkrete Algorithmen anwenden können (linearSearch, insertionSort, randSelect, randQuicksort).
5. **Monte Carlo Wiederholungsformel** anwenden: Wie oft muss ein MC-Algorithmus laufen, um eine gewünschte Mindest-Erfolgswahrscheinlichkeit zu erreichen?

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Randomisierter Algorithmus** | Algorithmus, der Zufallszahlen oder Zufallsentscheidungen während seiner Berechnung verwendet. Dadurch kann sich seine *Laufzeit* oder das *Ergebnis* bei jeder Ausführung unterscheiden. |
| **Erwartete Berechnungskomplexität** | Gibt an, wie lange ein Algorithmus **im Durchschnitt** benötigt, um ein Problem der Eingabegrösse $n$ zu lösen. Formal: $E(X)$, wobei $X : \omega \longrightarrow$ Anzahl Rechenschritte bei Eingabe $\omega$. |
| **Las Vegas Algorithmus** | Gibt **immer ein korrektes** Ergebnis zurück, nutzt aber zufällige Entscheidungen → die **Laufzeit variiert** (nicht deterministisch). Er beendet die Berechnung erst, wenn eine gültige Lösung gefunden wurde. |
| **Monte Carlo Algorithmus** | Gibt das Ergebnis innerhalb einer **festgelegten Laufzeit** zurück, es kann aber mit einer bestimmten Wahrscheinlichkeit **falsch** sein. Die Fehlerwahrscheinlichkeit kann durch mehrfaches Ausführen beliebig reduziert werden. |
| **Minimum Cut (Min-Cut)** | Kleinste Menge von Kanten in einem Graphen $G=(V,E)$, deren Entfernung den Graphen in zwei getrennte Komponenten teilt. |
| **Pivot (Quicksort/Select)** | Zufällig gewähltes Element, das als Trennwert für die Partitionierung einer Liste dient. |

---

## 📐 Definitionen, Sätze & Beweise

### Definition 1: Erwartete Berechnungskomplexität

> Die **erwartete Berechnungskomplexität** eines Algorithmus gibt an, wie lange ein Algorithmus im Durchschnitt benötigt, um ein Problem mit einer Eingabegrösse $n$ zu lösen. Wir können die Input-Werte $\Omega$ des Algorithmus zufällig wählen (z.B. uniform zufällig). Der Erwartungswert $E(X)$ der Zufallsvariable
>
> $$X : \omega \longrightarrow \text{Anzahl Rechenschritte bei Eingabe } \omega$$
>
> beschreibt dann die durchschnittliche Laufzeit des Algorithmus.

**💡 Intuition:** Man betrachtet alle möglichen Eingaben, berechnet für jede die Anzahl Rechenschritte, und bildet den gewichteten Durchschnitt. Dies nutzt direkt den **Erwartungswert** aus SW 04.

**🔗 Verbindung zu SW 04:** Die erwartete Berechnungskomplexität ist nichts anderes als der Erwartungswert einer Zufallsvariable, die jedem Input die Anzahl Operationen zuordnet. Man verwendet exakt die Formel $E(X) = \sum_i x_i \cdot P(X = x_i)$.

---

### Satz 1: Erwartete Komplexität von linearSearch

> Sei `linearSearch(Liste, Element)` der Algorithmus, der eine Liste der Länge $n$ sequenziell durchsucht. Das Element ist mit Wahrscheinlichkeit $p$ in der Liste enthalten, und wenn ja, dann uniform zufällig an einer der $n$ Positionen.

**Code:**
```python
def linearSearch(Liste, Element):
    for i in range(len(Liste)):        # Rechenschritt (Vergleich)
        if Liste[i] == Element: return True
    return False                        # Rechenschritt
```

**Analyse (aus der Musterlösung des Dozenten):**

Die Anzahl Rechenschritte $X$ hängt davon ab, **wo** das Element in der Liste steht:

- Jeder Vergleich `Liste[i] == Element` zählt als ein Rechenschritt
- Die `for`-Schleife selbst hat ebenfalls Schritte (Inkrement, Vergleich)
- Am Ende: `return False` zählt ebenfalls

**Detaillierte Berechnung:**

Input $L = [a_1, a_2, a_3, \ldots, a_n]$ mit $P(\text{Element} \in L) = p$.

| Rechenschritte $x$ | 3 | 5 | 7 | $\ldots$ | $2n+1$ | $2n+2$ |
|---|---|---|---|---|---|---|
| $P(X = x)$ | $p \cdot \frac{1}{n}$ | $p \cdot \frac{1}{n}$ | $p \cdot \frac{1}{n}$ | $\ldots$ | $p \cdot \frac{1}{n}$ | $1-p$ |

**Test:** $n \cdot \frac{p}{n} + (1-p) = p + 1 - p = 1$ ✓

$$E(X) = 3 \cdot \frac{p}{n} + 5 \cdot \frac{p}{n} + 7 \cdot \frac{p}{n} + \cdots + (2n+1) \cdot \frac{p}{n} + (2n+2) \cdot (1-p)$$

$$= \frac{p}{n} \cdot \big(1 + 3 + 5 + 7 + \cdots + (2n+1) - 1\big) + (2n+2)(1-p)$$

$$= \frac{p}{n} \cdot \big((n+1)^2 - 1\big) + (1-p) \cdot (2n+2)$$

$$= \frac{p}{n} \cdot (n^2 + 2n + 1 - 1) + 2n + 2 - 2np - 2p$$

$$= p \cdot n + 2p + 2n + 2 - 2np - 2p$$

$$= 2n - pn + 2$$

$$\boxed{E(X) = (2-p) \cdot n + 2 \in \Theta(n)}$$

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:** Der Schlüssel der Berechnung ist die Summenformel $1 + 3 + 5 + \cdots + (2n+1) = (n+1)^2$, die aus der Formel $\sum_{k=1}^{n} (2k-1) = n^2$ folgt.

**📌 Zahlenbeispiel:** Für $n = 100$ und $p = 0.5$:

$$E(X) = (2 - 0.5) \cdot 100 + 2 = 1.5 \cdot 100 + 2 = 152 \text{ Rechenschritte}$$

---

### Satz 2: Erwartete Komplexität von insertionSort

> Sei `insertionSort(Liste)` der Algorithmus für eine Liste der Länge $n=5$ mit paarweise verschiedenen Elementen. $X_i$ = Anzahl Rechenschritte im while-Loop bei der $i$-ten Iteration der for-Schleife.

**Code:**
```python
def insertionSort(Liste):
    for i in range(1, len(Liste)):
        j = i                              # Rechenschritt
        while j > 0 and Liste[j] < Liste[j-1]:  # Rechenschritt
            temp = Liste[j]                # Rechenschritt
            Liste[j] = Liste[j-1]          # Rechenschritt
            Liste[j-1] = temp              # Rechenschritt
            j = j - 1                      # Rechenschritt
```

**Analyse (aus der Musterlösung des Dozenten für $n = 5$):**

Für jede Iteration $i$ der `for`-Schleife betrachten wir alle möglichen Permutationen:

**Iteration $i = 1$ (2 Elemente):**

| $x$ | 2 | 8 |
|---|---|---|
| $P(X_1 = x)$ | $\frac{1}{2}$ | $\frac{1}{2}$ |

$E(X_1) = \frac{1}{2} \cdot 2 + \frac{1}{2} \cdot 8 = 5$

Es gibt $2! = 2$ Permutationen: Eine braucht 2 Schritte (bereits sortiert), eine braucht 8 Schritte (ein Swap).

**Iteration $i = 2$ (3 Elemente):**

| $x$ | 2 | 8 | 14 |
|---|---|---|---|
| $P(X_2 = x)$ | $\frac{1}{3}$ | $\frac{1}{3}$ | $\frac{1}{3}$ |

$E(X_2) = \frac{1}{3} \cdot 2 + \frac{1}{3} \cdot 8 + \frac{1}{3} \cdot 14 = 8$

Es gibt $3! = 6$ Permutationen, aufgeteilt in 3 Gruppen.

**Iteration $i = 3$ (4 Elemente):**

$E(X_3) = \frac{1}{4} \cdot 2 + \frac{1}{4} \cdot 8 + \frac{1}{4} \cdot 14 + \frac{1}{4} \cdot 20 = 11$

**Iteration $i = 4$ (5 Elemente):**

$E(X_4) = \frac{1}{5} \cdot 2 + \frac{1}{5} \cdot 8 + \frac{1}{5} \cdot 14 + \frac{1}{5} \cdot 20 + \frac{1}{5} \cdot 26 = 14$

**Gesamte erwartete Komplexität:**

$$X = 2 + X_1 + 2 + X_2 + 2 + X_3 + 2 + X_4$$

$$E(X) = 2 + E(X_1) + 2 + E(X_2) + 2 + E(X_3) + 2 + E(X_4)$$

$$= 2 + 5 + 2 + 8 + 2 + 11 + 2 + 14 = \boxed{46}$$

---

### Definition 2: Las Vegas vs. Monte Carlo Algorithmen

> Man unterscheidet **zwei Hauptkategorien** von randomisierten Algorithmen, die sich hinsichtlich ihrer **Korrektheit** und ihrem **Laufzeitverhalten** unterscheiden:

| Eigenschaft | Las Vegas | Monte Carlo |
|---|---|---|
| **Ergebnis** | **Immer korrekt** | Kann falsch sein |
| **Laufzeit** | Variiert (nicht deterministisch) | **Festgelegt** (deterministisch) |
| **Terminierung** | Erst wenn gültige Lösung gefunden | Immer in fester Zeit |
| **Fehlerreduktion** | Nicht nötig (immer korrekt) | Durch Wiederholung beliebig reduzierbar |

**💡 Intuition:**
- **Las Vegas** = Casino: Du gewinnst immer (korrektes Ergebnis), weisst aber nicht wie lange du spielen musst (variable Laufzeit).
- **Monte Carlo** = Glücksspiel: Du spielst immer gleich lang (feste Laufzeit), könntest aber verlieren (falsches Ergebnis).

---

### Satz 3: Monte Carlo Wiederholungsformel

> Wenn die Wahrscheinlichkeit für eine **korrekte Lösung** bei einem einzigen Durchlauf eines Monte Carlo Algorithmus $p_{\text{korrekt}}$ beträgt, dann berechnet sich die Mindestanzahl Durchläufe $n$, um mit Wahrscheinlichkeit mindestens $1 - \varepsilon$ ein korrektes Resultat zu finden, wie folgt:

$$P(\text{mind. 1 mal richtig in } n \text{ Versuchen}) = 1 - (1 - p_{\text{korrekt}})^n \geq 1 - \varepsilon$$

$$\Leftrightarrow (1 - p_{\text{korrekt}})^n \leq \varepsilon$$

$$\Leftrightarrow n \geq \frac{\log(\varepsilon)}{\log(1 - p_{\text{korrekt}})}$$

**💡 Intuition:** Die Idee ist das Gegenereignis: Die Wahrscheinlichkeit, dass **alle** $n$ Durchläufe falsch sind, ist $(1 - p_{\text{korrekt}})^n$. Diese soll kleiner als $\varepsilon$ sein.

**🔗 Verbindung zu SW 01–03:** Dies nutzt die Gegenwahrscheinlichkeit ($P(\bar{A}) = 1 - P(A)$) und die Unabhängigkeit der Versuche (Multiplikationssatz aus SW 02).

**📌 Zahlenbeispiel (Aufgabe 5):**

$p_{\text{korrekt}} = 0.4$, gewünscht: $P(\text{korrekt}) \geq 0.999$

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**
> 
> - $T$ = Lösung richtig, $F$ = Lösung falsch
> - $P(\text{mind. 1 mal richtig}) = 1 - P(\text{immer falsch}) = 1 - 0.6^n$
> - $1 - 0.6^n = 0.999 \Leftrightarrow 0.6^n = 0.001$
> - $n = \log_{0.6}(0.001) = \frac{\log(0.001)}{\log(0.6)} \approx 13.52$
> - **Aufrunden:** $n = 14$

$$\boxed{n = 14 \text{ Durchläufe}}$$

**Wenn wir also 14 Lösungen berechnen, ist mit Wahrscheinlichkeit 99.9% mindestens eine korrekt.**

```python
import math

def monte_carlo_wiederholungen(p_korrekt, ziel_wahrscheinlichkeit):
    """Berechnet Mindestanzahl Durchläufe für gewünschte Erfolgswahrscheinlichkeit."""
    epsilon = 1 - ziel_wahrscheinlichkeit
    p_falsch = 1 - p_korrekt
    n = math.log(epsilon) / math.log(p_falsch)
    return math.ceil(n)  # Aufrunden!

# Aufgabe 5: p_korrekt = 0.4, Ziel = 99.9%
n = monte_carlo_wiederholungen(0.4, 0.999)
print(f"Mindestens {n} Durchläufe nötig")  # → 14
```

---

## 🧮 Formeln & Rechenregeln

### Kernformeln der Woche

| Formel | Beschreibung | Variablen |
|---|---|---|
| $E(X) = \sum_i x_i \cdot P(X = x_i)$ | Erwartete Berechnungskomplexität | $X$ = Anzahl Rechenschritte, $x_i$ = mögliche Werte |
| $E(X) = (2-p) \cdot n + 2$ | linearSearch Komplexität | $n$ = Listenlänge, $p$ = P(Element in Liste) |
| $1 - (1-p)^n \geq 1 - \varepsilon$ | Monte Carlo Wiederholung | $p$ = P(korrekt pro Durchlauf), $n$ = Anzahl Durchläufe |
| $n \geq \frac{\log(\varepsilon)}{\log(1-p)}$ | Mindestanzahl MC-Durchläufe | $\varepsilon$ = erlaubte Fehlerwahrscheinlichkeit |
| $\sum_{k=1}^{n}(2k-1) = n^2$ | Summe der ungeraden Zahlen | Hilfssumme für linearSearch-Herleitung |
| $\frac{\pi}{4} \approx \frac{\text{Punkte im Kreis}}{n}$ | Monte Carlo Pi-Schätzung | $n$ = Gesamtzahl zufälliger Punkte |

### Wichtige Randfälle

| Situation | Hinweis |
|---|---|
| $p = 1$ (Element sicher in Liste) | linearSearch: $E(X) = n + 2$ (im Mittel halbe Liste durchsuchen) |
| $p = 0$ (Element sicher nicht vorhanden) | linearSearch: $E(X) = 2n + 2$ (immer ganze Liste durchlaufen) |
| $p_{\text{korrekt}} = 0$ bei Monte Carlo | Division durch 0 in der Wiederholungsformel → kein korrektes Ergebnis möglich |
| $p_{\text{korrekt}} = 1$ bei Monte Carlo | Kein Monte Carlo, sondern deterministisch korrekt |
| Aufrunden bei $n$ Durchläufen | Monte Carlo: **Immer aufrunden** ($\lceil \cdot \rceil$), da halbe Durchläufe nicht möglich |

---

## 🍳 Kochrezepte (Schritt-für-Schritt-Anleitungen)

### Kochrezept 1: Erwartete Berechnungskomplexität bestimmen

```
Schritt 1: Alle möglichen Inputs aufzählen
           → Was sind die möglichen Eingaben? (= Ω)

Schritt 2: Pro Input: Rechenschritte zählen
           → X(ω) = Anzahl Operationen für Input ω

Schritt 3: Jedem Input die Wahrscheinlichkeit zuweisen
           → P(ω) = Wahrscheinlichkeit für diesen Input
           → Oft: Gleichverteilung → P(ω) = 1/|Ω|

Schritt 4: Erwartungswert berechnen
           → E(X) = Σ X(ω) · P(ω)

Beispiel: linearSearch in Liste der Länge n
  → X(Position i) = i Vergleiche
  → P(Position i) = 1/n
  → E(X) = (1 + 2 + ... + n) / n = (n+1)/2
```

### Kochrezept 2: Algorithmus klassifizieren (Las Vegas vs. Monte Carlo)

```
Frage 1: Ist das Ergebnis IMMER korrekt?
├── JA → Las Vegas
│        → Laufzeit ist die Zufallsvariable
│        → "Immer richtig, aber manchmal langsam"
│
└── NEIN → Frage 2: Terminiert der Algorithmus IMMER in fester Zeit?
           ├── JA → Monte Carlo
           │        → Korrektheit ist die Zufallsvariable
           │        → "Immer schnell, aber manchmal falsch"
           └── NEIN → Weder noch (oder beides prüfen)

Merkregel:
  "Las Vegas = immer RICHTIG" (Las Vegas ist echt/real)
  "Monte Carlo = immer SCHNELL" (Monte Carlo ist ein Spiel/Glück)
```

### Kochrezept 3: Monte Carlo Wiederholungsformel

```
Gegeben: MC-Algorithmus mit Erfolgswahrscheinlichkeit p pro Durchlauf
Gesucht: Wie oft wiederholen für Gesamterfolg ≥ 1 - ε?

Schritt 1: p bestimmen (Erfolgswahrscheinlichkeit eines Durchlaufs)
Schritt 2: ε bestimmen (gewünschte Fehlerwahrscheinlichkeit)
Schritt 3: Formel anwenden:
           n ≥ ⌈log(ε) / log(1 - p)⌉
           ⚠️ AUFRUNDEN! (⌈...⌉)

Beispiel: p = 1/2, ε = 0.001 (99.9% Sicherheit)
  → n ≥ ⌈log(0.001) / log(0.5)⌉ = ⌈9.97⌉ = 10 Wiederholungen

Herleitung: P(alle n falsch) = (1-p)^n ≤ ε
  → n · log(1-p) ≤ log(ε)
  → n ≥ log(ε) / log(1-p)    (Division durch negative Zahl → ≥ dreht!)
```

### Entscheidungsbaum: Welche Analyse brauche ich?

```
Aufgabenstellung lesen:
│
├── "Erwartete Komplexität von Algorithmus X?"
│   └── Kochrezept 1: E(X) = Σ Schritte · P(Input)
│
├── "Las Vegas oder Monte Carlo?"
│   └── Kochrezept 2: Immer korrekt? → Las Vegas. Immer schnell? → Monte Carlo.
│
├── "Wie oft wiederholen für Sicherheit ≥ ...?"
│   └── Kochrezept 3: n ≥ ⌈log(ε) / log(1-p)⌉
│
├── "Erwartete Komplexität von randQuicksort?"
│   └── O(n log n) – jedes Paar wird mit P = 2/(j-i+1) verglichen
│
└── "Karger Min-Cut: Wie oft wiederholen?"
    └── P(Erfolg) ≥ 2/(n(n-1))  →  MC-Formel mit p = 2/(n(n-1))
```

---

## 📊 Vergleiche & Klassifizierungen

### Las Vegas vs. Monte Carlo – Detailvergleich

| Kriterium | Las Vegas | Monte Carlo |
|---|---|---|
| **Korrektheit** | ✅ Immer korrekt | ⚠️ Kann falsch sein |
| **Laufzeit** | ⚠️ Variabel, nicht vorhersagbar | ✅ Fest/beschränkt |
| **Terminierung** | Endet erst bei gültiger Lösung | Endet immer in fester Zeit |
| **Fehlerreduktion** | Nicht nötig | Wiederholung → Fehler $\to 0$ |
| **Typische Anwendung** | Sortieren, Selektion | Approximation, Optimierung |
| **Beispiel aus Serie** | randQuicksort, randSelect | monteCarloEstimator (π), Karger's Min-Cut |
| **Merkregel** | "Richtig, aber langsam (manchmal)" | "Schnell, aber unsicher" |

### Algorithmen-Klassifizierung aus der Serie

| Algorithmus | Kategorie | Begründung |
|---|---|---|
| `randQuicksort` | **Las Vegas** | Sortiert immer korrekt. Nur die Aufteilung in L, M, R ist zufällig (abhängig vom Pivot). |
| `randSelect` | **Las Vegas** | Gibt immer das korrekte $i$-te Element der sortierten Liste zurück. Nur die Pivot-Wahl ist zufällig. |
| `monteCarloEstimator` (π) | **Monte Carlo** | Approximiert $\pi$ – das Ergebnis ist eine Schätzung, die falsch sein kann, aber mit mehr Punkten genauer wird. |
| Karger's Min-Cut | **Monte Carlo** | Kann den falschen Schnitt finden. Durch Wiederholung wird die Fehlerwahrscheinlichkeit reduziert. |

---

## 💻 Code-Beispiele (Python)

### 1. Monte Carlo Pi-Schätzung (Estimator)

**Mathematischer Hintergrund:**
Ein Viertelkreis mit Radius 1 hat die Fläche $\frac{\pi}{4}$, ein Einheitsquadrat hat Fläche 1. Wenn wir $n$ uniform zufällige Punkte $(x, y) \in [0,1] \times [0,1]$ erzeugen und zählen, wie viele im Viertelkreis liegen ($x^2 + y^2 \leq 1$), dann gilt:

$$\frac{\text{Punkte im Kreis}}{n} \approx \frac{\pi}{4} \quad \Rightarrow \quad \pi \approx 4 \cdot \frac{\text{Punkte im Kreis}}{n}$$

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**
> Der Anteil der Punkte, die im Viertelkreis mit Radius 1 liegen, ist $\approx \frac{1}{4} \cdot 1^2 \cdot \pi = \frac{\pi}{4}$.
> Für jeden zufällig erzeugten Punkt, der im Kreis $x^2 + y^2 \leq 1^2$ liegt, wird im "test" eine 1 gespeichert.
> **→ Dies ist ein Monte Carlo Algorithmus, der $\pi$ approximiert.**

```python
import numpy as np
import matplotlib.pyplot as plt

def monteCarloEstimator(n):
    """Monte Carlo Schätzung von Pi.

    Erzeugt n zufällige Punkte im Einheitsquadrat
    und berechnet den Anteil, der im Viertelkreis liegt.

    Kategorie: Monte Carlo (approximiert pi, Ergebnis kann ungenau sein)
    """
    x = np.random.uniform(0, 1, n)  # n zufällige x-Koordinaten in [0,1]
    y = np.random.uniform(0, 1, n)  # n zufällige y-Koordinaten in [0,1]
    # Für jeden Punkt prüfen: liegt er im Viertelkreis? (x² + y² ≤ 1)
    kreis = [1 for i in range(n) if x[i]**2 + y[i]**2 <= 1]
    return 4 * sum(kreis) / n  # Schätzung von pi

# Beispiel: Abweichung von pi
print(f"Schätzung - pi = {monteCarloEstimator(10_000_000) - np.pi}")
# Typische Ausgabe: ≈ 4.2e-05 (sehr nahe an 0)
```

**Visualisierung:**
```python
# Visualisierung der Monte Carlo Pi-Schätzung
anzahlPunkte = 50
x = np.random.uniform(0, 1, anzahlPunkte)
y = np.random.uniform(0, 1, anzahlPunkte)

x_k = np.linspace(0, 1, 200)     # Kreisbogen-Koordinaten
y_k = np.sqrt(1 - x_k**2)        # Viertelkreis: y = sqrt(1 - x²)

fig = plt.figure(figsize=(5, 5))
plt.scatter(x, y, s=5)            # Zufällige Punkte
plt.plot(x_k, y_k, color="red")   # Viertelkreis
plt.vlines([0, 1], 0, 1, color="blue")  # Quadrat-Ränder
plt.hlines([0, 1], 0, 1, color="blue")
plt.title("Monte Carlo Pi-Schätzung")
plt.show()
```

---

### 2. Randomized Quicksort (Las Vegas)

**Mathematischer Hintergrund:**
Quicksort wählt ein zufälliges Pivot-Element, partitioniert das Array in drei Teile (kleiner, gleich, grösser als Pivot) und sortiert rekursiv. Die **zufällige Pivot-Wahl** vermeidet Worst-Case-Szenarien ($O(n^2)$) und führt zu erwarteter Laufzeit $O(n \log n)$.

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**
> "Der Algorithmus sortiert immer korrekt. Nur die Aufteilung in L, M und R ist zufällig. ⟹ **Las Vegas-Algorithmus**"

```python
import random as rd

def randomized_quicksort(arr):
    """Randomisierter Quicksort – sortiert eine Liste.

    Wählt zufällig ein Pivot-Element und teilt die Liste
    in drei Teile: kleiner, gleich, grösser als Pivot.

    Kategorie: Las Vegas (immer korrektes Ergebnis)
    Erwartete Komplexität: O(n log n)
    Worst-Case: O(n²) – aber extrem unwahrscheinlich bei zufälligem Pivot
    """
    if len(arr) <= 1:
        return arr
    pivot = rd.choice(arr)  # Zufällige Pivot-Wahl
    left = [x for x in arr if x < pivot]      # Elemente kleiner als Pivot
    middle = [x for x in arr if x == pivot]    # Elemente gleich Pivot
    right = [x for x in arr if x > pivot]      # Elemente grösser als Pivot
    # Korrekte Zusammensetzung: sortiert(links) + mitte + sortiert(rechts)
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Beispiel
print(randomized_quicksort([7, 7, 9, 7, 7, 9, 4, 3, 5, 7, 1, 2, 7, 1, 9, -1, 6]))
# → [-1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 9, 9, 9]
```

---

### 3. Randomized Select (Las Vegas)

**Mathematischer Hintergrund:**
Gibt das **$i$-te Element** der sortierten Liste zurück, **ohne die gesamte Liste zu sortieren**. Wählt ein zufälliges Pivot, partitioniert in $L$ (kleiner) und $R$ (grösser), und sucht rekursiv nur in der relevanten Hälfte.

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**
> - $|L|$ Elemente sind kleiner als $x$ (das Pivot-Element)
> - $|A| - |L| - 1$ Elemente sind grössergleich als $x$
> - Zufällige Aufteilung in $[\ldots] < x \leq [\ldots]$
> - Wenn $i < |L|$: das $i$-kleinste Element in der sortierten Liste $L$ suchen
> - Wenn $i = |L|$: $x$ ist das $i$-te Element in der sortierten Liste $A$
> - Sonst: das $(i - |L| - 1)$-te Element in der sortierten Liste $R$ suchen
> - **Immer korrekt ⟹ Las Vegas-Algorithmus**
> - **Erwartete Berechnungskomplexität: $O(n)$**

```python
import numpy as np

def randSelect(A, i):
    """Findet das i-te Element der sortierten Liste (0-indexiert).

    Sucht rekursiv mit zufälligem Pivot – wie Quicksort,
    aber nur eine Seite wird weiterverfolgt.

    Kategorie: Las Vegas (immer korrektes Ergebnis)
    Erwartete Komplexität: O(n)
    """
    n = len(A)
    if n == 1:
        return A[n - 1]  # Nur ein Element → das ist das Ergebnis

    pivot = np.random.randint(n)  # Zufälliger Index als Pivot
    L = []  # Elemente kleiner als Pivot
    R = []  # Elemente grösser/gleich Pivot

    for j in range(len(A)):
        if j != pivot:
            if A[j] < A[pivot]:
                L.append(A[j])
            else:
                R.append(A[j])

    if i < len(L):        # i-kleinstes Element muss in L sein
        return randSelect(L, i)
    elif i == len(L):      # Pivot ist genau das i-te Element
        return A[pivot]
    else:                  # Element ist in R
        return randSelect(R, i - (len(L) + 1))

# Beispiel: 3. Element (0-indexiert) der sortierten Liste finden
print(randSelect([8, 4, 7, 3, 2, 5, 5, 8, 5, 2], 3))  # → 4
# Sortiert: [2, 2, 3, 4, 5, 5, 5, 7, 8, 8] → Index 3 = 4 ✓
```

**📌 Durchgerechnetes Beispiel (aus der Musterlösung):**

$A = [7, 5, 1, 8, 8, 7, 4, 1, 2, 8]$, $i = 6$ (suche das 7. Element der sortierten Liste)

Sortiert wäre: $[1, 1, 2, 4, 5, 7, 7, 8, 8, 8]$ → das 7. Element (Index 6) ist **7**.

1. **Pivot = 6** (zufällig), $A[\text{pivot}] = 4$:
   - $L = [1, 1, 2]$ (3 Elemente), $R = [7, 5, 8, 8, 7, 8]$ (6 Elemente)
   - $i = 6 > 3$ → rechts suchen: $i = 6 - 3 - 1 = 2$

2. **Pivot = 3** (zufällig), Wäre $[5, 7, 7]$, Pivot = $8$:
   - $L = [7, 5, 7]$, $R = [8, 8]$
   - $i = 2 < 3$ → links das 2-te Element suchen

3. **Pivot = 0**, Wäre $[5, 7, 7]$, Pivot = $7$:
   - $L = [5]$, $R = [7]$
   - $i = 2 > 1$ → rechts: $i = 2 - 1 - 1 = 0$

4. $|R| = [7]$ → nur 1 Element → **return 7** ✓

---

### 4. Linear Search

```python
def linearSearch(Liste, Element):
    """Lineare Suche – durchsucht Liste sequenziell.

    Deterministischer Algorithmus (kein Zufall).
    Best-Case: O(1), Worst-Case: O(n), Erwartet: O(n)
    """
    for i in range(len(Liste)):
        if Liste[i] == Element:
            return True
    return False

print(linearSearch([1, 2, 3, 4], 1))  # → True
```

---

### 5. Insertion Sort

```python
def insertionSort(Liste):
    """Insertion Sort – sortiert Liste in-place.

    Deterministischer Algorithmus.
    Best-Case: O(n), Worst-Case: O(n²), Erwartet: O(n²)
    """
    for i in range(1, len(Liste)):
        j = i
        while j > 0 and Liste[j] < Liste[j-1]:
            # Elemente tauschen (Swap)
            temp = Liste[j]
            Liste[j] = Liste[j-1]
            Liste[j-1] = temp
            j = j - 1

lst = [8, 7, 6, 5, 4, 3, 2, 1]
insertionSort(lst)
print(lst)  # → [1, 2, 3, 4, 5, 6, 7, 8]
```

---

### 6. Karger's Minimum Cut (Monte Carlo)

**Mathematischer Hintergrund:**
Der Algorithmus findet einen Minimum Cut eines Graphen, indem er wiederholt zufällig eine Kante wählt und die beiden Endknoten verschmilzt, bis nur zwei Knoten übrig sind. Die verbleibenden Kanten bilden einen Schnitt.

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**
> Der Algorithmus kann den falschen Cut finden (z.B. return 2, obwohl der tatsächliche Min-Cut 1 ist). **⟹ Monte Carlo Algorithmus**
> Durch mehrere Durchläufe und Wahl des Minimums wird die Genauigkeit erhöht.

```python
import random
import copy

def find_min_cut(graph):
    """Karger's randomisierter Min-Cut Algorithmus.

    Verschmilzt zufällig Kanten, bis nur 2 Knoten übrig sind.
    Die Anzahl verbleibender Kanten ist der geschätzte Min-Cut.

    Kategorie: Monte Carlo (kann falsches Ergebnis liefern)
    Verbesserung: Mehrfach ausführen, Minimum nehmen!
    """
    g = copy.deepcopy(graph)  # Kopie, damit Original unverändert bleibt

    while len(g) > 2:
        # Schritt 1: Wähle zufällig eine Kante {u, v}
        u = random.choice(list(g.keys()))
        v = random.choice(g[u])

        # Schritt 2: Verschmelze v in u
        g[u].extend(g[v])

        # Schritt 3: Ersetze alle Vorkommen von v durch u
        for node in g[v]:
            g[node] = [u if x == v else x for x in g[node]]

        # Schritt 4: Entferne Selbstschleifen
        g[u] = [x for x in g[u] if x != u]

        # Schritt 5: Entferne Knoten v
        del g[v]

    # Die Anzahl der verbleibenden Kanten = geschätzter Min-Cut
    return len(list(g.values())[0])

# Beispielgraph als Adjazenzliste (vollständiger Graph K4)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}

# Mehrere Durchläufe für höhere Genauigkeit (Monte Carlo!)
min_cut = min(find_min_cut(graph) for _ in range(100))
print(f"Geschätzter Minimum Cut: {min_cut}")  # → 3
```

---

### 7. Monte Carlo Wiederholungsberechnung

```python
import math

def mc_wiederholungen(p_korrekt, ziel):
    """Berechnet Mindestanzahl Durchläufe eines Monte Carlo Algorithmus.

    Args:
        p_korrekt: Wahrscheinlichkeit für korrekte Lösung pro Durchlauf
        ziel: Gewünschte Gesamtwahrscheinlichkeit (z.B. 0.999 für 99.9%)

    Returns:
        Mindestanzahl Durchläufe (aufgerundet)
    """
    epsilon = 1 - ziel           # Erlaubte Fehlerwahrscheinlichkeit
    p_falsch = 1 - p_korrekt     # Wahrscheinlichkeit für falsches Ergebnis
    n = math.log(epsilon) / math.log(p_falsch)
    return math.ceil(n)          # Aufrunden!

# Aufgabe 5: p = 0.4, Ziel = 99.9%
print(f"Mindestens {mc_wiederholungen(0.4, 0.999)} Durchläufe")  # → 14

# Weitere Beispiele
print(f"p=0.5, 99%: {mc_wiederholungen(0.5, 0.99)} Durchläufe")  # → 7
print(f"p=0.1, 95%: {mc_wiederholungen(0.1, 0.95)} Durchläufe")  # → 29
```

---

## ✏️ Übungsaufgaben-Zusammenfassung

| Nr. | Thema / Konzept | Lösungsansatz | Typische Stolpersteine |
|---|---|---|---|
| **1** | Erwartete Komplexität von `linearSearch` | Fälle aufstellen (Element an Position 1..n oder nicht vorhanden), Wahrscheinlichkeiten zuordnen, $E(X)$ berechnen | Rechenschritte korrekt zählen (for-Loop-Overhead!). Summenformel für ungerade Zahlen: $1+3+5+\cdots+(2n+1)=(n+1)^2$ |
| **2** | Erwartete Komplexität von `insertionSort` | Alle Permutationen für $n=5$ durchgehen, pro while-Loop-Iteration die Rechenschritte zählen, $E(X_i)$ berechnen, mit Linearität des EW addieren | Permutationen vollständig aufzählen. Die 2 Schritte pro for-Iteration nicht vergessen (Overhead). |
| **3** | `randQuicksort` klassifizieren | Argument: Ergebnis ist **immer korrekt sortiert**, nur Pivot (und damit Partitionierung) ist zufällig → **Las Vegas** | Nicht verwechseln: Zufällige Laufzeit ≠ zufälliges Ergebnis |
| **4** | Karger's Min-Cut klassifizieren | Beispiel zeigen: Algorithmus kann falschen Cut liefern → **Monte Carlo** | Verstehen, warum zufällige Kantenwahl auch nicht-minimale Cuts erzeugen kann |
| **5** | Monte Carlo Wiederholungen | $1 - 0.6^n \geq 0.999$ lösen → $n = \lceil\log_{0.6}(0.001)\rceil = 14$ | **Aufrunden** nicht vergessen! Logarithmus-Basis beachten |
| **6** | Pi-Estimator klassifizieren & erklären | Viertelkreis im Einheitsquadrat, Anteil $\approx \frac{\pi}{4}$, daher $\pi \approx 4 \cdot \frac{\text{Treffer}}{n}$ → **Monte Carlo** | Erkennen, dass $x^2 + y^2 \leq 1$ den Viertelkreis definiert |
| **7** | `randSelect` klassifizieren & erklären | Argument: Ergebnis ist **immer korrekt** (das $i$-te Element), nur Pivot ist zufällig → **Las Vegas**. Optional: Erwartete Komplexität $O(n)$ zeigen | Rekursion korrekt nachvollziehen: $i$-Anpassung beim Wechsel zu $R$ |

---

## ⚠️ Prüfungsrelevante Hinweise

### ⚡ Typische Aufgabentypen und wie man sie erkennt

1. **"Bestimmen Sie die erwartete Berechnungskomplexität"**
   → Alle möglichen Eingaben/Fälle aufstellen, Rechenschritte pro Fall zählen, Wahrscheinlichkeiten zuweisen, $E(X)$ berechnen.

2. **"Zu welcher Kategorie gehört folgender Algorithmus?"**
   → Prüfe: Ist das **Ergebnis immer korrekt**? Ja → Las Vegas. Kann es falsch sein → Monte Carlo.

3. **"Wie oft muss der Algorithmus ausgeführt werden?"**
   → Monte Carlo Wiederholungsformel: $n \geq \frac{\log(\varepsilon)}{\log(1-p)}$

4. **"Was berechnet folgender Algorithmus?"**
   → Code lesen, Invarianten identifizieren, Beispiel durchrechnen.

### 🔑 Merkregeln und Eselsbrücken

| Merkregel | Erklärung |
|---|---|
| **"Las Vegas = immer richtig"** | Wie in Las Vegas: das Casino gewinnt immer (= korrekt). Aber du weisst nicht, wie lange du spielst (= variable Laufzeit). |
| **"Monte Carlo = schnell aber unsicher"** | Wie Monte Carlo Simulation: feste Rechenzeit, aber das Ergebnis ist eine Schätzung. |
| **"Pivot zufällig → Las Vegas"** | Wenn nur der Zufall in der Pivot-Wahl steckt (Quicksort, Select) und das Ergebnis trotzdem korrekt ist → immer Las Vegas. |
| **"Aufrunden bei MC-Wiederholungen"** | $n$ muss ganzzahlig sein → immer $\lceil \cdot \rceil$ verwenden. |
| **Summenformel** | $1 + 3 + 5 + \cdots + (2k-1) = k^2$ (Summe der ersten $k$ ungeraden Zahlen) |

### 🧠 Formeln die man auswendig wissen muss

1. **Erwartungswert:** $E(X) = \sum_i x_i \cdot P(X = x_i)$
2. **Monte Carlo Wiederholung:** $n \geq \frac{\log(\varepsilon)}{\log(1-p)}$
3. **Gegenwahrscheinlichkeit:** $P(\text{mind. 1 korrekt}) = 1 - (1-p)^n$
4. **Las Vegas vs. Monte Carlo Unterscheidung** (Korrektheit vs. Laufzeit)

### ❌ Häufige Fehlerquellen

1. **Rechenschritte falsch zählen:** Jede Zuweisung, jeder Vergleich, jeder Schleifendurchlauf zählt. Besonders den Overhead der `for`- und `while`-Schleifen nicht vergessen!
2. **Las Vegas / Monte Carlo verwechseln:** Der entscheidende Unterschied ist die **Korrektheit des Ergebnisses**, nicht die Laufzeit!
3. **Logarithmus-Basis bei MC-Wiederholungsformel:** $\log_{(1-p)}(\varepsilon) = \frac{\ln(\varepsilon)}{\ln(1-p)}$ – beides muss den gleichen Logarithmus verwenden.
4. **Nicht aufrunden:** Bei der MC-Wiederholungsformel immer auf die nächste ganze Zahl **aufrunden**.
5. **randSelect $i$-Anpassung:** Beim Wechsel in die rechte Teilliste $R$ muss $i$ um $|L| + 1$ reduziert werden (Pivot wird mitgezählt!).

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

```
SW 01 Wahrscheinlichkeit
  └── Grundbegriffe: Ω, P, Laplace, Mengenoperationen
       │
SW 02 Bedingte Wahrscheinlichkeit
  └── P(A|B), Unabhängigkeit, Multiplikationssatz
       │        └──── wird genutzt für MC-Wiederholungsformel
       │               (unabhängige Durchläufe!)
SW 03 Satz von Bayes
  └── Totale Wahrscheinlichkeit, Baumdiagramme
       │
SW 04 Zufallsvariablen
  └── E(X), Verteilungen, Linearität des Erwartungswerts
       │        └──── DIREKTE GRUNDLAGE für erwartete
       │               Berechnungskomplexität!
       │
██████████████████████████████████████████████████████████
█  SW 05 Randomisierte Algorithmen  ◄── WIR SIND HIER  █
██████████████████████████████████████████████████████████
       │
       │  Schlüsselkonzepte:
       │  • Erwartete Berechnungskomplexität
       │  • Las Vegas vs. Monte Carlo
       │  • randQuicksort, randSelect, Karger's Min-Cut
       │  • Monte Carlo Pi-Schätzung
       │  • Wiederholungsformel
       │
SW 06 Markov-Ketten
  └── Übergangsmatrizen, stationäre Verteilung
       │        └──── Randomisierte Prozesse mit Zustandsübergängen
       │               (Erweiterung der probabilistischen Analyse)
       │
SW 07 Matrizenalgebra
  └── Matrizenmultiplikation, Inverse
       └──── Verifizierbare Algorithmen (z.B. randomisierter
              Matrizenmultiplikations-Check = Monte Carlo Paradigma)
```

### Konkrete Verbindungen

| Woche | Verbindung zu SW 05 |
|---|---|
| **SW 01–03** | Wahrscheinlichkeitsrechnung ist die **Grundlage** für die Analyse randomisierter Algorithmen. Gegenwahrscheinlichkeit und Multiplikationssatz werden direkt in der MC-Wiederholungsformel verwendet. |
| **SW 04** | Der **Erwartungswert** $E(X)$ ist das zentrale Werkzeug zur Berechnung der erwarteten Berechnungskomplexität. Die **Linearität des Erwartungswerts** wird bei insertionSort direkt angewandt (Zerlegung in $X_i$). |
| **SW 06** | Markov-Ketten sind selbst randomisierte Prozesse mit Zustandsübergängen – das Paradigma "Zufall in der Berechnung" wird fortgesetzt. |
| **SW 07+** | Randomisierte Algorithmen tauchen auch in der linearen Algebra auf (z.B. Freivalds' Algorithmus zur Matrizenmultiplikations-Verifikation ist ein Monte Carlo Algorithmus). |

---

> **📌 Zusammenfassung auf einen Blick:**
> SW 05 führt das Konzept der **randomisierten Algorithmen** ein und klassifiziert sie in **Las Vegas** (immer korrekt, variable Laufzeit) und **Monte Carlo** (feste Laufzeit, möglicherweise falsch). Die **erwartete Berechnungskomplexität** verbindet den Erwartungswert aus SW 04 mit konkreter Algorithmenanalyse. Wichtigste Formeln: $E(X) = (2-p)n+2$ für linearSearch und $n \geq \frac{\log \varepsilon}{\log(1-p)}$ für Monte Carlo Wiederholungen. Alle sechs Algorithmen aus der Serie (linearSearch, insertionSort, randQuicksort, randSelect, Pi-Estimator, Karger's Min-Cut) müssen klassifiziert und erklärt werden können.
