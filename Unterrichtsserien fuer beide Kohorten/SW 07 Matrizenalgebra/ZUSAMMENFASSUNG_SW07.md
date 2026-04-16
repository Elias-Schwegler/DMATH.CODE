# DMATH.CODE – SW 07: Matrizenalgebra

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Semesterwoche:** SW 07
> **Thema:** Matrizenalgebra
> **Dozent:** Dr. Reto Berger · HSLU · Frühlingssemester 25

---

## 🎯 Lernziele

1. Die **Matrizenmultiplikation** berechnen können (Skalarprodukt, Matrixprodukt).
2. Die **Matrix-Vektor-Iteration** verstehen und anwenden können.
3. **Invariante Verteilungen** von Markov-Ketten numerisch bestimmen können.
4. Weitere Anwendungen der Matrizenmultiplikation kennen: **Populationsdynamik (Leslie-Matrix)**, **Eigenwerte/Eigenvektoren**, **Potenzmethode**.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Skalarprodukt** | Summe aller komponentenweisen Produkte zweier Vektoren: $\langle a_{i*}, b_{*j}\rangle = a_{i1} b_{1j} + a_{i2} b_{2j} + \ldots + a_{ik} b_{kj}$ |
| **Matrixprodukt** | Rechteckige Anordnung aller Skalarprodukte von Zeilen in $A$ und Spalten in $B$. Ergebnis: $(A \cdot B)_{ij} = \langle a_{i*}, b_{*j}\rangle$ |
| **Identitätsmatrix** | Matrix $\text{Id}$ mit 1 auf der Diagonale und 0 sonst. Es gilt $\text{Id} \cdot A = A \cdot \text{Id} = A$. |
| **Matrixpotenz** | $T^t = \underbrace{T \cdot T \cdot \ldots \cdot T}_{t \text{ Mal}}$. Beschreibt $t$ Zeitschritte einer Markov-Kette: $p(t) = p(0) \cdot T^t$. |
| **Matrix-Vektor-Iteration** | Wiederholte Berechnung $v_{t+1} = v_t \cdot T$, bis Konvergenz eintritt (Fixpunkt). |
| **Fixpunkt** | Vektor $\vec{\pi}$, der sich bei der Iteration nicht mehr ändert: $\vec{\pi} \cdot T = \vec{\pi}$. |
| **Eigenvektor** | Vektor $v \neq 0$ mit $v \cdot A = \lambda v$ für eine Zahl $\lambda$. |
| **Eigenwert** | Die Zahl $\lambda$ in der Gleichung $v \cdot A = \lambda v$. |
| **Dominanter Eigenwert** | Der betragsmässig grösste Eigenwert $\lambda$. |
| **Potenzmethode** | Iterativer Algorithmus, der den Eigenvektor zum dominanten Eigenwert berechnet. |
| **Leslie-Matrix** | Matrix zur Modellierung von **Populationsdynamik** (Geburtenraten + Überlebensraten pro Lebensphase). |
| **Normierung** | Vektor auf Länge 1 setzen: $v_{\text{norm}} = \frac{1}{\sqrt{\langle v, v \rangle}} \cdot v$. |

---

## 📐 Definitionen, Sätze & Beweise

### Definition 1: Matrizenmultiplikation

> Sei $A$ eine $m \times k$ Matrix und $B$ eine $k \times n$ Matrix.
>
> Das **Matrixprodukt** $C = A \cdot B$ ist eine $m \times n$ Matrix mit:
>
> $$C_{ij} = \langle a_{i*}, b_{*j}\rangle = \sum_{\ell=1}^{k} a_{i\ell} \cdot b_{\ell j}$$

**💡 Intuition:** Jeder Eintrag im Ergebnis entsteht durch **Zeile von $A$ × Spalte von $B$** – komponentenweise multiplizieren und aufsummieren.

**⚠️ Voraussetzung:** Die Anzahl **Spalten in $A$** muss gleich der Anzahl **Zeilen in $B$** sein! $(m \times \mathbf{k}) \cdot (\mathbf{k} \times n) = (m \times n)$

**Zahlenbeispiel:**

$$\begin{pmatrix} 0 & 8 & 0 \\ 9 & 6 & 0 \\ 2 & 3 & 3 \end{pmatrix} \cdot \begin{pmatrix} 5 & 8 \\ 7 & 5 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 0 \cdot 5 + 8 \cdot 7 + 0 \cdot 3 & 0 \cdot 8 + 8 \cdot 5 + 0 \cdot 2 \\ 9 \cdot 5 + 6 \cdot 7 + 0 \cdot 3 & 9 \cdot 8 + 6 \cdot 5 + 0 \cdot 2 \\ 2 \cdot 5 + 3 \cdot 7 + 3 \cdot 3 & 2 \cdot 8 + 3 \cdot 5 + 3 \cdot 2 \end{pmatrix} = \begin{pmatrix} 56 & 40 \\ 87 & 102 \\ 40 & 37 \end{pmatrix}$$

---

