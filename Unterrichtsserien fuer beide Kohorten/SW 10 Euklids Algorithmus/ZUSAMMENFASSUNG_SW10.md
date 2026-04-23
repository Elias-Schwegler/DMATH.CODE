# DMATH.CODE – SW 10: Euklids Algorithmus

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Semesterwoche:** SW 10
> **Thema:** Euklids Algorithmus, erweiteter Algorithmus, multiplikative Inverse in modularer Arithmetik
> **Dozent:** Dr. Reto Berger · HSLU · Frühlingssemester 25
> **Quelle:** `DMATH-CODE-Serie10-final.pdf`

---

## 🎯 Lernziele

1. Sie wissen was die **Teiler einer natürlichen Zahl** sind und können die Anzahl der Teiler bestimmen.
2. Sie wissen was der **grösste gemeinsame Teiler (ggT)** ist und können ihn mit dem **Algorithmus von Euklid** berechnen.
3. Sie können mit dem **erweiterten Algorithmus** eine **Linearkombination** für den grössten gemeinsamen Teiler berechnen.
4. Sie wissen was in der **modularen Arithmetik inverse Zahlen** sind und Sie können diese berechnen.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Teiler einer Zahl** $T_n$ | Die Menge aller natürlichen Zahlen, die $n$ ohne Rest teilen. $T_0 = \mathbb{N}$ (weil $a \cdot 0 = 0$), $T_1 = \{1\}$, $T_2 = \{1,2\}$, … |
| **Primfaktorzerlegung** | Jede ganze Zahl $n \geq 2$ lässt sich **eindeutig** als endliches Produkt von Primzahlen schreiben: $n = 2^{n_1} \cdot 3^{n_2} \cdot 5^{n_3} \cdot \ldots \cdot p_k^{n_k}$ |
| **Anzahl Teiler** $\|T_n\|$ | Aus der Primfaktorzerlegung: $\|T_n\| = (n_1+1)(n_2+1)\cdots(n_k+1)$ |
| **Grösster gemeinsamer Teiler (ggT)** | $\text{ggT}(a,b) = \max(T_a \cap T_b)$: die grösste Zahl, die sowohl $a$ als auch $b$ teilt |
| **Euklids Algorithmus** | Rekursives Verfahren: $\text{ggT}(a,b) = \text{ggT}(b,\,a \bmod b)$, Abbruch bei $\text{ggT}(a,0) = a$. Laufzeit: $\mathcal{O}(\log b)$ |
| **Erweiterter Euklidischer Algorithmus** | Berechnet zusätzlich zu $\text{ggT}(a,b)$ auch die Koeffizienten $s, t$ der Linearkombination $\text{ggT}(a,b) = s \cdot a + t \cdot b$ |
| **Linearkombination (Satz von Bachet)** | Für $a, b \in \mathbb{N}$ existieren $s, t \in \mathbb{Z}$ mit $\text{ggT}(a,b) = s \cdot a + t \cdot b$ (sogar unendlich viele Varianten) |
| **Additiv inverse Zahl** $-a$ | Zahl mit $a + (-a) = 0$. In modularer Arithmetik: $-r \equiv m - r \pmod m$ |
| **Multiplikativ inverse Zahl** $a^{-1}$ | Zahl mit $a \cdot a^{-1} = 1$. In modularer Arithmetik nur vorhanden, wenn $\text{ggT}(m, a) = 1$ (d.h. $a$ teilerfremd zu $m$) |
| **Teilerfremd** | Zwei Zahlen $a, b$ sind teilerfremd, wenn $\text{ggT}(a,b) = 1$ |
| **Probedivision** | Naiver Algorithmus zur Primfaktorzerlegung. Exponentielle Laufzeit $e^{N/2}$ mit $N$ = Bitlänge |
| **Zahlkörpersieb** | Bester bekannter Algorithmus zur Primfaktorzerlegung. Subexponentielle Laufzeit $e^{c \cdot N^{1/3} \cdot \log(N)^{2/3}}$ |

---

## 📐 Definitionen, Sätze & Beweise

### 1. Teiler einer Zahl und Primfaktorzerlegung

#### Definition: Teiler-Menge
Für alle $n \in \mathbb{N} \cup \{0\}$ bezeichnet $T_n$ die Menge aller Teiler von $n$:

