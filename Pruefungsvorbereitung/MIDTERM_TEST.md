# DMATH.CODE – Midterm Test (SW 01–08)

> **Modul:** DMATH-CODE · Diskrete Mathematik
> **Umfang:** SW 01 (Wahrscheinlichkeit) bis SW 08 (Modulare Arithmetik)
> **Dauer:** ca. 90 Minuten
> **Hilfsmittel:** Keine (ausser wo angegeben)
> **Hinweis:** Zeige deinen Lösungsweg! Nur das Endergebnis gibt keine volle Punktzahl.

---

## Teil A: Verständnisfragen (20 Punkte)

> Kurze Antworten – max. 2-3 Sätze pro Frage.

### A1 (2P) – Wahrscheinlichkeit
Was ist der Unterschied zwischen einem **Laplace-Experiment** und einem **nicht-uniformen** Zufallsexperiment? Nenne je ein Beispiel.

### A2 (2P) – Bedingte Wahrscheinlichkeit
Erkläre in eigenen Worten: Warum sind **disjunkte** Ereignisse ($A \cap B = \emptyset$) **nicht** unabhängig (sofern $P(A), P(B) > 0$)?

### A3 (2P) – Satz von Bayes
Was ist der Unterschied zwischen **Apriori-** und **Aposteriori-Wahrscheinlichkeit**? Gib ein Beispiel.

### A4 (2P) – Zufallsvariablen
Welche Verteilung wählst du in den folgenden Situationen? (Nur Name + Begründung in 1 Satz)
- a) Ein Passwort besteht aus 8 Zeichen (je 26 Möglichkeiten). Wie wahrscheinlich ist ein Treffer beim zufälligen Raten?
- b) Ein Server erhält im Schnitt 5 Anfragen pro Sekunde. Wie wahrscheinlich sind genau 8 Anfragen?
- c) Aus 100 Festplatten (12 defekt) werden 10 getestet. Wie viele defekte erwartet man?

### A5 (2P) – Randomisierte Algorithmen
Erkläre den Unterschied zwischen einem **Las Vegas** und einem **Monte Carlo** Algorithmus. Welche Eigenschaft ist bei welchem Typ die Zufallsvariable?

### A6 (2P) – Markov-Ketten
Was bedeutet die **Markov-Eigenschaft** (Gedächtnislosigkeit)? Warum ist sie wichtig für die Übergangsmatrix?

### A7 (2P) – Markov-Ketten
Erkläre: Warum kann eine **nicht-irreduzible** Markov-Kette **mehrere** invariante Verteilungen haben?

### A8 (2P) – Matrizenalgebra
Warum muss man bei der **Potenzmethode** den Vektor nach jedem Schritt **normieren**? Was passiert sonst?

### A9 (2P) – Modulare Arithmetik
Erkläre, warum $-14 \text{ mod } 5 = 1$ und **nicht** $-4$. Was ist die Regel für den Rest bei negativen Zahlen?

### A10 (2P) – Modulare Arithmetik
Warum ist der **Square-and-Multiply** Algorithmus so wichtig für die RSA-Verschlüsselung? Was wäre die Alternative und warum ist sie nicht praktikabel?

---

## Teil B: Entscheidungsfragen (15 Punkte)

> Welche Methode/Formel/Verteilung ist die richtige? Begründe kurz.

### B1 (3P) – Welche Verteilung?

Ordne jeder Situation die passende Verteilung zu und gib die Parameter an:

| Situation | Verteilung? | Parameter? |
|---|---|---|
| a) Ein Hacker versucht 1000 Passwörter, jedes mit $p = 0.001$ Erfolgswahrscheinlichkeit. Wie viele Treffer? | | |
| b) Ein Qualitätstest: Aus 500 Chips (30 defekt) werden 20 zufällig gezogen. Wie viele defekte? | | |
| c) Ein Student rät bei 25 Multiple-Choice-Fragen (je 4 Antworten). Wie oft richtig? | | |
| d) Wie viele Versuche braucht man im Schnitt, bis man bei einer Lotterie (Chance 1:1000) gewinnt? | | |
| e) In einem Datencenter fallen im Schnitt 2 Server pro Tag aus. Wie wahrscheinlich sind 0 Ausfälle? | | |

### B2 (3P) – Bayes oder nicht?

