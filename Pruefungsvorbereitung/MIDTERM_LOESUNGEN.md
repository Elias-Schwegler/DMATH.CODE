# DMATH.CODE – Midterm Test: LÖSUNGEN

---

## Teil A: Verständnisfragen

### A1
**Laplace-Experiment:** Alle Ergebnisse gleich wahrscheinlich → $P(\omega) = \frac{1}{|\Omega|}$. Beispiel: Fairer Würfel.
**Nicht-uniform:** Ergebnisse haben unterschiedliche Wahrscheinlichkeiten. Beispiel: Gezinkter Würfel.

### A2
Wenn $A$ und $B$ disjunkt sind und $A$ eintritt, kann $B$ **unmöglich** eintreten → $P(B|A) = 0 \neq P(B)$. Das Eintreten von $A$ gibt also **Information** über $B$ (nämlich: $B$ ist unmöglich). Unabhängigkeit würde bedeuten, dass keine Information fliesst.

### A3
**Apriori** $P(A)$: Wahrscheinlichkeit **vor** einer Beobachtung (z.B. $P(\text{krank}) = 0.001$).
**Aposteriori** $P(A|B)$: Wahrscheinlichkeit **nach** einer Beobachtung (z.B. $P(\text{krank} | \text{Test+}) = 0.083$).
Der Satz von Bayes berechnet die Aposteriori aus der Apriori.

### A4
- a) Kein Standard-Verteilung nötig. $P = \frac{1}{26^8}$ (Laplace, $|\Omega| = 26^8$).
- b) **Poissonverteilung** $\text{Poi}(\mu = 5)$: Seltene Ereignisse pro Zeiteinheit.
- c) **Hypergeometrische Verteilung** $H(n=10, M=12, N=88)$: Ziehen ohne Zurücklegen aus endlicher Population. $E(X) = 10 \cdot \frac{12}{100} = 1.2$.

### A5
**Las Vegas:** Ergebnis ist **immer korrekt**, aber die **Laufzeit** ist die Zufallsvariable. (z.B. randomisiertes Quicksort)
**Monte Carlo:** Laufzeit ist **immer gleich/begrenzt**, aber die **Korrektheit** ist die Zufallsvariable. (z.B. Karger's Min-Cut)

### A6
Die Markov-Eigenschaft besagt: $P(X_{t+1} = x | X_0, X_1, \ldots, X_t) = P(X_{t+1} = x | X_t)$. Der nächste Zustand hängt **nur vom aktuellen** Zustand ab, nicht von der Vergangenheit. Deshalb reicht eine einzige Übergangsmatrix $T$ (zeitunabhängig), um das gesamte Verhalten zu beschreiben.

### A7
Bei nicht-irreduziblen Ketten zerfällt der Graph in **getrennte Komponenten**. Innerhalb jeder Komponente kann sich eine eigene invariante Verteilung bilden. Je nachdem, in welcher Komponente man startet, konvergiert man zu einer anderen Verteilung.

### A8
- Wenn $|\lambda| > 1$: Vektoren werden bei jeder Iteration länger → **numerischer Überlauf**
- Wenn $|\lambda| < 1$: Vektoren werden kürzer → **Unterlauf** (alles wird 0)

Normierung hält die Länge bei 1 – die **Richtung** (= Eigenvektor) bleibt erhalten.

### A9
Der Rest ist **immer nicht-negativ**: $R \in \{0, 1, \ldots, m-1\}$.

$-14 = Q \cdot 5 + R$ mit $R \geq 0$: $-14 = (-3) \cdot 5 + 1$, also $R = 1$.

Faustregel: $(-a) \text{ mod } m = m - (a \text{ mod } m)$ (wenn $a \text{ mod } m \neq 0$).

### A10
RSA braucht $m^e \text{ mod } M$ mit riesigem $e$ (z.B. $e = 65537$) und $M$ (2048 Bits). **Naive Methode:** 65536 Multiplikationen mit riesigen Zahlen → viel zu langsam. **Square-and-Multiply:** Nur 17 Operationen ($65537 = 2^{16}+1$, also 16 Quadrierungen + 1 Multiplikation).

---

## Teil B: Entscheidungsfragen

### B1

| Situation | Verteilung | Parameter |
|---|---|---|
| a) 1000 Versuche, $p = 0.001$, Anzahl Treffer | **Binomial** $B(n, p)$ | $n = 1000$, $p = 0.001$ |
| b) 20 aus 500 (30 defekt), ohne Zurücklegen | **Hypergeometrisch** $H(n, M, N)$ | $n = 20$, $M = 30$, $N = 470$ |
| c) 25 Fragen, je $p = 1/4$ | **Binomial** $B(n, p)$ | $n = 25$, $p = 0.25$ |
| d) Warten auf ersten Erfolg, $p = 1/1000$ | **Geometrisch** $\text{Geo}(p)$ | $p = 0.001$, $E(X) = 1000$ |
| e) 2 Ausfälle/Tag im Schnitt, $P(X = 0)$? | **Poisson** $\text{Poi}(\mu)$ | $\mu = 2$ |