### Satz 1: Rechenregeln für Matrizen

> Wenn die Matrizenmultiplikation durchführbar ist, gilt:
>
> 1. $x(A \cdot B) = (xA) \cdot B = A \cdot (xB)$ für alle $x \in \mathbb{R}$ (Skalarmultiplikation)
> 2. $A \cdot (B + C) = A \cdot B + A \cdot C$ (Distributivgesetz links)
> 3. $(A + B) \cdot C = A \cdot C + B \cdot C$ (Distributivgesetz rechts)
> 4. $\text{Id} \cdot A = A \cdot \text{Id} = A$ (Identitätsmatrix)

**⚠️ ACHTUNG: $A \cdot B \neq B \cdot A$ im Allgemeinen!** Die Matrizenmultiplikation ist **NICHT kommutativ**.

**Zahlenbeispiel (Nicht-Kommutativität):**

$$\begin{pmatrix} 3 & 1 \\ 0 & 8 \end{pmatrix} \cdot \begin{pmatrix} 8 & 4 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 27 & 14 \\ 24 & 16 \end{pmatrix} \quad \neq \quad \begin{pmatrix} 8 & 4 \\ 3 & 2 \end{pmatrix} \cdot \begin{pmatrix} 3 & 1 \\ 0 & 8 \end{pmatrix} = \begin{pmatrix} 24 & 40 \\ 9 & 19 \end{pmatrix}$$

---

### Matrixpotenzen und Markov-Ketten

Die Potenzen der Übergangsmatrix bestimmen die Wahrscheinlichkeitsverteilung zum Zeitpunkt $t$:

$$p(t) = p(0) \cdot T^t$$

**Herleitung (iterativ):**

$$p(1) = p(0) \cdot T$$
$$p(2) = p(1) \cdot T = p(0) \cdot T^2$$
$$p(3) = p(2) \cdot T = p(0) \cdot T^3$$
$$\vdots$$
$$p(t) = p(0) \cdot T^t$$

**Zahlenbeispiel:** Markov-Kette mit $T = \frac{1}{12}\begin{pmatrix} 0 & 6 & 6 \\ 3 & 6 & 3 \\ 4 & 4 & 4 \end{pmatrix}$, Start $p(0) = (0, 0, 1)$:

$$T^2 = \frac{1}{144}\begin{pmatrix} 42 & 60 & 42 \\ 30 & 66 & 48 \\ 28 & 64 & 52 \end{pmatrix}$$

$$p(2) = (0, 0, 1) \cdot T^2 = (0.194, 0.444, 0.361)$$

---

### Matrix-Vektor-Iteration (Fixpunktiteration)

> Für Markov-Ketten mit sehr vielen Zuständen ist das Lösen des LGS für die invariante Verteilung aufwändig. Stattdessen iteriert man:
>
> $$v_{t+1} = v_t \cdot T$$
>
> bis sich der Vektor stabilisiert: $|v_{t+1} - v_t| < \varepsilon$

**💡 Intuition:** Statt ein grosses Gleichungssystem zu lösen, lässt man die Markov-Kette einfach "laufen" – nach genügend Schritten konvergiert die Verteilung zur invarianten Verteilung (sofern irreduzibel & aperiodisch).

**Konvergenz-Beispiel** (aus Vorlesung):

| Iteration | $p_1$ | $p_2$ | $p_3$ |
|---|---|---|---|
| 1 | 0.0000 | 0.5000 | 0.5000 |
| 2 | 0.2917 | 0.4167 | 0.2917 |
| 5 | 0.2203 | 0.4451 | 0.3346 |
| 8 | 0.2223 | 0.4444 | 0.3333 |
| 11 | **0.2222** | **0.4444** | **0.3333** |

→ Konvergiert zur invarianten Verteilung $\vec{\pi} = \left(\frac{2}{9}, \frac{4}{9}, \frac{3}{9}\right) \approx (0.222, 0.444, 0.333)$

---

### Aufgabe 5: Invariante Verteilung per LGS (von Hand)

Gegeben: $T = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 1/4 & 1/2 & 1/4 \\ 1/3 & 1/3 & 1/3 \end{pmatrix}$

**LGS aufstellen** aus $\vec{\pi} \cdot T = \vec{\pi}$ und $p_1 + p_2 + p_3 = 1$:

$$\frac{1}{4} p_2 + \frac{1}{3} p_3 = p_1$$
$$\frac{1}{2} p_1 + \frac{1}{2} p_2 + \frac{1}{3} p_3 = p_2$$
$$\frac{1}{2} p_1 + \frac{1}{4} p_2 + \frac{1}{3} p_3 = p_3$$
$$p_1 + p_2 + p_3 = 1$$

**Lösung:** $p_1 = \frac{2}{9}, \quad p_2 = \frac{4}{9}, \quad p_3 = \frac{3}{9} = \frac{1}{3}$

**Kontrolle:** $\left(\frac{2}{9}, \frac{4}{9}, \frac{3}{9}\right) \cdot T = \left(\frac{2}{9}, \frac{4}{9}, \frac{3}{9}\right)$ ✓

