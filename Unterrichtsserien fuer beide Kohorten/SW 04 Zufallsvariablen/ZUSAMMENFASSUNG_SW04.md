# DMATH.CODE – SW 04: Zufallsvariablen

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Semesterwoche:** SW 04
> **Thema:** Zufallsvariablen & Diskrete Wahrscheinlichkeitsverteilungen
> **Dozent:** Dr. Reto Berger · HSLU · Frühlingssemester 25

---

## 🎯 Lernziele

1. **Wissen**, was eine Zufallsvariable ist, und können mit der Wahrscheinlichkeitsverteilung Wahrscheinlichkeiten berechnen.
2. **Verstehen**, was der Erwartungswert einer Zufallsvariablen ist, und können ihn berechnen.
3. **Kennen** wichtige diskrete Wahrscheinlichkeitsverteilungen:
   - Bernoulli-Verteilung
   - Binomialverteilung
   - Geometrische Verteilung
   - Hypergeometrische Verteilung
   - Poissonverteilung

---

## 📖 Wichtigste Begriffe

| Begriff                                 | Definition                                                                                                                       |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Zufallsvariable** $X$         | Funktion$X: \Omega \to \mathbb{R}$, die jedem Ergebnis eines Zufallsexperiments eine reelle Zahl zuordnet                      |
| **Wertemenge** $\mathbf{W}_X$   | Menge aller möglichen Werte:$\mathbf{W}_X = \{X(\omega) : \omega \in \Omega\} = \{x_1, x_2, \ldots, x_k\} \subset \mathbb{R}$ |
| **Realisierung**                  | Für$x \in \mathbf{W}_X$ ist das Ereignis $\{X = x\} = \{\omega : X(\omega) = x\} \subset \Omega$ die Realisierung von $x$ |
| **Wahrscheinlichkeitsverteilung** | Tabelle aller Realisierungen mit ihren Wahrscheinlichkeiten$(ProbabilityUnterDerBedinung) P(X = x_i)$                          |
| **Erwartungswert** $E(X)$       | Mittlerer Wert (gewichtetes Mittel):$E(X) = \sum_{i} x_i \cdot P(X = x_i)$                                                     |
| **Bernoulli-Verteilung**          | Spezialfall der Binomialverteilung mit$n = 1$ (ein einziger Versuch)                                                           |
| **Binomialverteilung**            | Anzahl Erfolge bei$n$ unabhängigen Versuchen mit Erfolgswahrscheinlichkeit $p$                                              |
| **Geometrische Verteilung**       | Anzahl Misserfolge vor dem ersten Erfolg                                                                                         |
| **Hypergeometrische Verteilung**  | Ziehen ohne Zurücklegen aus endlicher Population                                                                                |
| **Poissonverteilung**             | Anzahl seltener Ereignisse in festem Zeitintervall/Bereich                                                                       |

---

## 📐 Definitionen, Sätze & Beweise

### Definition 1: Zufallsvariable

> Sei $\Omega = \{\omega_1, \omega_2, \ldots, \omega_n\}$ die Ergebnismenge eines Zufallsexperiments und $P$ eine Wahrscheinlichkeitsfunktion.

- Eine Funktion $X : \Omega \longrightarrow \mathbb{R}$ heisst **Zufallsvariable**.
- $\mathbf{W}_X = \{X(\omega) : \omega \in \Omega\} = \{x_1, x_2, \ldots, x_k\} \subset \mathbb{R}$ heisst **Wertemenge**. k, da ohne Dublikaten
- Für alle $x \in \mathbf{W}_X$ heisst $\{X = x\} = \{\omega : X(\omega) = x\} \subset \Omega$ die **Realisierung** von $x$. Gross X ist die Funktion, klein x ist der Wert der Funktion
- Die Auflistung aller Wahrscheinlichkeiten $P(X = x_i)$ heisst **Wahrscheinlichkeitsverteilung** von $X$.

**💡 Intuition:** Eine Zufallsvariable ist **keine Variable**, sondern eine **Funktion**, die jedem Ergebnis eines Zufallsexperiments eine Zahl zuordnet. Beispiel: Beim dreimaligen Münzwurf ordnet $X_1$ jedem Ergebnis die **Anzahl Köpfe** zu.

