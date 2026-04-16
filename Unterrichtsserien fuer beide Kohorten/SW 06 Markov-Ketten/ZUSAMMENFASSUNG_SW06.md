# DMATH.CODE – SW 06: Markov-Ketten

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Semesterwoche:** SW 06
> **Thema:** Markov-Ketten
> **Dozent:** Dr. Reto Berger · HSLU · Frühlingssemester 25

---

## 🎯 Lernziele

1. Das **Konzept einer Markov-Kette** kennen und die **Markov-Eigenschaft** verstehen.
2. Die **Übergangsmatrix** aus einem gerichteten Graphen korrekt aufstellen können.
3. **Wahrscheinlichkeitsverteilungen über mehrere Zeitschritte** berechnen können (Matrix-Vektor-Multiplikation).
4. Die **invariante (stationäre) Verteilung** einer Markov-Kette berechnen können.
5. Entscheiden können, ob eine Markov-Kette **irreduzibel** bzw. **aperiodisch** ist.
6. Das **PageRank-Modell** (Zufallssurfer) als Anwendung von Markov-Ketten verstehen.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Markov-Kette** | Folge von Zufallsvariablen $X_0, X_1, X_2, \ldots$, bei der der zukünftige Zustand **nur vom aktuellen Zustand** abhängt, nicht von der Vergangenheit. |
| **Markov-Eigenschaft** | $P(X_{t+1} = x \mid X_0 = s_0 \wedge \ldots \wedge X_t = s_t) = P(X_{t+1} = x \mid X_t = s_t)$ – "Gedächtnislosigkeit". |
| **Zustandsmenge** | Menge $S \subset \mathbb{N}$ aller möglichen Zustände (= Knoten des Graphen). |
| **Übergangswahrscheinlichkeit** | $p_{s_t, x} = P(X_{t+1} = x \mid X_t = s_t)$ – Wahrscheinlichkeit, von Zustand $s_t$ nach $x$ zu wechseln. |
| **Übergangsmatrix** | Matrix $T$ mit allen Übergangswahrscheinlichkeiten $p_{i,j}$. Jede **Zeile summiert zu 1** (stochastische Matrix). |
| **Homogene Markov-Kette** | Die Übergangswahrscheinlichkeiten $p_{s_t, x}$ sind für **alle Zeitpunkte gleich**. |
| **Startverteilung** | Wahrscheinlichkeitsverteilung für $X_0$: $P(X_0 = s_1), P(X_0 = s_2), \ldots$ |
| **Invariante (stationäre) Verteilung** | Verteilung $\pi$, die sich unter der Übergangsmatrix **nicht mehr ändert**: $P(X_{t+1} = x) = P(X_t = x)$ für alle $t, x$. |
| **Irreduzibel** | Für alle zwei Knoten im Graphen existiert ein **Verbindungspfad** entlang der Kanten. |
| **Aperiodisch** | Für jeden Knoten $s$ ist der **ggT** aller Rückkehrzeiten $N_s = \{t : P(X_t = s \mid X_0 = s) > 0\}$ gleich **1**. |
| **PageRank** | Google-Algorithmus zur Bewertung von Webseiten basierend auf dem Zufallssurfer-Modell (= Markov-Kette auf dem Link-Netzwerk). |

---

## 📐 Definitionen, Sätze & Beweise

### Definition 1: Markov-Kette & Übergangsmatrix

> Gegeben sei ein **gerichteter Graph**. Seine Knoten repräsentieren die **Zustände** eines dynamischen Systems und seine Kanten alle möglichen **Zustandsübergänge**.
>
> - Die Knoten werden nummeriert, ihre Nummern bilden die **Zustandsmenge** $S \subset \mathbb{N}$.
> - Zu jedem **Zeitpunkt** $t = 0, 1, 2, \ldots$ definieren wir die Zufallsvariable $X_t : \Omega \to S$, die den Zustand $s_t$ im Zeitpunkt $t$ angibt.
>
> Die Folge $X_0, X_1, X_2, \ldots$ heisst **Markov-Kette**, wenn für alle Zeitpunkte $t$ gilt:
>
> $$P(X_{t+1} = x \mid X_0 = s_0 \wedge \ldots \wedge X_t = s_t) = P(X_{t+1} = x \mid X_t = s_t)$$

**💡 Intuition:** Das System hat **kein Gedächtnis** – es ist egal, wie man in den aktuellen Zustand gekommen ist. Nur der aktuelle Zustand bestimmt die Zukunft.

**Übergangsmatrix:**

$$T = \begin{pmatrix} p_{1,1} & p_{1,2} & \cdots & p_{1,n} \\ p_{2,1} & p_{2,2} & \cdots & p_{2,n} \\ \vdots & \vdots & \ddots & \vdots \\ p_{n,1} & p_{n,2} & \cdots & p_{n,n} \end{pmatrix}$$

- **Zeile $i$:** Übergangswahrscheinlichkeiten **von** Zustand $i$ **nach** allen anderen Zuständen
- **Spalte $j$:** Wahrscheinlichkeit, **in** Zustand $j$ **anzukommen** von allen Zuständen
- 🔑 **Jede Zeile summiert zu 1** (stochastische Matrix)

---

### Aufgabe 1: Übergangsmatrix aus Graph ablesen

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**

Gegeben: Graph mit 3 Zuständen und Kantenbeschriftungen:
- Von 1: nach 1 mit 0.7, nach 3 mit 0.3
- Von 2: nach 1 mit 0.4, nach 3 mit 0.6
- Von 3: nach 1 mit 0.2, nach 2 mit 0.3, nach 3 mit 0.5

$$T = \begin{pmatrix} 0.7 & 0 & 0.3 \\ 0.4 & 0 & 0.6 \\ 0.2 & 0.3 & 0.5 \end{pmatrix} \quad \text{sum} = 1 \text{ pro Zeile ✓}$$

