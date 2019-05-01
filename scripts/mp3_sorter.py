from pytag import Audio
import os

UNKNOWN_DIR = 'Unknown'

def handleMp3(name):
    audio = Audio(name)

    if not audio.artist:
        os.rename(name, UNKNOWN_DIR + '/' + name)
        return
    
    if not os.path.exists(audio.artist):
        os.makedirs(audio.artist)
    
    if not audio.album:
        path = audio.artist
    else:    
        path = audio.artist + '/' + audio.album

    if not os.path.exists(path):
        os.makedirs(path)

    os.rename(name, path + '/' + name)

### START

if not os.path.exists(UNKNOWN_DIR):
    os.makedirs(UNKNOWN_DIR)

for i in [f for f in os.listdir() if os.path.isfile(f) and '.mp3' in f ]:
    handleMp3(i)




