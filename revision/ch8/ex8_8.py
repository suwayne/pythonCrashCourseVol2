#ex:user albums
"""
Start with your program from Exercise 8-7. Write a while loop that allows users to enter an albums 
artist and title. Once you have that information, call make_album() with the users input and print 
the dictionary thats created. Be sure to include a quit value in the while loop.
"""

def make_album(album_name, artist_name, tracks = 0):
    album_dict = {
        'artist': artist_name,
        'album': album_name,
    }

    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

#prepare the prompts:
print("Enter quit to end the program")
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
track_prompt = "How many tracks? "

while True:
    album_name = input(title_prompt)
    if album_name == 'quit':
        break
    
    artist_name = input(artist_prompt)
    if artist_name == 'quit':
        break

    tracks = input(track_prompt)
    if tracks == 'quit':
        break

    album = make_album(album_name, artist_name, tracks)
    print(album)

print("\nThanks for responding!")