**📌 Beispiel (Münzwurf):**

| $\omega$                         | KKK | KKZ | KZK | KZZ | ZKK | ZKZ | ZZK | ZZZ |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| $X_1(\omega)$ (Anzahl Kopf)      | 3   | 2   | 2   | 1   | 2   | 1   | 1   | 0   |
| $X_2(\omega)$ (Köpfe am Anfang) | 3   | 2   | 1   | 1   | 0   | 0   | 0   | 0   |

Daraus folgt die Wahrscheinlichkeitsverteilung:

| $x$          | 0               | 1               | 2               | 3               |
| -------------- | --------------- | --------------- | --------------- | --------------- |
| $P(X_1 = x)$ | $\frac{1}{8}$ | $\frac{3}{8}$ | $\frac{3}{8}$ | $\frac{1}{8}$ |
| $P(X_2 = x)$ | $\frac{1}{2}$ | $\frac{1}{4}$ | $\frac{1}{8}$ | $\frac{1}{8}$ |

---

### Definition 2: Erwartungswert

> Sei $\Omega = \{\omega_1, \omega_2, \ldots\}$ die Ergebnismenge, $P$ eine Wahrscheinlichkeitsfunktion und $X : \Omega \longrightarrow \{x_1, x_2, \ldots\}$ eine Zufallsvariable. Der **Erwartungswert** $E(X)$ ist der mittlere Wert von $X$:

$$
E(X) = X(\omega_1) \cdot P(\omega_1) + X(\omega_2) \cdot P(\omega_2) + \ldots
$$

oder gleichwertig:

$$
E(X) = x_1 \cdot P(X = x_1) + x_2 \cdot P(X = x_2) + \ldots = \sum_i x_i \cdot P(X = x_i)
$$

**💡 Intuition:** Der Erwartungswert ist das **gewichtete Mittel** aller möglichen Werte, wobei jeder Wert mit seiner Eintretenswahrscheinlichkeit gewichtet wird. Man kann ihn als den "durchschnittlichen" Ausgang bei vielen Wiederholungen des Experiments verstehen.

**📌 Beispiel:** Für die Münzwurf-Zufallsvariable $X_1$ (Anzahl Kopf bei 3 Würfen):

$$
E(X_1) = 0 \cdot \frac{1}{8} + 1 \cdot \frac{3}{8} + 2 \cdot \frac{3}{8} + 3 \cdot \frac{1}{8} = \frac{12}{8} = 1.5
$$

---

### Satz 1: Linearität des Erwartungswerts

> Für die **Summe** zweier Zufallsvariablen $X$ und $Y$ gilt:

$$
E(X + Y) = E(X) + E(Y)
$$

**💡 Intuition:** Der Erwartungswert ist **additiv** – egal ob die Zufallsvariablen unabhängig sind oder nicht! Dies ist eine extrem nützliche Eigenschaft.

**📌 Beweisskizze:** Folgt direkt aus der Linearität der Summation und den Eigenschaften der Wahrscheinlichkeit.

**📌 Beispiel (Augensumme bei $n$ Würfeln):**

- Für einen Würfel: $E(X_i) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6} = 3.5$
- Augensumme: $X = X_1 + X_2 + \ldots + X_n$
- $E(X) = E(X_1) + E(X_2) + \ldots + E(X_n) = 3.5n$

---

### Definition 3: Bernoulli- & Binomialverteilung

> Sei $X$ die Anzahl 1-Bit, die ein Zufallsgenerator $G$ zurückgibt, wenn mit ihm $n$ Bits erzeugt werden. Die Wahrscheinlichkeitsverteilung von $X$ heisst:
>
> - **Bernoulli-Verteilung** mit Parameter $p$ für $n = 1$
> - **Binomialverteilung** mit Parameter $p$ und $n > 1$

**Formel der Binomialverteilung:**

$$
P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}, \quad k = 0, 1, \ldots, n
$$

**Erwartungswert:**

$$
E(X) = n \cdot p
$$

**💡 Intuition:** $X$ zählt, wie oft ein Ereignis mit Wahrscheinlichkeit $p$ bei $n$ **unabhängigen** Versuchen eintritt. Jeder Versuch ist wie ein Münzwurf (Erfolg/Misserfolg).

