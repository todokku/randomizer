from randomizer import *
import os

# os.chdir('C:/Users/thena/Music')
# os.getcwd()

os.chdir('/home/nathan/Music')
os.getcwd()

track_name = 'Bonobo Cirrus [Official Video].mp3'
track_format = 'mp3'

def music_generator(track_name,track_format):
    song_import(track_name,track_format)
    
    song_slice()

music_generator(track_name,track_format)