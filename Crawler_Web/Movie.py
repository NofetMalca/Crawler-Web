from WebScraping import WebScraping
#from Movie import *
import webbrowser
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import bs4


class Movie(WebScraping):
    movie_scraping = WebScraping()
    movie_name = ""

    def _init_(self, movie_title, genre, mpaa_rating, movie_duration, director, str_actors):
        self.movie_title = movie_title
        self.genre = genre
        self.mpaa_rating = mpaa_rating
        self.movie_duration = movie_duration
        self.director = director
        self.str_actors = str_actors

    @staticmethod
    def get_name_movie():
        name_movie_input = input()
        print(name_movie_input)
        return name_movie_input

    @staticmethod
    def get_write_in_file(attributes):
        for i in range(len(attributes)):
            if i == 3:
                with open('./movies.txt', "a", encoding='utf-8') as f:
                    f.write(attributes[i])
            else:
                for j in range(len(attributes[i])):
                    if len(attributes[i]) == 0 or len(attributes[i]) == 1:
                        with open('./movies.txt', "a", encoding='utf-8') as f:
                            f.write(attributes[i][j])
                    else:
                        with open('./movies.txt', "a", encoding='utf-8') as f:
                            f.write(attributes[i][j])
                            if j in range(len(attributes[i])-1):
                                f.write(",")
                            else:
                                pass
            with open('./movies.txt', "a", encoding='utf-8') as f:
                f.write(" |")
        with open('./movies.txt', "a", encoding='utf-8') as f:
            f.write("\n")



    def create_movie_file(self, movie_name):
        url = self.movie_scraping.get_url_movie(movie_name)
        list_links_filtering_name_movie = self.get_list_pages_movie(url)
        print(list_links_filtering_name_movie)
        for link_index in range(len(list_links_filtering_name_movie)):
            extract_attributes = self.extract_all_attribute(self.movie_name, list_links_filtering_name_movie[link_index])
            if extract_attributes:
                extract_attributes[3] = list(extract_attributes[3])
                print(extract_attributes[3])
                extract_attributes[3] = str("".join(extract_attributes[3]))
                print(extract_attributes[3])
                self.get_write_in_file(extract_attributes)
            else:
                continue
        return