---

### Aufgabe 6: Nicht-irreduzible Markov-Kette

Gegeben: $T = \begin{pmatrix} 1/2 & 1/2 & 0 & 0 \\ 1/4 & 3/4 & 0 & 0 \\ 0 & 0 & 1/2 & 1/2 \\ 0 & 0 & 1/2 & 1/2 \end{pmatrix}$

**Nicht irreduzibel**, weil die Matrix in **zwei Blöcke** zerfällt:
- Block 1: Zustände {1, 2} (keine Verbindung zu {3, 4})
- Block 2: Zustände {3, 4} (keine Verbindung zu {1, 2})

**Zwei verschiedene invariante Verteilungen** (abhängig von der Startverteilung!):

| Startverteilung | Invariante Verteilung | Iterationen |
|---|---|---|
| $p(0) = (1, 0, 0, 0)$ | $(1/3, 2/3, 0, 0)$ | 18 |
| $p(0) = (0, 0, 1, 0)$ | $(0, 0, 1/2, 1/2)$ | 2 |

📌 **Merke:** Nicht-irreduzible Ketten können **mehrere** invariante Verteilungen haben! Die Startverteilung bestimmt, welche angenommen wird.

---

### Definition 2: Eigenwert & Eigenvektor

> Ein Vektor $v \neq 0$ heisst **Eigenvektor** einer quadratischen Matrix $A$, wenn es eine Zahl $\lambda \in \mathbb{R}$ gibt, sodass:
>
> $$v \cdot A = \lambda v$$
>
> Die Zahl $\lambda$ heisst **Eigenwert** zum Vektor $v$.
> Das betragsmässig grösste $\lambda$ heisst **dominanter Eigenwert**.

**💡 Intuition:**
- Ein Eigenvektor wird durch die Matrix $A$ nur **gestreckt/gestaucht** (Faktor $\lambda$), aber **nicht gedreht**.
- Bei Markov-Ketten: Die invariante Verteilung $\vec{\pi}$ ist der Eigenvektor zum Eigenwert $\lambda = 1$ (weil $\vec{\pi} \cdot T = 1 \cdot \vec{\pi}$).
- Dominanter Eigenwert $\lambda > 1$ → **Population wächst**
- Dominanter Eigenwert $\lambda < 1$ → **Population schrumpft**
- Dominanter Eigenwert $\lambda = 1$ → **Population stabil** (Gleichgewicht)

---

### Algorithmus: Potenzmethode (Power Iteration)

> Berechnet den Eigenvektor zum **dominanten Eigenwert**:
>
> 1. Wähle einen Startvektor $v$.
> 2. Berechne $v' = v \cdot A$ und normiere: $v = \frac{1}{\sqrt{\langle v', v'\rangle}} \cdot v'$
> 3. Wiederhole Schritt 2, bis $v$ stabil ist (Abbruchbedingung: $|v_{\text{alt}} - v_{\text{neu}}| < \varepsilon$).
> 4. Gib den Eigenvektor $v$ und den Eigenwert $\lambda = \langle v, v \cdot A\rangle$ zurück.

**💡 Warum normieren?**
- Wenn $|\lambda| > 1$: Vektoren werden bei jeder Iteration länger → Überlauf
- Wenn $|\lambda| < 1$: Vektoren werden kürzer → Unterlauf
- Normierung hält den Vektor bei Länge 1 – die **Richtung** (= Eigenvektor) bleibt erhalten

**📌 Unterschied zur Markov-Iteration:**

| | Markov-Iteration | Potenzmethode |
|---|---|---|
| **Ziel** | Invariante Verteilung $\vec{\pi}$ | Dominanter Eigenvektor + Eigenwert |
| **Matrix** | Stochastische Matrix $T$ (Zeilensumme = 1) | Beliebige quadratische Matrix $A$ |
| **Normierung** | Nicht nötig (Summe bleibt 1) | Nötig (auf Länge 1 normieren) |
| **Eigenwert** | Immer $\lambda = 1$ | Beliebiges $\lambda$ |

---

### Aufgabe 8: Populationsdynamik (Leslie-Matrix) – Meeresschildkröten

**Lebensphasen:** N(eu), J(ung), P(fast ausgewachsen), E(rstbrüter), B(rüter), A(lt)

**Leslie-Matrix (a):**

$$A = \begin{pmatrix} 0 & 0.09 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0.15 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0.33 & 0 & 0 \\ 180 & 0 & 0 & 0 & 0.75 & 0 \\ 70 & 0 & 0 & 0 & 0 & 0.8 \\ 0 & 0 & 0 & 0 & 0 & 0.5 \end{pmatrix}$$

**Interpretation der Matrix:**
- **Zeile = Lebensphase "Von"**, **Spalte = Lebensphase "Nach"**
- Zeile 1: Von N → J mit Rate 0.09 (9% der Neugeschlüpften überleben)
- Zeile 4: E → N mit Rate 180 (Geburtenrate: 180 Eier pro Erstbrüter), E → B mit 0.75
- Zeile 5: B → N mit 70, B → A mit 0.8