**📌 Rezept zum Aufstellen der Übergangsmatrix:**
1. Knoten nummerieren → Zeilen und Spalten der Matrix
2. Für jeden Knoten $i$: Alle ausgehenden Kanten ablesen → Zeile $i$ ausfüllen
3. Fehlende Übergänge = 0
4. **Kontrolle:** Jede Zeile muss 1 ergeben!

---

### Aufgabe 2: Irrfahrt auf Doppelpyramide

> Bei einer **Irrfahrt** wird von jedem Knoten **uniform zufällig** auf einen seiner Nachbarknoten gewechselt → $p_{i,j} = \frac{1}{\text{Grad}(i)}$

Doppelpyramide mit 5 Knoten (1 oben, 2-3-4 Mitte verbunden, 5 unten):
- Knoten 1: Nachbarn {2, 3, 4} → je $\frac{1}{3}$
- Knoten 2: Nachbarn {1, 3, 4, 5} → je $\frac{1}{4}$
- Knoten 3: Nachbarn {1, 2, 4, 5} → je $\frac{1}{4}$
- Knoten 4: Nachbarn {1, 2, 3, 5} → je $\frac{1}{4}$
- Knoten 5: Nachbarn {2, 3, 4} → je $\frac{1}{3}$

$$T = \frac{1}{12} \begin{pmatrix} 0 & 4 & 4 & 4 & 0 \\ 3 & 0 & 3 & 3 & 3 \\ 3 & 3 & 0 & 3 & 3 \\ 3 & 3 & 3 & 0 & 3 \\ 0 & 4 & 4 & 4 & 0 \end{pmatrix}$$

---

### Definition 2: Startverteilung

> Am Anfang der Markov-Kette können wir die **Startverteilung** von $X_0$ festlegen, indem wir für die Knoten $s \in S$ eine Wahrscheinlichkeitsverteilung definieren:
>
> | | $s_1$ | $s_2$ | $s_3$ | $\ldots$ | $s_n$ |
> |---|---|---|---|---|---|
> | $P(X_0 = s)$ | $P(X_0 = s_1)$ | $P(X_0 = s_2)$ | $P(X_0 = s_3)$ | $\ldots$ | $P(X_0 = s_n)$ |

Oft wird genau einem Knoten die Wahrscheinlichkeit 1 zugeordnet (deterministischer Start), z.B. $(s_1, s_2, s_3) = (0, 0, 1)$ bedeutet: Start im Zustand 3.

---

### Satz 1: Verteilung über mehrere Zeitschritte

> Sei $X_0, X_1, X_2, \ldots$ eine Markov-Kette, dann gilt:
>
> $$P(X_{t+1} = x) = P(X_t = s_1) \cdot p_{s_1, x} + P(X_t = s_2) \cdot p_{s_2, x} + \ldots + P(X_t = s_n) \cdot p_{s_n, x}$$

**💡 Intuition:** Die Verteilung zum Zeitpunkt $t+1$ ergibt sich aus der Verteilung zum Zeitpunkt $t$ **multipliziert mit der Übergangsmatrix**. In Vektorschreibweise:

$$\vec{v}_{t+1} = \vec{v}_t \cdot T$$

> 👨‍🏫 **Aus den handschriftlichen Notizen des Dozenten:**
>
> $P(X_1 = x) = P(X_0 = s_1) \cdot P(X_1 = x \mid X_0 = s_1) + P(X_0 = s_2) \cdot P(X_1 = x \mid X_0 = s_2) + \ldots$
>
> wobei $P(X_1 = x \mid X_0 = s_i) = p_{s_i, x}$ (Übergangswahrscheinlichkeit).

Dies ist dieselbe Formel wie der **Satz der totalen Wahrscheinlichkeit** aus SW 03!

---

### Aufgabe 5: Wahrscheinlichkeitsverteilungen X₁ bis X₄ durchrechnen

> 👨‍🏫 **Vollständige handschriftliche Lösung des Dozenten:**

**Startverteilung:** $(s_1, s_2, s_3) = (0, 0, 1)$ (Start in Zustand 3)

**$X_1$:** (Verteilung nach 1 Schritt)
$$P(X_1 = 1) = 0 \cdot 0.7 + 0 \cdot 0.4 + 1 \cdot 0.2 = 0.2$$
$$P(X_1 = 2) = 0 \cdot 0 + 0 \cdot 0 + 1 \cdot 0.3 = 0.3$$
$$P(X_1 = 3) = 0 \cdot 0.3 + 0 \cdot 0.6 + 1 \cdot 0.5 = 0.5$$

**$X_2$:** (Verteilung nach 2 Schritten)
$$P(X_2 = 1) = 0.2 \cdot 0.7 + 0.3 \cdot 0.4 + 0.5 \cdot 0.2 = 0.36$$
$$P(X_2 = 2) = 0.2 \cdot 0 + 0.3 \cdot 0 + 0.5 \cdot 0.3 = 0.15$$
$$P(X_2 = 3) = 0.2 \cdot 0.3 + 0.3 \cdot 0.6 + 0.5 \cdot 0.5 = 0.49$$

**$X_3$:**
$$P(X_3 = 1) = 0.36 \cdot 0.7 + 0.15 \cdot 0.4 + 0.49 \cdot 0.2 = 0.41$$
$$P(X_3 = 2) = 0.36 \cdot 0 + 0.15 \cdot 0 + 0.49 \cdot 0.3 = 0.147$$
$$P(X_3 = 3) = 0.36 \cdot 0.3 + 0.15 \cdot 0.6 + 0.49 \cdot 0.5 = 0.443$$

**$X_4$:**
$$P(X_4 = 1) = 0.41 \cdot 0.7 + 0.147 \cdot 0.4 + 0.443 \cdot 0.2 = 0.4344$$
$$P(X_4 = 2) = 0.41 \cdot 0 + 0.147 \cdot 0 + 0.443 \cdot 0.3 = 0.1329$$
$$P(X_4 = 3) = 0.41 \cdot 0.3 + 0.147 \cdot 0.6 + 0.443 \cdot 0.5 = 0.4327$$

