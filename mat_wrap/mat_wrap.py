#Imports the matlab engine
# print("before import")
# import matlab.engine
# import os, sys 
# print("before eng")
#creates an instance of the matlab engine
#eng = matlab.engine.start_matlab()
# print("after eng")
#defines the wrapper class

def stuff():
	print("stuff")
# class wrapper:
#     #lets you add to the path of the matlab wrapper
#     def addToPath(self, folder):
#         eng.addpath(folder)
#         os.chdir(folder)
#         print("added " + folder + " to the path")

#     #this wraps through python using the functions name
#     def wrap(self, func):
#         inputs = "nargout=0"
#         try:
#             evald = eval("eng" + "." + func + "(" + inputs + ")")
#         except:
#             evald ="The function or inputs were invalid, try again!"