**📌 Herleitung von $E(X) = np$:** Jedes Bit $X_i$ ist Bernoulli-verteilt mit $E(X_i) = p$. Da $X = X_1 + X_2 + \ldots + X_n$, folgt mit Satz 1: $E(X) = np$.

**📌 Beispiel (Spam-Filter, Aufgabe 5):**

- Spam-Erkennungsrate $p = 0.8$, $n = 10$ E-Mails
- a) $P(X = 8) = \binom{10}{8} \cdot 0.8^8 \cdot 0.2^2 \approx 30.2\%$
- b) $P(X \geq 9) = \binom{10}{9} \cdot 0.8^9 \cdot 0.2^1 + 0.8^{10} \approx 37.6\%$
- c) $E(X) = 10 \cdot 0.8 = 8$ E-Mails

**📌 Beispiel (Brute-Force-Angriff, Aufgabe 8):**

- $p = 0.0001$, $n = 10000$ Versuche
- a) $P(X = 2) = \binom{10000}{2} \cdot 0.0001^2 \cdot 0.9999^{9998} \approx 18.4\%$
- b) $P(X \geq 1) = 1 - P(X = 0) = 1 - 0.9999^{10000} \approx 63.2\%$
- c) $E(X) = 10000 \cdot 0.0001 = 1$

---

### Definition 4: Geometrische Verteilung

> Sei $X$ die Anzahl 0-Bit, die ein Zufallsgenerator $G$ erzeugt, bis er zum ersten Mal ein 1-Bit zurückgibt. Die Wahrscheinlichkeitsverteilung von $X$ heisst:
>
> - **Geometrische Verteilung** mit Parameter $p$.

**Formel:**

$$
P(X = k) = (1-p)^k \cdot p, \quad k = 0, 1, 2, \ldots
$$

**Erwartungswert:**

$$
E(X) = \frac{1-p}{p}
$$

> ⚠️ **Achtung:** $X$ zählt die Anzahl **Misserfolge vor** dem ersten Erfolg. Wenn man die Anzahl **Versuche bis inkl. erstem Erfolg** will, ist das $X + 1$ mit Erwartungswert $E(X) + 1 = \frac{1}{p}$.

**💡 Intuition:** Man „wartet" auf den ersten Erfolg. $X$ ist die Wartezeit (in Misserfolgen gemessen). Die Verteilung ist **gedächtnislos**: Egal wie lange man schon gewartet hat, die Chancen auf Erfolg beim nächsten Versuch bleiben gleich.

**📌 Herleitung von $E(X) = \frac{1-p}{p}$:** (Rekursiver Trick)

$$
E(X) = p \cdot 0 + (1-p) \cdot [1 + E(X)]
$$

$$
E(X) = 0 + 1 + E(X) - p - p \cdot E(X)
$$

$$
p \cdot E(X) = 1 - p
$$

$$
E(X) = \frac{1-p}{p}
$$

**📌 Beispiel (Passwort-Eingabe, Aufgabe 11):**

- $p = 0.02$ (Erfolgswahrscheinlichkeit)
- a) Erst beim 5. Versuch: $P(X = 4) = 0.98^4 \cdot 0.02 \approx 1.85\%$
- b) Durchschnittliche Versuche: $E(X) + 1 = \frac{0.98}{0.02} + 1 = 50$

**📌 Beispiel (Router-Paket, Aufgabe 10):**

- Fehlerwahrscheinlichkeit $0.1$, also Erfolg $p = 0.9$
- a) Erstes fehlerfreies Paket beim 3. Versuch: $P(X = 2) = 0.1^2 \cdot 0.9 = 0.9\%$
- b) Durchschnittliche Versuche: $E(X) + 1 = \frac{0.1}{0.9} + 1 \approx 1.11$

---

### Definition 5: Hypergeometrische Verteilung

> Ein Zufallsgenerator $G$ gibt uniform zufällig $n$ Bits aus einer Liste mit insgesamt $M$ 0-Bits und $N$ 1-Bits zurück (alle Bits können nur **einmal** gewählt werden!). Sei $X$ die Anzahl 1-Bit. Die Wahrscheinlichkeitsverteilung von $X$ heisst:
>
> - **Hypergeometrische Verteilung** mit Parameter $n$, $M$ und $N$.