**Zusammenfassung:**

| | $S_1$ | $S_2$ | $S_3$ |
|---|---|---|---|
| $X_1$ | 0.2 | 0.3 | 0.5 |
| $X_2$ | 0.36 | 0.15 | 0.49 |
| $X_3$ | 0.41 | 0.147 | 0.443 |
| $X_4$ | 0.4344 | 0.1329 | 0.4327 |

📌 **Beobachtung:** Die Verteilung konvergiert! → Sie nähert sich der **invarianten Verteilung** an.

---

### Definition 3: Invariante (stationäre) Verteilung

> Eine Wahrscheinlichkeitsverteilung für $X_t$ heisst **invariant** oder **stationär**, wenn sie im Laufe der Zeit unverändert bleibt, wenn also
>
> $$P(X_{t+1} = x) = P(X_t = x)$$
>
> für alle Zeitpunkte $t$ und alle Zustände $x \in S$ gilt.

**💡 Intuition:** Die stationäre Verteilung ist der "Gleichgewichtszustand" – wenn die Kette dort angekommen ist, ändert sich nichts mehr. Sie beschreibt, **wie oft jeder Zustand im Langzeitverhalten besucht wird**.

**🔗 Verbindung zum Erwartungswert:** Die stationäre Verteilung gibt an, mit welcher relativen Häufigkeit man sich langfristig in jedem Zustand befindet.

### Satz 2: Existenz invarianter Verteilungen

> Jede Markov-Kette $X_0, X_1, X_2, \ldots$ mit endlich vielen Zuständen hat **mindestens eine** invariante Verteilung.

---

### Aufgabe 6: Invariante Verteilung berechnen (Detailliert!)

> 👨‍🏫 **Vollständige handschriftliche Lösung des Dozenten:**

Gesucht: Vektor $\vec{\pi} = (x, y, z)$ mit $\vec{\pi} \cdot T = \vec{\pi}$ und $x + y + z = 1$.

**Gleichungssystem aufstellen** (Verteilung $\cdot$ Matrix = gleiche Verteilung):

$$x \cdot 0.7 + y \cdot 0.4 + z \cdot 0.2 = x$$
$$x \cdot 0 + y \cdot 0 + z \cdot 0.3 = y$$
$$x \cdot 0.3 + y \cdot 0.6 + z \cdot 0.5 = z$$
$$x + y + z = 1$$

**Umformen** (alles auf eine Seite):

$$-0.3x + 0.4y + 0.2z = 0$$
$$-y + 0.3z = 0 \quad \Rightarrow \quad y = 0.3z$$
$$0.3x + 0.6y - 0.5z = 0$$
$$x + y + z = 1$$

**Lösen:**

Aus Gl. 2: $y = 0.3z$, also $10y = 3z$.

Einsetzen: $-3x + 4y + 2z = 0$ und $x + y + z = 1$.

Mit $y = \frac{3}{10}z$ in $x + y + z = 1$:

$$7y + 5z = 3 \quad \text{und} \quad 10y - 3z = 0$$

$$\Rightarrow 71y = 9 \quad \Rightarrow \quad y = \frac{9}{71}$$
$$z = 10 \cdot \frac{9}{71} \cdot \frac{1}{3} = \frac{30}{71}$$
$$x = 1 - \frac{9}{71} - \frac{30}{71} = \frac{32}{71}$$

$$\boxed{\vec{\pi} = \frac{1}{71}(32, 9, 30) \approx (0.4507, 0.1268, 0.4225)}$$

**📌 Kontrolle:** Vergleiche mit $X_4 = (0.4344, 0.1329, 0.4327)$ → die Werte nähern sich tatsächlich an! ✓

---

### Definition 4: Irreduzibel & Aperiodisch

> Eine Markov-Kette heisst:
>
> - **irreduzibel**, wenn es für alle zwei Knoten im Graphen einen **Verbindungspfad entlang der Kanten** gibt.
> - **aperiodisch**, wenn für jeden Knoten $s$ der **grösste gemeinsame Teiler** (ggT) aller seiner Rückkehrzeiten $N_s = \{t : P(X_t = s \mid X_0 = s) > 0\}$ gleich **1** ist.

**💡 Intuition:**
- **Irreduzibel** = Man kann von **überall** nach **überall** gelangen (stark zusammenhängend).
- **Aperiodisch** = Die Rückkehr zu einem Zustand geschieht **nicht in regelmässigen Zyklen**.

**Prüfverfahren irreduzibel:** Für jeden Knoten $i$ prüfen: Gibt es einen gerichteten Pfad von $i$ zu jedem anderen Knoten $j$?

**Prüfverfahren aperiodisch:** Für jeden Knoten $s$ die Menge $N_s$ der möglichen Rückkehrzeiten bestimmen und $\gcd(N_s)$ berechnen. Alle müssen 1 ergeben.

---

### Satz 3: Eindeutigkeit und Konvergenz

> Wenn eine Markov-Kette mit endlich vielen Zuständen...
>
> - **irreduzibel** ist → sie hat nur eine **einzige** invariante Verteilung.
> - **irreduzibel** und **aperiodisch** ist → die Kette wird im **Langzeitverhalten** die invariante Verteilung annehmen, **egal welche Startverteilung** gewählt wird.

**💡 Intuition:** Wenn man von überall überall hinkommt (irreduzibel) und es keine Zyklen gibt (aperiodisch), dann "vergisst" die Kette ihren Startzustand und konvergiert zum Gleichgewicht.

---

### Aufgabe 7: Irreduzibel & Aperiodisch prüfen (Aufgabe 1)

> 👨‍🏫 **Lösung des Dozenten:**

