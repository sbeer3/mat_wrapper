
#Imports the matlab engine
import matlab.engine as me
import os, sys 

#creates an instance of the matlab engine
eng = me.start_matlab()

#defines the wrapper class
class wrapper:

    #lets you add to the path of the matlab wrapper
    def addFolders(self, folder):
        eng.addpath(folder)
        os.chdir(folder)

    #this wraps through python using the functions name
    def wrap(self, func, inputs):
        if(inputs == ""):
            inputs = "nargout=0"
        try:
            evald = eval("eng" + "." + func + "(" + inputs + ")")
        except:
            evald ="The function or inputs were invalid, try again!"
