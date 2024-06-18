import numpy as np
import pandas as pd

import statsmodels
import statsmodels.api as sm
from statsmodel.tsa.stattools import  coint, adfuller


# Generating random points from a normal distribution of prices. (Price vs Prob density)

def generate_datapoints(params):
    mu = params[0]
    sigma = params[1]
    return np.random.normal(mu , sigma)

#Stationarity = Time Series parameter don't change with time 

#Series A 

params = (0,1)
T=100

A = pd.Series(index=range(T))
A.name = 'A'

for t in range(T):
    A[t] = generate_datapoints(params)


plt.plot(A)
plt.xlabel("Time")
plt.ylabel("value")
plt.legen(['Series A'])



#Series B 


T=100

B = pd.Series(index=range(T))
B.name = 'B'

params = (t*0.1 , 1)
#now parameters vary over time so non-stationarity comes

for t in range(T):
    B[t] = generate_datapoints(params)


plt.plot(B)
plt.xlabel("Time")
plt.ylabel("value")
plt.legen(['Series B'])




#Check for stationarity 

def check_stn(X , cutoff = 0.01):  # i.e 1 percent
    pvalue = adfuller(X)[1]
    if pvalue < cutoff :
        print("Sationary")
    
    else:
        print("Not Stationary")


check_stn(A)
check_stn(B)



#Caution when parameters are of the form sint , even though its non-sationary graph is very similar to stationarity and even test fails here === Bro! WE have limitations


#Certain other tests like Cointegrations etc are too needed (NOT Coded tho)