**Irreduzibel?** Alle Pfade prüfen:

| Von → Nach | Pfad |
|---|---|
| 1 → 1 | Selbstschleife |
| 1 → 3 → 2 | ✓ |
| 1 → 3 | ✓ |
| 2 → 1 | ✓ |
| 2 → 3 → 2 | ✓ |
| 2 → 3 | ✓ |
| 3 → 1 | ✓ |
| 3 → 2 | ✓ |
| 3 → 3 | Selbstschleife |

**→ Irreduzibel ✓** (alle Knoten erreichbar)

**Aperiodisch?** Rückkehrzeiten bestimmen:

- $N_1 = \{1, 2, 3, 4, \ldots\}$ → $\gcd(N_1) = 1$ ✓ (wegen Selbstschleife mit $p_{1,1} = 0.7$)
- $N_2 = \{2, 3, 4, 5, \ldots\}$ → $\gcd(N_2) = 1$ ✓
- $N_3 = \{1, 2, 3, 4, \ldots\}$ → $\gcd(N_3) = 1$ ✓ (wegen Selbstschleife mit $p_{3,3} = 0.5$)

**→ Aperiodisch ✓**

**📌 Merke:** Wenn ein Knoten eine **Selbstschleife** hat ($p_{i,i} > 0$), ist die Rückkehrzeit 1 möglich, was den ggT automatisch auf 1 setzt → **aperiodisch** für diesen Knoten.

---

### Aufgabe 8: Drei Graphen klassifizieren

> 👨‍🏫 **Lösung des Dozenten:**

| Graph | Irreduzibel? | Aperiodisch? | Begründung |
|---|---|---|---|
| **Graph 1** (1↔2↔3↔4↔1, mit Diagonalen) | ✅ Ja | ❌ Nein | $N_1 = \{2, 4, 6, 8, \ldots\}$, $\gcd = 2$ |
| **Graph 2** (1→2→3→4→1, mit Rückkanten) | ✅ Ja | ✅ Ja | $N_1 = N_3 = \{2, 4, 5, 6, \ldots\}$, $N_2 = N_4 = \{1, 2, 3, 4, \ldots\}$, $\gcd = 1$ |
| **Graph 3** (1↔2, 3↔4, keine Verbindung) | ❌ Nein | ❌ Nein | Kein Pfad von 1 nach 3 möglich; $N_2 = \{3, 6, 3, 12, \ldots\}$, $\gcd \neq 1$ |

---

## 🧮 Formeln & Rechenregeln

### Kernformeln der Woche

| Formel | Beschreibung | Variablen |
|---|---|---|
| $P(X_{t+1} = x \mid X_t = s_t) = p_{s_t, x}$ | Übergangswahrscheinlichkeit | $s_t$ = aktueller Zustand, $x$ = nächster Zustand |
| $\vec{v}_{t+1} = \vec{v}_t \cdot T$ | Verteilung nach einem Schritt | $\vec{v}_t$ = Verteilungsvektor, $T$ = Übergangsmatrix |
| $\vec{v}_t = \vec{v}_0 \cdot T^t$ | Verteilung nach $t$ Schritten | $T^t$ = $t$-fache Matrixmultiplikation |
| $\vec{\pi} \cdot T = \vec{\pi}$ | Invariante Verteilung | $\vec{\pi}$ = stationärer Verteilungsvektor |
| $\sum_j p_{i,j} = 1$ | Zeilensumme = 1 | Stochastische Matrix |
| $\gcd(N_s) = 1$ | Aperiodizitäts-Bedingung | $N_s$ = Menge der Rückkehrzeiten |
| $T_{\text{PageRank}} = d \cdot T_{\text{Link}} + (1-d) \cdot \frac{1}{n}$ | PageRank Übergangsmatrix | $d$ = Dämpfungsfaktor, $n$ = Anzahl Seiten |

### Rezept: Invariante Verteilung berechnen

1. **Gleichungssystem aufstellen:** $\vec{\pi} \cdot T = \vec{\pi}$ (jede Spalte gibt eine Gleichung)
2. **Normierung hinzufügen:** $\pi_1 + \pi_2 + \ldots + \pi_n = 1$
3. **Eine Gleichung weglassen** (sie ist redundant, da die Zeilen von $T$ zu 1 summieren)
4. **System lösen** (Einsetzen oder Gauss-Elimination)

### Rezept: Irreduzibel & Aperiodisch prüfen

**Irreduzibel:**
1. Für jedes Knotenpaar $(i, j)$: Gibt es einen gerichteten Pfad $i \to \ldots \to j$?
2. Wenn ja für alle Paare → irreduzibel

**Aperiodisch:**
1. Für jeden Knoten $s$: Bestimme $N_s = \{t : P(X_t = s \mid X_0 = s) > 0\}$
2. Berechne $\gcd(N_s)$
3. Wenn $\gcd(N_s) = 1$ für **alle** $s$ → aperiodisch

**🔑 Shortcut:** Wenn $p_{i,i} > 0$ (Selbstschleife) → $1 \in N_i$ → $\gcd(N_i) = 1$ automatisch.

---

## 🍳 Kochrezepte (Schritt-für-Schritt-Anleitungen)

### Kochrezept 1: Übergangsmatrix aus Graph aufstellen

```
Schritt 1: Knoten nummerieren → das werden Zeilen UND Spalten

Schritt 2: Für jeden Knoten i (= Zeile i):
           → Alle AUSGEHENDEN Kanten ablesen
           → Wahrscheinlichkeiten in Zeile i eintragen
           → Fehlende Übergänge = 0

Schritt 3: Kontrolle: JEDE ZEILE muss Summe 1 ergeben!

⚠️ Merke: "Zeile = VON, Spalte = NACH"
   T[i][j] = Wahrscheinlichkeit, von i nach j zu gehen
```

### Kochrezept 2: Irrfahrt-Übergangsmatrix

