# DMATH-CODE — SW 03: Satz von Bayes

> **Modul:** DMATH-CODE, HSLU | **Dozent:** Dr. Reto Berger | **Semester:** Frühlingssemester 25

---

## 🎯 Lernziele

1. **Satz von Bayes verstehen und anwenden** — Sie verstehen den Satz von Bayes und können damit bedingte Wahrscheinlichkeiten berechnen (insbesondere die «Umkehrung» $P(A|B) \leftrightarrow P(B|A)$).
2. **Wahrscheinlichkeiten mit einer Partition berechnen** — Sie können Wahrscheinlichkeiten mit Hilfe einer Partition der Ergebnismenge berechnen (Satz von der totalen Wahrscheinlichkeit).
3. **Baumdiagramme für Bayes nutzen** — Sie können ein Baumdiagramm zeichnen und daraus systematisch die Bayes-Formel ablesen.
4. **Apriori- und Aposteriori-Überzeugungen unterscheiden** — Sie verstehen, wie der Satz von Bayes subjektive Überzeugungen durch neue Evidenz aktualisiert.

---

## 📖 Wichtigste Begriffe

| Begriff | Definition |
|---------|-----------|
| **Satz von Bayes** | Formel zur Berechnung der «umgekehrten» bedingten Wahrscheinlichkeit: $P(A\|B) = \frac{P(A) \cdot P(B\|A)}{P(B)}$. Ermöglicht es, von $P(B\|A)$ auf $P(A\|B)$ zu schliessen. |
| **Partition** | Eine Zerlegung der Ergebnismenge $\Omega$ in paarweise disjunkte Teilmengen $\Omega_1, \Omega_2, \ldots, \Omega_n$ mit $\Omega_1 \cup \Omega_2 \cup \ldots \cup \Omega_n = \Omega$. **Hinweis:** «Partition» in diesem Skript = «Satz von der totalen Wahrscheinlichkeit» in anderen Werken. |
| **Totale Wahrscheinlichkeit** | Die Berechnung von $P(B)$ über eine Partition: $P(B) = \sum_i P(\Omega_i) \cdot P(B\|\Omega_i)$. Wird als Nenner im Satz von Bayes benötigt. |
| **Apriori-Überzeugung** $P(A)$ | Die ursprüngliche Wahrscheinlichkeit eines Ereignisses $A$ **vor** Eintreffen neuer Beobachtungen. Kann objektiv (z.B. Krankheitsprävalenz) oder subjektiv (z.B. «Ich glaube, morgen wird schönes Wetter» $= 2/3$) sein. |
| **Aposteriori-Überzeugung** $P(A\|B)$ | Die aktualisierte Wahrscheinlichkeit von $A$ **nach** Berücksichtigung der Beobachtung $B$, berechnet über den Satz von Bayes. |
| **Bayesscher Spam-Filter** | Anwendung des Satzes von Bayes zur Klassifikation von Nachrichten als Spam/Nicht-Spam basierend auf dem Vorkommen bestimmter Wörter. Kernidee des **Naive Bayes Classifiers**. |
| **Paritätsbit** | Ein zusätzliches Bit, das an eine Nachricht angehängt wird, um Übertragungsfehler zu erkennen. Die Gesamtanzahl der 1-Bits wird gerade gemacht. |

---

## 📐 Definitionen, Sätze & Beweise

### Definition 1: Satz von Bayes

> Sei $P$ eine Wahrscheinlichkeitsfunktion und $A$ und $B$ beliebige Ereignisse mit $P(B) > 0$. Dann gilt:
>
> $$P(A|B) = \frac{P(A) \cdot P(B|A)}{P(B)}$$

**Intuitive Erklärung:** Der Satz von Bayes beantwortet die Frage: «Was ist die Ursache, wenn ich die Wirkung beobachtet habe?» Er dreht die Richtung der bedingten Wahrscheinlichkeit um. Man kennt oft $P(B|A)$ (z.B. «Wie wahrscheinlich ist ein positiver Test bei einem Kranken?»), sucht aber $P(A|B)$ (z.B. «Wie wahrscheinlich bin ich krank bei positivem Test?»).

**Beweisskizze:**
1. Aus der Definition der bedingten Wahrscheinlichkeit (SW 02): $P(A|B) = \frac{P(A \cap B)}{P(B)}$
2. Aus der Produktregel (SW 02): $P(A \cap B) = P(A) \cdot P(B|A)$
3. Einsetzen von 2. in 1.: $P(A|B) = \frac{P(A) \cdot P(B|A)}{P(B)}$ $\blacksquare$

