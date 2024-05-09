def make_album(person, album, songs=None):
    artist = {'name': person.title(), 
              'album_name': album.title()}
    if songs:
        artist['num_songs'] = songs
    return artist

while True:
    print('\033[31mTell me about an artist\033[m\n'
          '(enter \'q\' to quit)')
    
    name = input("What's the name: ")
    if name == 'q':
        break

    album = input("Album's title: ")
    if album == 'q':
        break

    songs = input('Number of tracks: ')
    if songs == 'q':
        break

    user_album = make_album(name, album, songs)
    print(user_album)