### B2
- a) **Satz von Bayes** – gesucht ist $P(\text{krank} | \text{Test+})$, aber gegeben ist $P(\text{Test+} | \text{krank})$ (umgekehrte Richtung).
- b) **Definition** reicht: $P(\text{gerade} | > 3) = \frac{P(\{4, 6\})}{P(\{4, 5, 6\})} = \frac{2/6}{3/6} = \frac{2}{3}$.
- c) **Totale Wahrscheinlichkeit**: $P(\text{Test+}) = P(\text{krank}) \cdot P(\text{Test+}|\text{krank}) + P(\text{gesund}) \cdot P(\text{Test+}|\text{gesund})$.

### B3
- a) **Ja, irreduzibel.** Alle Knoten sind gegenseitig erreichbar: $1 \to 2 \to 3 \to 4 \to 1$ (und umgekehrt).
- b) **Nein, nicht aperiodisch.** $N_1 = \{2, 4, 6, \ldots\}$ (nur gerade Rückkehrzeiten, da der Graph bipartit ist: $\{1,3\}$ und $\{2,4\}$). $\gcd(N_1) = 2 \neq 1$.
- c) Es gibt **genau eine** invariante Verteilung (irreduzibel), aber die Kette **konvergiert nicht** unbedingt (nicht aperiodisch → kann oszillieren).

### B4
- a) **Naive Methode:** $100 - 1 = 99$ Multiplikationen.
- b) $100 = 1100100_2$ (7 Bits)
- c) **S&M:** 6 Quadrierungen (Bits nach dem ersten) + 2 Multiplikationen (für die 1-Bits nach dem ersten) = **8 Operationen**.

### B5
- a) **LGS von Hand** – 3 Zustände sind klein genug, exakte Lösung möglich.
- b) **Matrix-Vektor-Iteration** (Python) – LGS mit 500 Variablen ist von Hand nicht machbar.
- c) **Potenzmethode** – keine stochastische Matrix, also braucht man Normierung und bekommt den dominanten Eigenwert + Eigenvektor.

---

## Teil C: Rechenaufgaben

### C1 – Wahrscheinlichkeit

**a)** $|\Omega| = 10^4 = 10000$ (4 Ziffern, je 10 Möglichkeiten, mit Zurücklegen)

**b)** Alle verschieden: $\frac{10 \cdot 9 \cdot 8 \cdot 7}{10^4} = \frac{5040}{10000} = 0.504$

**c)** Mindestens zwei gleich = Gegenereignis von "alle verschieden":
$$P(\text{mind. 2 gleich}) = 1 - 0.504 = \boxed{0.496}$$

---

### C2 – Bedingte Wahrscheinlichkeit & Bayes

**a) Baumdiagramm:**

```
              ┌── Vorfall (0.02)  → P = 0.7 · 0.02 = 0.014
Intern (0.7) ─┤
              └── Kein Vorfall (0.98)
              ┌── Vorfall (0.15)  → P = 0.3 · 0.15 = 0.045
Extern (0.3) ─┤
              └── Kein Vorfall (0.85)
```

$$P(\text{Vorfall}) = 0.7 \cdot 0.02 + 0.3 \cdot 0.15 = 0.014 + 0.045 = \boxed{0.059}$$

**b) Bayes:**

$$P(\text{extern} | \text{Vorfall}) = \frac{P(\text{extern}) \cdot P(\text{Vorfall} | \text{extern})}{P(\text{Vorfall})} = \frac{0.3 \cdot 0.15}{0.059} = \frac{0.045}{0.059} = \boxed{0.763}$$