**Schritt-für-Schritt Zahlenbeispiel (Monty-Hall / Let's Make a Deal):**

Der Kandidat wählt Tor 1. Der Moderator öffnet Tor 3 (dahinter ist eine Ziege). Soll der Kandidat wechseln?

- Ereignisse: $G_i$ = Gewinn hinter Tor $i$, $M_3$ = Moderator öffnet Tor 3
- Apriori: $P(G_1) = P(G_2) = P(G_3) = \frac{1}{3}$
- Bedingte WS:
  - $P(M_3|G_1) = \frac{1}{2}$ (Moderator wählt zufällig zwischen Tor 2 und 3)
  - $P(M_3|G_2) = 1$ (Moderator *muss* Tor 3 öffnen, weil Tor 1 gewählt und Tor 2 den Gewinn hat)
  - $P(M_3|G_3) = 0$ (Moderator kann Tor 3 nicht öffnen, wenn dort der Gewinn ist)

$$P(G_2|M_3) = \frac{P(G_2) \cdot P(M_3|G_2)}{P(G_1) \cdot P(M_3|G_1) + P(G_2) \cdot P(M_3|G_2) + P(G_3) \cdot P(M_3|G_3)}$$

$$= \frac{\frac{1}{3} \cdot 1}{\frac{1}{3} \cdot \frac{1}{2} + \frac{1}{3} \cdot 1 + \frac{1}{3} \cdot 0} = \frac{\frac{1}{3}}{\frac{1}{6} + \frac{1}{3} + 0} = \frac{\frac{1}{3}}{\frac{1}{2}} = \frac{2}{3}$$

→ **Wechseln verdoppelt die Gewinnchance von $\frac{1}{3}$ auf $\frac{2}{3}$!**

---

### Definition 2: Satz von der totalen Wahrscheinlichkeit (Partition)

> Wenn $\Omega = \Omega_1 \cup \Omega_2 \cup \ldots \cup \Omega_n$ eine **Partition** ist ($\Omega_i \cap \Omega_j = \emptyset$ für $i \neq j$), dann gilt für jedes Ereignis $B$:
>
> $$P(B) = P(\Omega_1) \cdot P(B|\Omega_1) + P(\Omega_2) \cdot P(B|\Omega_2) + \ldots + P(\Omega_n) \cdot P(B|\Omega_n)$$

**Intuitive Erklärung:** Man zerlegt den Ergebnisraum in vollständige, sich nicht überlappende Teile und berechnet $P(B)$ als gewichtete Summe über alle Teile. Im Baumdiagramm entspricht dies der **Summe aller Pfade**, die bei $B$ enden.

**Häufigster Spezialfall** (Partition in $A$ und $\overline{A}$):

$$P(B) = P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})$$

Damit wird der Satz von Bayes in ausführlicher Form:

$$\boxed{P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})}}$$

**Schritt-für-Schritt Zahlenbeispiel (Aufgabe 1 — Urnenmodell):**

Urne $A$: 9 weisse Kugeln (Nr. 1–9). Urne $B$: 5 schwarze Kugeln (Nr. 1–5). Eine Urne wird uniform zufällig gewählt, dann eine Kugel gezogen. Frage: Die gezogene Nummer ist gerade — wie wahrscheinlich stammt die Kugel aus Urne $A$?

1. **Ereignisse definieren:** $A$ = «Kugel aus Urne A», $G$ = «Nummer ist gerade»
2. **Apriori:** $P(A) = \frac{1}{2}$, $P(B) = \frac{1}{2}$
3. **Bedingte WS:** $P(G|A) = \frac{4}{9}$ (gerade in A: 2,4,6,8), $P(G|B) = \frac{2}{5}$ (gerade in B: 2,4)
4. **Totale WS:** $P(G) = P(A) \cdot P(G|A) + P(B) \cdot P(G|B) = \frac{1}{2} \cdot \frac{4}{9} + \frac{1}{2} \cdot \frac{2}{5} = \frac{2}{9} + \frac{1}{5} = \frac{19}{45}$
5. **Bayes:** $P(A|G) = \frac{P(A) \cdot P(G|A)}{P(G)} = \frac{\frac{1}{2} \cdot \frac{4}{9}}{\frac{19}{45}} = \frac{\frac{2}{9}}{\frac{19}{45}} = \frac{2}{9} \cdot \frac{45}{19} = \frac{10}{19} \approx 52.6\%$

#### 📸 Musterlösung: Aufgabe 1 — Baumdiagramm & Bayes-Rechnung

> Das Baumdiagramm zeigt die zweistufige Struktur: **1. Stufe** = Urnenwahl ($A$ oder $B$, je $1/2$), **2. Stufe** = Ziehung (Gerade $G$ oder Ungerade $U$). Die handschriftliche Rechnung rechts wendet den Satz von Bayes schrittweise an — man sieht, wie $P(G)$ im Nenner über die totale WS berechnet wird.

![Aufgabe 1: Baumdiagramm mit Urne A (4/9 gerade, 5/9 ungerade) und Urne B (2/5 gerade, 3/5 ungerade), daneben handschriftliche Bayes-Rechnung → 10/19 ≈ 52.6%](img_tmp/DMATH-CODE-Serie03-final_page_4.png)

---

### Zusammenführung: Produktregel → Totale WS → Bayes

