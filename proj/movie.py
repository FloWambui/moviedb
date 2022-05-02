class Movie:
    def __init__(self, id, title, overview, poster_path, vote_average, release_date):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster_path = 'https://image.tmdb.org/t/p/w500/'+ poster_path
        self.vote_average = vote_average
        self.release_date = release_date
