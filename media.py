class Movie():
    # This movie class will be used to create movie instances with the following properties: a movie title, a poster url and a youtube trailer url.
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