> Die drei Konzepte bauen direkt aufeinander auf:
>
> 1. **Produktregel** (SW 02): $P(A \cap B) = P(A) \cdot P(B|A)$ → berechnet einen einzelnen Pfad im Baum
> 2. **Totale Wahrscheinlichkeit**: $P(B) = \sum_i P(\Omega_i) \cdot P(B|\Omega_i)$ → summiert alle Pfade, die bei $B$ enden
> 3. **Satz von Bayes**: $P(A|B) = \frac{\text{ein Pfad}}{\text{alle Pfade zu } B}$ → der Anteil eines bestimmten Pfades an der Gesamtheit

**⭐ Merkhilfe:** Im Baumdiagramm ist der Satz von Bayes nichts anderes als:

$$P(A|B) = \frac{\text{Wahrscheinlichkeit des Ziel-Pfades (A und B)}}{\text{Summe aller Pfade, die bei B enden}}$$

---

## 🧮 Formeln & Rechenregeln

### Kernformeln dieser Woche

| # | Formel | Beschreibung | Variablen |
|---|--------|-------------|-----------|
| 1 | $P(A\|B) = \frac{P(A) \cdot P(B\|A)}{P(B)}$ | **Satz von Bayes** (Kurzform) | $A$: gesuchte Ursache, $B$: beobachtete Wirkung |
| 2 | $P(B) = \sum_{i} P(\Omega_i) \cdot P(B\|\Omega_i)$ | **Totale Wahrscheinlichkeit** | $\Omega_i$: Elemente einer Partition von $\Omega$ |
| 3 | $P(A\|B) = \frac{P(A)P(B\|A)}{P(A)P(B\|A) + P(\overline{A})P(B\|\overline{A})}$ | **Bayes ausführlich** (Partition $A, \overline{A}$) | Am häufigsten verwendete Form |

### Formeln aus SW 01/02 (weiterhin benötigt)

| Formel | Beschreibung |
|--------|-------------|
| $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ | Bedingte Wahrscheinlichkeit (Definition, SW 02) |
| $P(A \cap B) = P(A) \cdot P(B\|A)$ | Produktregel / Multiplikationssatz (SW 02) |
| $P(\overline{A}) = 1 - P(A)$ | Gegenereignis (SW 01) |
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Inklusion-Exklusion (SW 01) |

### ⚠️ Randfälle

- **$P(B) = 0$:** Bayes-Formel ist **nicht definiert**. Ist $P(B) = 0$, konnte $B$ gar nicht eintreten.
- **$P(A) = 0$:** Wenn die Apriori-Wahrscheinlichkeit 0 ist, kann auch noch so starke Evidenz nichts daran ändern: $P(A|B) = 0$.
- **$P(A) = 1$:** Analog: $P(A|B) = 1$. Absolute Sicherheit wird durch Evidenz nicht verändert.
- **Unabhängigkeit:** Wenn $A$ und $B$ unabhängig sind, liefert Bayes: $P(A|B) = P(A)$ — die Evidenz ändert nichts.

---

## 📊 Vergleiche & Klassifizierungen

### Apriori vs. Aposteriori

| Eigenschaft | Apriori $P(A)$ | Aposteriori $P(A\|B)$ |
|-------------|----------------|----------------------|
| **Zeitpunkt** | Vor der Beobachtung | Nach der Beobachtung |
| **Berechnung** | Gegeben / geschätzt | Über Satz von Bayes berechnet |
| **Beispiel (Medizin)** | $P(\text{krank}) = 0.001$ | $P(\text{krank}\|\text{Test }+) = 0.0826$ |
| **Beispiel (Spam)** | $P(\text{Spam}) = 0.5$ | $P(\text{Spam}\|\text{«Rolex»}) = 0.962$ |

### Bayes vs. «Einfache» bedingte WS (SW 02)

| Eigenschaft | SW 02: $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ | SW 03: $P(A\|B) = \frac{P(A) \cdot P(B\|A)}{P(B)}$ |
|-------------|-------------------------------------------|---------------------------------------------------|
| **Wann nützlich** | Wenn $P(A \cap B)$ direkt bekannt ist | Wenn nur die «umgekehrte» Richtung $P(B\|A)$ bekannt ist |
| **Typische Aufgaben** | «Würfelsumme, gegeben mind. eine 1» | «Krankheit, gegeben positiver Test» |
| **Schwierigkeit** | Schnitt direkt ausrechnen | Baumdiagramm mit totaler WS nötig |

### Direkter vs. indirekter Schluss

| Richtung | Bekannt | Gesucht | Methode |
|----------|---------|---------|---------|
| **Vorwärts** (kausal) | Ursache $A$ → Wirkung $B$ | $P(B\|A)$ | Direkt aus Daten/Studien |
| **Rückwärts** (diagnostisch) | Wirkung $B$ → Ursache $A$? | $P(A\|B)$ | **Satz von Bayes** |

---

## 💻 Code-Beispiele (Python)

*Hinweis: In den Dokumenten von SW 03 war kein Jupyter Notebook vorhanden. Die folgenden Implementierungen illustrieren die Aufgabentypen der Serie.*

### Allgemeine Bayes-Funktion

**Mathematischer Hintergrund:** Die Funktion implementiert den Satz von Bayes in ausführlicher Form über einer Partition $\{A, \overline{A}\}$.

