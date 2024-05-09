def make_album(person, album, songs=None):
    artist = {'name': person.title(), 
              'album_name': album.title()}
    if songs:
        artist['num_songs'] = songs
    print(artist)
    return artist

make_album('taylor swift', 'evermore')
make_album('loreen', 'ride', 10)
make_album('seafret', 'most of us are strangers')
