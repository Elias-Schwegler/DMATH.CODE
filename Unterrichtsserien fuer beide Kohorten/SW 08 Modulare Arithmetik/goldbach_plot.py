"""
Goldbach-Zerlegung – EFFIZIENTE Version mit FFT-Faltung.

Mathematik:
  count(n) = Σ 1_prim(p) · 1_prim(n-p)  für p ≤ n/2
  Das ist eine Faltung (Convolution) des Primzahl-Indikator-Arrays!

  Naive Berechnung: O(n · π(n))     → ~1h für 10M
  FFT-Faltung:      O(n · log(n))   → ~10s für 10M  (1000x schneller!)

Trick: numpy.fft berechnet die Faltung über:
  count = IFFT(FFT(is_prime) · FFT(is_prime))
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
import sys


def sieve_of_eratosthenes(limit):
    """Sieb des Eratosthenes – O(n log log n)."""
    is_prime = np.zeros(limit + 1, dtype=np.float64)
    is_prime[2] = 1.0
    if limit >= 3:
        is_prime[3::2] = 1.0  # Alle ungeraden als Kandidaten
        for i in range(3, int(limit**0.5) + 1, 2):
            if is_prime[i]:
                is_prime[i*i::2*i] = 0.0
    return is_prime


def goldbach_fft(limit):
    """Goldbach-Zählung via FFT-Faltung – O(n log n)."""
    print(f"Sieb des Eratosthenes bis {limit:,}...")
    t0 = time.time()
    is_prime = sieve_of_eratosthenes(limit)
    n_primes = int(is_prime.sum())
    print(f"  {n_primes:,} Primzahlen in {time.time()-t0:.2f}s")

    print(f"FFT-Faltung (Autokorrelation)...")
    t0 = time.time()

    # Faltung via FFT: count[n] = Σ is_prime[k] · is_prime[n-k]
    # Nutze rfft (real FFT) für Speicher-Effizienz
    ft = np.fft.rfft(is_prime, n=2 * len(is_prime))
    conv = np.fft.irfft(ft * ft)
    # conv[n] = Anzahl Zerlegungen von n in p + q (mit p,q prim, Reihenfolge zählt)
    counts_raw = np.round(conv[:limit + 1]).astype(np.int64)

    print(f"  FFT fertig in {time.time()-t0:.2f}s")

    # Nur gerade Zahlen ab 4
    even_idx = np.arange(4, limit + 1, 2)
    counts = counts_raw[even_idx]

    # counts zählt (p,q) und (q,p) separat → dividiere durch 2
    # Ausnahme: wenn p = q = n/2 und beide prim → wird nur 1x gezählt nach /2
    # Korrektur: counts zählt geordnete Paare, wir wollen ungeordnete
    # Für n = p+q mit p<q: wird 2x gezählt. Für p=q: wird 1x gezählt.
    # → (counts + selbst) / 2, wobei selbst = 1 wenn n/2 prim
    half_primes = is_prime[(even_idx // 2).astype(int)]
    counts_unordered = (counts + half_primes.astype(np.int64)) // 2

    return even_idx, counts_unordered


def plot_goldbach(limit=10_000_000):
    """Scatter-Plot der Goldbach-Zerlegungen."""
    t_total = time.time()
    even_numbers, counts = goldbach_fft(limit)

    print(f"Erstelle Plot ({len(even_numbers):,} Punkte)...")
    t0 = time.time()

    fig, ax = plt.subplots(figsize=(14, 8))

    # Punkt-Grösse/Transparenz an Datenmenge anpassen
    if limit >= 5_000_000:
        s, alpha = 0.01, 0.15
    elif limit >= 1_000_000:
        s, alpha = 0.03, 0.25
    else:
        s, alpha = 0.15, 0.4

    ax.scatter(even_numbers, counts,
               s=s, c='steelblue', alpha=alpha, linewidths=0, rasterized=True)

    ax.set_xlabel('Gerade Zahl n', fontsize=14)
    ax.set_ylabel('Anzahl Goldbach-Zerlegungen', fontsize=14)
    ax.set_title('Für grosse gerade Zahlen gibt es eine tendenziell wachsende Anzahl von\n'
                 'Goldbach-Zerlegungen', fontsize=15)
    ax.set_xlim(0, limit * 1.02)
    ax.set_ylim(0, None)
    ax.grid(True, alpha=0.15)

    plt.tight_layout()
    outfile = f'goldbach_zerlegungen_{limit // 1000}k.png'
    plt.savefig(outfile, dpi=250)
    print(f"  Plot gespeichert: {outfile} ({time.time()-t0:.1f}s)")
    print(f"\nTotal: {time.time()-t_total:.1f}s")


if __name__ == '__main__':
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    plot_goldbach(limit)
