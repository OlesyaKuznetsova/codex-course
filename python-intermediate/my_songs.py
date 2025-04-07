liked_songs = {
    'Cold Carti': 'Фонарики на крыше',
    'Toxis': 'Nothing',
    'Miladze': 'Salut, Vera!',
    'Big Baby Tape': '5 Nights Crazy'
}

def write_liked_songs_to_file(songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in songs.items():
            file.write(f'{song} by {artist}\n')

    print(f'Successfully added Liked songs to {file_name} ')

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')