| $n$ | $T_n$ |
|---|---|
| $0$ | $\{1, 2, 3, 4, 5, \ldots\}$ (weil $a \cdot 0 = 0$ für jedes $a$) |
| $1$ | $\{1\}$ |
| $2$ | $\{1, 2\}$ |
| $3$ | $\{1, 3\}$ |
| $4$ | $\{1, 2, 4\}$ |
| $60$ | $\{1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60\}$ |
| $61$ | $\{1, 61\}$ (Primzahl!) |
| $62$ | $\{1, 2, 31, 62\}$ |

### Satz 1: Primfaktorzerlegung und Anzahl Teiler

> Sei $(2, 3, 5, 7, 11, \ldots)$ die Folge aller Primzahlen der Grösse nach.
>
> - Jede ganze Zahl $n \geq 2$ kann **eindeutig** als endliches Produkt von Primzahlen geschrieben werden:
>   $$n = 2^{n_1} \cdot 3^{n_2} \cdot 5^{n_3} \cdot 7^{n_4} \cdot 11^{n_5} \cdots p_k^{n_k}$$
> - Die Anzahl der Teiler berechnet sich aus den Exponenten:
>   $$\boxed{\|T_n\| = (n_1+1)(n_2+1)(n_3+1) \cdots (n_k+1)}$$

**Begründung:** In einem Teiler kommt jeder Primfaktor $p_i$ entweder $0$-mal, $1$-mal, …, oder $n_i$-mal vor — das sind genau $(n_i+1)$ Möglichkeiten. Über alle Primfaktoren multipliziert ergibt das $(n_1+1)(n_2+1)\cdots$

**Beispiel:** $n = 60$

$$60 = 2^1 \cdot 30 = 2^2 \cdot 15 = 2^2 \cdot 3^1 \cdot 5 = \boxed{2^2 \cdot 3^1 \cdot 5^1}$$

Aus den Exponenten $n_1 = 2, n_2 = 1, n_3 = 1$:

$$\|T_{60}\| = (2+1)(1+1)(1+1) = 3 \cdot 2 \cdot 2 = \boxed{12}$$

**Weitere Beispiele aus Aufgabe 1:**

| $n$ | Primfaktorzerlegung | Anzahl Teiler |
|---|---|---|
| 4400 | $2^4 \cdot 5^2 \cdot 11^1$ | $(4+1)(2+1)(1+1) = 5 \cdot 3 \cdot 2 = \mathbf{30}$ |
| 4'500'000 | $2^5 \cdot 3^2 \cdot 5^6$ | $(5+1)(2+1)(6+1) = 6 \cdot 3 \cdot 7 = \mathbf{126}$ |

---

### 2. Laufzeit der Primfaktorzerlegung – Warum das wichtig ist

Die obige Methode zur Berechnung der Anzahl Teiler **braucht die Primfaktorzerlegung**. Und hier beginnt das Problem:

> **Offenes Problem:** Es ist **nicht bekannt**, ob ein Algorithmus mit polynomieller Laufzeit für die Primfaktorzerlegung existiert!

Für die bekannten Algorithmen gilt die Laufzeit-Abschätzung:

$$\text{Laufzeit} = e^{c \cdot N^\alpha \cdot \log(N)^{1-\alpha}} \qquad \text{mit } N = \text{Bitlänge von } n$$

| Algorithmus | $\alpha$ | $c$ | Laufzeit | Bewertung |
|---|---|---|---|---|
| **Probedivision** | $1$ | $\tfrac{1}{2}$ | $e^{\tfrac{1}{2} \cdot N} = (\sqrt{e})^N$ | **Exponentiell** |
| **Quadratisches Sieb** | $\tfrac{1}{2}$ | $1$ | $e^{\sqrt{N} \cdot \sqrt{\log N}}$ | subexponentiell |
| **Zahlkörpersieb** | $\tfrac{1}{3}$ | $c \gg 1$ | $e^{c \cdot N^{1/3} \cdot \log(N)^{2/3}}$ | **Aktuell bester Algorithmus!** |
| *(hypothetisch)* | $0$ | — | $e^{c \cdot \log N} = N^c$ | Polynomiell *(existiert nicht bekannt)* |

