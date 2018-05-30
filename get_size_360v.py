import os 

TOTAL_VIDEO_CHUNCK = 299
BITRATE_LEVELS = 6
TILE_NUM = 64
VIDEO_PATH = '/home/kannuowen/RL/Source_video/'
VIDEO_FOLDER = 'video_'
TILE_FOLDER = 'tile_'
FILE_FOLDER = '/home/kannuowen/RL/360VCRL/sim/'

# assume videos are in ../video_servers/video[0, 1, 2, 3, 4, 5]
# the quality at video_0 is the lowest and video_5 is the highest

if not os.path.exists('./Videosize'):
      os.mkdir('./Videosize')

for bitrate in xrange(BITRATE_LEVELS):
    os.chdir(FILE_FOLDER + 'Videosize')
    if not os.path.exists('./video_'+ str(bitrate)):
          os.mkdir('./video_' + str(bitrate))
    os.chdir('./video_'+ str(bitrate))
    for tile in xrange(TILE_NUM):
	    with open('tile_size_' + str(tile), 'wb') as f:
		    for chunk_num in range(1, TOTAL_VIDEO_CHUNCK + 1):
			    video_chunk_path = VIDEO_PATH + VIDEO_FOLDER + str(bitrate) + '/' + \
                                               TILE_FOLDER + str(tile) + '/' + 'chunk_' + str(chunk_num) + '.m4s'
			    chunk_size = os.path.getsize(video_chunk_path)
			    f.write(str(chunk_size) + '\n')
