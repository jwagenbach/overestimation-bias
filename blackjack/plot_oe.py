import numpy as np 
import matplotlib.pyplot as mpl
from scipy.stats import sem

fig, ax = mpl.subplots()
axins = ax.inset_axes([0.4, 0.1, 0.5, 0.5])
mpl.grid()
x = np.linspace(0, 100000, 100000)

def smoothen(x, w=300):
    head = []
    for i in range(1,w):
        head.append(np.mean(x[0:i]))
    tail = np.convolve(x, np.ones(w), 'valid') / w
    return list(np.concatenate([head, list(tail)]))

def plot(data, color, name):
    _, overestimation, _, oe_error = data
    lower_avg = overestimation - oe_error
    upper_avg = overestimation + oe_error
    overestimation = smoothen(overestimation)
    upper_avg = smoothen(upper_avg)
    lower_avg = smoothen(lower_avg)
    mpl.plot(x, overestimation, c=color,linestyle='solid', label=name)
    mpl.fill_between(x, lower_avg, upper_avg, alpha=.3, linewidth=0, color= color)

plot(np.load("./data/standard.npy", allow_pickle=True), "blue", "standard")
plot(np.load("./data/lr_05.npy", allow_pickle=True), "orange", "lr 0.05")
plot(np.load("./data/double_q.npy", allow_pickle=True), "green", "double q")
plot(np.load("./data/avgr.npy", allow_pickle=True), "purple", "avg r")
plot(np.load("./data/SCQL.npy", allow_pickle=True), "yellow", "SCQL")


mpl.title(r'Performance of difference algorithms')
mpl.axhline(y = 0, color = 'black', linestyle = '--')
mpl.text(s="optimum",y=-0.053, x=0)
mpl.legend(loc='lower right', ncol=3)
mpl.show()