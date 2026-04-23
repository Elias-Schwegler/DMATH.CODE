# DMATH.CODE – SW 09: Primzahlen

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Semesterwoche:** SW 09
> **Thema:** Primzahlen, Mersenne-Primzahlen, Primzahlsatz, Sieb des Eratosthenes, Miller-Rabin-Test
> **Dozent:** Dr. Reto Berger · HSLU · Frühlingssemester 25
> **Quelle:** `DMATH-CODE-Serie09-final.pdf`

---

## 🎯 Lernziele

1. Sie kennen den **Unterschied von prim und zusammengesetzt**.
2. Sie verstehen, was **Mersenne-Primzahlen** sind und wissen, wie der **Lucas-Lehmer-Test** funktioniert.
3. Sie kennen den **Primzahlsatz** und können die Anzahl Primzahlen in einem Bereich abschätzen.
4. Sie verstehen den **kleinen Satz von Fermat** und wissen, wie der **Miller-Rabin-Test** funktioniert.

> 💡 **Warum Primzahlen wichtig sind:** Kryptographie (RSA), Pseudozufallszahlen, Hashing, Prüfziffern. Die Suche nach grossen Primzahlen ist ein aktives Forschungsgebiet (z.B. GIMPS, Great Internet Mersenne Prime Search).

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---|---|
| **Prim** | Positive ganze Zahl $n \in \mathbb{N}$ mit **genau zwei verschiedenen Teilern** (1 und $n$ selbst) |
| **Zusammengesetzt** | Positive ganze Zahl $n \in \mathbb{N}$ mit **mehr als zwei Teilern** |
| **Multiplikative Einheit** | Die Zahl $1$ ist weder prim noch zusammengesetzt – Sonderfall |
| **Primzahlzwillinge** | Zwei aufeinanderfolgende Primzahlen mit Abstand 2, z.B. $(3,5), (5,7), (11,13), \ldots$ |
| **Ulam-Spirale** | Spiralförmige Anordnung der natürlichen Zahlen, bei der Primzahlen diagonale Muster bilden |
| **Mersenne-Zahl** $M_n$ | Zahl der Form $M_n = 2^n - 1$, z.B. $M_1=1, M_2=3, M_3=7, M_4=15, M_5=31$ |
| **Mersenne-Primzahl** | Mersenne-Zahl, die selbst prim ist – nur wenn $n$ prim ist (aber nicht umgekehrt!) |
| **Goldbach-Zerlegung** | Darstellung einer geraden Zahl $> 2$ als Summe zweier Primzahlen |
| **Primzahlfunktion** $\pi(n) = \text{primes}(n)$ | Anzahl Primzahlen $\leq n$ |
| **Primzahlsatz** | Asymptotische Aussage: $\pi(n) \sim \frac{n}{\ln n}$ |
| **Sieb des Eratosthenes** | Algorithmus zur Berechnung aller Primzahlen $\leq n$ |
| **Fermat-Eigenschaft** | $a^{p-1} \bmod p = 1$ für jede Primzahl $p$ und $a \in \{1, \ldots, p-1\}$ |
| **Pseudoprimzahl** | Zusammengesetzte Zahl, die die Fermat-Eigenschaft für einige (oder viele) Basen erfüllt |
| **Lucas-Lehmer-Test** | Deterministischer Primzahltest für Mersenne-Zahlen |
| **Miller-Rabin-Test** | Probabilistischer (zufallsbasierter) Primzahltest |

---

## 📐 Definitionen, Sätze & Beweise

### 1. Die drei Sorten natürlicher Zahlen

#### Definition 1: Prim vs. zusammengesetzt

> Positive ganze Zahlen werden in **drei Sorten** unterteilt:
>
> $$\mathbb{N} = \{1\} \cup \{\text{prim}\} \cup \{\text{zusammengesetzt}\}$$
>
> - **Prim**: genau zwei verschiedene Teiler
> - **Zusammengesetzt**: mehr als zwei Teiler
> - **Einheit** (1): weder noch

