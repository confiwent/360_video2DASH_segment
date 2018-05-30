""" 'ffmpeg' should be build in windows """

import os 

BITRATE = [600, 1500, 3000, 5000, 10000, 20000] # Kbps
BITRATE_file = ['600Kbps', '1500Kbps', '3000Kbps', '5000Kbps', '10000Kbps', '20000Kbps']

filepath = 'F:\\Research\\Video\\Bridge\\multi-bitrate'

tile_number = 64

os.chdir(filepath)

for bitrate in range(len(BITRATE)):
    command = 'mkdir' + ' ' + 'video_' + str(bitrate)
    os.system(command)

for bitrate in range(len(BITRATE)):
    video_path = 'F:\\Research\\Video\\Bridge\\multi-bitrate\\Bridge_'
    outputpath = 'F:\\Research\\Video\\Bridge\\multi-bitrate\\video_' + str(bitrate) + '\\'
    for tile in range(tile_number):
        os.chdir('F:\\Research\\Video\\Bridge\\multi-bitrate\\video_' + str(bitrate))
        y = 256 * (tile/8)
        x = 512 * (tile%8)
        command =  'ffmpeg -i ' + video_path + BITRATE_file[bitrate] +'.mp4 \
        -strict -2 -vf crop=512:256:' + str(x) + ':' + str(y) + ' ' + outputpath + 'tile_' \
        + str(tile) + '.mp4'
        # crop a 360-degree video into 64 tiles, all tiles have the same size
        # x,y mean the left-top axis (in pixel)
        # 512,256 mean the tile size (in pixel) 
        os.system(command)




    

 