```python
def bayes(prior_A, p_B_given_A, p_B_given_notA):
    """
    Berechnet P(A|B) nach dem Satz von Bayes (Partition A, Ā).

    Parameter:
        prior_A:        P(A) — Apriori-Wahrscheinlichkeit
        p_B_given_A:    P(B|A) — Likelihood (Evidenz unter Bedingung A)
        p_B_given_notA: P(B|Ā) — Likelihood (Evidenz unter Bedingung Nicht-A)

    Rückgabe:
        P(A|B) — Aposteriori-Wahrscheinlichkeit
    """
    # Apriori des Gegenereignisses
    prior_notA = 1.0 - prior_A

    # Satz von der totalen Wahrscheinlichkeit → Nenner
    p_B = prior_A * p_B_given_A + prior_notA * p_B_given_notA

    # Satz von Bayes → Zähler / Nenner
    posterior = (prior_A * p_B_given_A) / p_B

    return posterior
```

> **Tipp:** Diese Funktion kann für fast alle Aufgaben der Serie 03 verwendet werden!

---

### Aufgabe 1 — Urnenmodell

**Mathematischer Hintergrund:** Zwei Urnen, eine wird uniform gewählt. Gezogene Nummer ist gerade — aus welcher Urne stammt sie wahrscheinlicher?

```python
# Aufgabe 1: Urne A (9 weisse, Nr. 1-9), Urne B (5 schwarze, Nr. 1-5)
# Gesucht: P(A | Nummer gerade)

P_A = 1/2                  # Urne A wird mit 50% gewählt
P_G_given_A = 4/9          # Gerade Nummern in A: {2,4,6,8} → 4 von 9
P_G_given_B = 2/5          # Gerade Nummern in B: {2,4} → 2 von 5

# Totale Wahrscheinlichkeit: P(G) = P(A)·P(G|A) + P(B)·P(G|B)
P_G = P_A * P_G_given_A + (1 - P_A) * P_G_given_B
print(f"P(Gerade) = {P_G:.4f}")  # = 19/45 ≈ 0.4222

# Bayes: P(A|G)
P_A_given_G = (P_A * P_G_given_A) / P_G
print(f"P(Urne A | Gerade) = {P_A_given_G:.4f}")  # = 10/19 ≈ 0.5263
# → ca. 52.6%
```

---

### Aufgabe 2 — Wettervorhersage (subjektive Wahrscheinlichkeit)

**Mathematischer Hintergrund:** Alice glaubt mit $P(S) = 2/3$ an schönes Wetter. Der Wetterbericht sagt schlechtes Wetter vorher. Wie ändert sich ihre Überzeugung?

```python
# Aufgabe 2: Apriori → Aposteriori-Überzeugung
# P(R|S) = 1/4 → Regen vorhergesagt, obwohl schön
# P(R|S̄) = 4/5 → Regen vorhergesagt, wenn schlecht

P_S = 2/3                  # Apriori: schönes Wetter
P_R_given_S = 1/4          # Fehlprognose bei schönem Wetter
P_R_given_notS = 4/5       # Korrekte Prognose bei schlechtem Wetter

# Bayes: P(S|R) = P(S)·P(R|S) / [P(S)·P(R|S) + P(S̄)·P(R|S̄)]
P_S_given_R = bayes(P_S, P_R_given_S, P_R_given_notS)
print(f"P(Schönes Wetter | Regen vorhergesagt) = {P_S_given_R:.4f}")
# = 5/13 ≈ 0.3846 → 38.5%
# → Die Aposteriori-Überzeugung sinkt von 66.7% auf 38.5%!
```

#### 📸 Musterlösung: Aufgabe 2 & 3 — Baumdiagramme (Wetter & Spam)

> **Obere Hälfte (Aufgabe 2):** Das Baumdiagramm zeigt die Apriori-Überzeugung ($S = 2/3$, $\overline{S} = 1/3$) und die bedingten WS für die Wetterprognose ($R|S = 1/4$, $R|\overline{S} = 4/5$). Die handschriftliche Rechnung rechts führt den vollständigen Bayes-Schluss durch.
>
> **Untere Hälfte (Aufgabe 3):** Baumdiagramm für den Spam-Filter mit «Rolex». Beachte die handschriftliche Notiz: *«Ja, weil der Schwellenwert überschritten wird»* — das Ergebnis $96.2\% > 0.9$ bestätigt die Filterung.

![Aufgabe 2: Baumdiagramm Wetter (S/S̄ → R/R̄) mit Bayes-Rechnung → 5/13 ≈ 38.5%. Aufgabe 3: Baumdiagramm Spam (S/S̄ → R/R̄) mit Bayes-Rechnung → 25/26 ≈ 96.2%, Schwellenwert überschritten](img_tmp/DMATH-CODE-Serie03-final_page_5.png)

---

### Aufgabe 3 — Spam-Filter (ein Merkmal: «Rolex»)

**Mathematischer Hintergrund:** Ein Wort kommt in Spam-Mails häufiger vor als in normalen Mails. Bayes berechnet $P(\text{Spam}|\text{Wort gefunden})$.