**Ergebnis (Potenzmethode):**
- **Dominanter Eigenwert:** $\lambda \approx 1.008 > 1$ → **Population wächst** (langfristiges Überleben gesichert ✓)
- **Verteilung im Gleichgewicht:** N: 89.7%, J: 8.0%, P: 1.2%, E: 0.4%, B: 0.3%, A: 0.5%

**Aufgabe 8d):** Mit verlangsamter Entwicklung (Umwelteinflüsse):
- $\lambda \approx 0.757 < 1$ → **Population schrumpft** → Langfristiges Überleben **NICHT** gesichert ✗

---

### Aufgabe 9: Sympathiegehalt (Paviane)

Jeder Pavian verteilt seinen Sympathiegehalt proportional zur Fellpflege. Die **Übergangsmatrix $N$** wird aus dem Graphen abgelesen (ähnlich wie bei Markov-Ketten / PageRank).

**Ergebnis (Potenzmethode):**

| Pavian | Ado | Bob | Ces | Don | Edi | Fay |
|---|---|---|---|---|---|---|
| **Sympathie (%)** | 22.8 | 7.3 | 16.7 | 9.4 | 25.0 | 19.0 |
| **Rang (Sympathie)** | 2 | 6 | 4 | 5 | 1 | 3 |
| **Stresshormon** | tief → hoch | hoch | mittel | mittel-hoch | tief | mittel-hoch |

📌 **Beobachtung:** Tiere mit **hohem Sympathiegehalt** haben tendenziell **tiefere Stresshormone** – sozialer Rang korreliert invers mit Stress!

---

### Aufgabe 2: Für welche $A$ gilt $A \cdot B = B \cdot A$?

Gesucht: Alle $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ mit $A \cdot \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix} \cdot A$

**Vergleich der Matrixprodukte:**

$$A \cdot B = \begin{pmatrix} a + 2c & 2a + 3c \\ b + 2d & 2b + 3d \end{pmatrix}, \quad B \cdot A = \begin{pmatrix} a + 2b & c + 2d \\ 2a + 3b & 2c + 3d \end{pmatrix}$$

**Koeffizientenvergleich:** $2c = 2b$ und $2a + 3c = c + 2d$ → $b = c$ und $d = a + c$

$$\boxed{A = \begin{pmatrix} a & c \\ c & a+c \end{pmatrix} \text{ für beliebige } a, c \in \mathbb{R}}$$

---

### Aufgabe 3: Alle Potenzen $A^n$ für $A = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$

**Berechnung:**

$$A^1 = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \quad A^2 = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$$

**Muster erkannt:** $\boxed{A^n = \begin{pmatrix} 1 & -n \\ 0 & 1 \end{pmatrix}}$

---

### Aufgabe 4: Komplexität der Matrixmultiplikation

Für zwei $n \times n$ Matrizen:
- Pro Eintrag: $n$ Multiplikationen + $(n-1)$ Additionen = $2n - 1$ Operationen
- Gesamtzahl Einträge: $n^2$
- **Total:** $n^2 \cdot (2n - 1) = 2n^3 - n^2$

$$\boxed{\Theta(n^3)}$$

---

## 🧮 Formeln & Rechenregeln

### Kernformeln der Woche

| Formel | Beschreibung | Variablen |
|---|---|---|
| $(A \cdot B)_{ij} = \sum_{\ell} a_{i\ell} \cdot b_{\ell j}$ | Matrixprodukt (Zeile × Spalte) | $A$: $m \times k$, $B$: $k \times n$ |
| $p(t) = p(0) \cdot T^t$ | Verteilung nach $t$ Schritten | $p(0)$ = Startverteilung, $T$ = Übergangsmatrix |
| $v_{t+1} = v_t \cdot T$ | Matrix-Vektor-Iteration | Konvergiert zur invarianten Verteilung |
| $v \cdot A = \lambda v$ | Eigenwertgleichung | $v$ = Eigenvektor, $\lambda$ = Eigenwert |
| $\lambda = \langle v, v \cdot A\rangle$ | Eigenwert aus Eigenvektor | Nach Konvergenz der Potenzmethode |
| $v_{\text{norm}} = \frac{v}{\sqrt{\langle v, v\rangle}}$ | Normierung (Länge 1) | Nötig bei Potenzmethode |

### Formeln aus vorherigen Wochen (weiterhin benötigt)

| Formel | Aus SW | Beschreibung |
|---|---|---|
| $\vec{\pi} \cdot T = \vec{\pi}$ mit $\sum \pi_i = 1$ | SW 06 | Invariante Verteilung (LGS) |
| Irreduzibel + Aperiodisch → Konvergenz | SW 06 | Eindeutigkeit der invarianten Verteilung |

---

## 🍳 Kochrezepte (Schritt-für-Schritt-Anleitungen)

