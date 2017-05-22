import media
import fresh_tomatoes

# Creation of 3 instances of the movie class
the_fellowship_of_the_ring = media.Movie(
    "The Fellowship Of The Ring",
    "http://vignette3.wikia.nocookie.net/lotr/images/7/74/LOTRFOTRmovie.jpg/revision/latest?cb=20150203040819",
    "https://www.youtube.com/watch?v=V75dMMIW2B4")
the_two_towers = media.Movie(
    "The Two Towers",
    "https://vignette3.wikia.nocookie.net/lotr/images/d/d2/The_Two_Towers_Poster_01.jpg/revision/latest?cb=20150203041549",
    "https://www.youtube.com/watch?v=LbfMDwc4azU")
the_return_of_the_king = media.Movie(
    "The Return Of The King",
    "http://vignette4.wikia.nocookie.net/lotr/images/7/77/The_Return_of_the_King_Poster_01.jpg/revision/latest?cb=20150203042330",
    "https://www.youtube.com/watch?v=WIrRJ8bCZYQ")

# Creation of a list of movies
favorite_movies = [the_fellowship_of_the_ring,
                   the_two_towers, the_return_of_the_king]

# Creation of the web page rendering the list of movies
fresh_tomatoes.open_movies_page(favorite_movies)
