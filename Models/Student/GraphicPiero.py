import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab

class graph:
    plt.figure(figsize=(7.20, 5))
    labels = ['Muy buen jugador (30 clicks)', 'Buen jugador (20 clicks)', 'Jugador Promedio (10 clicks)',
              'Mal jugador (5 clicks)']
    values = [30, 20, 10, 5]
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Statistics')

    def autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}% ({v:d})'.format(p=pct, v=val)

        return my_autopct

    plt.pie(values, labels=labels, autopct=autopct(values))
    plt.title("Player Categories", y=1.00, x=-0.1)
    plt.legend(loc="upper left", bbox_to_anchor=(-0.40, 1.00))