> 💡 **Diese Schwierigkeit ist die Grundlage moderner Kryptographie** (z.B. RSA): Das Verschlüsseln mit einem öffentlichen Schlüssel ist einfach, das Brechen ohne privaten Schlüssel erfordert eine Primfaktorzerlegung — und die ist praktisch unmöglich für sehr grosse Zahlen.

---

### 3. Grösster gemeinsamer Teiler (ggT)

#### Definition 1: ggT
> Für $a, b \in \mathbb{N}$ heisst die Zahl
>
> $$\boxed{\text{ggT}(a, b) = \max(T_a \cap T_b)}$$
>
> der **grösste gemeinsame Teiler** von $a$ und $b$. Anschaulich: $\text{ggT}(a,b)$ ist die grösste Zahl, die sowohl $a$ als auch $b$ teilt.

**Beispiel:**
$$\text{ggT}(4, 62) = \max(T_4 \cap T_{62}) = \max(\{1, 2, 4\} \cap \{1, 2, 31, 62\}) = \max\{1, 2\} = \mathbf{2}$$

### Satz 2: ggT via Primfaktorzerlegung

> Aus den Primfaktorzerlegungen $a = 2^{n_1} \cdot 3^{n_2} \cdot 5^{n_3} \cdots$ und $b = 2^{m_1} \cdot 3^{m_2} \cdot 5^{m_3} \cdots$ folgt:
>
> $$\boxed{\text{ggT}(a, b) = 2^{\min\{n_1, m_1\}} \cdot 3^{\min\{n_2, m_2\}} \cdot 5^{\min\{n_3, m_3\}} \cdots}$$

**Beispiel:** $a = 120, b = 700$

$$120 = 2^3 \cdot 3^1 \cdot 5^1 \qquad 700 = 2^2 \cdot 5^2 \cdot 7^1$$

$$\text{ggT}(120, 700) = 2^{\min\{3,2\}} \cdot 3^{\min\{1,0\}} \cdot 5^{\min\{1,2\}} \cdot 7^{\min\{0,1\}} = 2^2 \cdot 3^0 \cdot 5^1 \cdot 7^0 = \mathbf{20}$$

> ⚠️ **Problem:** Diese Methode braucht die Primfaktorzerlegung — und die ist, wie wir gesehen haben, praktisch nicht effizient berechenbar für grosse Zahlen! Deshalb: **Euklids Algorithmus** 👇

---

### 4. Der Algorithmus von Euklid (Satz 2)

> **Die geniale Idee:** Den ggT **ohne Primfaktorzerlegung** berechnen!

Euklid (antikes Griechenland) beschrieb das Verfahren im Buch VII seines Geometrie-Lehrwerks *Die Elemente* als **"abwechselnd das Kleinere vom Grösseren wegnehmen"**.

#### Das Fundament: Eine Gleichheit der Teilermengen

Aus der Division mit Rest $a = (a \text{ div } b) \cdot b + (a \bmod b)$ folgen zwei Implikationen:

$$x \in T_b \cap T_{a \bmod b} \implies a = \underbrace{(a \text{ div } b) \cdot b + (a \bmod b)}_{\text{durch } x \text{ teilbar}} \implies x \in T_a$$

$$x \in T_a \cap T_b \implies (a \bmod b) = \underbrace{a - (a \text{ div } b) \cdot b}_{\text{durch } x \text{ teilbar}} \implies x \in T_{a \bmod b}$$

Daraus folgt die **zentrale Gleichheit**:

$$\boxed{T_a \cap T_b = T_b \cap T_{a \bmod b}}$$

#### Satz 2 (Algorithmus von Euklid)

> Für $a, b \in \mathbb{N}$ mit $a \geq b$ wiederhole:
>
> $$\text{ggT}(a, b) = T_a \cap T_b = T_b \cap T_{a \bmod b} = \text{ggT}(b, a \bmod b)$$
>
> bis der Rest $a \bmod b$ Null wird. Dann gilt der Basisfall:
>
> $$\boxed{\text{ggT}(a, 0) = T_a \cap T_0 = \{1, \ldots, a\} \cap \mathbb{N} = a}$$

#### Klassisches Beispiel: $\text{ggT}(174, 102)$

