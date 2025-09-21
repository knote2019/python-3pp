import numpy as np
import matplotlib.pyplot as plot

data = [[100, 100, 99, 95], [66, 71, 76, 82], [73, 75, 79, 81],
        [17, 23, 42, 55], [12, 18, 26, 20]]

data = list(map(list, zip(*data)))
columns = ('2010', '2012', '2014', '2016')

rows = ("Make Calls", "Take Photos", "Texting", "Internet",
        "Playing games")[::-1]

fig, axs = plot.subplots(2, 2)
axs[0, 0].pie(data[0], labels=rows, autopct='%1.1f%%', shadow=True)
axs[0, 0].set_title(columns[0])
axs[0, 1].pie(data[1], labels=rows, autopct='%1.1f%%', shadow=True)
axs[0, 1].set_title(columns[1])
axs[1, 0].pie(data[2], labels=rows, autopct='%1.1f%%', shadow=True)
axs[1, 0].set_title(columns[2])
axs[1, 1].pie(data[3], labels=rows, autopct='%1.1f%%', shadow=True)
axs[1, 1].set_title(columns[3])

plot.show()