Entscheide für jede Situation: Brauchst du den **Satz von Bayes**, die **totale Wahrscheinlichkeit**, oder reicht die **Definition** der bedingten Wahrscheinlichkeit?

- a) $P(\text{krank}) = 0.01$, $P(\text{Test+} | \text{krank}) = 0.95$, $P(\text{Test+} | \text{gesund}) = 0.03$. Gesucht: $P(\text{krank} | \text{Test+})$.
- b) Ein Würfel wird geworfen. Gesucht: $P(\text{gerade} | \text{grösser als 3})$.
- c) Gegeben die Werte aus (a). Gesucht: $P(\text{Test+})$.

### B3 (3P) – Markov-Kette klassifizieren

Gegeben der Graph:
```
    1 ←→ 2
    ↑     ↓
    4 ←→ 3
```
(Alle Kanten sind bidirektional, $p = 1/\text{Grad}$ für alle Übergänge)

- a) Ist die Kette **irreduzibel**? Begründe.
- b) Ist die Kette **aperiodisch**? Begründe. (Hinweis: Bestimme $N_1$)
- c) Was bedeutet dein Ergebnis für die invariante Verteilung?

### B4 (3P) – Square-and-Multiply vs. naiv

Für die Berechnung von $7^{100} \text{ mod } 13$:
- a) Wie viele Multiplikationen braucht die **naive** Methode?
- b) Wandle 100 in **Binär** um.
- c) Wie viele **Quadrierungen** und **Multiplikationen** braucht Square-and-Multiply?

### B5 (3P) – Welche Methode für invariante Verteilung?

Du hast eine Markov-Kette mit:
- a) 3 Zuständen → Welche Methode?
- b) 500 Zuständen → Welche Methode?
- c) Eine Matrix die KEINE stochastische Matrix ist (Populationsmodell) → Welche Methode?

Begründe jeweils kurz.

---

## Teil C: Rechenaufgaben (45 Punkte)

### C1 (5P) – Wahrscheinlichkeit

Ein Passwort besteht aus **4 Ziffern** (0–9).

- a) (1P) Wie gross ist $|\Omega|$?
- b) (2P) Wie gross ist die Wahrscheinlichkeit, dass **alle 4 Ziffern verschieden** sind?
- c) (2P) Wie gross ist die Wahrscheinlichkeit, dass **mindestens zwei Ziffern gleich** sind?

---

### C2 (5P) – Bedingte Wahrscheinlichkeit

In einem IT-System sind 70% der Nutzer intern und 30% extern. Interne Nutzer verursachen mit $P = 0.02$ einen Sicherheitsvorfall, externe mit $P = 0.15$.

- a) (2P) Zeichne ein **Baumdiagramm** und berechne die Wahrscheinlichkeit für einen Sicherheitsvorfall.
- b) (3P) Es wird ein Sicherheitsvorfall entdeckt. Wie wahrscheinlich war es ein **externer** Nutzer? (Satz von Bayes)

---

### C3 (5P) – Zufallsvariablen

Ein Router leitet Pakete weiter. Jedes Paket wird unabhängig mit $p = 0.05$ fehlerhaft übertragen. Es werden $n = 20$ Pakete gesendet.

- a) (1P) Welche Verteilung? Gib die Parameter an.
- b) (2P) Berechne $P(X = 0)$, also die Wahrscheinlichkeit dass **kein** Paket fehlerhaft ist.
- c) (2P) Berechne $P(X \geq 2)$, also die Wahrscheinlichkeit dass **mindestens 2** fehlerhaft sind.

---

### C4 (5P) – Erwartete Komplexität

Eine Suchfunktion durchsucht eine **sortierte** Liste der Länge $n = 6$.
- Das gesuchte Element ist mit gleicher Wahrscheinlichkeit an jeder Position.
- An Position $i$ braucht die binäre Suche $c_i$ Vergleiche:

| Position | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Vergleiche $c_i$ | 3 | 2 | 3 | 1 | 3 | 2 |

- a) (2P) Berechne die **erwartete Anzahl Vergleiche** $E(X)$.
- b) (1P) Wie heisst dieser Algorithmus-Typ: Las Vegas oder Monte Carlo? Warum?
- c) (2P) Wie oft müsste man einen Monte-Carlo-Algorithmus mit Erfolgswahrscheinlichkeit $p = 0.6$ wiederholen, um eine Gesamterfolgswahrscheinlichkeit von mindestens $99\%$ zu erreichen?