| Schritt | Rechnung | Begründung |
|---|---|---|
| 1 | $\text{ggT}(174, 102) = \text{ggT}(102, 72)$ | weil $174 \bmod 102 = 72$ |
| 2 | $= \text{ggT}(72, 30)$ | weil $102 \bmod 72 = 30$ |
| 3 | $= \text{ggT}(30, 12)$ | weil $72 \bmod 30 = 12$ |
| 4 | $= \text{ggT}(12, 6)$ | weil $30 \bmod 12 = 6$ |
| 5 | $= \text{ggT}(6, 0) = \mathbf{6}$ | weil $12 \bmod 6 = 0$ (Basisfall!) |

### Satz 3: Laufzeit des Algorithmus von Euklid

> Für die Anzahl Iterationen im Algorithmus von Euklid gilt in Abhängigkeit von $b$ die asymptotische Abschätzung $\mathcal{O}(\log b)$.

**Herleitung (Aufgabe 3, optional):** Die Zahlen $b_1, b_2, b_3, \ldots$, bei denen jeweils eine Iteration mehr nötig ist, erfüllen die Rekursion

$$b_n = b_{n-1} + b_{n-2}$$

Das sind die **Fibonacci-Zahlen**! Mit der bekannten Lösung (via Binet-Formel):

$$b_n = \tfrac{1}{\sqrt{5}}\left[\left(\tfrac{1+\sqrt{5}}{2}\right)^n - \left(\tfrac{1-\sqrt{5}}{2}\right)^n\right] \leq 3^n$$

Umgestellt: **Anzahl Iterationen** $n \leq \log_3(b)$, also $\mathcal{O}(\log b)$.

> 💡 **Worst-Case:** Aufeinanderfolgende Fibonacci-Zahlen wie $(21, 13)$ brauchen die meisten Iterationen!

---

### 5. Erweiterter Euklidischer Algorithmus

### Satz 4 (Bachet de Méziriac, 1624)

> Der grösste gemeinsame Teiler von $a$ und $b$ ist eine **Linearkombination** von $a$ und $b$ mit ganzzahligen Koeffizienten.
>
> Es gibt also immer zwei ganze Zahlen $s, t \in \mathbb{Z}$, sodass:
>
> $$\boxed{\text{ggT}(a, b) = s \cdot a + t \cdot b}$$
>
> Tatsächlich gibt es **unendlich viele** Linearkombinationen:
>
> $$\text{ggT}(a, b) = (s - k \cdot b) \cdot a + (t + k \cdot a) \cdot b \quad \text{für alle } k \in \mathbb{Z}$$

**Beweis für die Unendlichkeit:**

$$(s - k \cdot b) \cdot a + (t + k \cdot a) \cdot b = s \cdot a - k \cdot b \cdot a + t \cdot b + k \cdot a \cdot b = s \cdot a + t \cdot b = \text{ggT}(a,b) \; \checkmark$$

#### Der Algorithmus – Rekursion für $s$ und $t$

Wir führen den Algorithmus von Euklid tabellarisch durch und berechnen **parallel** die Koeffizienten:

$$\boxed{s_n = s_{n-2} - q_n \cdot s_{n-1} \qquad t_n = t_{n-2} - q_n \cdot t_{n-1}}$$

mit den Startwerten $s_0 = 1, s_1 = 0$ und $t_0 = 0, t_1 = 1$.

In der **zweitletzten Zeile** der Tabelle steht der ggT und seine Linearkombinations-Koeffizienten.

#### Beispiel: $\text{ggT}(174, 102)$

| $a$ | $b$ | $a \text{ div } b$ $(q)$ | $a \bmod b$ $(r)$ | $s$ | $t$ |
|---|---|---|---|---|---|
| | | | | **1** | **0** |
| | | | | **0** | **1** |
| 174 | 102 | 1 | 72 | $1 - 1 \cdot 0 = 1$ | $0 - 1 \cdot 1 = -1$ |
| 102 | 72 | 1 | 30 | $0 - 1 \cdot 1 = -1$ | $1 - 1 \cdot (-1) = 2$ |
| 72 | 30 | 2 | 12 | $1 - 2 \cdot (-1) = 3$ | $-1 - 2 \cdot 2 = -5$ |
| 30 | 12 | 2 | **6** | $-1 - 2 \cdot 3 = \mathbf{-7}$ | $2 - 2 \cdot (-5) = \mathbf{12}$ |
| 12 | 6 | 2 | 0 | *(stopp)* | |