76.3% – obwohl nur 30% der Nutzer extern sind, verursachen sie 76% der Vorfälle!

---

### C3 – Zufallsvariablen

**a)** $X \sim B(n = 20, p = 0.05)$ – Binomialverteilung (feste Anzahl unabhängiger Versuche, gleiche Erfolgswahrscheinlichkeit).

**b)**

$$P(X = 0) = \binom{20}{0} \cdot 0.05^0 \cdot 0.95^{20} = 1 \cdot 1 \cdot 0.95^{20}$$

$$0.95^{20} = 0.95^{10} \cdot 0.95^{10}$$

$0.95^{10} \approx 0.5987$ → $0.95^{20} \approx 0.5987^2 \approx \boxed{0.3585}$

**c)** Gegenereignis:

$$P(X \geq 2) = 1 - P(X = 0) - P(X = 1)$$

$$P(X = 1) = \binom{20}{1} \cdot 0.05^1 \cdot 0.95^{19} = 20 \cdot 0.05 \cdot 0.95^{19}$$

$0.95^{19} = 0.95^{20} / 0.95 \approx 0.3585 / 0.95 \approx 0.3774$

$P(X = 1) = 20 \cdot 0.05 \cdot 0.3774 = 0.3774$

$$P(X \geq 2) = 1 - 0.3585 - 0.3774 = \boxed{0.2641}$$

---

### C4 – Erwartete Komplexität

**a)**

$$E(X) = \sum_{i=1}^{6} c_i \cdot P(X = c_i) = \frac{1}{6}(3 + 2 + 3 + 1 + 3 + 2) = \frac{14}{6} = \boxed{\frac{7}{3} \approx 2.33}$$

**b)** **Las Vegas** – die binäre Suche findet das Element **immer korrekt**, aber die Laufzeit (Anzahl Vergleiche) variiert je nach Position.

**c)** MC-Wiederholungsformel: $n \geq \left\lceil\frac{\log(\varepsilon)}{\log(1-p)}\right\rceil$ mit $p = 0.6$, $\varepsilon = 0.01$:

$$n \geq \left\lceil\frac{\log(0.01)}{\log(0.4)}\right\rceil = \left\lceil\frac{-2}{-0.3979}\right\rceil = \left\lceil 5.026 \right\rceil = \boxed{6 \text{ Wiederholungen}}$$

---

### C5 – Markov-Kette

**a)** Zeilensummen prüfen:
- Zeile 1: $0 + 0.5 + 0.5 = 1$ ✓
- Zeile 2: $0.3 + 0 + 0.7 = 1$ ✓
- Zeile 3: $0.4 + 0.6 + 0 = 1$ ✓

→ **Ja, gültige stochastische Matrix.**

**b)** $\vec{v}_1 = \vec{v}_0 \cdot T = (1, 0, 0) \cdot T$:

$$v_1(1) = 1 \cdot 0 + 0 \cdot 0.3 + 0 \cdot 0.4 = 0$$
$$v_1(2) = 1 \cdot 0.5 + 0 \cdot 0 + 0 \cdot 0.6 = 0.5$$
$$v_1(3) = 1 \cdot 0.5 + 0 \cdot 0.7 + 0 \cdot 0 = 0.5$$

$$\boxed{\vec{v}_1 = (0, 0.5, 0.5)}$$

$\vec{v}_2 = \vec{v}_1 \cdot T = (0, 0.5, 0.5) \cdot T$:

$$v_2(1) = 0 \cdot 0 + 0.5 \cdot 0.3 + 0.5 \cdot 0.4 = 0.15 + 0.20 = 0.35$$
$$v_2(2) = 0 \cdot 0.5 + 0.5 \cdot 0 + 0.5 \cdot 0.6 = 0.30$$
$$v_2(3) = 0 \cdot 0.5 + 0.5 \cdot 0.7 + 0.5 \cdot 0 = 0.35$$

$$\boxed{\vec{v}_2 = (0.35, 0.30, 0.35)}$$

**c)** LGS aus $\vec{\pi} \cdot T = \vec{\pi}$:

Spalte 1: $0 \cdot \pi_1 + 0.3 \cdot \pi_2 + 0.4 \cdot \pi_3 = \pi_1$ → $0.3\pi_2 + 0.4\pi_3 = \pi_1$ ... (I)

