import os

#This file needs to be placed within the directory of swapping extentions 
#(where the original files are and will be swapped to in the same location)

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        os.rename(filename, filename + '.bak')