**Formel:**

$$
P(X = x) = \frac{\binom{M}{x} \cdot \binom{N}{n-x}}{\binom{M+N}{n}}
$$

**Erwartungswert:**

$$
E(X) = n \cdot \frac{M}{M + N}
$$

**💡 Intuition:** Man zieht $n$ Elemente **ohne Zurücklegen** aus einer Population mit $M$ "Erfolgen" und $N$ "Misserfolgen". Im Gegensatz zur Binomialverteilung sind die Ziehungen **nicht unabhängig**.

**📌 Herleitung von $E(X)$:** Sei $X_i$ der Indikator für das $i$-te Bit. Dann:

$$
P(X_i = 1) = \frac{M}{M+N}
$$

$$
E(X_i) = 0 \cdot P(X_i = 0) + 1 \cdot P(X_i = 1) = \frac{M}{M+N}
$$

$$
E(X) = E(X_1) + E(X_2) + \ldots + E(X_n) = n \cdot \frac{M}{M+N}
$$

**📌 Beispiel (Speicherzellen, Aufgabe 16):**

- 5000 Zellen, davon 200 fehlerhaft → $M = 200$, $N = 4800$, $n = 50$
- a) $P(X = 5) = \frac{\binom{200}{5} \cdot \binom{4800}{45}}{\binom{5000}{50}} \approx 3.4\%$
- b) $P(X = 0) = \frac{\binom{200}{0} \cdot \binom{4800}{50}}{\binom{5000}{50}} \approx 12.9\%$

**📌 Beispiel (Codezeilen, Aufgabe 15):**

- 1000 Zeilen, 50 fehlerhaft → $M = 50$, $N = 950$, $n = 20$
- a) $P(X = 3) = \frac{\binom{50}{3} \cdot \binom{950}{17}}{\binom{1000}{20}} \approx 5.3\%$
- b) $P(X \geq 1) = 1 - P(X = 0) = 1 - \frac{\binom{50}{0} \cdot \binom{950}{20}}{\binom{1000}{20}} \approx 64.5\%$

---

### Definition 6: Poissonverteilung

> Ein Zufallsgenerator $G$ gibt in einer fest bestimmten Zeit oder einer fest gegebenen Anzahl Bits im Mittel immer mit **konstanter Rate $\mu$** 1-Bit zurück, die Wahrscheinlichkeit eines einzelnen Bit 1 ist aber relativ klein. Sei $X$ die Anzahl 1-Bit. Die Wahrscheinlichkeitsverteilung von $X$ heisst:
>
> - **Poissonverteilung** mit Parameter $\mu$.

**Formel:**

$$
P(X = x) = \frac{\mu^x}{x!} \cdot e^{-\mu}
$$

**📌 Herleitung (Grenzwert der Binomialverteilung):**

$$
P(X = x) = \binom{n}{x}\left(\frac{\mu}{n}\right)^x \left(1 - \frac{\mu}{n}\right)^{n-x}
$$

Für $n \to \infty$: Die Terme $\frac{n}{n-\mu} \cdot \frac{n-1}{n-\mu} \cdots \to 1$ und $\left(1 - \frac{\mu}{n}\right)^n \to e^{-\mu}$, also:

$$
P(X = x) \to \frac{\mu^x}{x!} e^{-\mu}
$$

### Satz 2: Erwartungswert der Poissonverteilung

> Hat eine Zufallsvariable $X$ eine **Poissonverteilung** mit Parameter $\mu$, dann gilt:

$$
E(X) = \mu
$$

**💡 Intuition:** Die Poissonverteilung modelliert **seltene, zufällige Ereignisse** in einem festen Zeitraum oder Bereich. Der Parameter $\mu$ ist gleichzeitig Erwartungswert und Rate.

**📌 Wann Poisson verwenden?**

- Seltene Ereignisse (kleine Einzelwahrscheinlichkeit)
- Zufällig und unabhängig voneinander
- Über einen festen Zeitraum/Bereich gezählt
- Konstante Rate

**📌 Beispiel (Webserver-Anfragen, Aufgabe 19):**

