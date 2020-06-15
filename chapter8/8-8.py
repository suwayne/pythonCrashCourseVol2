def make_album(artist, title,):
    """build a dictionary containing info about an album"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# prepare the prompts.
