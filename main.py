from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fast')


def zaehlen(n, quelle, hilfsstapel, zielstapel):  # zählt die Rekursionen
    if n > 0:
        return 1 + zaehlen(n - 1, quelle, zielstapel, hilfsstapel) + zaehlen(n - 1, hilfsstapel, quelle, zielstapel)
    else:
        return 0


if __name__ == "__main__":
    n = 0  # Anzahl der Ringe auf dem ursprünglichem Stapel

    # Erstellen von Arrays, um den Graphen zu visualisieren
    menge = np.array([0])
    rekursionen = np.array([0])
    ypoints = np.array([0])

    while 1:
        n = n + 1  # Erhöhe Turmanzahl
        start = timer()  # Zeit messen
        ergebnis = zaehlen(n, 0, 0, 0)  # Aufruf der Zähl-Methode
        t = timer() - start # Differenz Systemzeit und Startzeit
        print(n, ergebnis, t)

        # Hinzufügen der temporären Ergebnisse zu den Arrays
        menge = np.append(menge, n)
        rekursionen = np.append(rekursionen, ergebnis)
        ypoints = np.append(ypoints, t)

        # Graphen konfigurieren
        fig, ax1 = plt.subplots()
        plt.title('Türme von Hanoi')
        color = 'tab:red'
        ax1.set_xlabel('Anzahl der Ringe')
        ax1.set_ylabel('Zeit in s', color=color)
        ax1.plot(menge, ypoints, color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        plt.yscale('log')

        ax2 = ax1.twinx()

        color = 'tab:blue'
        ax2.set_ylabel('Anzahl der Rekursionen', color=color)
        ax2.plot(menge, rekursionen, color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        plt.yscale('log')

        fig.tight_layout()
        plt.show()