```python
# Aufgabe 3: Spam-Filter mit Wort "Rolex"
# 2000 Spam-Nachrichten, 1000 Nicht-Spam-Nachrichten
# "Rolex" in 250 von 2000 Spam, in 5 von 1000 Nicht-Spam

P_Spam = 1/2                           # Gleichwahrscheinlich (Annahme)
P_Rolex_given_Spam = 250 / 2000        # = 0.125
P_Rolex_given_NotSpam = 5 / 1000       # = 0.005

P_Spam_given_Rolex = bayes(P_Spam, P_Rolex_given_Spam, P_Rolex_given_NotSpam)
print(f"P(Spam | 'Rolex') = {P_Spam_given_Rolex:.4f}")
# = 25/26 ≈ 0.9615 → 96.2%
# Schwellenwert 0.9 → JA, Nachricht wird als Spam abgelehnt!
```

---

### Aufgabe 4 — Spam-Filter (zwei Merkmale: «Aktie» UND «unterbewertet»)

**Mathematischer Hintergrund:** Bei zwei Merkmalen wird die **bedingte Unabhängigkeit** angenommen (Naive Bayes): $P(A \cap u | S) = P(A|S) \cdot P(u|S)$.

```python
# Aufgabe 4: Spam-Filter mit zwei Wörtern
# "Aktie" in 400/2000 Spam, 60/1000 NotSpam
# "unterbewertet" in 200/2000 Spam, 25/1000 NotSpam

P_Spam = 1/2
P_A_given_S = 400/2000      # P(Aktie | Spam) = 0.20
P_A_given_NS = 60/1000      # P(Aktie | NotSpam) = 0.06
P_U_given_S = 200/2000      # P(unterbewertet | Spam) = 0.10
P_U_given_NS = 25/1000      # P(unterbewertet | NotSpam) = 0.025

# Naive Bayes: Wörter bedingt unabhängig → Multiplikation
# P(A∩u | S) = P(A|S) · P(u|S)
P_AU_given_S = P_A_given_S * P_U_given_S       # = 0.02
P_AU_given_NS = P_A_given_NS * P_U_given_NS    # = 0.0015

P_Spam_given_AU = bayes(P_Spam, P_AU_given_S, P_AU_given_NS)
print(f"P(Spam | 'Aktie' ∧ 'unterbewertet') = {P_Spam_given_AU:.4f}")
# = 40/43 ≈ 0.9302 → 93.0%
# Schwellenwert 0.9 → JA, wird als Spam abgelehnt!
```

#### 📸 Musterlösung: Aufgabe 4 — Naive Bayes mit bedingter Unabhängigkeit

> **Wichtig:** Die handschriftliche Notiz des Dozenten erklärt die zentrale Annahme: *«Wenn wir annehmen, dass A und u unabhängig sind, dann gilt $P(A \cap u) = P(A) \cdot P(u)$»*. Diese **bedingte Unabhängigkeit** ist die Kernidee hinter dem Naive Bayes Classifier — ohne diese Annahme könnten wir die Einzelwahrscheinlichkeiten nicht einfach multiplizieren. Das Baumdiagramm zeigt die Aufspaltung in $S/\overline{S}$ mit den kombinierten Häufigkeiten.

![Aufgabe 4: Naive Bayes Spam-Filter — Dozenten-Notiz zur bedingten Unabhängigkeit von «Aktie» und «unterbewertet», Baumdiagramm mit kombinierten Häufigkeiten → 40/43 ≈ 93.0%](img_tmp/DMATH-CODE-Serie03-final_page_6.png)

---

### Aufgabe 5 — Rauschender Kanal mit Paritätsbit

**Mathematischer Hintergrund:** Alice sendet «011» + Paritätsbit = «0110». Ein Bit wird mit Wahrscheinlichkeit $p$ umgedreht. Bob akzeptiert nur bei gerader Anzahl 1-Bits.

```python
from math import comb

def kanal_bayes(p):
    """
    Berechnet P(korrekte Nachricht | gerade Parität empfangen).

    p: Fehlerwahrscheinlichkeit pro Bit
    """
    q = 1 - p   # Korrekte Übertragung pro Bit

    # P(G|A): Gerade Parität, wenn Nachricht korrekt → 0 Fehler
    P_G_given_A = q**4   # Alle 4 Bits korrekt

    # P(G|F_i): Gerade Parität bei i Fehlern (gerade Anzahl Fehler)
    # Fehlerszenarien mit gerader Parität: 0, 2, 4 Fehler
    # P(G|nicht A) = gewichtete Summe über 2-Fehler und 4-Fehler Szenarien
    # geteilt durch P(nicht A)
    P_G_0_Fehler = q**4
    P_G_2_Fehler = comb(4, 2) * p**2 * q**2
    P_G_4_Fehler = p**4

    P_G = P_G_0_Fehler + P_G_2_Fehler + P_G_4_Fehler

    P_A_given_G = P_G_given_A / P_G
    return P_A_given_G

# a) p = 1%
print(f"a) P(korrekt | gerade Parität, p=1%) = {kanal_bayes(0.01):.4f}")
# ≈ 0.9994 → 99.94%

# b) p = 10%
print(f"b) P(korrekt | gerade Parität, p=10%) = {kanal_bayes(0.10):.4f}")
# ≈ 0.9302 → 93.02%
```

