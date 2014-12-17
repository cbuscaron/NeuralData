#
#  NAME
#    problem_set4_solutions.py
#
#
#  DESCRIPTION
#    In Problem Set 4, you will classify EEG data into NREM sleep stages and
#    create spectrograms and hypnograms.
#
#
from __future__ import division
import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as m


def load_examples(filename):
    """
    load_examples takes the file name and reads in the data.  It returns an
    array containing the 4 examples of the 4 stages in its rows (row 0 = REM;
    1 = stage 1 NREM; 2 = stage 2; 3 = stage 3 and 4) and the sampling rate for
    the data in Hz (samples per second).
    """
    data = np.load(filename)
    return data['examples'], int(data['srate'])

def load_eeg(filename):
    """
    load_eeg takes the file name and reads in the data.  It returns an
    array containing EEG data and the sampling rate for
    the data in Hz (samples per second).
    """
    data = np.load(filename)
    return data['eeg'], int(data['srate'])

def load_stages(filename):
    """
    load_stages takes the file name and reads in the stages data.  It returns an
    array containing the correct stages (one for each 30s epoch)
    """
    data = np.load(filename)
    return data['stages']

def plot_example_psds(example,rate):
    """
    This function creates a figure with 4 lines to show the overall psd for 
    the four sleep examples. (Recall row 0 is REM, rows 1-3 are NREM stages 1,
    2 and 3/4)
    """
    plt.figure()
    for i in range(4):
        Pxx, freqs = m.psd(examples[i,:],NFFT=512,Fs=rate)
        plt.plot(freqs,Pxx/sum(Pxx),hold=True)
    plt.xlim((0,30))
    plt.legend(('REM','NREM 1','NREM 2','NREM 3/4'))    

def plot_example_spectrograms(example,rate):
    """
    This function creates a figure with spectrogram sublpots to of the four
    sleep examples. (Recall row 0 is REM, rows 1-3 are NREM stages 1,
    2 and 3/4)
    """
    plt.figure()
    for i in range(4):
        plt.subplot(2,2,i+1)
        Pxx, freqs, bins, im = plt.specgram(examples[i,:],NFFT=512,Fs=rate)
        if i == 0:
            plt.title('REM example')
        else:
            plt.title('NREM ' + str(i) + ' example')
        plt.ylim((0,40))
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
    
    return bins
        
        
    
def classify_epoch(epoch,rate):
    """
    This function returns a sleep stage classification (integers: 1 for NREM
    stage 1, 2 for NREM stage 2, and 3 for NREM stage 3/4) given an epoch of 
    EEG and a sampling rate.
    """
    Pxx, freqs = m.psd(epoch,NFFT=256,Fs=rate)
    nPxx = Pxx/float(sum(Pxx))
    delta_f = plt.find((0<freqs) & (freqs <=3))
 #   delta_power = sum(Pxx[delta_f])
    ndelta_power = sum(nPxx[delta_f])
    spindles_f = plt.find((11 <= freqs) & (freqs <= 15))
 #   spindle_power = sum(Pxx[spindles_f])
    nspindle_power = sum(nPxx[spindles_f])
  #  ratio = spindle_power/delta_power
    
    if (ndelta_power > 0.8): #suggests stage 3
        stage = 3
    else:  
        if (nspindle_power > 0.03): #suggests stage 2
            stage = 2
        else: 
            stage = 1
    
    return stage


def plot_hypnogram(eeg, stages, srate):
    """
    This function takes the eeg, the stages and sampling rate and draws a 
    hypnogram over the spectrogram of the data.
    """
    
    fig,ax1 = plt.subplots()  #Needed for the multiple y-axes
    #Use the specgram function to draw the spectrogram as usual
    Pxx, freqs, bins, im = plt.specgram(eeg,NFFT=512,Fs=srate) 

    #Label your x and y axes and set the y limits for the spectrogram
    plt.xlabel('Time (sec)')
    plt.ylim((0,30))
    plt.ylabel('Frequency (Hz)')

    
    ax2 = ax1.twinx() #Necessary for multiple y-axes
    #Use ax2.plot to draw the hypnogram.  Be sure your x values are in seconds
    #HINT: Use drawstyle='steps' to allow step functions in your plot
    ax2.plot(np.arange(0,len(stages)*30,30),stages,drawstyle='steps')

    #Label your right y-axis and change the text color to match your plot
    ax2.set_ylabel('NREM Stage',color='b')

 
    #Only display the possible values for the stages
    plt.xlim(0,3600)
    plt.ylim((0.5,3.5))
    ax2.set_yticks(np.arange(1,4))
    
    #Change the left axis tick color to match your plot
    for t1 in ax2.get_yticklabels():
        t1.set_color('b')
    
    #Title your plot    
    plt.title('Hypnogram - Practice Data')

        
def classifier_tester(classifiedEEG, actualEEG):
    """
    returns percent of 30s epochs correctly classified
    """
    epochs = len(classifiedEEG)
    incorrect = np.nonzero(classifiedEEG-actualEEG)[0]
    percorrect = (epochs - len(incorrect))/epochs*100
    
    print 'EEG Classifier Performance: '
    print '     Correct Epochs = ' + str(epochs-len(incorrect))
    print '     Incorrect Epochs = ' + str(len(incorrect))
    print '     Percent Correct= ' + str(percorrect) 
    print 
    return percorrect
  
    
def test_examples(examples, srate):
    """
    This is one example of how you might write the code to test the provided 
    examples.
    """
    i = 0
    bin_size = 30*srate
    c = np.zeros((4,len(examples[1,:])/bin_size))
    while i + bin_size < len(examples[1,:]):
        for j in range(1,4):
            c[j,i/bin_size] = classify_epoch(examples[j,range(i,i+bin_size)],srate)
        i = i + bin_size
    
    totalcorrect = 0
    num_examples = 0
    for j in range(1,4):
        canswers = np.ones(len(c[j,:]))*j
        correct = classifier_tester(c[j,:],canswers)
        totalcorrect = totalcorrect + correct
        num_examples = num_examples + 1
    
    average_percent_correct = totalcorrect/num_examples
    print 'Average Percent Correct= ' + str(average_percent_correct) 
    return average_percent_correct

def classify_eeg(eeg,srate):
    """
    DO NOT MODIFY THIS FUNCTION
    classify_eeg takes an array of eeg amplitude values and a sampling rate and 
    breaks it into 30s epochs for classification with the classify_epoch function.
    It returns an array of the classified stages.
    """
    bin_size_sec = 30
    bin_size_samp = bin_size_sec*srate
    t = 0
    classified = np.zeros(len(eeg)/bin_size_samp)
    while t + bin_size_samp < len(eeg):
       classified[t/bin_size_samp] = classify_epoch(eeg[range(t,t+bin_size_samp)],srate)
       t = t + bin_size_samp
    return classified
        
##########################
#You can put the code that calls the above functions down here    
if __name__ == "__main__":
    plt.close('all')
    examples, srate = load_examples('example_stages.npz')
    plot_example_psds(examples,srate)
    plot_example_spectrograms(examples,srate)

    test_examples(examples,srate)

    eeg, srate = load_eeg('practice_eeg.npz')
    stages = load_stages('practice_answers.npz')
    classified = classify_eeg(eeg,srate)
    performance = classifier_tester(classified,stages)