**Ergebnis:** $\text{ggT}(174, 102) = 6$ mit Linearkombination:

$$\boxed{6 = -7 \cdot 174 + 12 \cdot 102}$$

**Probe:** $-7 \cdot 174 + 12 \cdot 102 = -1218 + 1224 = 6 \; \checkmark$

---

## 💻 Aufgabe 4 – Erweiterter Euklid für $\text{ggT}(963, 218)$

| $a$ | $b$ | $a \text{ div } b$ | $a \bmod b$ | $s$ | $t$ |
|---|---|---|---|---|---|
| | | | | 1 | 0 |
| | | | | 0 | 1 |
| 963 | 218 | 4 | 91 | 1 | -4 |
| 218 | 91 | 2 | 36 | -2 | 9 |
| 91 | 36 | 2 | 19 | 5 | -22 |
| 36 | 19 | 1 | 17 | -7 | 31 |
| 19 | 17 | 1 | 2 | 12 | -53 |
| 17 | 2 | 8 | **1** | $\mathbf{-103}$ | $\mathbf{455}$ |
| 2 | 1 | 2 | 0 | *stopp* | |

**Ergebnis:** $\text{ggT}(963, 218) = 1$ mit

$$1 = (-103) \cdot 963 + 455 \cdot 218$$

**Eine zweite Linearkombination** (mit positivem $s$) via $k = 1$:

$$s_2 = s_1 + 218 = 115, \quad t_2 = t_1 - 963 = -508$$

$$1 = 115 \cdot 963 + (-508) \cdot 218$$

---

### 6. Inverse Zahlen in modularer Arithmetik

#### Motivation: Lineare Gleichung $a \cdot x + b = c$

In $\mathbb{Q}$ oder $\mathbb{R}$ können wir lineare Gleichungen nach $x$ auflösen:

$$a \cdot x + b = c \quad|\, +(-b)$$
$$a \cdot x = c + (-b) \quad|\, \cdot a^{-1}$$
$$x = a^{-1} \cdot (c + (-b))$$

**Das geht nur**, weil wir Addition mit $b$ und Multiplikation mit $a$ **rückgängig machen** können.

#### Definition 2: Inverse Zahlen

> Eine Zahl $a$ hat eine
>
> - **additiv inverse Zahl** $-a$, wenn $a + (-a) = 0$ gilt
> - **multiplikativ inverse Zahl** $a^{-1}$, wenn $a \cdot a^{-1} = 1$ gilt

#### Existenz von Inversen in verschiedenen Mengen

| Zahlenmenge | Additiv inverse | Multiplikativ inverse |
|---|---|---|
| $\mathbb{Q}, \mathbb{R}$ | ✅ existiert immer | ✅ existiert für $a \neq 0$ |
| $\mathbb{Z}$ | ✅ existiert immer | ❌ nur für $\pm 1$ |
| $\mathbb{Z}_m$ *(modulare Arithmetik)* | ✅ existiert immer (siehe Satz 5) | ⚠️ nur wenn $\text{ggT}(m, a) = 1$ |

> 💡 $0$ hat in keiner Zahlenmenge eine multiplikativ inverse Zahl — $0 \cdot x$ ist immer $0$!

### Satz 5: Inverse Zahlen in der modularen Arithmetik

> In der modularen Arithmetik mit Modulus $m \geq 2$ gilt:
>
> - Für alle $r \in \{0, 1, 2, \ldots, m-1\}$ gibt es eine **additiv inverse Zahl**
>   $$\boxed{r + \underbrace{(m-r)}_{= (-r)} \bmod m = 0}$$
> - Wenn $\text{ggT}(m, r) = 1$ (d.h. $r$ ist teilerfremd zu $m$), dann hat $r$ eine **multiplikativ inverse Zahl**
>   $$1 = \text{ggT}(m, r) = s \cdot m + t \cdot r \implies \underbrace{t \cdot r \bmod m = 1}_{\Rightarrow \; t = r^{-1}}$$