---

### Aufgabe 6 — Medizinischer Test (TBC-Diagnose)

**Mathematischer Hintergrund:** Seltene Krankheiten und diagnostische Tests — das «Base Rate Paradox». Selbst ein guter Test hat bei sehr seltenen Krankheiten eine hohe Falsch-Positiv-Rate.

```python
# Aufgabe 6a: TBC-Screening
# P(TBC) = 0.001 (0.1% Bevölkerung)
# Test-Sensitivität: P(D+|TBC) = 0.90 (90% der Kranken werden erkannt)
# Test-Spezifität: P(D-|gesund) = 0.99 → P(D+|gesund) = 0.01

P_TBC_6a = bayes(0.001, 0.90, 0.01)
print(f"6a) P(TBC | positiver Test) = {P_TBC_6a:.4f}")
# ≈ 0.0826 → nur 8.26%!

# Aufgabe 6b: Bayern 1973
# P(TBC) = 0.00190 (= 0.190%), Sensitivität ≥ 0.98, P(D+|gesund) ≤ 13·10⁻⁶
P_TBC_6b = bayes(0.00190, 0.98, 13e-6)
print(f"6b) P(TBC | positiver Test) ≥ {P_TBC_6b:.4f}")
# ≥ 0.9931 → ≥ 99.31%
# Höhere Prävalenz + besserer Test → viel höhere Aposteriori-WS!
```

> **Wichtige Erkenntnis:** Bei einer Prävalenz von nur 0.1% und 1% Falsch-Positiv-Rate sind **über 90% der positiven Testergebnisse falsch!** Die Apriori-Wahrscheinlichkeit (Prävalenz) dominiert das Ergebnis.

---

### Aufgabe 8 — Gefälschte Münze (Likelihood-Vergleich)

**Mathematischer Hintergrund:** Eine faire ($p=1/2$) und eine gefälschte ($p=3/4$ für Kopf) Münze. Je mehr Kopf-Würfe beobachtet werden, desto stärker spricht die Evidenz für die gefälschte Münze.

```python
# Aufgabe 8: Gefälschte Münze
P_G = 1/2   # Apriori: 50% Chance, gefälschte Münze gezogen

# a) p = 2/3, beobachte einen Kopf
P_K_given_G_a = 2/3    # Gefälschte Münze
P_K_given_F = 1/2       # Faire Münze
print(f"8a) P(Gefälscht | K) = {bayes(P_G, P_K_given_G_a, P_K_given_F):.4f}")
# = 4/7 ≈ 0.5714 → 57.1%

# b) p = 3/4, beobachte KKKZ
P_W_given_G_b = (3/4)**3 * (1/4)    # = 27/256
P_W_given_F = (1/2)**4               # = 1/16
print(f"8b) P(Gefälscht | KKKZ) = {bayes(P_G, P_W_given_G_b, P_W_given_F):.4f}")
# = 27/43 ≈ 0.6279 → 62.8%

# c) p = 3/4, beobachte KZZZKZ
P_W_given_G_c = (3/4)**2 * (1/4)**4   # K, Z, Z, Z, K, Z
P_W_given_F_c = (1/2)**6
print(f"8c) P(Gefälscht | KZZZKZ) = {bayes(P_G, P_W_given_G_c, P_W_given_F_c):.4f}")
# = 9/73 ≈ 0.1233 → 12.3%
# → Wenige Köpfe → Evidenz spricht GEGEN gefälschte Münze!
```

---

### Aufgabe 9 — Urnenraten (Mehrstufiger Bayes)

```python
# Aufgabe 9: Urne I (2G, 1R) vs Urne II (4G, 1R), ohne Zurücklegen
# c) Beide gezogene Kugeln sind grün → P(Urne II | GG)?

P_UI = 1/2
P_UII = 1/2

# P(GG | Urne I): 2/3 · 1/2 = 1/3
P_GG_UI = (2/3) * (1/2)
# P(GG | Urne II): 4/5 · 3/4 = 3/5
P_GG_UII = (4/5) * (3/4)

P_UII_given_GG = bayes(P_UII, P_GG_UII, P_GG_UI)
print(f"9c) P(Urne II | GG) = {P_UII_given_GG:.4f}")
# = 9/14 ≈ 0.6429 → 64.3%
```

---

## ✏️ Übungsaufgaben-Zusammenfassung

