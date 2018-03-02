import numpy as np
import matplotlib.pyplot as plt

x = 0.1
xN = 1
xR = 1
T = 130
N = 100

V = 2
xP = np.sqrt(V) * np.random.randn(N) + x

zOut = np.zeros(T)
xOut = np.zeros(T)
xEst = np.zeros(T)
xEstOut = np.zeros(T)
zOut[0] = x**2 / 20 + np.sqrt(V) * np.random.randn(1)
xOut[0] = x
xEst[0] = x

xPUpdate = np.zeros(N)
zUpdate = np.zeros(N)
wP = np.zeros(N)

for t in range(1, T):
    x = 0.5 * x + 25 * x / (1 + x**2) + 8 * np.cos(1.2*(t-1)) \
        + np.sqrt(xN) * np.random.randn(1)
    z = x**2 / 20 + np.sqrt(xR) * np.random.randn(1)

    for i in range(N):
        xPUpdate[i] = 0.5 * xP[i] + 25 * xP[i] / (1 + xP[i]**2) \
                      + 8 * np.cos(1.2*(t-1)) \
                      + np.sqrt(xN) * np.random.randn(1)
        zUpdate[i] = xPUpdate[i]**2 / 20
        wP[i] = (1/np.sqrt(2*np.pi*xR)) \
                * np.exp(-(z - zUpdate[i])**2/(2*xR))
    wP = wP / np.sum(wP)

    for i in range(N):
        cdf = np.cumsum(wP)
        s = np.random.rand(1)
        #print(cdf)
        #print(s)
        #print(s < cdf)
        ix = np.where(
            s<cdf
        )[0][0]
        xP[i] = xPUpdate[ix]

    xEst[t] = np.mean(xP)
    xOut[t] = x
    zOut[t] = z


plt.plot(range(T), xOut, '.-b',
         range(T), xEst, '-.r',
         linewidth=3)

plt.show()