Spalte 2: $0.5 \cdot \pi_1 + 0 \cdot \pi_2 + 0.6 \cdot \pi_3 = \pi_2$ → $0.5\pi_1 + 0.6\pi_3 = \pi_2$ ... (II)

Spalte 3: $0.5 \cdot \pi_1 + 0.7 \cdot \pi_2 + 0 \cdot \pi_3 = \pi_3$ → $0.5\pi_1 + 0.7\pi_2 = \pi_3$ ... (III)

Normierung: $\pi_1 + \pi_2 + \pi_3 = 1$ ... (IV)

Aus (I): $\pi_1 = 0.3\pi_2 + 0.4\pi_3$

Aus (III): $\pi_3 = 0.5\pi_1 + 0.7\pi_2$

Einsetzen von (I) in (III):
$\pi_3 = 0.5(0.3\pi_2 + 0.4\pi_3) + 0.7\pi_2 = 0.15\pi_2 + 0.2\pi_3 + 0.7\pi_2$
$\pi_3 - 0.2\pi_3 = 0.85\pi_2$
$0.8\pi_3 = 0.85\pi_2$
$\pi_3 = \frac{0.85}{0.8}\pi_2 = \frac{17}{16}\pi_2$

Einsetzen in (I):
$\pi_1 = 0.3\pi_2 + 0.4 \cdot \frac{17}{16}\pi_2 = 0.3\pi_2 + \frac{17}{40}\pi_2 = \frac{12}{40}\pi_2 + \frac{17}{40}\pi_2 = \frac{29}{40}\pi_2$

Normierung (IV):
$\frac{29}{40}\pi_2 + \pi_2 + \frac{17}{16}\pi_2 = 1$

$\pi_2 \left(\frac{29}{40} + 1 + \frac{17}{16}\right) = 1$

$\pi_2 \left(\frac{29}{40} + \frac{40}{40} + \frac{42.5}{40}\right) = \pi_2 \cdot \frac{111.5}{40} = 1$

$\pi_2 = \frac{40}{111.5} = \frac{80}{223}$

$\pi_1 = \frac{29}{40} \cdot \frac{80}{223} = \frac{58}{223}$

$\pi_3 = \frac{17}{16} \cdot \frac{80}{223} = \frac{85}{223}$

$$\boxed{\vec{\pi} = \frac{1}{223}(58, 80, 85) \approx (0.260, 0.359, 0.381)}$$

**Kontrolle:** $58 + 80 + 85 = 223$ ✓

---

### C6 – Matrizenmultiplikation

**a)**

$$A \cdot B = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \cdot \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 2 \cdot 1 + 1 \cdot 2 & 2 \cdot 4 + 1 \cdot 0 \\ 0 \cdot 1 + 3 \cdot 2 & 0 \cdot 4 + 3 \cdot 0 \end{pmatrix} = \boxed{\begin{pmatrix} 4 & 8 \\ 6 & 0 \end{pmatrix}}$$

**b)**

$$B \cdot A = \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1 \cdot 2 + 4 \cdot 0 & 1 \cdot 1 + 4 \cdot 3 \\ 2 \cdot 2 + 0 \cdot 0 & 2 \cdot 1 + 0 \cdot 3 \end{pmatrix} = \boxed{\begin{pmatrix} 2 & 13 \\ 4 & 2 \end{pmatrix}}$$

**c)** $A \cdot B \neq B \cdot A$! → **Matrizenmultiplikation ist NICHT kommutativ.**

---

### C7 – Modulares Rechnen

**a)** $(247 \cdot 583 + 1291) \text{ mod } 7$

Erst reduzieren:
- $247 \text{ mod } 7$: $247 = 35 \cdot 7 + 2$ → $2$
- $583 \text{ mod } 7$: $583 = 83 \cdot 7 + 2$ → $2$
- $1291 \text{ mod } 7$: $1291 = 184 \cdot 7 + 3$ → $3$

Dann rechnen:
$(2 \cdot 2 + 3) \text{ mod } 7 = 7 \text{ mod } 7 = \boxed{0}$

**b)** $3^{13} \text{ mod } 7$

Schritt 1: $13 = 1101_2$ (Bits: 1, 1, 0, 1)