```
Ersten Zahlen klassifiziert:

  N │ Teiler      │ Eigenschaft
 ───┼─────────────┼──────────────────
  1 │ {1}         │ Einheit (Sonderfall)
  2 │ {1,2}       │ ◆ prim (einzige gerade Primzahl!)
  3 │ {1,3}       │ ◆ prim
  4 │ {1,2,4}     │ ■ zusammengesetzt
  5 │ {1,5}       │ ◆ prim
  6 │ {1,2,3,6}   │ ■ zusammengesetzt
  7 │ {1,7}       │ ◆ prim
  8 │ {1,2,4,8}   │ ■ zusammengesetzt
  9 │ {1,3,9}     │ ■ zusammengesetzt
 10 │ {1,2,5,10}  │ ■ zusammengesetzt
 11 │ {1,11}      │ ◆ prim
```

---

### 2. 📊 Graph: Die Ulam-Spirale

> **Erläuterung:** 1963 kritzelte der polnische Mathematiker **Stanisław Ulam** aus Langeweile während eines Vortrags die Zahlen in Spiralform auf Papier. Er entdeckte, dass die Primzahlen **verblüffend oft auf diagonalen Linien** liegen – ein bis heute nicht vollständig erklärtes Muster!

```
Ulam-Spirale (von 1 in der Mitte nach aussen)
Primzahlen sind *gross* markiert:

   37─36─35─34─33─32─31
    │                  │
   38  17─16─15─14─13  30
    │   │           │   │
   39  18   5─ 4─ 3  12  29
    │   │   │       │   │   │
   40  19   6   1─ 2  11  28
    │   │   │           │   │
   41  20   7─ 8─ 9─10  27
    │   │                  │
   42  21─22─23─24─25─26
    │
   43─44─45─46─47─48─49 ...

Wenn man die Primzahlen hervorhebt:

   .  .  .  .  . 32 31
    │                  │
   38 17  .  .  . 13  .
    │                      │
    .  .  5  .  3  .  29
                     │   │
    .  19   .   .  2 11  .
                                 │
   41  . 7  .  .  . 27
    │                  │
    . . 23  . . .
                     │
   43 . . . 47 .
```

### Satz 1: Primzahlen in drei Sorten

> Primzahlen können in drei Sorten unterteilt werden:
>
> $$\mathbb{P} = \{2\} \cup \{n \in \mathbb{P}: n \bmod 4 = 1\} \cup \{n \in \mathbb{P}: n \bmod 4 = 3\}$$

**Begründung (Aufgabe 2a):** Für jede Zahl $n$ gilt $n = (n \text{ div } 4) \cdot 4 + (n \bmod 4)$. Der erste Summand ist durch 2 teilbar. Eine Primzahl $n > 2$ ist **nicht** durch 2 teilbar, also muss $n \bmod 4 \in \{1, 3\}$ sein (nicht $0$ oder $2$, weil dann gerade).

---

### 3. Primzahlzwillinge

#### Definition 2: Primzahlzwillinge
> Zwei aufeinanderfolgende Primzahlen heissen **Zwillinge**, wenn sie einen Abstand von 2 haben.

**Die ersten Primzahlzwillinge:**
$$(3,5),\ (5,7),\ (11,13),\ (17,19),\ (29,31),\ (41,43),\ (59,61),\ (71,73),\ \ldots$$

### Satz (Aufgabe 3): Alle Primzahlzwillinge ausser (3,5) haben $a \bmod 6 = 5$

**Beweis:** Es gilt $a = (a \text{ div } 6) \cdot 6 + (a \bmod 6)$ mit $b = a + 2$.

- $(a \bmod 6) \in \{0, 1, 2, 3, 4, 5\}$. Die Werte $0, 2, 3, 4$ scheiden aus, weil durch 2 oder 3 teilbar.
- Bleibt $(a \bmod 6) \in \{1, 5\}$.
- Wäre $a \bmod 6 = 1$, dann $b \bmod 6 = 3$ → aber $b$ durch 3 teilbar → nicht prim!
- Bleibt: $a \bmod 6 = 5$ (ausser bei $a=3$, dem Sonderfall).

