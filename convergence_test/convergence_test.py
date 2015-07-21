from data_extract import cutoff_data, entropy_data, expectation_data, overlap_data
from regression_test import regression_test

def convergence_test(data_files, cutoff_files, filename, exp_type, regtype):
    file= open(filename,'w')
    if exp_type == 'entropy':
        (time,data)=entropy_data(data_files)
        
    elif exp_type == 'expectation':
        (time,data)=expectation_data(data_files)
        
    elif exp_type == 'overlap':
        (time,data)=overlap_data(data_files)
        
    else:
        return ValueError('I can only look at entropy, expectation or overlap files!')
        
    cutoff=cutoff_data(cutoff_files)
    R = regression_test(cutoff, data, regtype)
    for i in range(len(time)):
        file.write("%s" % time[i])
        if regtype=='linear':
            file.write("%s" % R[i][0])
            file.write("%s\n" % R[i][1])
        if regtype=='exponential':
            file.write("%s" % R[i][0])
            file.write("%s" % R[i][1])
            file.write("%s\n" % R[i][2])
        else:
            return ValueError("How did you make it this far? There should have already been an error...")

    file.close
    
convergence_test(("C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C8 min S val 5e-4\overlap.dat",
"C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C4 min S val 5e-4\entropy.dat", 
"C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C6 min S val 5e-4\entropy.dat",
"C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C8 min S val 5e-4\entropy.dat"),
("C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C4 min S val 5e-4\iTEBD_sim.cpp",
"C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C6 min S val 5e-4\iTEBD_sim.cpp",
"C:\Users\Andrew\Dropbox\MRes\LL\ll_001_coupling\R4\ll_001_coupling_R4_C8 min S val 5e-4\iTEBD_sim.cpp"),
'test.txt','entropy','linear')
    