```
Schritt 1: Für jeden Knoten i: Grad(i) = Anzahl Nachbarn bestimmen

Schritt 2: Übergangswahrscheinlichkeit:
           p(i,j) = 1/Grad(i)  für jeden Nachbar j von i
           p(i,j) = 0           für Nicht-Nachbarn

Schritt 3: Kontrolle: Zeilensumme = 1?
```

### Kochrezept 3: Invariante Verteilung per LGS (von Hand)

```
Schritt 1: Gleichungen aus π · T = π aufstellen
           → Spalte j: Σᵢ πᵢ · Tᵢⱼ = πⱼ

Schritt 2: Eine Gleichung streichen (ist redundant!)
           → Ersetzen durch Normierung: π₁ + π₂ + ... + πₙ = 1

Schritt 3: LGS lösen (Einsetzen oder Gauss)
           → Tipp: Erst eine Variable durch andere ausdrücken

Schritt 4: Kontrolle
           → Alle πᵢ ≥ 0? Summe = 1? π · T = π?
```

### Kochrezept 4: Irreduzibel & Aperiodisch prüfen

```
IRREDUZIBEL prüfen:
  Schritt 1: Für jedes Knotenpaar (i, j): Gibt es einen Pfad i → ... → j?
  Schritt 2: Alle Paare erreichbar? → JA = irreduzibel
  🔑 Shortcut: Wenn der Graph "stark zusammenhängend" aussieht → irreduzibel

APERIODISCH prüfen:
  Schritt 1: Für jeden Knoten s: Rückkehrzeiten N_s bestimmen
             N_s = {t : P(X_t = s | X_0 = s) > 0}
  Schritt 2: ggT(N_s) berechnen
  Schritt 3: Alle ggT = 1? → JA = aperiodisch
  🔑 Shortcut: Selbstschleife bei Knoten s → 1 ∈ N_s → ggT = 1 automatisch!
```

### Entscheidungsbaum: Was sagt mir die Klassifikation?

```
Markov-Kette analysiert:
│
├── Irreduzibel?
│   ├── JA → GENAU EINE invariante Verteilung
│   │   └── Auch aperiodisch?
│   │       ├── JA → Konvergenz EGAL welcher Startzustand!
│   │       │        (Langzeitverhalten = invariante Verteilung)
│   │       └── NEIN → Kette kann oszillieren
│   │                  (invariante Vert. existiert, aber keine Konvergenz)
│   │
│   └── NEIN → MEHRERE invariante Verteilungen möglich!
│              (Startverteilung bestimmt, welche angenommen wird)
│
└── PageRank-Aufgabe?
    → T = d · T_Link + (1-d) · (1/n)
    → Invariante Verteilung = PageRank-Werte
```

---

## 📊 Vergleiche & Klassifizierungen

### Markov-Kette Eigenschaften – Übersicht

| Eigenschaft | Bedeutung | Konsequenz |
|---|---|---|
| **Homogen** | Übergangswahrscheinlichkeiten zeitunabhängig | Eine einzige Matrix $T$ reicht |
| **Irreduzibel** | Alle Zustände gegenseitig erreichbar | **Genau eine** invariante Verteilung |
| **Aperiodisch** | Kein regelmässiger Zyklus bei Rückkehr | Konvergenz unabhängig vom Start |
| **Irreduzibel + Aperiodisch** | Beides zusammen | Langzeitverhalten = invariante Verteilung, **egal welcher Startzustand** |

### Typische Aufgabentypen vs. benötigte Konzepte

| Aufgabentyp | Konzept | Vorgehen |
|---|---|---|
| Übergangsmatrix aufstellen | Definition 1 | Kanten des Graphen → Zeilen der Matrix |
| Irrfahrt-Übergangsmatrix | Uniform zufällig | $p_{i,j} = \frac{1}{\text{Grad}(i)}$ für alle Nachbarn $j$ |
| Verteilung nach $t$ Schritten | Satz 1 | $\vec{v}_t = \vec{v}_0 \cdot T^t$ iterativ berechnen |
| Invariante Verteilung | Definition 3 | $\vec{\pi} T = \vec{\pi}$, $\sum \pi_i = 1$ als LGS lösen |
| Irreduzibel? | Definition 4 | Pfade zwischen allen Knotenpaaren prüfen |
| Aperiodisch? | Definition 4 | $\gcd(N_s) = 1$ für alle Knoten prüfen |

---

## 💻 Code-Beispiele (Python)

### 1. Übergangsmatrix und Verteilung berechnen

```python
import numpy as np

# Übergangsmatrix aus Aufgabe 1
T = np.array([
    [0.7, 0.0, 0.3],   # Von Zustand 1
    [0.4, 0.0, 0.6],   # Von Zustand 2
    [0.2, 0.3, 0.5]    # Von Zustand 3
])

# Kontrolle: Jede Zeile muss 1 ergeben
print("Zeilensummen:", T.sum(axis=1))  # → [1. 1. 1.] ✓

# Startverteilung: Start in Zustand 3
v = np.array([0, 0, 1])

# Verteilungen über 4 Zeitschritte berechnen
for t in range(1, 5):
    v = v @ T  # Matrixmultiplikation: v_new = v_old * T
    print(f"X_{t}: {np.round(v, 4)}")

# Ausgabe:
# X_1: [0.2    0.3    0.5   ]
# X_2: [0.36   0.15   0.49  ]
# X_3: [0.41   0.147  0.443 ]
# X_4: [0.4344 0.1329 0.4327]
```

### 2. Invariante Verteilung berechnen