> ⚠️ **Offenes Problem:** Es wird **vermutet**, dass es unendlich viele Primzahlzwillinge gibt – aber bis heute **nicht bewiesen**!

---

### 4. 📊 Graph: Die Goldbach-Vermutung

#### Vermutung von Goldbach (1742)
> Jede **gerade Zahl** grösser als 2 ist die Summe zweier Primzahlen.

**Beispiele:**
```
  4 = 2 + 2
  6 = 3 + 3
  8 = 3 + 5
 10 = 3 + 7  ODER  5 + 5    ← nicht eindeutig!
 12 = 5 + 7
 14 = 3 + 11 ODER  7 + 7
 16 = 3 + 13 ODER  5 + 11
 18 = 7 + 11 ODER  5 + 13   ← 2 Zerlegungen
 ...
```

> ⚠️ **Auch ungelöst!** Zählt zu den berühmtesten offenen Problemen der Mathematik.

**Graph aus dem Skript: Anzahl Goldbach-Zerlegungen**

```
Anzahl Zerlegungen
      ↑
 3500 ┤                                           ....
      │                                      ....:'''
 3000 ┤                                  ....':'
      │                              ...''':
 2500 ┤                          ....':'
      │                       ...''':
 2000 ┤                     ..':''
      │                  ...':
 1500 ┤            ■    ..':           ← bei a = 60'000 gibt es
      │         .....:''                  ca. 1500 Goldbach-Zerlegungen
 1000 ┤      ..''''
      │   .:'''
  500 ┤ .'''
      │.'
    0 ┼──────┬──────┬──────┬──────┬──────┬──────→
      0    40'000  80'000  120'000   160'000     a

💡 Je GRÖSSER die Zahl, desto MEHR Zerlegungen gibt es!
   Das ist ein starkes empirisches Indiz für Goldbach –
   aber kein Beweis.
```

---

### 5. Mersenne-Zahlen und Mersenne-Primzahlen

#### Definition 3: Mersenne-Zahl
> Die Zahlen $M_n = 2^n - 1$ heissen **Mersenne-Zahlen**.

```
n:    1   2   3    4    5    6     7     ...
Mₙ:   1   3   7   15   31   63   127    ...
      │   ◆   ◆   ■    ◆    ■     ◆
     ein  prim prim zus. prim zus. prim
```

**Im Binärsystem (Aufgabe 4):**
$$M_n = 2^n - 1 = \underbrace{111\ldots 1}_{n\text{ Einsen}}$$

Beispiele: $M_2 = 11_2$, $M_3 = 111_2$, $M_4 = 1111_2 = 15$

### Satz 2: Wenn $n$ zusammengesetzt ist, ist auch $M_n$ zusammengesetzt

**Beweis** (clevere geometrische Reihe):
$$M_{a \cdot b} = 2^{a \cdot b} - 1 = (2^a - 1) \cdot \left(2^{a \cdot 0} + 2^{a \cdot 1} + 2^{a \cdot 2} + \ldots + 2^{a(b-1)}\right)$$

→ $M_{ab}$ ist durch $M_a$ teilbar → zusammengesetzt!

> 💡 **Folgerung:** Für Mersenne-**Primzahlen** muss $n$ eine Primzahl sein.
>
> ⚠️ **ABER:** Die Umkehrung gilt NICHT! $n = 11$ ist prim, aber $M_{11} = 2047 = 23 \cdot 89$ ist zusammengesetzt.

```
 n prim:    2    3    5    7     11            13     17
 Mₙ:        3    7   31  127   2047=23·89    8191  131071
           ◆    ◆    ◆    ◆     ■             ◆     ◆
          prim prim prim prim  ZUSAMMEN!     prim   prim
```