| Nr. | Thema / Konzept | Lösungsansatz | Typische Stolpersteine |
|-----|----------------|---------------|----------------------|
| **1** | Urnenmodell (2 Urnen) | Baumdiagramm: $P(A\|G) = \frac{P(A)P(G\|A)}{P(A)P(G\|A)+P(B)P(G\|B)}$. Ergebnis: $\frac{10}{19} \approx 52.6\%$ | Totale WS im Nenner vergessen; $P(G\|A)$ und $P(G\|B)$ verwechseln |
| **2** | Subjektive Wettervorhersage | Apriori $P(S) = 2/3$ → Aposteriori: $P(S\|R) = \frac{5}{13} \approx 38.5\%$ | Subjektive Apriori-WS mit den bedingten WS aus der Wetterprognose richtig verknüpfen |
| **3** | Spam-Filter (1 Merkmal) | $P(S\|\text{Rolex}) = \frac{25}{26} \approx 96.2\%$. Schwellenwert 0.9 → filtern | Häufigkeiten (250/2000) in bedingte WS (0.125) umrechnen |
| **4** | Spam-Filter (2 Merkmale) | Naive Bayes: $P(A \cap u\|S) = P(A\|S) \cdot P(u\|S)$. Ergebnis: $\frac{40}{43} \approx 93.0\%$ → filtern | Bedingte Unabhängigkeit muss **angenommen** werden! |
| **5** | Rauschender Kanal + Parität | Fehlerszenarien zählen: 0/2/4 Bitfehler → gerade Parität. a) $p=1\%$: $99.94\%$, b) $p=10\%$: $93.02\%$ | Alle geraden Fehleranzahlen berücksichtigen; $\binom{4}{k}$ nicht vergessen |
| **6** | Medizintest (TBC) | a) $P(T\|D) = \frac{0.001 \cdot 0.9}{0.001 \cdot 0.9 + 0.999 \cdot 0.01} \approx 8.26\%$. b) $\geq 99.31\%$ | **Base Rate Paradox**: seltene Krankheit → positiver Test meist falsch-positiv! |
| **7** | Signalübertragung (0/1) | Störungs-WS: $\frac{2}{5}$ der Nullen, $\frac{1}{3}$ der Einsen. Sendeverhältnis 5:3. a) $P(S_0\|E_0) = 75\%$, b) $P(S_1\|E_1) = 50\%$ | Sendeverhältnis (5:3 → $P(S_0)=5/8$) als Apriori nicht vergessen |
| **8** | Gefälschte Münze | Verschiedene Wurfsequenzen bewerten: a) $K$ → $57.1\%$, b) $KKKZ$ → $62.8\%$, c) $KZZZKZ$ → $12.3\%$ | P(Wurfsequenz) separat für faire *und* gefälschte Münze exakt berechnen |
| **9** | Urnenraten (ohne Zurücklegen) | a) Farbkombinationen berechnen, b) Rateplan: $P(T) \approx 63.3\%$, c) $P(UII\|GG) \approx 64.3\%$ | WS *ohne Zurücklegen* → 2. Zug hat andere Nenner als 1. Zug! |

---

## ⚠️ Prüfungsrelevante Hinweise

### Typische Aufgabentypen und wie man sie erkennt

| Aufgabentyp | Erkennungsmerkmal | Lösungsstrategie |
|-------------|-------------------|--------------------|
| «Umgekehrte» bedingte WS | «Wie wahrscheinlich ist *Ursache* $A$, wenn *Wirkung* $B$ beobachtet?» | **Satz von Bayes** mit Baumdiagramm |
| Medizinische Diagnostik | Test positiv/negativ, Sensitivität/Spezifität, Prävalenz | Bayes: $P(\text{krank}\|\text{Test}+) = \frac{P(T) \cdot \text{Sens.}}{P(T) \cdot \text{Sens.} + P(\overline{T}) \cdot (1-\text{Spez.})}$ |
| Spam / Klassifikation | Wort kommt in Spam häufiger vor, Schwellenwert | Naive Bayes: Merkmale als bedingt unabhängig annehmen |
| Urnen / Quellen-Identifikation | «Aus welcher Urne/Quelle stammt das Ergebnis?» | Baumdiagramm: 1. Stufe = Quelle, 2. Stufe = Beobachtung |
| Fehlerkorrektur (Kanal) | Bits werden mit WS $p$ umgedreht, Paritätsbit | Alle Fehlerszenarien (0, 2, 4 Bitfehler) aufzählen |

### 🚨 Häufige Fehlerquellen und Fallstricke

1. **$P(A|B) \neq P(B|A)$** — DER häufigste Fehler! «90% der Kranken testen positiv» ($P(+|K) = 0.9$) heisst **NICHT**, dass 90% der positiv Getesteten krank sind ($P(K|+) \neq 0.9$).
2. **Totale WS im Nenner vergessen:** Im Baumdiagramm müssen **alle** Pfade, die zu $B$ führen, aufsummiert werden — nicht nur der «interessante» Pfad.
3. **Apriori-WS ignorieren (Base Rate Neglect):** Die Ausgangslage $P(A)$ beeinflusst das Ergebnis massiv. Bei seltenen Krankheiten ($P(A) = 0.001$) ist selbst ein guter Test meist falsch-positiv.
4. **Bedingte Unabhängigkeit nicht prüfen:** Bei Naive Bayes darf man $P(A \cap B|S) = P(A|S) \cdot P(B|S)$ nur verwenden, wenn die Merkmale **unter der Bedingung $S$** unabhängig sind.
5. **WS ohne Zurücklegen falsch:** Bei Aufgabe 9 ändert sich nach dem 1. Zug der Nenner (z.B. $\frac{2}{3} \cdot \frac{1}{2}$ statt $\frac{2}{3} \cdot \frac{2}{3}$).

