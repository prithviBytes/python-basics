playlist = {
    "title": "Romantic Songs",
    "author": "Prithvi Suvarna",
    "songs": [
        {"title": "Kun Faya","artists": ["AR. Rahman","Mohit Chauhan"],"duration": 3.5},
        {"title": "Barso","artists": ["Ritviz"],"duration": 2.5},
        {"title": "Kun Faya","artists": ["AR. Rahman","Mohit Chauhan"],"duration": 3.5},
        {"title": "Barso","artists": ["Ritviz"],"duration": 2.5},
        {"title": "Kun Faya","artists": ["AR. Rahman","Mohit Chauhan"],"duration": 3.5}
    ]
}

print(f"Playlist title: {playlist.get('title')}")
print(f"Author: {playlist['author']}")

for song in playlist["songs"]:
    artists = " ".join(artist for artist in song['artists'])
    print(f"Song Name: {song['title']} Artists: {artists} Durations: {song['duration']}")