- $\mu = 5$ Anfragen pro Sekunde
- a) $P(X = 7) = \frac{5^7}{7!} \cdot e^{-5} \approx 10.4\%$
- b) $P(X \leq 3) = \sum_{i=0}^{3} \frac{5^i}{i!} \cdot e^{-5} \approx 26.5\%$

**📌 Beispiel (Prozessor-Fehler, Aufgabe 20):**

- $\mu = 2$ Fehler pro Tag
- a) $P(X = 0) = \frac{2^0}{0!} \cdot e^{-2} \approx 13.5\%$
- b) $P(X > 3) = 1 - P(X \leq 3) = 1 - \sum_{i=0}^{3} \frac{2^i}{i!} \cdot e^{-2} \approx 14.3\%$

**📌 Beispiel (DDoS-Angriffe, Aufgabe 22):**

- $\mu = 3$ Angriffe/Monat
- a) $P(X = 5) = \frac{3^5}{5!} \cdot e^{-3} \approx 10.1\%$
- b) Zwei Monate → $\mu_{\text{neu}} = 6$: $P(X \leq 4) = \sum_{i=0}^{4} \frac{6^i}{i!} \cdot e^{-6} \approx 28.5\%$

---

## 📊 Formelsammlung

### Übersichtstabelle aller Verteilungen

| Verteilung                 | Parameter   | $P(X = k)$                                          | $E(X)$           | Voraussetzung                                     |
| -------------------------- | ----------- | ----------------------------------------------------- | ------------------ | ------------------------------------------------- |
| **Bernoulli**        | $p$       | $p^k (1-p)^{1-k}$ für $k \in \{0,1\}$            | $p$              | 1 Versuch, Erfolg/Misserfolg                      |
| **Binomial**         | $n, p$    | $\binom{n}{k} p^k (1-p)^{n-k}$                      | $np$             | $n$ unabh. Versuche, **mit** Zurücklegen |
| **Geometrisch**      | $p$       | $(1-p)^k \cdot p$                                   | $\frac{1-p}{p}$  | Warten auf ersten Erfolg                          |
| **Hypergeometrisch** | $n, M, N$ | $\frac{\binom{M}{k}\binom{N}{n-k}}{\binom{M+N}{n}}$ | $\frac{nM}{M+N}$ | $n$ Ziehungen **ohne** Zurücklegen       |
| **Poisson**          | $\mu$     | $\frac{\mu^k}{k!} e^{-\mu}$                         | $\mu$            | Seltene Ereignisse, festes Intervall              |

### Wichtige Rechenregeln

| Situation                       | Formel                                                           |
| ------------------------------- | ---------------------------------------------------------------- |
| Erwartungswert der Summe        | $E(X + Y) = E(X) + E(Y)$                                       |
| Gegenwahrscheinlichkeit         | $P(X \geq 1) = 1 - P(X = 0)$                                   |
| Mindestens$k$                 | $P(X \geq k) = 1 - P(X < k) = 1 - \sum_{i=0}^{k-1} P(X = i)$   |
| Poisson-Zeitintervall skalieren | Neues Intervall →$\mu_{\text{neu}} = \mu \cdot \text{Faktor}$ |
| Geom. Versuche bis Erfolg       | $E(\text{Versuche}) = E(X) + 1 = \frac{1}{p}$                  |

---

## 🔄 Vergleichstabelle: Binomial vs. Hypergeometrisch

| Eigenschaft                  | Binomialverteilung                 | Hypergeometrische Verteilung              |
| ---------------------------- | ---------------------------------- | ----------------------------------------- |
| **Ziehen**             | **Mit** Zurücklegen         | **Ohne** Zurücklegen               |
| **Unabhängigkeit**    | Versuche sind**unabhängig** | Versuche sind**abhängig**          |
| **Population**         | Unbeschränkt / gross              | Endlich, bekannte Grösse                 |
| **Parameter**          | $n, p$                           | $n, M, N$                               |
| **Typisches Szenario** | Spam-Erkennung, Brute-Force        | Stichprobe aus Datenbank, Speichertest    |
| **Approximation**      | –                                 | $\approx$ Binomial wenn $M + N \gg n$ |

---

## 🔄 Vergleichstabelle: Binomial vs. Poisson

