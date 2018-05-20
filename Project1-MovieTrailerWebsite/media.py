iimport webbrowser


class Movie():
    """Creates a Movie object using the movie's title, storyline,
    poster image and youtube trailer.

    Attributes:
        movie_title (str): The title of the movie
        movie_storyline (str): Short description of the movie's plot
        poster_image_url (str): The url for poster image of the movie
        trailer_youtube_url (str): The url for the movie's trailer
    
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