### 🧠 Merkregeln & Eselsbrücken

- **⭐ Baumdiagramm ist King:** Zeichne IMMER zuerst ein Baumdiagramm. Dann ist Bayes = 
  `Zielpfad ÷ Summe aller Pfade die bei B enden`
- **«Partition» = «Totale WS»:** Im Skript von Dr. Berger heisst es «Partition», in anderen Büchern «Satz von der totalen Wahrscheinlichkeit» — dasselbe Konzept.
- **«Seltene Krankheit → schlechter Test»:** Bei $P(A) \ll 1$ dominiert die Falsch-Positiv-Rate → $P(A|B)$ ist viel kleiner als man denkt.
- **Naive Bayes = Multiplikation der Likelihoods:** Bedingt unabhängige Merkmale darf man multiplizieren. Das macht Spam-Filter schnell und skalierbar.

### 📌 Formeln zum Auswendiglernen

$$\boxed{P(A|B) = \frac{P(A) \cdot P(B|A)}{P(B)} \quad \text{(Satz von Bayes)}}$$

$$\boxed{P(B) = P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A}) \quad \text{(Totale Wahrscheinlichkeit)}}$$

$$\boxed{P(A|B) = \frac{P(A) \cdot P(B|A)}{P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A})} \quad \text{(Bayes ausführlich)}}$$

---

## 🔗 Verbindung zu vorherigen/folgenden Wochen

### Rückbezug zu SW 01 und SW 02

| SW 01/02 Konzept | Wie es in SW 03 genutzt wird |
|-----------------|------------------------------|
| $P(A \cap B)$ (Schnitt, SW 01) | Steht im Zähler des Satzes von Bayes: $P(A \cap B) = P(A) \cdot P(B\|A)$ |
| $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ (SW 02) | Ausgangspunkt der Herleitung des Satzes von Bayes |
| **Produktregel** $P(A \cap B) = P(A) \cdot P(B\|A)$ (SW 02) | Wird im Zähler UND im Nenner (totale WS) des Satzes von Bayes benötigt |
| **Baumdiagramme** (SW 02) | Zentrales Werkzeug zum Aufstellen der Bayes-Formel |
| **Gegenereignis** $P(\overline{A}) = 1 - P(A)$ (SW 01) | Für die Partition $\{A, \overline{A}\}$ im Nenner benötigt |

### Vorausschau

| Folgewoche | Thema | Bezug zu SW 03 |
|-----------|-------|----------------|
| **SW 04** | Zufallsvariablen | Diskrete Verteilungen formalisieren die Apriori-/Aposteriori-Strukturen |
| **SW 05** | Randomisierte Algorithmen | Monte-Carlo-Methoden nutzen Bayes für probabilistische Entscheidungen |
| **SW 06** | Markov-Ketten | Übergangswahrscheinlichkeiten sind bedingte WS; Bayessche Updates = Zustandsschätzung |

### Wie baut der Stoff auf?

```
SW 01: Wahrscheinlichkeit (Grundlagen)
  │
  ├── Ergebnismenge Ω, P(E) = |E|/|Ω|
  │   │
  │   └── SW 02: Bedingte WS
  │       │   P(A|E) = P(A∩E)/P(E)
  │       │   Produktregel: P(A∩E) = P(E)·P(A|E)
  │       │   Unabhängigkeit, Baumdiagramme
  │       │
  │       └── SW 03: Satz von Bayes  ← WIR SIND HIER
  │           │   P(A|B) = P(A)·P(B|A) / P(B)
  │           │   Totale WS (Partition)
  │           │   Apriori → Aposteriori
  │           │
  │           ├── SW 04: Zufallsvariablen
  │           │   Verteilungen, Erwartungswert
  │           │
  │           ├── SW 05: Randomisierte Algorithmen
  │           │   Monte-Carlo, Las Vegas
  │           │
  │           └── SW 06: Markov-Ketten
  │               Übergangsmatrizen = bedingte WS
  │
  └── Zählprinzipien (n^k, C(n,k))
      └── SW 04+: Binomialverteilung, Kombinatorik
```

### Wichtigste Konzepte für später

- **Satz von Bayes** ist das Herzstück des maschinellen Lernens: Bayessche Netze, Naive Bayes Classifier, Partikelfilter.
- **Totale Wahrscheinlichkeit** wird bei Markov-Ketten (SW 06) als Übergangsgleichung verwendet.
- Die **Apriori → Aposteriori-Logik** kommt in jedem iterativen Lernalgorithmus vor.
- **Naive Bayes** (bedingte Unabhängigkeit der Merkmale) skaliert den Spam-Filter auf beliebig viele Wörter.

---

> **Quellen:** DMATH-CODE-Serie03.pdf, DMATH-CODE-Serie03-final.pdf, notes.md
