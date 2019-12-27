# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:48:18 2019

@author: thena
"""

from pydub import AudioSegment
from random import randint, seed

# This function imports individual tracks into memory, taking into account
# format. Unnecessary?
def song_import(track_name, track_format):
    
    # Imports song based on format
    
    if track_format == 'wav':
        song = AudioSegment.from_wav(track_name)
    elif track_format == 'mp3':
        song = AudioSegment.from_mp3(track_name)
    elif track_format == 'ogg':
        song = AudioSegment.from_ogg(track_name)
    elif track_format == 'flv':
        song = AudioSegment.from_flv(track_name)
    else: 
        try: 
            song = AudioSegment.from_file(track_name)
        except: 
            print('Error importing file in song_import function')

    # Normalise song volume - unnecessary
    return song

# song_chop chops song up into segments of random length between 0.1 and 4 seconds.
# Input is a string that helps to identify the song name, so that 
# the song fragments can be identified. e.g. 'Bonobo_cirrus.mp3'.
# The output will then be song slices that have the name 'Bonobo_cirrus_0'
# up to the number of slices used, e.g. 'Bonobo_cirrus.mp3_slice_30', etc.

def song_slice():

    # Determine song length in milliseconds
    song_length = len(song)

    seed(42)
    i = 0 # i used to determine position in song in milliseconds
    j = 0 # used to determine slice number

    # Loop below creates random integer number between 100 and 4000 milliseconds,
    # and uses it to generate randomly sized song samples

    while i < (song_length-4000):
        
        rand_4000 = randint(100,4000)
        song_slice = song[i:(i+rand_4000)] 
        i = i + rand_4000  

        slice_name = track_name + '_slice_' + str(j)

        j = j + 1