```python
import numpy as np

T = np.array([
    [0.7, 0.0, 0.3],
    [0.4, 0.0, 0.6],
    [0.2, 0.3, 0.5]
])

# Methode 1: Eigenwertzerlegung
# Die invariante Verteilung ist der linke Eigenvektor zum Eigenwert 1
# d.h. pi * T = pi  ⟺  T^T * pi^T = pi^T
eigenvalues, eigenvectors = np.linalg.eig(T.T)
# Finde den Eigenvektor zum Eigenwert 1
idx = np.argmin(np.abs(eigenvalues - 1))
pi = eigenvectors[:, idx].real
pi = pi / pi.sum()  # Normieren (Summe = 1)
print(f"Invariante Verteilung: {np.round(pi, 4)}")
# → [0.4507  0.1268  0.4225]  ≈ 1/71 * (32, 9, 30)

# Methode 2: Lange Iteration (Konvergenz)
v = np.array([1/3, 1/3, 1/3])  # beliebige Startverteilung
for _ in range(1000):
    v = v @ T
print(f"Nach 1000 Iterationen: {np.round(v, 4)}")
# → [0.4507  0.1268  0.4225]  identisch! ✓

# Methode 3: Lineares Gleichungssystem lösen
# pi * T = pi  ⟺  pi * (T - I) = 0  mit  sum(pi) = 1
A = (T.T - np.eye(3))        # (T - I)^T
A[-1] = [1, 1, 1]             # Letzte Zeile ersetzen durch Normierung
b = np.zeros(3)
b[-1] = 1                     # sum(pi) = 1
pi_lgs = np.linalg.solve(A, b)
print(f"LGS-Lösung: {np.round(pi_lgs, 4)}")
# → [0.4507  0.1268  0.4225] ✓
```

### 3. Irreduzibel & Aperiodisch prüfen

```python
import numpy as np
from math import gcd
from functools import reduce

def ist_irreduzibel(T, max_potenz=100):
    """Prüft, ob die Markov-Kette irreduzibel ist.

    Methode: Wenn T^k für ein k alle Einträge > 0 hat,
    ist die Kette irreduzibel (und sogar aperiodisch).
    Alternativ: Prüfen ob Summe T + T^2 + ... + T^n alle > 0 sind.
    """
    n = len(T)
    erreichbar = np.zeros_like(T)
    Tk = np.eye(n)
    for k in range(1, max_potenz + 1):
        Tk = Tk @ T
        erreichbar += (Tk > 1e-10).astype(float)
    # Irreduzibel wenn alle Einträge der Erreichbarkeitsmatrix > 0
    return np.all(erreichbar > 0)

def rueckkehrzeiten(T, zustand, max_t=20):
    """Bestimmt die Rückkehrzeiten N_s für einen Zustand s."""
    n = len(T)
    Tk = np.eye(n)
    zeiten = []
    for t in range(1, max_t + 1):
        Tk = Tk @ T
        if Tk[zustand, zustand] > 1e-10:
            zeiten.append(t)
    return zeiten

def ist_aperiodisch(T, max_t=20):
    """Prüft, ob die Markov-Kette aperiodisch ist."""
    n = len(T)
    for s in range(n):
        zeiten = rueckkehrzeiten(T, s, max_t)
        if not zeiten:
            return False
        g = reduce(gcd, zeiten)
        if g != 1:
            return False
    return True

# Test mit Aufgabe 1
T = np.array([
    [0.7, 0.0, 0.3],
    [0.4, 0.0, 0.6],
    [0.2, 0.3, 0.5]
])

print(f"Irreduzibel: {ist_irreduzibel(T)}")   # → True
print(f"Aperiodisch: {ist_aperiodisch(T)}")    # → True
```

### 4. Mini-Monopoly Übergangsmatrix (Aufgabe 3)

```python
import numpy as np

# Mini-Monopoly: 8 Felder, fairer Würfel (1-6)
# Spezialregel: Wer auf Feld 3 landet, geht direkt auf Feld 7
n = 8

# Übergangsmatrix initialisieren
T = np.zeros((n, n))

for i in range(n):
    for wurf in range(1, 7):  # Würfelwurf 1 bis 6
        ziel = (i + wurf) % n  # Zielfeld (zyklisch)
        if ziel == 2:          # Feld 3 (0-indexiert = Index 2)
            ziel = 6           # → Direkt auf Feld 7 (Index 6)
        T[i, ziel] += 1/6

print("Übergangsmatrix (Mini-Monopoly):")
print(np.round(T, 4))
print("Zeilensummen:", T.sum(axis=1))  # Alle 1.0 ✓
```

### 5. PageRank als Markov-Kette

```python
import numpy as np

def pagerank(adj_matrix, d=0.85, max_iter=100, tol=1e-8):
    """Berechnet PageRank mittels Markov-Ketten-Iteration.

    Args:
        adj_matrix: Adjazenzmatrix (1 = Link vorhanden)
        d: Dämpfungsfaktor (typisch 0.85)
        max_iter: Maximale Iterationen
        tol: Konvergenz-Schwellenwert
    """
    n = len(adj_matrix)

    # Schritt 1: Link-Übergangsmatrix (uniform über ausgehende Links)
    T_link = np.zeros((n, n))
    for i in range(n):
        ausgehend = adj_matrix[i].sum()
        if ausgehend > 0:
            T_link[i] = adj_matrix[i] / ausgehend
        else:
            T_link[i] = 1/n  # Dangling node: springt überall hin

    # Schritt 2: PageRank-Übergangsmatrix
    # T = d * T_link + (1-d) * (1/n) * Einsmatrix
    T = d * T_link + (1 - d) / n * np.ones((n, n))

    # Schritt 3: Iteriere bis Konvergenz (= invariante Verteilung)
    v = np.ones(n) / n  # Gleichverteilung als Start
    for i in range(max_iter):
        v_new = v @ T
        if np.linalg.norm(v_new - v) < tol:
            print(f"Konvergiert nach {i+1} Iterationen")
            break
        v = v_new

    return v

# Beispiel: Einfaches Netzwerk mit 4 Seiten
# Seite 1 → 2, 3
# Seite 2 → 3
# Seite 3 → 1
# Seite 4 → 1, 2, 3
adj = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
])

ranks = pagerank(adj)
print("PageRank-Werte:")
for i, r in enumerate(ranks):
    print(f"  Seite {i+1}: {r:.4f}")
```