### Lucas-Lehmer-Test – der effiziente Mersenne-Primzahltest

Rekursion: $S(1) = 4$, $\;S(k+1) = S(k)^2 - 2 \bmod M_p$

> $M_p$ ist **genau dann** prim, wenn $S(p-1) = 0$ gilt.

**Aufgabe 6 – Test für $M_7 = 127$:**

| $k$ | $S(k)$ | Rechnung |
|---|---|---|
| 1 | 4 | (Initial) |
| 2 | 14 | $4^2 - 2 \bmod 127 = 14$ |
| 3 | 67 | $14^2 - 2 \bmod 127 = 67$ |
| 4 | 42 | $67^2 - 2 \bmod 127 = 42$ |
| 5 | 111 | $42^2 - 2 \bmod 127 = 111$ |
| **6** | **0** | $111^2 - 2 \bmod 127 = \mathbf{0}$ ✅ |

→ $M_7 = 127$ ist **prim**! Da $p - 1 = 6$ und $S(6) = 0$.

**Aufgabe 6 – Test für $M_{11} = 2047$:**

| $k$ | $S(k)$ |
|---|---|
| 1 | 4 |
| 2 | 14 |
| 3 | 194 |
| 4 | 788 |
| 5 | 701 |
| 6 | 119 |
| 7 | 1877 |
| 8 | 240 |
| 9 | 282 |
| **10** | **1736** ≠ 0 ❌ |

→ $M_{11}$ ist **NICHT prim** (konsistent mit $2047 = 23 \cdot 89$).

> 💡 **GIMPS** (Great Internet Mersenne Prime Search) sucht weltweit verteilt nach Mersenne-Primzahlen. Im Oktober 2024 wurde die **52. Mersenne-Primzahl** $M_{136\,279\,841}$ gefunden – sie hat **41'024'320 Dezimalstellen**! *(Aufgabe 5)*

---

### 6. Wie viele Primzahlen gibt es?

### Satz 3: Es gibt unendlich viele Primzahlen (Euklid, ca. 300 v. Chr.)

**Beweis per Widerspruch** (berühmter antiker Beweis):

1. Angenommen, es gäbe nur endlich viele Primzahlen $p_1, p_2, \ldots, p_k$.
2. Konstruiere die Zahl $P = p_1 \cdot p_2 \cdot p_3 \cdots p_k + 1$
3. $P$ ist durch **keine** der Primzahlen $p_1, \ldots, p_k$ teilbar (Rest immer 1).
4. **Fakt:** Jede natürliche Zahl $n \geq 2$ hat eine Primzahl $p \leq n$ als Teiler.
5. Also muss $P$ einen Primteiler haben, der **nicht** in $\{p_1, \ldots, p_k\}$ ist.
6. **Widerspruch!** → Es gibt unendlich viele Primzahlen. ∎

### 📊 Graph: Die Primzahlfunktion π(n) = primes(n)

> **Erläuterung:** $\pi(n)$ (auch `primes(n)` geschrieben) zählt die Primzahlen $\leq n$. Carl Friedrich Gauss definierte diese rekursiv.

```python
def primes(n):
    if n == 1: return 0
    elif isPrime(n): return primes(n-1) + 1
    else: return primes(n-1)
```

**Graph 1: $\pi(n)$ vs. $n$ (links) und $\pi(n) / (n/\ln n)$ (rechts)**

```
 π(n)                                    π(n) / (n/ln n)
  ↑                                       ↑
400 ┤         .....                   2.0 ┤
    │      ..'''                          │
300 ┤   ..''                          1.5 ┤
    │ .'                                  │      ...''''''''''''''
200 ┤.'                                1.0 ┤─────'─────────────────
    │'                                    │
100 ┤                                 0.5 ┤
    │                                     │
  0 ┼──────┬──────┬──────┬───            0 ┼──────┬──────┬──────┬───
    0    500   1500   2500  n              0    500   1500   2500  n

LINKS: π(n) wächst ungefähr linear,     RECHTS: Das Verhältnis π(n)/(n/ln n)
       mit leicht abnehmender Steigung.         konvergiert gegen 1!
       Treppenstufen, weil π nur bei             → Primzahlsatz!
       jeder neuen Primzahl wächst.
```

