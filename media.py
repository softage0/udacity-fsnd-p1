import webbrowser


class Movie(object):
    """ This class is Movie class.

    Attributes:
        release_date: Release Date of Movie in United States
        poster_image: URL link to show the poster image
        trailer_youtube: Youtube URL link to see the trailer video
    """

    def __init__(self, movie_title, release_date, director, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.release_date = release_date
        self.director = director
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
