# coding: latin-1

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "12/22/1995",
                        "John Lasseter",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "12/18/2009",
                     "James Cameron",
                     "Avatar is a 2009 American epic science fiction film directed, written, produced,\
                      and co-edited by James Cameron.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

starwars_tfa = media.Movie("Star Wars: The Force Awakens",
                           "12/18/2015",
                           "J. J. Abrams",
                           "Star Wars is an American epic space opera franchise,\
                            centered on a film series created by George Lucas.",
                           "https://upload.wikimedia.org/wikipedia\/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=sGbxmsDFVnE")

terminator_genisys = media.Movie("Terminator Genisys",
                                 "07/01/2015",
                                 "Alan Taylor",
                                 "Terminator Genisys is a 2015 American science fiction action film, directed by\
                                  Alan Taylor and written by Laeta Kalogridis and Patrick Lussier.",
                                 "https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG",
                                 "https://www.youtube.com/watch?v=62E4FJTwSuc")

chef = media.Movie("Chef",
                   "05/09/2014",
                   "Jon Favreau",
                   "Chef is a 2014 American comedy-drama film written, produced, directed by and\
                    starring Jon Favreau, and co-starring Sofía Vergara, John Leguizamo, Scarlett\
                     Johansson, Oliver Platt, Bobby Cannavale, Dustin Hoffman, and Robert Downey, Jr.",
                   "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                   "https://www.youtube.com/watch?v=mLuixZwiIdU")


# Append each movie to a list and call open movies
movies = [toy_story, avatar, starwars_tfa, terminator_genisys, chef]
fresh_tomatoes.open_movies_page(movies)