### Primzahlsatz (Gauss/Legendre, bewiesen 1962 von Rosser & Schoenfeld)

> Für alle natürlichen Zahlen $n \geq 67$ gilt:
>
> $$\boxed{\frac{n}{\ln(n) - 0.5} < \pi(n) < \frac{n}{\ln(n) - 1.5}}$$
>
> Asymptotisch: $\pi(n) \sim \dfrac{n}{\ln(n)}$

**Anschauliche Interpretation:**
- Bei der Zahl $n$ ist "jede $\ln(n)$-te Zahl" ungefähr eine Primzahl
- Je grösser $n$, desto "dünner" werden die Primzahlen gestreut

---

### 7. Anwendungen des Primzahlsatzes

#### Aufgabe 7: Wie viele 10-stellige Primzahlen gibt es?

$$\pi(10^{10}) - \pi(10^9) \approx \frac{10^{10}}{\ln(10^{10})} - \frac{10^9}{\ln(10^9)}$$

$$= \frac{10^{10}}{10 \ln 10} - \frac{10^9}{9 \ln 10} = \frac{10^9}{\ln 10} \cdot \left(1 - \frac{1}{9}\right) \approx \boxed{386\,039\,539}$$

→ Rund **386 Millionen** 10-stellige Primzahlen!

#### Aufgabe 8: Wahrscheinlichkeit, dass eine zufällige 200-stellige ungerade Zahl prim ist

$$P(\text{prim}) = \frac{\text{Anzahl 200-stellige Primzahlen}}{\text{Anzahl 200-stellige ungerade Zahlen}} \approx \frac{10^{199} \cdot 0.0195}{0.5 \cdot 10^{199} \cdot 9} \approx \mathbf{0.43\%}$$

→ Ungefähr **0.5%** – das ist der Grund, warum man bei der RSA-Schlüsselgenerierung "nur" wenige tausend Zufallszahlen testen muss!

---

### 8. Sieb des Eratosthenes

> **Erläuterung:** Der älteste bekannte Primzahlfinder! Benannt nach **Eratosthenes von Kyrene** (ca. 276-194 v. Chr.).

### 📊 Graph: Sieb-Algorithmus visualisiert

**Beispiel für $n = 25$:**

```
Schritt 0 – Alle Zahlen von 2 bis 25:
 2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

Schritt 1: i = 2 (kleinste Primzahl)
           Streiche alle Vielfachen i·k mit k ≥ i:
           4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24
 2  3  ×  5  ×  7  ×  9  × 11  × 13  × 15  × 17  × 19  × 21  × 23  × 25

Schritt 2: i = 3
           Streiche: 9, 15, 21 (restliche noch nicht gestrichen)
 2  3  .  5  .  7  .  ×  . 11  . 13  .  ×  . 17  . 19  .  ×  . 23  . 25

Schritt 3: i = 4 ∉ primes (schon gestrichen) → skip

Schritt 4: i = 5
           Streiche: 25 (5·5)
 2  3  .  5  .  7  .  .  . 11  . 13  .  .  . 17  . 19  .  .  . 23  .  ×

Schritt 5: i = 6 > √25 = 5 → STOPP

╔══════════════════════════════════════════════════════════════╗
║ Primzahlen ≤ 25: {2, 3, 5, 7, 11, 13, 17, 19, 23}            ║
╚══════════════════════════════════════════════════════════════╝
```

**Python-Implementation:**
```python
import math
def eratosthenes(n):
    primes = [i for i in range(2, n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if i in primes:
            for k in range(n // i, i - 1, -1):
                if k in primes:
                    primes.remove(i * k)
    return primes
```

