from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def main():
    x = np.linspace(-0.2,0.2,10000)
    y = np.sin(1/x)
    plt.plot(x,y,)
    plt.show()
if __name__ == '__main__':
    main()