| Eigenschaft                        | Binomialverteilung                   | Poissonverteilung                 |
| ---------------------------------- | ------------------------------------ | --------------------------------- |
| **Anzahl Versuche**          | Fest, bekannt ($n$)                | Nicht direkt gegeben              |
| **Einzelwahrscheinlichkeit** | Bekannt ($p$)                      | Sehr klein                        |
| **Modelliert**               | Anzahl Erfolge bei$n$ Versuchen    | Anzahl Ereignisse pro Zeiteinheit |
| **Approximation**            | Poisson wenn$n$ gross, $p$ klein | Grenzfall der Binomialvert.       |
| **Typisches Szenario**       | Paketübertragung, Server-Ausfall    | Webserver-Anfragen, DDoS, Defekte |

---

## 💻 Code-Beispiele (Python)

### Binomialverteilung

```python
from math import comb, factorial
import math

# === Binomialverteilung ===
def binom_pmf(n, p, k):
    """P(X = k) für Binomialverteilung"""
    return comb(n, k) * p**k * (1 - p)**(n - k)

def binom_erwartungswert(n, p):
    """E(X) = n * p"""
    return n * p

# Beispiel: Spam-Filter (Aufgabe 5)
n, p = 10, 0.8
print(f"P(X=8) = {binom_pmf(n, p, 8):.4f}")          # ≈ 0.3020
print(f"P(X≥9) = {binom_pmf(n, p, 9) + binom_pmf(n, p, 10):.4f}")  # ≈ 0.3758
print(f"E(X) = {binom_erwartungswert(n, p)}")          # = 8.0
```

### Geometrische Verteilung

```python
# === Geometrische Verteilung ===
def geom_pmf(p, k):
    """P(X = k) – Anzahl Misserfolge vor erstem Erfolg"""
    return (1 - p)**k * p

def geom_erwartungswert(p):
    """E(X) = (1-p)/p, E(Versuche) = 1/p"""
    return (1 - p) / p

# Beispiel: Passwort-Eingabe (Aufgabe 11)
p = 0.02
print(f"P(X=4) = {geom_pmf(p, 4):.4f}")              # ≈ 0.0185
print(f"E(Versuche) = {geom_erwartungswert(p) + 1}")   # = 50
```

### Hypergeometrische Verteilung

```python
# === Hypergeometrische Verteilung ===
def hypergeom_pmf(M, N, n, x):
    """P(X = x): M=Erfolge, N=Misserfolge, n=Ziehungen"""
    return comb(M, x) * comb(N, n - x) / comb(M + N, n)

def hypergeom_erwartungswert(M, N, n):
    """E(X) = n * M / (M + N)"""
    return n * M / (M + N)

# Beispiel: Codezeilen (Aufgabe 15)
M, N, n = 50, 950, 20
print(f"P(X=3) = {hypergeom_pmf(M, N, n, 3):.4f}")   # ≈ 0.0530
print(f"P(X≥1) = {1 - hypergeom_pmf(M, N, n, 0):.4f}") # ≈ 0.6450
```

### Poissonverteilung

```python
# === Poissonverteilung ===
def poisson_pmf(mu, x):
    """P(X = x) = mu^x / x! * e^(-mu)"""
    return mu**x / factorial(x) * math.exp(-mu)

def poisson_erwartungswert(mu):
    """E(X) = mu"""
    return mu

# Beispiel: Webserver (Aufgabe 19)
mu = 5
print(f"P(X=7) = {poisson_pmf(mu, 7):.4f}")           # ≈ 0.1044
print(f"P(X≤3) = {sum(poisson_pmf(mu, i) for i in range(4)):.4f}")  # ≈ 0.2650

# Beispiel: DDoS (Aufgabe 22) – Zeitintervall skalieren
mu_1_monat = 3
mu_2_monate = 6  # Poisson skaliert linear!
print(f"P(X≤4, 2 Monate) = {sum(poisson_pmf(mu_2_monate, i) for i in range(5)):.4f}")  # ≈ 0.2851
```

---

## 📝 Übungsaufgaben – Zusammenfassung & Lösungswege

### Aufgabe 1: Zufallsvariablen bestimmen

