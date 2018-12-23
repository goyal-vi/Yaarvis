import spotipy
import sys
import pprint
print(sys.argv[1])
if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'
sp = spotipy.Spotify()
track = sp.track(urn)
pprint.pprint(track)
