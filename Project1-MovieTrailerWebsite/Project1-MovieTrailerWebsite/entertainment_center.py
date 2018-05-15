import media
import fresh_tomatoes

goodfellas = media.Movie("Goodfellas",
                         "The story of Henry Hill and his life in the mob",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=xWMxvFvhAB8")


bladerunner = media.Movie("Blade Runner (1982)",
                          "A movie about human replicants",
                          "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                          "https://www.youtube.com/watch?v=eogpIG53Cis")


groundhogday = media.Movie("Groundhog Day",
                           "A man finds himself in the same day over and over",
                           "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
                           "https://www.youtube.com/watch?v=GncQtURdcE4")

apollo13 = media.Movie("Apollo 13",
                       "NASA must return Apollo 13 to Earth",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
                       "https://www.youtube.com/watch?v=Y_rkXC9HH9k")

sicario = media.Movie("Sicario",
                      "FBI agent must aid in the drug war at US/Mexican border",
                      "https://upload.wikimedia.org/wikipedia/en/4/4b/Sicario_poster.jpg",
                      "https://www.youtube.com/watch?v=sR0SDT2GeFg")

johnwick2 = media.Movie("John Wick 2",
                        "An ex-hitman must survive a large bounty on his life",
                        "https://upload.wikimedia.org/wikipedia/en/3/31/John_Wick_Chapter_Two.png",
                        "https://www.youtube.com/watch?v=ChpLV9AMqm4")

movies = [goodfellas, bladerunner, johnwick2, groundhogday,
          apollo13, sicario]
fresh_tomatoes.open_movies_page(movies)