---

### C5 (8P) – Markov-Kette

Gegeben die Übergangsmatrix:

$$T = \begin{pmatrix} 0 & 0.5 & 0.5 \\ 0.3 & 0 & 0.7 \\ 0.4 & 0.6 & 0 \end{pmatrix}$$

- a) (1P) Prüfe: Ist $T$ eine gültige stochastische Matrix?
- b) (3P) Berechne die Verteilung $\vec{v}_1$ und $\vec{v}_2$ bei Startverteilung $\vec{v}_0 = (1, 0, 0)$.
- c) (4P) Berechne die **invariante Verteilung** $\vec{\pi}$ durch Lösen des LGS $\vec{\pi} \cdot T = \vec{\pi}$ mit $\sum \pi_i = 1$.

---

### C6 (5P) – Matrizenmultiplikation

Gegeben:

$$A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix}$$

- a) (2P) Berechne $A \cdot B$.
- b) (2P) Berechne $B \cdot A$.
- c) (1P) Ist $A \cdot B = B \cdot A$? Was zeigt dieses Beispiel?

---

### C7 (5P) – Modulares Rechnen

- a) (2P) Berechne **ohne Taschenrechner:** $(247 \cdot 583 + 1291) \text{ mod } 7$
- b) (3P) Berechne mit **Square-and-Multiply:** $3^{13} \text{ mod } 7$.
  Zeige jeden Schritt (Binärdarstellung, Q/M-Operationen, Zwischenergebnisse mod 7).

---

### C8 (7P) – Gemischte Anwendung

Ein Unternehmen hat ein Intrusion Detection System (IDS):
- **Angriffs-Apriori:** $P(\text{Angriff}) = 0.005$
- **Erkennungsrate:** $P(\text{Alarm} | \text{Angriff}) = 0.92$
- **Fehlalarm-Rate:** $P(\text{Alarm} | \text{kein Angriff}) = 0.08$

- a) (2P) Berechne $P(\text{Alarm})$ (totale Wahrscheinlichkeit).
- b) (3P) Berechne $P(\text{Angriff} | \text{Alarm})$ (Satz von Bayes).
- c) (2P) Der IDS-Log wird mit einer Hashfunktion $H(x) = x \text{ mod } 13$ gespeichert. Berechne die Hash-Adressen für die Alarm-IDs 247, 1039 und 598.

---

## Teil D: Bonus (10 Punkte)

### D1 (5P) – Populationsdynamik

Eine Tierpopulation hat 3 Lebensphasen: Jung (J), Erwachsen (E), Alt (A).

Leslie-Matrix: $L = \begin{pmatrix} 0 & 0.2 & 0 \\ 4 & 0 & 0 \\ 0 & 0.8 & 0.5 \end{pmatrix}$

(Leserichtung: Zeile = Von, Spalte = Nach. Z.B. Von E nach J: 4 Nachkommen)

- a) (2P) Interpretiere die Matrix: Was bedeuten die Einträge $L_{2,1} = 4$ und $L_{3,3} = 0.5$?
- b) (3P) Wenn der dominante Eigenwert $\lambda \approx 1.12$ ist: Überlebt die Population langfristig? Welche Wachstumsrate hat sie pro Zeitschritt?

### D2 (5P) – Modulare Wurzeln

- a) (3P) Bestimme **alle** Quadratwurzeln von $2 \text{ mod } 7$, d.h. alle $x \in \{0, 1, ..., 6\}$ mit $x^2 \text{ mod } 7 = 2$.
- b) (2P) Hat die Zahl $5$ eine Quadratwurzel mod 7? Begründe durch systematisches Durchprobieren.

---

## Checkliste nach dem Test

Wenn du fertig bist, prüfe:

- [ ] Alle Wahrscheinlichkeiten zwischen 0 und 1?
- [ ] Bei "mindestens"-Aufgaben: Gegenereignis verwendet?
- [ ] Übergangsmatrix: Zeilensummen = 1?
- [ ] Invariante Verteilung: $\sum \pi_i = 1$ und $\vec{\pi} \cdot T = \vec{\pi}$?
- [ ] Modulare Arithmetik: Rest immer $\geq 0$?
- [ ] Square-and-Multiply: Mod nach jedem Schritt genommen?
- [ ] Lösungsweg vollständig gezeigt?

---

**Viel Erfolg!** 🍀