**Warum funktioniert das?** (Aufgabe 9)
- Jede zusammengesetzte Zahl $n$ hat einen Primteiler $p \leq \sqrt{n}$
- Also reicht es, nur bis $\sqrt{n}$ zu sieben
- Wegen Kommutativität $i \cdot k = k \cdot i$ brauchen wir nur $i \leq k$ zu betrachten → Start bei $i \cdot i$

---

### 9. Kleiner Satz von Fermat & Miller-Rabin-Test

### Satz (Kleiner Satz von Fermat)

> Wenn $p$ eine Primzahl ist, dann gilt für alle $a \in \{1, 2, \ldots, p-1\}$:
>
> $$\boxed{a^{p-1} \bmod p = 1}$$

**Beispiel für $p = 5$:**
$$1^4 = 1,\ 2^4 = 16 \equiv 1,\ 3^4 = 81 \equiv 1,\ 4^4 = 256 \equiv 1 \pmod 5 \; \checkmark$$

### Die Idee für einen Primzahltest

Wir wählen zufällig $a \in \{1, \ldots, n-1\}$ und berechnen $a^{n-1} \bmod n$:
- Wenn $a^{n-1} \bmod n \neq 1$ → $n$ ist **garantiert nicht prim**
- Wenn $a^{n-1} \bmod n = 1$ → $n$ **könnte** prim sein, aber…

### ⚠️ Das Problem: Pseudoprimzahlen

Für $n = 341 = 11 \cdot 31$ (zusammengesetzt!) gilt:

$$2^{340} \bmod 341 = 1$$

→ Der Fermat-Test mit $a = 2$ erkennt $341$ fälschlicherweise als prim!

Aber: $3^{340} \bmod 341 = 56 \neq 1$ → mit $a = 3$ wird $341$ korrekt als zusammengesetzt erkannt.

→ **Lösung:** Mehrere Basen $a$ testen! Das führt zum **Miller-Rabin-Test**.

### 📊 Graph: Ablauf des Miller-Rabin-Tests

```
┌─────────────────────────────────────────────────────┐
│               MILLER-RABIN-TEST                     │
│           Input: ungerade Zahl n > 2                │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
  ╔═══════════════════════════════════════════╗
  ║ Schritt 1: Schreibe n - 1 = 2^s · d        ║
  ║            (d ungerade)                    ║
  ║                                            ║
  ║ Beispiel n = 561:                          ║
  ║   n - 1 = 560 = 2^4 · 35                   ║
  ║   → s = 4, d = 35                          ║
  ╚═══════════════════════════════════════════╝
                         │
                         ▼
  ╔═══════════════════════════════════════════╗
  ║ Schritt 2: Wähle zufällig a ∈ {2,...,n-2}  ║
  ╚═══════════════════════════════════════════╝
                         │
                         ▼
        ┌────────────────────────────────┐
        │ Schritt 3: a^d mod n == 1 ?    │
        └────────────────────────────────┘
              │                      │
          JA  │                      │  NEIN
              ▼                      ▼
    ┌─────────────────┐   ┌──────────────────────────────┐
    │  "vermutlich     │  │ Schritt 4: Wiederhole für    │
    │   prim" ✓        │  │ r = 0 bis s-1:               │
    └─────────────────┘   │   a^(2^r · d) mod n == n-1 ?  │
                          └──────────────────────────────┘
                             │                      │
                         JA  │                      │  NEIN (alle r)
                             ▼                      ▼
                   ┌─────────────────┐   ┌──────────────────┐
                   │  "vermutlich    │   │  "zusammen-      │
                   │   prim" ✓       │   │   gesetzt" ✗     │
                   └─────────────────┘   └──────────────────┘
```

### Analyse des Miller-Rabin

| Antwort | Bedeutung | Sicherheit |
|---|---|---|
| "zusammengesetzt" | $n$ ist **garantiert** zusammengesetzt | 100% |
| "vermutlich prim" | $n$ ist prim **mit** Wahrscheinlichkeit $\geq 75\%$ | 25% Fehlerrate pro Test |