### Kochrezept 1: Matrixprodukt berechnen

```
Schritt 1: Dimensionen prüfen
           A ist (m × k), B ist (k × n) → Ergebnis ist (m × n)
           ⚠️ Spalten(A) ≠ Zeilen(B) → NICHT möglich!

Schritt 2: Für jeden Eintrag (i, j) im Ergebnis:
           → Nimm Zeile i von A
           → Nimm Spalte j von B
           → Multipliziere komponentenweise und summiere

Schritt 3: Kontrolle
           → Ergebnis hat richtige Dimension (m × n)?
           → Bei Übergangsmatrizen: Zeilensumme = 1?
```

### Kochrezept 2: Invariante Verteilung per Matrix-Vektor-Iteration

```
Schritt 1: Übergangsmatrix T aufstellen
           → Zeilensumme = 1 prüfen!

Schritt 2: Startverteilung wählen (z.B. (1, 0, 0, ...))
           → Beliebig wählbar (bei irreduzibel + aperiodisch)

Schritt 3: Iterieren: v_neu = v_alt · T
           → Wiederholen bis |v_neu - v_alt| < ε (z.B. 10⁻¹⁰)

Schritt 4: Ergebnis = invariante Verteilung π
           → Kontrolle: Summe = 1?
           → Kontrolle: π · T ≈ π?
```

### Kochrezept 3: Invariante Verteilung per LGS (von Hand)

```
Schritt 1: Gleichungen aus π · T = π aufstellen
           → Spalte j: Σᵢ πᵢ · Tᵢⱼ = πⱼ
           → Das ergibt n Gleichungen

Schritt 2: Eine Gleichung streichen (ist redundant!)
           → Ersetzen durch: π₁ + π₂ + ... + πₙ = 1

Schritt 3: LGS lösen (Einsetzen oder Gauss)
           → Tipp: Erst eine Variable durch eine andere ausdrücken

Schritt 4: Kontrolle
           → Alle πᵢ ≥ 0?
           → Summe = 1?
           → π · T = π?
```

### Kochrezept 4: Potenzmethode (dominanter Eigenwert/Eigenvektor)

```
Schritt 1: Matrix A aufstellen
           → Bei Leslie-Matrix: Zeile i = Von Phase i, Spalte j = Nach Phase j

Schritt 2: Startvektor wählen (z.B. v = (1, 1, 1, ...))
           → Normieren: v = v / ||v||

Schritt 3: Iterieren:
           a) v' = v · A
           b) v = v' / ||v'||    (normieren!)
           → Wiederholen bis |v_alt - v_neu| < ε

Schritt 4: Eigenwert berechnen: λ = ⟨v, v · A⟩

Schritt 5: Interpretation:
           → λ > 1: System wächst (Population überlebt)
           → λ < 1: System schrumpft (Population stirbt aus)
           → λ = 1: Gleichgewicht
           → Eigenvektor v: Gleichgewichtsverteilung (nach Normierung auf Summe 1)
```

### Entscheidungsbaum: Welche Methode für invariante Verteilung?

```
Invariante Verteilung gesucht?
│
├── Wenige Zustände (n ≤ 4)?
│   └── JA → Kochrezept 3: LGS von Hand lösen
│              (exakte Lösung, gut für Prüfung)
│
├── Viele Zustände (n > 4)?
│   └── JA → Kochrezept 2: Matrix-Vektor-Iteration (Python)
│              (numerische Lösung, schnell programmiert)
│
└── Keine stochastische Matrix (beliebige Matrix A)?
    └── JA → Kochrezept 4: Potenzmethode
               (findet dominanten Eigenvektor + Eigenwert)
```

### Entscheidungsbaum: Was sagt der dominante Eigenwert?

```
Dominanter Eigenwert λ bestimmt?
│
├── λ > 1 → System wächst exponentiell
│            (Population überlebt langfristig)
│
├── λ = 1 → System ist stabil
│            (Gleichgewicht, wie bei Markov-Ketten)
│
└── λ < 1 → System schrumpft exponentiell
             (Population stirbt aus)
```

---

## 📊 Vergleiche & Klassifizierungen

### Methoden zur Berechnung invarianter Verteilungen

| Methode | Wann nutzen? | Vorteile | Nachteile |
|---|---|---|---|
| **LGS lösen** (von Hand) | Wenige Zustände (≤ 4) | Exakte Lösung | Bei vielen Zuständen zu aufwändig |
| **Matrix-Vektor-Iteration** | Stochastische Matrizen | Einfach zu programmieren, schnell | Nur numerische Näherung |
| **Eigenwert-Zerlegung** (numpy) | Beliebige Matrizen | Exakt (numerisch), findet alle Eigenwerte | Mathematisch anspruchsvoller |
| **Potenzmethode** | Dominanter Eigenwert gesucht | Einfach, auch für grosse Matrizen | Findet nur den dominanten Eigenwert |

### Matrix-Vektor-Iteration vs. Potenzmethode

