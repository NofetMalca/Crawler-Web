from Movie import Movie


def main():
    movie = Movie()
    print("Welcome to the IMDb(Internet Movie Database)!!\n".upper() +
          "Enter a movie name or Keyword For a specific movie search:\n")
    input_name_movie = movie.get_name_movie()
    return movie.create_movie_file(input_name_movie)


if __name__ == "__main__":
    main()
