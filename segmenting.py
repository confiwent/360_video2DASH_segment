import os 

BITRATE = [600, 1500, 3000, 5000, 10000, 20000] # Kbps
tile_num = 64
video_path = '/home/kannuowen/Video/Bridge/multi-bitrate'

for bitrate in range(len(BITRATE)):
    for tile in range(tile_num):        
        os.chdir(video_path + '/video_' + str(bitrate)) # cd path
        command = 'mkdir' + ' ' + 'tile_' + str(tile) # creat folder
        os.system(command)
        input_tile_video_path = video_path + '/video_' + str(bitrate) + '/tile_' + str(tile)
        os.chdir(input_tile_video_path)
        command = 'MP4Box -dash 100 -frag 100 -segment-name chunk_ ../tile_' + str(tile) + '.mp4'  # transfer mp4 to dash file, each segment(chunk) has a 0.1s duration
        os.system(command)