| | Matrix-Vektor-Iteration | Potenzmethode |
|---|---|---|
| **Anwendung** | Markov-Ketten (stochastische Matrix) | Beliebige quadratische Matrix |
| **Ziel** | Invariante Verteilung $\vec{\pi}$ | Eigenvektor + Eigenwert |
| **Normierung** | Nicht nötig (Summe bleibt 1) | Nötig (Länge auf 1 setzen) |
| **Bedingung** | Irreduzibel + Aperiodisch für Eindeutigkeit | Matrix hat bestimmte algebraische Eigenschaften |
| **Eigenwert** | Immer $\lambda = 1$ | Beliebig |

---

## 💻 Code-Beispiele (Python)

### 1. Matrixmultiplikation

```python
import numpy as np

A = np.array([[0, 8, 0],
              [9, 6, 0],
              [2, 3, 3]])

B = np.array([[5, 8],
              [7, 5],
              [3, 2]])

# Matrixprodukt
C = np.matmul(A, B)    # oder: C = A @ B
print("A · B =\n", C)
# [[56  40]
#  [87 102]
#  [40  37]]

# Dimensionen: (3×3) · (3×2) = (3×2) ✓
print("Dimensionen:", A.shape, "·", B.shape, "=", C.shape)
```

### 2. Matrix-Vektor-Iteration für invariante Verteilung

```python
import numpy as np

# Übergangsmatrix
T = 1/12 * np.array([[0, 6, 6],
                      [3, 6, 3],
                      [4, 4, 4]])

# Kontrolle: Zeilensumme = 1
print("Zeilensummen:", T.sum(axis=1))  # → [1. 1. 1.] ✓

# Startverteilung
p = np.array([1, 0, 0])

# Iteration mit Abbruchbedingung
for i in range(100):
    p_alt = p
    p = np.matmul(p, T)
    if np.abs(p_alt - p).sum() < 1e-10:
        print(f"Konvergiert nach {i+1} Iterationen")
        break

print("Invariante Verteilung:", np.round(p, 4))
# → [0.2222 0.4444 0.3333]
print("Summentest:", np.round(p.sum(), 4))  # → 1.0 ✓
```

### 3. Potenzmethode (Leslie-Matrix / Populationsdynamik)

```python
import numpy as np

# Leslie-Matrix: Meeresschildkröten
# Lebensphasen: N, J, P, E, B, A
A = np.array([[  0, 0.09, 0   , 0   , 0   , 0  ],
              [  0, 0   , 0.15, 0   , 0   , 0  ],
              [  0, 0   , 0   , 0.33, 0   , 0  ],
              [180, 0   , 0   , 0   , 0.75, 0  ],
              [ 70, 0   , 0   , 0   , 0   , 0.8],
              [  0, 0   , 0   , 0   , 0   , 0.5]])

# Startvektor
v = np.array([1, 1, 1, 1, 1, 1], dtype=float)
v = v / np.sqrt(np.dot(v, v))  # Normieren

# Potenzmethode
for i in range(500):
    v_alt = v
    v_next = np.matmul(v, A)
    v = v_next / np.sqrt(np.dot(v_next, v_next))  # Normieren!
    if np.abs(v_alt - v).sum() < 1e-10:
        print(f"Konvergiert nach {i+1} Iterationen")
        break

# Eigenwert berechnen
eigenwert = np.dot(v, np.matmul(v, A))
print(f"Dominanter Eigenwert: λ = {eigenwert:.6f}")
# → λ ≈ 1.0084 > 1: Population wächst!

# Gleichgewichtsverteilung
verteilung = v / v.sum() * 100
print("Verteilung (%):", np.round(verteilung, 2))
# → [89.67, 8.00, 1.19, 0.39, 0.29, 0.46]
```

### 4. Nicht-irreduzible Markov-Kette (zwei invariante Verteilungen)

```python
import numpy as np

# Block-diagonale Übergangsmatrix (NICHT irreduzibel)
T = 1/4 * np.array([[2, 2, 0, 0],
                     [1, 3, 0, 0],
                     [0, 0, 2, 2],
                     [0, 0, 2, 2]])

# Start in Block 1
p1 = np.array([1, 0, 0, 0])
for _ in range(100):
    p1_alt = p1
    p1 = np.matmul(p1, T)
    if np.abs(p1_alt - p1).sum() < 1e-10:
        break
print("Start in Block 1 → π =", np.round(p1, 4))
# → [0.3333, 0.6667, 0.0, 0.0]

# Start in Block 2
p2 = np.array([0, 0, 1, 0])
for _ in range(100):
    p2_alt = p2
    p2 = np.matmul(p2, T)
    if np.abs(p2_alt - p2).sum() < 1e-10:
        break
print("Start in Block 2 → π =", np.round(p2, 4))
# → [0.0, 0.0, 0.5, 0.5]

# Zwei verschiedene invariante Verteilungen! → nicht irreduzibel
```

### 5. Identitätsmatrix und Matrixpotenzen

