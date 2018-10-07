# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import numpy as np
  

def fun1(df,myfile): 
    df=df[1:75]
    print(df[1:2])
    t=[0 for j in range(len(df[0]))]
    with open(myfile,'a') as f:
        for i in range(len(df)):
            for k in range(len(df[i])):
                t[k]+=int(df[i][k])
        f.write("1."+str(t)+"\n")
def fun2(df,myfile): 
    df=df[75:149]
    t=[0 for j in range(len(df[0]))]
    with open(myfile,'a') as f:
        for i in range(len(df)):
            for k in range(len(df[i])):
                t[k]+=int(df[i][k])
        f.write("2."+str(t)+"\n")
  
if __name__ == "__main__": 
    # creating thread 
    df=np.genfromtxt("lymphography.csv",delimiter=',')
    print(df)
    t1 = threading.Thread(target=fun1, args=(df,"./myfile.txt")) 
    t2 = threading.Thread(target=fun2, args=(df,"./myfile.txt")) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