**Typ:** Wahrscheinlichkeitsverteilung aufstellen
**Kontext:** Wörter $\Omega = \{\text{Now, is, the, winter, of, our, discontent}\}$, $P$ proportional zur Buchstabenzahl
**Lösung:** Gesamtlänge = 23, daher $P(\omega) = \frac{\text{Länge}(\omega)}{23}$

| $x$          | 2                | 3                | 6                | 10                |
| -------------- | ---------------- | ---------------- | ---------------- | ----------------- |
| $P(X_1 = x)$ | $\frac{4}{23}$ | $\frac{3}{23}$ | $\frac{6}{23}$ | $\frac{10}{23}$ |

### Aufgaben 2–3: Erwartungswert berechnen

**Typ:** $E(X)$ mit Linearität

- $E(X_2) = 1 \cdot \frac{10}{23} + 2 \cdot \frac{3}{23} + 3 \cdot \frac{10}{23} = \frac{58}{23} \approx 2.52$ (Vokale)
- Augensumme $n$ Würfel: $E(X) = 3.5n$

### Aufgaben 4–8: Binomialverteilung

**Lösungsmuster:**

1. Parameter identifizieren: $n$ (Versuche), $p$ (Erfolgswahrscheinlichkeit)
2. Formel anwenden: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
3. Bei "mindestens": Gegenwahrscheinlichkeit nutzen

| Aufgabe | Kontext         | $n$ | $p$  | Zentrale Ergebnisse                     |
| ------- | --------------- | ----- | ------ | --------------------------------------- |
| 5       | Spam-Filter     | 10    | 0.8    | $P(X=8) \approx 30.2\%$, $E(X)=8$   |
| 6       | Server-Ausfall  | 50    | 0.02   | $P(X=2) \approx 18.6\%$, $E(X)=1$   |
| 7       | Netzwerk-Pakete | 20    | 0.95   | $P(X=18) \approx 18.9\%$, $E(X)=19$ |
| 8       | Brute-Force     | 10000 | 0.0001 | $P(X=2) \approx 18.4\%$, $E(X)=1$   |

### Aufgaben 9–13: Geometrische Verteilung

**Lösungsmuster:**

1. $p$ = Erfolgswahrscheinlichkeit bestimmen
2. $P(X = k) = (1-p)^k \cdot p$ (Misserfolge vor erstem Erfolg)
3. Durchschnittliche Versuche: $\frac{1}{p}$

| Aufgabe | Kontext          | $p$ | Zentrale Ergebnisse                                    |
| ------- | ---------------- | ----- | ------------------------------------------------------ |
| 10      | Router-Paket     | 0.9   | $P(X=2) = 0.9\%$, Ø $\approx 1.11$ Versuche       |
| 11      | Passwort         | 0.02  | $P(X=4) \approx 1.85\%$, Ø = 50 Versuche            |
| 12      | Bug-Fix          | 0.3   | $P(X=4) \approx 7.2\%$, Ø $\approx 3.33$ Versuche |
| 13      | Penetrationstest | 0.05  | $P(X=6) \approx 3.7\%$, Ø = 20 Tests                |

### Aufgaben 14–18: Hypergeometrische Verteilung

**Lösungsmuster:**

1. Population aufteilen: $M$ (Erfolge), $N$ (Misserfolge), $n$ (Stichprobe)
2. $P(X = x) = \frac{\binom{M}{x}\binom{N}{n-x}}{\binom{M+N}{n}}$

| Aufgabe | Kontext        | $M$ | $N$ | $n$ | Zentrale Ergebnisse                                        |
| ------- | -------------- | ----- | ----- | ----- | ---------------------------------------------------------- |
| 15      | Codezeilen     | 50    | 950   | 20    | $P(X=3) \approx 5.3\%$, $P(X \geq 1) \approx 64.5\%$   |
| 16      | Speicherzellen | 200   | 4800  | 50    | $P(X=5) \approx 3.4\%$, $P(X=0) \approx 12.9\%$        |
| 17      | Passwort-DB    | 500   | 9500  | 100   | $P(X \geq 10) \approx 2.8\%$, $P(X=5) \approx 18.1\%$  |
| 18      | Testfälle     | 100   | 400   | 50    | $P(X \geq 20) \approx 0.05\%$, $P(X=15) \approx 2.7\%$ |

### Aufgaben 19–22: Poissonverteilung

**Lösungsmuster:**