| Schritt | Bit | Operation | Rechnung | mod 7 |
|---|---|---|---|---|
| Start | 1 | — | 3 | 3 |
| | 1 | Q, M | $3^2 = 9 \to 2$, $2 \cdot 3 = 6$ | 6 |
| | 0 | Q | $6^2 = 36$ | $36 \text{ mod } 7 = 1$ |
| | 1 | Q, M | $1^2 = 1$, $1 \cdot 3 = 3$ | 3 |

$$\boxed{3^{13} \text{ mod } 7 = 3}$$

Kontrolle: $3^6 = 729$, $729 \text{ mod } 7 = 1$ (kleiner Fermat). Also $3^{13} = 3^{12} \cdot 3 = (3^6)^2 \cdot 3 = 1 \cdot 3 = 3$ ✓

---

### C8 – Gemischte Anwendung

**a) Totale Wahrscheinlichkeit:**

$$P(\text{Alarm}) = P(\text{Angriff}) \cdot P(\text{Alarm}|\text{Angriff}) + P(\text{kein Angriff}) \cdot P(\text{Alarm}|\text{kein Angriff})$$
$$= 0.005 \cdot 0.92 + 0.995 \cdot 0.08 = 0.0046 + 0.0796 = \boxed{0.0842}$$

**b) Satz von Bayes:**

$$P(\text{Angriff}|\text{Alarm}) = \frac{P(\text{Angriff}) \cdot P(\text{Alarm}|\text{Angriff})}{P(\text{Alarm})} = \frac{0.005 \cdot 0.92}{0.0842} = \frac{0.0046}{0.0842} = \boxed{0.0546}$$

Nur 5.5%! Trotz gutem IDS (92% Erkennung, 8% Fehlalarm) ist die Mehrheit der Alarme **Fehlalarme** – ein klassisches **Base Rate Neglect**-Problem (vgl. SW 03).

**c) Hashfunktion:**
- $247 \text{ mod } 13 = 247 - 19 \cdot 13 = 247 - 247 = \boxed{0}$
- $1039 \text{ mod } 13 = 1039 - 79 \cdot 13 = 1039 - 1027 = \boxed{12}$
- $598 \text{ mod } 13 = 598 - 46 \cdot 13 = 598 - 598 = \boxed{0}$

⚠️ Kollision! 247 und 598 landen auf derselben Adresse 0.

---

## Teil D: Bonus

### D1 – Populationsdynamik

**a)**
- $L_{2,1} = 4$: Jedes **erwachsene Tier** erzeugt im Schnitt **4 Jungtiere** pro Zeitschritt.
- $L_{3,3} = 0.5$: **50%** der alten Tiere überleben zum nächsten Zeitschritt (bleiben in Phase "Alt").

**b)** $\lambda \approx 1.12 > 1$ → **Ja, die Population überlebt langfristig.**
Wachstumsrate: Die Population wächst um ca. **12% pro Zeitschritt** ($\lambda - 1 = 0.12$).

### D2 – Modulare Wurzeln

**a)** Alle $x^2 \text{ mod } 7$ berechnen:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $x^2$ | 0 | 1 | 4 | 9 | 16 | 25 | 36 |
| $x^2 \text{ mod } 7$ | 0 | 1 | 4 | **2** | **2** | 4 | 1 |

$$\boxed{\sqrt{2} \text{ mod } 7 = \{3, 4\}}$$

**b)** Aus der Tabelle: Kein $x$ ergibt $x^2 \text{ mod } 7 = 5$.
$$\boxed{5 \text{ hat KEINE Quadratwurzel mod } 7}$$

Die quadratischen Reste mod 7 sind nur $\{0, 1, 2, 4\}$. Die Zahlen $\{3, 5, 6\}$ sind **keine quadratischen Reste**.

---

## Bewertung

| Teil | Punkte |
|---|---|
| A: Verständnisfragen | /20 |
| B: Entscheidungsfragen | /15 |
| C: Rechenaufgaben | /45 |
| D: Bonus | /10 |
| **Total** | **/80 (+10 Bonus)** |

| Note | Punkte |
|---|---|
| 6 | ≥ 72 |
| 5.5 | 64–71 |
| 5 | 56–63 |
| 4.5 | 48–55 |
| 4 | 40–47 |
| < 4 | < 40 |