> 🎯 **Kernaussage:** Mit dem **erweiterten Algorithmus von Euklid** finden wir für den ggT eine Linearkombination — und damit bekommen wir die **multiplikativ inverse Zahl** quasi geschenkt!

---

## 💻 Aufgabe 5 – Inverse berechnen

### a) $r = 13$ in modularer Arithmetik mit $m = 211$

**Additiv invers:** $-13 = 211 - 13 = \mathbf{198}$

**Multiplikativ invers:** Erweiteter Euklid auf $(211, 13)$:

| $a$ | $b$ | div | mod | $s$ | $t$ |
|---|---|---|---|---|---|
| | | | | 1 | 0 |
| | | | | 0 | 1 |
| 211 | 13 | 16 | 3 | 1 | -16 |
| 13 | 3 | 4 | 1 | -4 | **65** |
| 3 | 1 | 3 | 0 | *stopp* | |

$\text{ggT}(211, 13) = 1$, also:
$$1 = (-4) \cdot 211 + 65 \cdot 13 \implies 13^{-1} \equiv \mathbf{65} \pmod{211}$$

### b) $r = 124$ in modularer Arithmetik mit $m = 345$

**Additiv invers:** $-124 = 345 - 124 = \mathbf{221}$

**Multiplikativ invers:** $\text{ggT}(345, 124) = 1 = (-23) \cdot 345 + 64 \cdot 124$

$$124^{-1} \equiv \mathbf{64} \pmod{345}$$

### c) $r = 129$ in modularer Arithmetik mit $m = 456$

**Additiv invers:** $-129 = 456 - 129 = \mathbf{327}$

**Multiplikativ invers:** $\text{ggT}(456, 129) = 3 \neq 1$ → **existiert NICHT!** ❌

> ⚠️ Weil $\text{ggT}(m, r) \neq 1$, hat $129$ keine multiplikativ inverse Zahl modulo $456$.

---

## 📝 Aufgaben-Zusammenfassung (Serie 10)

| Aufgabe | Thema | Kernkonzept |
|---|---|---|
| **1)** | Anzahl Teiler bestimmen | Primfaktorzerlegung → $(n_1+1)(n_2+1)\cdots$ |
| **2)** | Worst-Case Iterationen Euklid | Fibonacci-Zahlen als Worst-Case-Eingaben |
| **3) *(opt.)*** | $\mathcal{O}(\log b)$ beweisen | Lineare homogene Rekursion mit Grad 2 |
| **4)** | Erweiteter Euklid | $\text{ggT}(963, 218)$ + 2 Linearkombinationen |
| **5)** | Modulare Inverse | Additiv vs. multiplikativ inverse Zahlen berechnen |

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Prüfungsfragen

1. **«Wie viele Teiler hat die Zahl $X$?»** → Primfaktorzerlegung → $(n_1+1)(n_2+1)\cdots$
2. **«Führe Euklids Algorithmus für $\text{ggT}(a,b)$ durch.»** → Tabellarisch mit $a, b, a \text{ div } b, a \bmod b$
3. **«Finde die Linearkombination $\text{ggT}(a,b) = s \cdot a + t \cdot b$.»** → Erweiterte Tabelle mit $s, t$ Spalten
4. **«Gib das multiplikativ Inverse von $r$ modulo $m$ an (oder begründe, dass keines existiert).»**
   - Schritt 1: $\text{ggT}(m, r)$ berechnen
   - Falls $\neq 1$: Inverse existiert nicht!
   - Falls $= 1$: $t$ aus Linearkombination lesen → $r^{-1} \equiv t \pmod m$
5. **«Warum ist die Primfaktorzerlegung kryptographisch wichtig?»** → Keine polynomielle Algorithmen bekannt (Zahlkörpersieb: subexponentiell)

### Häufige Fehler