### 📊 Graph: Wie oft den Test wiederholen?

> Bei einer Pseudoprimzahl ist die Wahrscheinlichkeit, dass $k$ zufällige Basen alle fälschlicherweise "vermutlich prim" sagen, höchstens $(1/4)^k$:

```
Wahrscheinlichkeit, dass eine zusammengesetzte Zahl
als prim durchgeht – je nach Anzahl Wiederholungen k:

 P_falsch
    ↑
  100% ●  (k = 0)
       │
   25% ┤●  (k = 1) ← einmal testen: 25% Fehler!
       │
  6.25%┤ ●  (k = 2)
       │
  1.56%┤  ●  (k = 3)
       │
   0.4%┤   ●  (k = 4)
       │
 0.098%┤    ●  (k = 5) ← 99.9% sicher!
       │
       ┼───┬───┬───┬───┬───┬───┬───┬─→
       0   1   2   3   4   5   6   7   k

Für 99.9% Sicherheit: k = ⌈log_{1/4}(0.001)⌉ = ⌈4.98⌉ = 5 Wiederholungen
```

**Berechnung (Aufgabe 10c):**
$$(1/4)^k \leq 0.001 \iff k \geq \log_{1/4}(0.001) = \lceil 4.98 \rceil = \mathbf{5}$$

---

## 💻 Aufgaben-Zusammenfassung (Serie 9)

| Aufgabe | Thema | Kernkonzept |
|---|---|---|
| **1) *(opt.)*** | Ulam-Spirale zeichnen | Zahlen in Spiralform, Punktgrösse = Anzahl Teiler |
| **2)** | Drei Sorten Primzahlen | Alle ausser 2 haben $n \bmod 4 \in \{1, 3\}$ |
| **3)** | Primzahlzwillinge | Alle ausser (3,5) haben $a \bmod 6 = 5$ |
| **4)** | Mersenne im Binärsystem | $M_n = 2^n - 1$ → $n$ Einsen binär |
| **5)** | Ziffern von $M_{136\,279\,841}$ | $\log_{10}(2^{136\,279\,841}) \approx 41\,024\,320$ |
| **6)** | Lucas-Lehmer-Test | Für $M_7$ (prim) und $M_{11}$ (nicht prim) |
| **7)** | Anzahl 10-stellige Primzahlen | $\approx 386$ Millionen |
| **8)** | $P(\text{prim}) = ?$ für 200-stellige | $\approx 0.5\%$ |
| **9)** | Sieb des Eratosthenes | Prinzip, Abbruch bei $\sqrt{n}$ |
| **10)** | Miller-Rabin-Test | Für $n=15, 13, 2047$ |

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Prüfungsfragen

1. **«Ist $n$ prim?»** → Teiler zählen (genau 2 ⇒ prim)
2. **«Führe Lucas-Lehmer für $M_p$ durch.»** → Rekursiv $S(k+1) = S(k)^2 - 2 \bmod M_p$ bis $k = p-1$
3. **«Wie viele Primzahlen gibt es zwischen $a$ und $b$?»** → $\pi(b) - \pi(a) \approx \frac{b}{\ln b} - \frac{a}{\ln a}$
4. **«Führe Miller-Rabin für $n$ aus.»** → $n-1 = 2^s \cdot d$, dann Bedingungen prüfen
5. **«Wie oft Miller-Rabin wiederholen für Sicherheit $1-p$?»** → $k = \lceil \log_{1/4}(p) \rceil$

### Häufige Fehler

