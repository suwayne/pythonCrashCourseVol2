"""
Write a function called make_album() that builds a dictionary describing a music album. The function should take 
in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. Print each return value to show that the 
dictionaries are storing the album information correctly.
"""

def make_album(artist_name, album_title):
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    return album_dict



jay_album = make_album('jay z', 'watch the throne')
print(jay_album)
