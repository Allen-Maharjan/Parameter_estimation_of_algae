import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

def plotting(file_name):
    data = pd.read_csv("{}.csv".format(file_name))
    time = (data['hour'])
    divide = data['A/A0']
    absorbance = data['abs']
    lnabs = np.log(divide)
    plt.title('graph of {} with A/A0'.format(file_name))
    plt.grid()
    plt.plot(time,absorbance)
    plt.show()
    plt.grid()
    plt.title('graph of {} with ln(A/A0)'.format(file_name))
    plt.plot (time,lnabs)
    plt.show()
    
plotting('2A')
plotting("BNP1")
plotting("BNP2")
plotting("DPR2CV")
plotting("DPR2SC")
plotting("GNP3")