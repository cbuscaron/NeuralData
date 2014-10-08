### Save this file back as problem_set0.py when you are done

'''
Part 1: Write a function that returns the string "hello, world"
'''
import numpy as np
import matplotlib.pyplot as plt
def hello_world():
    
    title = "how to find a circle's area"
    pi = 3.14159
    radius = 5
    area= pi*(radius**2)
    print title
    print area
    
    x = 5
    if x > 0:
        print "True"
    else:
        print "False"
    
    n = 5;
    
    while n > 0:
        print n
        n = n -1
    print "blastoff!"
    
    x=5
    
    for i in range(x):
        print i
        
        x = 10
        
        
    mylist= [1,2,3]
    
    print mylist
    
    name = 'Matilda'
    print name[2:]
    
    print len(mylist)
    
    startlist = [1,5,6,7,1,12,5,2,7,8,9]
    cutoff = 5
    smallvals=[]
    largevals=[]
    
    
    x= len(startlist)
    
    
    for i in range(x):
           if(startlist[i]<cutoff):
               ##print startlist[i]
               smallvals.append(startlist[i])                    
           else:
               ##print startlist[i]
               largevals.append(startlist[i])
               
    
    smallvals.sort()
    largevals.sort()

    print smallvals
    print largevals
           
           
    print print_hello("Young CLO")
    
    ##help(median)
    
    import numpy as np
    ##import matplotlib
    import matplotlib.pyplot as plt
    
    ##%matplotlib inline
    
    x= np.linspace(0,3*np.pi,500)
    plt.plot(x, np.sin(x))
    plt.title("A Sinewave")
    plt.show()
    
    
    
    
    return "hello, world"
    
    
def print_hello(name):
    return "Hello" + name +"!"
    
def create_waveform(times, data):
    plt.plot(times, data, 'g-')
    plt.title('waveform')    
    
def add_line(yval):
    """Add Horizontal line at particular location"""
    plt.axhline(y=yval)
    
    
    
    
    

        
        



   