| Fehler | Korrektur |
|---|---|
| $1$ als Primzahl zählen | 1 ist **weder** prim noch zusammengesetzt (nur 1 Teiler, braucht 2!) |
| Mersenne-Primalität falsch schliessen | $n$ prim $\Rightarrow$ $M_n$ prim – **FALSCH!** Nur die Umkehrung gilt |
| Sieb des Eratosthenes zu weit laufen lassen | Abbruch bei $i > \sqrt{n}$ – alles danach wäre unnötig |
| Fermat-Test als deterministisch benutzen | Pseudoprimzahlen existieren (z.B. $341$)! → Miller-Rabin nutzen |
| "vermutlich prim" als "prim" interpretieren | Miller-Rabin ist probabilistisch! Wiederholen für höhere Sicherheit |
| Euklid-Beweis ohne "+1" schreiben | $P = p_1 \cdots p_k + 1$ ist **nicht** durch die $p_i$ teilbar (Rest immer 1) |

---

## 🔗 Verbindung zu anderen Wochen

| Woche | Thema | Verbindung zu SW 09 |
|---|---|---|
| **SW 07** | Matrizenalgebra | Mersenne-Zahlen als $2^n - 1$ entstehen aus Binärzahlen-Matrizen |
| **SW 08** | Modulare Arithmetik | **Direkte Grundlage!** Fermat-Eigenschaft, Lucas-Lehmer, Miller-Rabin sind alle modular |
| **SW 10** | **Euklids Algorithmus** | Primzahlen sind die "Atome" der Primfaktorzerlegung, die wir in SW 10 für den ggT nutzen |
| *(Ausblick SW 11)* | Chinesischer Restsatz | Funktioniert elegant, wenn die Moduli **paarweise teilerfremd** sind – Primzahlen sind das extrem |
| *(Ausblick SW 12)* | Endliche Gruppen | $(\mathbb{Z}_p^*, \cdot)$ ist eine zyklische Gruppe der Ordnung $p - 1$ |
| *(Ausblick SW 13)* | Endliche Körper | $\mathbb{Z}_p$ ist **genau dann** ein Körper, wenn $p$ eine **Primzahl** ist |

---

## 🧠 Das grosse Bild

```
                      ┌─────────────────────────┐
                      │  PRIMZAHLEN sind die    │
                      │  "Atome" der Zahlen     │
                      └───────────┬─────────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
          ┌─────▼─────┐    ┌─────▼──────┐    ┌────▼─────┐
          │ Verteilung│    │   Tests    │    │ Spezielle│
          │   (Wie    │    │ (Ist n     │    │ Formen   │
          │   viele?) │    │  prim?)    │    │          │
          └───────────┘    └────────────┘    └──────────┘
                │                 │                 │
           Primzahlsatz      Eratosthenes       Mersenne
           π(n) ~ n/ln n     Miller-Rabin      Mₙ = 2ⁿ - 1
           Euklid: ∞         Lucas-Lehmer      Goldbach
           viele             Fermat            Zwillinge
                │                 │                 │
                └─────────────────┼─────────────────┘
                                  │
                                  ▼
                      ┌─────────────────────────┐
                      │   ANWENDUNG:            │
                      │   Kryptographie (RSA),  │
                      │   Hashing, Zufallszahlen│
                      └─────────────────────────┘
```

---

## 🧠 Kompakte Merksätze

- **Prim = genau 2 Teiler.** Nicht 1 Teiler (das wäre 1), nicht 3+ (das wäre zusammengesetzt).
- **Es gibt unendlich viele Primzahlen.** (Euklid, via $P = p_1 \cdots p_k + 1$)
- **Mersenne-Primzahl $M_n$ erfordert $n$ prim** – aber nicht jede prime $n$ gibt eine!
- **$\pi(n) \sim n/\ln(n)$** – je grösser, desto dünner streuen sich die Primzahlen.
- **Eratosthenes läuft nur bis $\sqrt{n}$** – das reicht für alle zusammengesetzten Zahlen.
- **Fermat-Test ist probabilistisch** – Pseudoprimzahlen existieren. Miller-Rabin ist besser.
- **Miller-Rabin mit 5 Runden** gibt 99.9% Sicherheit.
- **Lucas-Lehmer ist deterministisch** – aber nur für Mersenne-Zahlen.