1. Rate $\mu$ bestimmen (Erwartungswert pro Zeiteinheit)
2. $P(X = x) = \frac{\mu^x}{x!} e^{-\mu}$
3. Bei anderem Zeitintervall: $\mu$ skalieren!

| Aufgabe | Kontext       | $\mu$ | Zentrale Ergebnisse                                                 |
| ------- | ------------- | ------- | ------------------------------------------------------------------- |
| 19      | Webserver     | 5/s     | $P(X=7) \approx 10.4\%$, $P(X \leq 3) \approx 26.5\%$           |
| 20      | Prozessor     | 2/Tag   | $P(X=0) \approx 13.5\%$, $P(X > 3) \approx 14.3\%$              |
| 21      | Router-Pakete | 1.5/h   | $P(X=2) \approx 25.1\%$, $P(X=0) \approx 22.3\%$                |
| 22      | DDoS          | 3/Monat | $P(X=5) \approx 10.1\%$, 2 Monate: $P(X \leq 4) \approx 28.5\%$ |

---

## 🎯 Prüfungsrelevante Hinweise

### ⚡ Typische Prüfungsfragen

1. **Verteilung erkennen:** Aus einem Textproblem die richtige Verteilung identifizieren
2. **Wahrscheinlichkeit berechnen:** $P(X = k)$, $P(X \geq k)$, $P(X \leq k)$
3. **Erwartungswert berechnen:** $E(X)$ mit der passenden Formel
4. **Linearität des Erwartungswerts** anwenden (Aufgaben 2, 3)

### 🔑 Entscheidungsbaum: Welche Verteilung?

```
Frage: Was wird modelliert?
│
├── Feste Anzahl n Versuche?
│   ├── JA → Ziehen MIT Zurücklegen / unabhängig?
│   │   ├── JA → BINOMIALVERTEILUNG (n, p)
│   │   │   └── n = 1 → BERNOULLI (p)
│   │   └── NEIN → Ziehen OHNE Zurücklegen?
│   │       └── JA → HYPERGEOMETRISCHE VERTEILUNG (n, M, N)
│   └── NEIN → Warten auf ersten Erfolg?
│       └── JA → GEOMETRISCHE VERTEILUNG (p)
│
└── Seltene Ereignisse pro Zeiteinheit?
    └── JA → POISSONVERTEILUNG (µ)
```

### ⚠️ Häufige Fehler

1. **Binomial vs. Hypergeometrisch verwechselt:** → Frage: Wird zurückgelegt? Population endlich?
2. **Geometrische Verteilung: Misserfolge vs. Versuche:** → $X$ = Misserfolge, Versuche = $X + 1$
3. **Poisson: Zeitintervall nicht skaliert:** → Bei doppeltem Intervall: $\mu_{\text{neu}} = 2\mu$
4. **"Mindestens 1" nicht mit Gegenereignis gelöst:** → $P(X \geq 1) = 1 - P(X = 0)$

---

## 🔗 Verbindung zu anderen Wochen

| Woche            | Thema                       | Verbindung zu SW 04                                                                                                       |
| ---------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **SW 01**  | Wahrscheinlichkeit          | Grundlagen: Ergebnismenge$\Omega$, Wahrscheinlichkeitsfunktion $P$, Laplace-Experiment → Basis für Zufallsvariablen |
| **SW 02**  | Bedingte Wahrscheinlichkeit | Unabhängigkeit von Ereignissen → zentral für Binomial- & Geometrische Verteilung (unabhängige Versuche)               |
| **SW 03**  | Satz von Bayes              | Bayes-Theorem, Totale Wahrscheinlichkeit → kann mit Binomial/Poisson-Likelihood kombiniert werden                        |
| **SW 05+** | (Vorausschau)               | Varianz, Standardabweichung, Normalverteilung als Grenzwert                                                               |

---

> **📌 Zusammenfassung auf einen Blick:**
> SW 04 führt die Zufallsvariable als zentrale Abstraktion ein und behandelt fünf diskrete Verteilungen. Der **Entscheidungsbaum** und die **Formelsammlung** sind die wichtigsten Prüfungshilfen. Alle Aufgaben haben IT-/Security-Kontext (Spam, Server, Brute-Force, DDoS, Penetration Testing).
