class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    def add_song_to_count():
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        (Song.genres.append(genre))
        set(Song.genres)
    
    @classmethod
    def add_to_artists(cls, artist):
        (Song.artists.append(artist))
        set(Song.artists)

    def add_to_genre_count(genre):
        if genre in Song.genre_count.keys():
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    def add_to_artist_count(artist):
        if artist in Song.artist_count.keys():
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1


