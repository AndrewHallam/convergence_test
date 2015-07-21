import numpy as np
from scipy.optimize import curve_fit
from scipy import stats

def regression_test(cutoff, data, regtype):
    for i in range(len(data[0])):
        
        x_data=np.empty(len(cutoff))    

        for j in range(len(cutoff)):
            x_data[j]=data[i][j]
                
        if regtype=='linear':    
            R=np.empty([len(data[0]),2])
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_data,cutoff)
            R[i]=(slope, intercept)
            return R
            
        elif regtype=='exponential':
            R=np.empty([len(data[0]),3])
            def func(x,a,b,c):
                return a*np.exp(-b * x)+c
            (popt, pcov) = curve_fit(func, x_data, cutoff)
            print popt
            R[i]=popt
            return R
        
        else:
            return ValueError("Right now regtype has to be linear or exponential :(")