---

## ✏️ Übungsaufgaben-Zusammenfassung

| Nr. | Thema / Konzept | Lösungsansatz | Typische Stolpersteine |
|---|---|---|---|
| **1** | Übergangsmatrix aus Graph | Kanten ablesen → Zeile $i$ ausfüllen für jeden Knoten $i$ | Zeilen (nicht Spalten!) entsprechen den Ausgangsknoten. **Zeile muss zu 1 summieren!** |
| **2** | Irrfahrt auf Doppelpyramide | Nachbarn zählen, $p = \frac{1}{\text{Grad}}$ für jeden Nachbarn | Grad korrekt bestimmen (Knoten 1 und 5 haben Grad 3, Knoten 2-4 haben Grad 4) |
| **3** | Mini-Monopoly (8 Felder) | Würfelwahrscheinlichkeiten pro Feld, Spezialregel Feld 3 → 7 | Zyklisches Spielbrett (Feld 8 → Feld 1). Spezialregel korrekt umleiten. |
| **4** | Leiterspiel (30 Felder) | Leitern (hoch) und Schlangen (runter) umleiten, Zielfeld nur mit direktem Wurf | Sehr grosse Matrix (31×31 inkl. Start). "Direkter Wurf" = muss exakt auf Feld 30 landen. |
| **5** | Verteilungen $X_1$ bis $X_4$ | $\vec{v}_{t+1} = \vec{v}_t \cdot T$ iterativ anwenden | Matrixmultiplikation korrekt ausführen. Zeile × Spalte beachten! |
| **6** | Invariante Verteilung | LGS: $\vec{\pi} T = \vec{\pi}$, $\sum \pi_i = 1$ | Eine Gleichung ist redundant → durch Normierung ersetzen. |
| **7** | Irreduzibel/Aperiodisch (Aufg. 1) | Pfade + Rückkehrzeiten prüfen | Selbstschleifen erkennen (→ automatisch aperiodisch für den Knoten). |
| **8** | Drei Graphen klassifizieren | Pfade + ggT der Rückkehrzeiten | Graph 1: irreduzibel aber **nicht** aperiodisch ($\gcd = 2$). Graph 3: **nicht** irreduzibel. |
| **9** | PageRank-Übergangsmatrix | $T = d \cdot T_{\text{Link}} + (1-d) \cdot \frac{1}{n}$ | Dämpfungsfaktor $d$ korrekt einbauen. Seiten ohne ausgehende Links separat behandeln. |

---

## ⚠️ Prüfungsrelevante Hinweise

### ⚡ Typische Aufgabentypen und wie man sie erkennt

1. **"Bestimmen Sie die Übergangsmatrix"**
   → Kanten des Graphen ablesen. Zeile = Ausgangsknoten, Spalte = Zielknoten. **Zeilensumme = 1!**

2. **"Irrfahrt auf Graph X"**
   → Uniform zufällig: $p_{i,j} = \frac{1}{\text{Grad}(i)}$ für jeden Nachbarn $j$ von $i$.

3. **"Bestimmen Sie die Verteilung $X_t$"**
   → $\vec{v}_t = \vec{v}_0 \cdot T^t$ (iterativ oder direkt mit Matrixpotenz).

4. **"Bestimmen Sie die invariante Verteilung"**
   → LGS lösen: $\vec{\pi} \cdot T = \vec{\pi}$ mit $\sum \pi_i = 1$.

5. **"Ist die Markov-Kette irreduzibel/aperiodisch?"**
   → Pfade prüfen (irreduzibel) + ggT der Rückkehrzeiten (aperiodisch).

### 🔑 Merkregeln und Eselsbrücken

| Merkregel | Erklärung |
|---|---|
| **"Zeile = Von, Spalte = Nach"** | $T_{i,j}$ = Wahrscheinlichkeit von Zustand $i$ nach Zustand $j$ |
| **"Zeilensumme = 1"** | Stochastische Matrix: von jedem Zustand muss man irgendwo hingehen |
| **"Markov = Gedächtnislos"** | Nur der aktuelle Zustand zählt, nicht der Weg dorthin |
| **"Selbstschleife → aperiodisch"** | Wenn $p_{i,i} > 0$: Rückkehr in 1 Schritt möglich → $\gcd = 1$ |
| **"$\vec{\pi} T = \vec{\pi}$: LGS with Normierung"** | Eine Gleichung ist redundant → durch $\sum \pi_i = 1$ ersetzen |
| **"Irreduzibel = stark zusammenhängend"** | Wie bei gerichteten Graphen: alle Knoten gegenseitig erreichbar |

### 🧠 Formeln die man auswendig wissen muss

1. **Markov-Eigenschaft:** $P(X_{t+1} = x \mid X_t = s_t) = p_{s_t, x}$
2. **Zeitentwicklung:** $\vec{v}_{t+1} = \vec{v}_t \cdot T$
3. **Invariante Verteilung:** $\vec{\pi} \cdot T = \vec{\pi}$ mit $\sum \pi_i = 1$
4. **Aperiodizität:** $\gcd(N_s) = 1$ für alle $s$
5. **PageRank:** $T = d \cdot T_{\text{Link}} + (1-d) \cdot \frac{1}{n}$

### ❌ Häufige Fehlerquellen