```python
import numpy as np

# Identitätsmatrix
Id = np.identity(3)
T = 1/12 * np.array([[0, 6, 6], [3, 6, 3], [4, 4, 4]])

# Id · T = T
print("Id · T = T?", np.allclose(np.matmul(Id, T), T))  # → True

# Matrixpotenzen: T^2
T2 = np.matmul(T, T)
print("T² =\n", np.round(T2, 4))

# A^n für A = [[1, -1], [0, 1]]
A = np.array([[1, -1], [0, 1]])
for n in range(1, 6):
    An = np.linalg.matrix_power(A, n)
    print(f"A^{n} = {An.tolist()}")
# A^1 = [[1, -1], [0, 1]]
# A^2 = [[1, -2], [0, 1]]
# A^3 = [[1, -3], [0, 1]]  → Muster: A^n = [[1, -n], [0, 1]]
```

---

## ✏️ Übungsaufgaben-Zusammenfassung

| Nr. | Thema / Konzept | Lösungsansatz | Typische Stolpersteine |
|---|---|---|---|
| **1** | Matrixprodukte berechnen | Zeile × Spalte, Dimension prüfen | $(m \times k) \cdot (k \times n)$: **Spalten(A) = Zeilen(B)** nötig! Sonst nicht möglich. |
| **2** | Kommutativität: $AB = BA$ | Beide Produkte ausrechnen, Koeffizientenvergleich | Nicht alle Matrizen kommutieren! Lösung ist eine **Matrizenfamilie**. |
| **3** | Matrixpotenzen $A^n$ | Erste Potenzen berechnen, Muster erkennen | Muster nicht voreilig verallgemeinern – erst $A^1, A^2, A^3$ prüfen. |
| **4** | Komplexität Matrixmultiplikation | Operationen zählen: $n^2$ Einträge × $(2n-1)$ Ops | $\Theta(n^3)$, nicht $O(n^2)$! Drei verschachtelte Schleifen. |
| **5** | Invariante Verteilung (LGS) | $\vec{\pi} T = \vec{\pi}$ + Normierung $\sum = 1$ | **Eine Gleichung ist redundant** → durch Normierung ersetzen! |
| **6** | Nicht-irreduzible Kette | Block-Struktur erkennen, zwei Startverteilungen testen | Nicht-irreduzibel → **mehrere** invariante Verteilungen möglich! |
| **7** | Invariante Vert. (Serie 06) mit Python | Matrix-Vektor-Iteration programmieren | Abbruchbedingung nicht vergessen! Summentest durchführen. |
| **8** | Populationsdynamik (Leslie-Matrix) | Potenzmethode: $v' = v \cdot A$, normieren, $\lambda$ berechnen | **Normierung nötig!** $\lambda > 1$: wächst, $\lambda < 1$: schrumpft. |
| **9** | Sympathiegehalt (Paviane) | Übergangsmatrix aus Graph, Potenzmethode | Ähnlich wie PageRank: Sympathie verteilen proportional zur Fellpflege. |

---

## ⚠️ Prüfungsrelevante Hinweise

### ⚡ Typische Aufgabentypen und wie man sie erkennt

1. **"Berechnen Sie das Matrixprodukt $A \cdot B$"**
   → Dimensionen prüfen, Zeile × Spalte für jeden Eintrag.

2. **"Bestimmen Sie die invariante Verteilung"**
   → Wenige Zustände: LGS (Kochrezept 3). Viele Zustände: Iteration (Kochrezept 2).

3. **"Ist das langfristige Überleben gesichert?"**
   → Potenzmethode → dominanter Eigenwert $\lambda$: $\lambda > 1$ = ja, $\lambda < 1$ = nein.

4. **"Bestimmen Sie alle Potenzen $A^n$"**
   → $A^1, A^2, A^3$ berechnen → Muster erkennen → Formel aufstellen.

5. **"Warum hat diese Markov-Kette mehrere invariante Verteilungen?"**
   → Nicht irreduzibel! Block-Struktur der Matrix erkennen.

6. **"Bestimmen Sie den dominanten Eigenwert"**
   → Potenzmethode: Iterieren + normieren → $\lambda = \langle v, v \cdot A\rangle$.

### 🔑 Merkregeln und Eselsbrücken

| Merkregel | Erklärung |
|---|---|
| **"Zeile × Spalte"** | Matrixprodukt: Eintrag $(i,j)$ = Skalarprodukt von Zeile $i$ und Spalte $j$ |
| **"Spalten = Zeilen"** | Matrixprodukt $A \cdot B$ nur möglich, wenn $\text{Spalten}(A) = \text{Zeilen}(B)$ |
| **"AB ≠ BA"** | Matrixmultiplikation ist **NICHT** kommutativ! |
| **"Iteration = Kette laufen lassen"** | Matrix-Vektor-Iteration simuliert die Markov-Kette bis zum Gleichgewicht |
| **"Normieren = Richtung behalten"** | Bei Potenzmethode: Normierung verhindert Über-/Unterlauf, Richtung bleibt erhalten |
| **"λ > 1 = wächst, λ < 1 = schrumpft"** | Dominanter Eigenwert bestimmt das Langzeitverhalten des Systems |
| **"Nicht irreduzibel = mehrere Gleichgewichte"** | Block-Struktur → verschiedene Startverteilungen → verschiedene invariante Verteilungen |

