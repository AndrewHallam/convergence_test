import numpy as np

def cutoff_data(cutoff_files):
    
    cutoff=np.empty(len(cutoff_files)) 
    
    length = 3 
    
    for i in range(len(cutoff_files)):
        
        with open(cutoff_files[i]) as searchfile:
            
            for line in searchfile:
                
                left,sep,right = line.partition('cutoff=')
                
                if sep: # True iff 'cutoff=' in line
                    
                    cutoff[i]=right[:length]
                    
    return cutoff


def entropy_data(data_files):
 
    time_data = np.loadtxt(data_files[0],usecols=[0],unpack=True)
    
    ent_data=np.zeros([(len(data_files)-1),len(time_data)])    
    
    for i in (range(len(data_files)-1)):
        
        ent_data[i,]= np.loadtxt(data_files[i+1],usecols=[0],unpack=True)
          
    return (time_data, ent_data)

                            
def expectation_data(data_files):
    
    time_data = np.loadtxt(data_files[0],usecols=[0],unpack=True)
    
    exp_data=np.zeros([len(data_files),len(time_data)])    

     
    for i in len(data_files):
        
        exp_data[i,]= np.loadtxt(data_files[i],usecols=[1],unpack=True)
          
    return (time_data, exp_data)

                
def overlap_data(data_files): 
    
    time_data = np.loadtxt(data_files[0],usecols=[0],unpack=True)

    overlap_data=np.zeros([len(data_files),len(time_data)])    
     
    for i in len(data_files):
        
        overlap_data[i,]= np.loadtxt(data_files[i],usecols=[3],unpack=True)
          
    return (time_data, overlap_data)