| Fehler | Korrektur |
|---|---|
| Bei $T_0$ nur $\{0\}$ angeben | $T_0 = \mathbb{N}$ (alle Zahlen teilen $0$, weil $a \cdot 0 = 0$) |
| Bei Primfaktoren vergessene/verdoppelte Primzahlen | Systematisch dividieren, bis Rest $= 1$ |
| Falsches Vorzeichen in Linearkombination | **Probe** machen: $s \cdot a + t \cdot b$ ausrechnen! |
| $r^{-1}$ existiert angenommen, aber $\text{ggT} \neq 1$ | **Immer zuerst** $\text{ggT}(m, r)$ prüfen! |
| Multiplikativ Inverse von $0$ gesucht | Existiert in keiner Zahlenmenge, niemals! |
| $t$ modulo $m$ negativ lassen | Ergebnis in $\{0, \ldots, m-1\}$ bringen: $t \bmod m$ |
| Spaltenreihenfolge $s, t$ vertauscht | $s$ ist Koeffizient für $a$, $t$ für $b$ — in dieser Reihenfolge |

### Merksätze

- **ggT-Formel via Primfaktoren:** "**min**" bei den Exponenten (kgV wäre "**max**")
- **Euklid-Abbruch:** sobald $b = 0$, dann ist der ggT der **vorletzte** $a$-Wert
- **Erweiterter Euklid:** die **zweitletzte Zeile** enthält ggT, $s$, $t$
- **Bachet-Formel:** $\text{ggT}(a,b) = s \cdot a + t \cdot b$ — **unendlich viele Lösungen!**
- **Multiplikatives Inverse existiert** $\Leftrightarrow \text{ggT}(m, r) = 1$ (teilerfremd!)

---

## 🔗 Verbindung zu anderen Wochen

| Woche | Thema | Verbindung zu SW 10 |
|---|---|---|
| **SW 07** | Matrizenalgebra | Lineare Gleichungen $Ax = b$ brauchen $A^{-1}$ — das ist ein Parallelkonzept zu multiplikativ inversen Zahlen |
| **SW 08** | Modulare Arithmetik | **Direkte Grundlage!** `div`, `mod`, Kongruenzen ($a \equiv b \pmod m$) — ohne das funktioniert Euklid nicht |
| **SW 09** | Primzahlen | **Satz 1 (Primfaktorzerlegung)** ist die Basis der Teileranzahl. Die Schwierigkeit der Faktorisierung ist der Grund für Euklid |
| *(Ausblick SW 11)* | **Chinesischer Restsatz** | Nutzt das multiplikativ Inverse aus SW 10 direkt! Gleichungssysteme $x \equiv a_i \pmod{m_i}$ lösen |
| *(Ausblick SW 12)* | **Endliche Gruppen** | Inverse Elemente sind die Grundlage von Gruppen $(\mathbb{Z}_m^*, \cdot)$ — die Elemente sind genau die, welche ein Inverses haben |
| *(Ausblick SW 13)* | **Endliche Körper** | $\mathbb{Z}_p$ ist genau dann ein Körper, wenn $p$ eine Primzahl ist — dann hat jedes Element $\neq 0$ ein multiplikativ Inverses |

---

## 🧠 Das grosse Bild

```
  SW 08 mod/div   SW 09 Primzahlen
        \              /
         \            /
    ┌─────▼──────────▼─────┐
    │      SW 10           │
    │  EUKLIDS ALGORITHMUS │
    │  - ggT               │
    │  - Linearkombination │
    │  - Modulare Inverse  │
    └──────────┬───────────┘
               │
               ▼
    SW 11 Chinesischer Restsatz
    SW 12 Endliche Gruppen
    SW 13 Endliche Körper → Kryptographie
```

Der **erweiterte Euklidische Algorithmus** ist das **zentrale Werkzeug** für die kommenden Wochen: Er löst lineare Gleichungssysteme in modularer Arithmetik, ermöglicht RSA-Schlüsselgenerierung und ist die Grundlage jeder ernsthaften Zahlentheorie.

---

## 🧠 Kurzübersicht: Die 3 wichtigsten Algorithmen

### 1️⃣ ggT mit Euklid (einfach)
```
ggT(a, b):
    while b != 0:
        a, b = b, a mod b
    return a
```

### 2️⃣ Erweiterter Euklid (mit Linearkombination)
```
extGgT(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while b != 0:
        q = a div b
        a, b = b, a mod b
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return a, s0, t0    # ggT, s, t
```

### 3️⃣ Multiplikativ Inverse modulo m
```
inverse(r, m):
    ggT, s, t = extGgT(m, r)
    if ggT != 1:
        return "existiert nicht"
    return t mod m     # Ergebnis in {0, ..., m-1}
```