1. **Zeile vs. Spalte verwechseln:** Zeile $i$ = **von** Zustand $i$. Nicht umgekehrt!
2. **Zeilensumme vergessen zu prüfen:** Wenn eine Zeile nicht 1 ergibt, ist die Matrix falsch.
3. **Invariante Verteilung: Redundante Gleichung nicht erkennen:** Das System $\vec{\pi} T = \vec{\pi}$ hat eine abhängige Gleichung – eine muss durch $\sum \pi_i = 1$ ersetzt werden.
4. **Aperiodisch mit irreduzibel verwechseln:** Irreduzibel = Erreichbarkeit. Aperiodisch = keine Zyklen. Beides unabhängig voneinander!
5. **Rückkehrzeiten falsch bestimmen:** $N_s$ enthält **alle** Zeitpunkte $t$, zu denen eine Rückkehr von $s$ nach $s$ **möglich** ist (nicht nur die kürzeste!).
6. **Irrfahrt: Grad falsch zählen:** Bei ungerichteten Graphen: Grad = Anzahl Nachbarn. Nicht vergessen: Selbstschleifen zählen doppelt zum Grad!

---

## 🌐 PageRank & Zufallssurfer-Modell

### Konzept

Der **PageRank-Algorithmus** von Google nutzt Markov-Ketten, um die Wichtigkeit von Webseiten zu bewerten:

1. **Zufallssurfer-Modell:** Ein Surfer springt zufällig von Webseite zu Webseite über Links.
2. **Problem:** Seiten ohne ausgehende Links (Sackgassen) würden Gewicht 0 erhalten.
3. **Lösung:** Mit Wahrscheinlichkeit $d$ folgt der Surfer einem Link, mit $1-d$ springt er zu einer **zufällig gewählten** Seite.

### Übergangsmatrix

$$T_{\text{PageRank}} = d \cdot T_{\text{Link}} + (1-d) \cdot \frac{1}{n} \cdot \mathbf{1}$$

wobei:
- $d \approx 0.85$ (Dämpfungsfaktor / damping factor)
- $T_{\text{Link}}$: Übergangsmatrix basierend auf den Links (uniform über ausgehende Links)
- $n$: Gesamtzahl der Webseiten
- $\mathbf{1}$: Matrix mit allen Einträgen 1

**💡 Intuition:** Der PageRank einer Seite ist ihre **invariante Wahrscheinlichkeit** in der Markov-Kette. Seiten mit vielen eingehenden Links von wichtigen Seiten erhalten einen hohen PageRank.

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

```
SW 01 Wahrscheinlichkeit
  └── Grundbegriffe: Ω, P, Mengenoperationen
       │
SW 02 Bedingte Wahrscheinlichkeit
  └── P(A|B), Unabhängigkeit
       │
SW 03 Satz von Bayes / Totale Wahrscheinlichkeit
  └── P(X_{t+1} = x) = Σ P(X_t = s_i) · p_{s_i,x}
       │        └──── GENAU DIE GLEICHE FORMEL wie
       │               Satz 1 (Totale Wahrscheinlichkeit)!
       │
SW 04 Zufallsvariablen
  └── E(X), Verteilungen
       │        └──── Verteilungsvektor v_t nutzt
       │               dieselben Konzepte
       │
SW 05 Randomisierte Algorithmen
  └── Las Vegas, Monte Carlo, erwartete Komplexität
       │        └──── Randomisierte Prozesse als Vorstufe
       │               zu Markov-Ketten
       │
████████████████████████████████████████████████
█  SW 06 Markov-Ketten  ◄── WIR SIND HIER    █
████████████████████████████████████████████████
       │
       │  Schlüsselkonzepte:
       │  • Markov-Eigenschaft & Übergangsmatrix
       │  • Zeitentwicklung: v_{t+1} = v_t · T
       │  • Invariante Verteilung: π · T = π
       │  • Irreduzibel & Aperiodisch
       │  • PageRank als Anwendung
       │
SW 07 Matrizenalgebra
  └── Matrizenmultiplikation, Inverse, Eigenwerte
       └──── Formale Grundlage für T^t, Eigenwert-
              zerlegung zur Berechnung von π
```

### Konkrete Verbindungen

| Woche | Verbindung zu SW 06 |
|---|---|
| **SW 03** | Der **Satz der totalen Wahrscheinlichkeit** ist exakt Satz 1: $P(X_{t+1} = x) = \sum_i P(X_t = s_i) \cdot p_{s_i, x}$ – dieselbe Aufspaltung nach Fällen! |
| **SW 04** | Die **Zufallsvariable** $X_t$ ordnet jedem Zeitpunkt einen Zustand zu – genau wie in SW 04, aber jetzt als Folge von Zufallsvariablen. |
| **SW 05** | Markov-Ketten sind selbst **randomisierte Prozesse** – die Zustandsübergänge sind zufällig. PageRank ist ein Monte-Carlo-ähnliches Verfahren (iterative Annäherung). |
| **SW 07** | Die Matrixpotenz $T^t$ und die **Eigenwertzerlegung** (zur Berechnung der invarianten Verteilung) nutzen Konzepte der linearen Algebra, die in SW 07 formalisiert werden. |

---

> **📌 Zusammenfassung auf einen Blick:**
> SW 06 führt **Markov-Ketten** ein – zufällige Prozesse mit "Gedächtnislosigkeit". Zentrale Konzepte: Die **Übergangsmatrix** $T$ (Zeile = Von, Spalte = Nach, Zeilensumme = 1), die **Zeitentwicklung** $\vec{v}_{t+1} = \vec{v}_t \cdot T$, die **invariante Verteilung** $\vec{\pi} T = \vec{\pi}$ (LGS mit Normierung lösen), und die Klassifizierung als **irreduzibel** (alle Knoten erreichbar) und **aperiodisch** ($\gcd(N_s) = 1$). Der **PageRank-Algorithmus** ist die wichtigste Praxisanwendung: $T = d \cdot T_{\text{Link}} + (1-d) \cdot \frac{1}{n}$. Satz 3 ist der Schlüsselsatz: Ist eine Kette irreduzibel und aperiodisch, konvergiert sie zur eindeutigen invarianten Verteilung, **egal welcher Startzustand**.
