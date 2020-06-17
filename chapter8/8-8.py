def make_album(artist, title, tracks=0):
    """build a dictionary containing info about an album"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# prepare the prompts.
album_prompt = "\nwhat album are you thinking of?"
artist_prompt = "who is the artist?"

# let the user know when it's time to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(album_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding.")
