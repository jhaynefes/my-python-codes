# author @sollano_jhaynefe

songs = ["Slow Down", "Don't Freak", "Clouds", "Waiting Shed", "I Know A Place"]
print(songs)

artists = ["Mac Ayres", "The Aces", "Any Name's Okay", "Glaiza De Castro", "MUNA"]
print(artists)

playlist = []

for i in range(len(songs)):
    playlist.append(songs[i] + " - " + artists[i])

for song in playlist:
    print(song)
