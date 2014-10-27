#
#  
#    problem_set2_solutions.py
#    Camilo Buscaron 10/27/2014

#  DESCRIPTION
#    Open, view, and analyze action potentials recorded during a behavioral
#    task. Code to create tuning curves.
#

#Helper code to import some functions we will use
import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as mlab
from scipy import optimize
from scipy import stats


def load_experiment(filename):
    """
    load_experiment takes the file name and reads in the data.  It returns a
    two-dimensional array, with the first column containing the direction of
    motion for the trial, and the second column giving you the time the
    animal began movement during thaht trial.
    """
    data = np.load(filename)[()];
    return np.array(data)

def load_neuraldata(filename):
    """
    load_neuraldata takes the file name and reads in the data for that neuron.
    It returns an arary of spike times.
    """
    data = np.load(filename)[()];
    return np.array(data)
    
def bin_spikes(trials, spk_times, time_bin):
    """
    bin_spikes takes the trials array (with directions and times) and the spk_times
    array with spike times and returns the average firing rate for each of the
    eight directions of motion, as calculated within a time_bin before and after
    the trial time (time_bin should be given in seconds).  For example,
    time_bin = .1 will count the spikes from 100ms before to 100ms after the 
    trial began.
    
    dir_rates should be an 8x2 array with the first column containing the directions
    (in degrees from 0-360) and the second column containing the average firing rate
    for each direction
    """
    
    spikes_per_trial =[]
    
    i = 0
    
    for y in range(len(trials)):
        for x in range(len(spk_times)):
            if((spk_times[x]>= trials[y,1] - time_bin) & (spk_times[x]<= trials[y,1] + time_bin)):
                i = i + 1
        spikes_per_trial.append(i)
        i = 0
    
    
    directions = np.arange(0,360,45)
    
    ##print(len(directions))
    ##print directions
    
    numberperdirection = []
    i = 0
    
    averageovertrials = []
    w = 0
    
    dir_rate =[]
    
    
    for y in range(len(directions)):
        for x in range(len(trials)):
            if(directions[y]==trials[x,0]):
                i = spikes_per_trial[x] + i
                w = w + 1
        averageovertrials.append((i/float(w))) 
        dir_rate.append((i/float(w))/(time_bin*2))
        numberperdirection.append(i)
        i=0
        w=0
        
    
    dir_rates = np.column_stack((directions,dir_rate))
        
    print(len(numberperdirection))
    print numberperdirection
    
    print(len(averageovertrials))
    print averageovertrials
    
    print(len(dir_rate))
    print dir_rate
    
    return dir_rates
    ##return dir_rates
    
def plot_tuning_curves(direction_rates, title):
    """
    This function takes the x-values and the y-values  in units of spikes/s 
    (found in the two columns of direction_rates) and plots a histogram and 
    polar representation of the tuning curve. It adds the given title.
    """

    
def roll_axes(direction_rates):
    """
    roll_axes takes the x-values (directions) and y-values (direction_rates)
    and return new x and y values that have been "rolled" to put the maximum
    direction_rate in the center of the curve. The first and last y-value in the
    returned list should be set to be the same. (See problem set directions)
    Hint: Use np.roll()
    """
   
    
    return new_xs, new_ys, roll_degrees    
    

def normal_fit(x,mu, sigma, A):
    """
    This creates a normal curve over the values in x with mean mu and
    variance sigma.  It is scaled up to height A.
    """
    n = A*mlab.normpdf(x,mu,sigma)
    return n

def fit_tuning_curve(centered_x,centered_y):
    """
    This takes our rolled curve, generates the guesses for the fit function,
    and runs the fit.  It returns the parameters to generate the curve.
    """

    return p
    


def plot_fits(direction_rates,fit_curve,title):
    """
    This function takes the x-values and the y-values  in units of spikes/s 
    (found in the two columns of direction_rates and fit_curve) and plots the 
    actual values with circles, and the curves as lines in both linear and 
    polar plots.
    """
    

def von_mises_fitfunc(x, A, kappa, l, s):
    """
    This creates a scaled Von Mises distrubition.
    """
    return A*stats.vonmises.pdf(x, kappa, loc=l, scale=s)


    
def preferred_direction(fit_curve):
    """
    The function takes a 2-dimensional array with the x-values of the fit curve
    in the first column and the y-values of the fit curve in the second.  
    It returns the preferred direction of the neuron (in degrees).
    """
  
    return pd
    
        
##########################
#You can put the code that calls the above functions down here    
if __name__ == "__main__":
    trials = load_experiment('trials.npy')   
    spk_times = load_neuraldata('example_spikes.npy') 