### 🧠 Formeln die man auswendig wissen muss

1. **Matrixprodukt:** $(A \cdot B)_{ij} = \sum_{\ell} a_{i\ell} \cdot b_{\ell j}$
2. **Zeitentwicklung:** $p(t) = p(0) \cdot T^t$
3. **Eigenwertgleichung:** $v \cdot A = \lambda v$
4. **Potenzmethode:** $v' = v \cdot A$, dann $v = v'/\|v'\|$, Eigenwert: $\lambda = \langle v, v \cdot A\rangle$
5. **Komplexität Matrixmultiplikation:** $\Theta(n^3)$

### ❌ Häufige Fehlerquellen

1. **Dimensionen nicht geprüft:** $(3 \times 2) \cdot (3 \times 3)$ geht **NICHT** – Spalten von $A$ müssen gleich Zeilen von $B$ sein!
2. **Kommutativität angenommen:** $A \cdot B \neq B \cdot A$ im Allgemeinen! Reihenfolge ist entscheidend.
3. **Normierung bei Potenzmethode vergessen:** Ohne Normierung laufen die Werte gegen $\infty$ oder $0$.
4. **Redundante Gleichung nicht erkannt:** Bei $\vec{\pi} \cdot T = \vec{\pi}$ ist eine Gleichung überflüssig → durch $\sum \pi_i = 1$ ersetzen.
5. **Nicht-Irreduzibilität übersehen:** Wenn die Matrix Block-diagonal ist, gibt es **mehrere** invariante Verteilungen – die Lösung hängt von der Startverteilung ab!
6. **Eigenwert-Interpretation verwechselt:** $\lambda > 1$ heisst Wachstum, nicht Stabilität! Bei Markov-Ketten ist $\lambda = 1$ der Gleichgewichtsfall.

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
       │
SW 04 Zufallsvariablen
  └── E(X), Verteilungen
       │
SW 05 Randomisierte Algorithmen
  └── Las Vegas, Monte Carlo, erwartete Komplexität
       │
SW 06 Markov-Ketten
  └── Übergangsmatrix T, invariante Verteilung π,
       │  irreduzibel, aperiodisch, PageRank
       │
████████████████████████████████████████████████
█  SW 07 Matrizenalgebra  ◄── WIR SIND HIER   █
████████████████████████████████████████████████
       │
       │  Schlüsselkonzepte:
       │  • Matrizenmultiplikation (Zeile × Spalte)
       │  • Matrix-Vektor-Iteration (numerisch)
       │  • Potenzmethode → Eigenwerte/Eigenvektoren
       │  • Leslie-Matrix (Populationsdynamik)
       │
SW 08 Modulare Arithmetik
  └── Rechnen mit Resten, Kongruenzen
       └──── Matrizen über endlichen Körpern
```

### Konkrete Verbindungen

| Woche | Verbindung zu SW 07 |
|---|---|
| **SW 06** | Die **Übergangsmatrix** $T$ aus SW 06 wird jetzt effizient mit **Matrizenmultiplikation** berechnet. Die invariante Verteilung wird alternativ zur LGS-Methode per **Matrix-Vektor-Iteration** bestimmt. |
| **SW 04** | Der **Erwartungswert** $E(X)$ wird bei der Populationsdynamik verwendet: Erwartete Anzahl Nachkommen pro Lebensphase. |
| **SW 05** | Die **Komplexitätsanalyse** aus SW 05 wird auf die Matrixmultiplikation angewendet: $\Theta(n^3)$ Operationen. |
| **SW 08+** | Matrizenoperationen über **endlichen Körpern** (modulare Arithmetik) bilden die Grundlage für Kryptographie. |

---

> **📌 Zusammenfassung auf einen Blick:**
> SW 07 formalisiert die **Matrizenmultiplikation** (Zeile × Spalte, Dimension $(m \times k) \cdot (k \times n) = (m \times n)$, **NICHT kommutativ!**) und führt die **Matrix-Vektor-Iteration** als numerische Methode zur Berechnung invarianter Verteilungen ein: $v_{t+1} = v_t \cdot T$ bis Konvergenz. Neu sind **Eigenwerte/Eigenvektoren** ($v \cdot A = \lambda v$) und die **Potenzmethode** zur Berechnung des dominanten Eigenwerts. Anwendung: **Leslie-Matrizen** für Populationsdynamik – der dominante Eigenwert $\lambda$ bestimmt, ob eine Population wächst ($\lambda > 1$), stabil bleibt ($\lambda = 1$) oder ausstirbt ($\lambda < 1$). Die Komplexität der Matrixmultiplikation ist $\Theta(n^3)$.
