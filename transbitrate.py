""" 'ffmpeg' should be build in windows """
import os

filepath = 'F:\\Research\\Video\\Bridge\\'  # path of files to be handle
resultpath = 'F:\\Research\\Video\\Bridge\\multi-bitrate\\'

BITRATE = [600, 1500, 3000, 5000, 10000, 20000] # Kbps

os.chdir(resultpath)  # cd the object folder

for sample in range(len(BITRATE)):
    command =  'ffmpeg -i ' + filepath + 'Bridge_4K.mp4 -b:v ' + str(BITRATE[sample]) \
    + 'k ' + resultpath + 'Bridge_' + str(BITRATE[sample]) + 'Kbps.mp4'  
    # transcode the video in different bitrate 
    # Notice: it not transfrom the frame-rate here !!
    os.system(command)  # execute the command above in system cmd