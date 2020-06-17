def make_album(artist_name, album_title):
    album_detail = {'name': artist_name, 'album': album_title}
    return album_detail


detail = make_album('mi', 'mr incredible')
print(detail)
detail = make_album('m.jackson', 'thriller')
print(detail)
detail = make_album('50 Cent', 'animal ambition')
print(detail)
