#from Movie import *
import webbrowser
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import bs4


class WebScraping:
    name_movie = ""

    def __init__(self, url=None, attribute=None):
        self.url = url
        self.attribute = attribute

    def get_url_movie(self, name_movie):
        self.url = "https://www.imdb.com/find?q=" + str(name_movie).replace(" ", "") + "&s=tt&ttype=ft&ref_=fn_ft"
        #webbrowser.open(self.url, new=2)
        return self.url

    @staticmethod
    def prepend(list_links, str_prefix):
        str_prefix += '{0}'
        list_links = [str_prefix.format(i) for i in list_links]
        return list_links

    def get_list_pages_movie(self, url):
        list_pages = []
        web_imdb = "https://www.imdb.com/"
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^/title/tt")}):
            list_pages = list_pages + [link.get('href')]
        list_pages = list(dict.fromkeys(list_pages))
        list_link = self.prepend(list_pages, web_imdb)
        for x in range(len(list_link)):
            list_link[x].replace(" ", "")
        return list_link

    @staticmethod
    def text_value(movie, movie_content, tag, class_=None, find_=None):
        if class_ == "":
            if find_ == 1:
                if movie.find(tag):
                    array_attribute=[]
                    array_attribute.append([movie.find(tag).text for movie in movie_content])
                    return array_attribute
                else:
                    return
            else:
                if movie.findAll(tag):
                    array_attribute = []
                    movie_findall = movie.findAll(tag)
                    for attribute_index in range(len(movie_findall)):
                        array_attribute.append(movie_findall[attribute_index].text)
                    return array_attribute
                else:
                    return
        else:
            if find_ == 1:
                if movie.find(tag, class_):
                    return [movie.find(tag, class_).text for movie in movie_content]
                else:
                    return
            else:
                if movie.findAll(tag, class_):
                    array_attribute = []
                    movie_findall = movie.findAll(tag, class_)
                    for attribute_index in range(len(movie_findall)):
                        array_attribute.append(movie_findall[attribute_index].text)
                    return array_attribute
                else:
                    return

    def nested_text_value(self, movie, tag_1, class_1, tag_2, class_2, find_=None, location=None):
        if find_ == 0:
            if class_1 == "":
                if movie.findAll(tag_1):
                    attribute_content = movie.findAll(tag_1)
                    array_attribute_nested = []
                    for attribute_content_index in range(len(attribute_content)):
                        array_attribute_nested.append(self.text_value(attribute_content[attribute_content_index], attribute_content, tag_2, class_2, find_))
                    return array_attribute_nested
                else:
                    return
            else:
                if movie.findAll(tag_1, class_1):
                    if location is not None:
                        attribute_content = movie.findAll(tag_1, class_1)[2]
                        print(attribute_content)
                        array_attribute_nested = []
                        array_attribute_nested.append(self.text_value(attribute_content, attribute_content, tag_2, class_2, find_))
                        return array_attribute_nested
                    else:
                        attribute_content = movie.findAll(tag_1, class_1)
                        array_attribute_nested = []
                        for attribute_content_index in range(len(attribute_content)):
                            array_attribute_nested.append(self.text_value(attribute_content[attribute_content_index], attribute_content, tag_2, class_2, find_))
                        return array_attribute_nested
                else:
                    return
        if find_ == 1:
            if class_1 == "":
                if movie.find(tag_1):
                    attribute_content = movie.find(tag_1)
                    array_attribute_nested = []
                    for attribute_content_index in range(len(attribute_content)):
                        array_attribute_nested.append(self.text_value(attribute_content[attribute_content_index], attribute_content, tag_2, class_2, find_=0))
                    return array_attribute_nested
                else:
                    return
            else:
                if movie.find(tag_1, class_1):
                    print(movie.find(tag_1, class_1))
                    attribute_content = movie.find(tag_1, class_1)
                    array_attribute_nested = []
                   # for attribute_content_index in range(len(attribute_content)):
                    array_attribute_nested.append(self.text_value(attribute_content, attribute_content, tag_2, class_2, find_=0))
                    return array_attribute_nested
                else:
                    return
        if find_ == 2:
            if class_1 == "":
                if movie.findAll(tag_1):
                    attribute_content = movie.findAll(tag_1)
                    array_attribute_nested =[]
                    for attribute_content_index in range(len(attribute_content)):
                        array_attribute_nested.append(self.text_value(attribute_content[attribute_content_index], attribute_content, tag_2, class_2, find_=1))
                    return array_attribute_nested
                else:
                    return
            else:
                if movie.findAll(tag_1, class_1):
                    attribute_content = movie.findAll(tag_1, class_1)
                    array_attribute_nested = []
                    for attribute_content_index in range(len(attribute_content)):
                        array_attribute_nested.append(self.text_value(attribute_content[attribute_content_index], attribute_content, tag_2, class_2, find_=1))
                    return array_attribute_nested
                else:
                    return

    # find=0 no find, find=1 find in first, find=2 find in second
    def extract_attribute(self, soup, tag_1, class_1='', tag_2='', class_2='',
                          nested=False, find_=None, location=None):
        movie_section = soup.findAll('section', class_='ipc-page-section ipc-page-section--baseAlt ipc-page-section--tp-xs ipc-page-section--bp-xs Hero__HeroParent-kvkd64-1 fARFJI')
        data_list = []
        for movie in range(len(movie_section)):
            if nested:
                #print(movie_section[movie])
                data_list.append(self.nested_text_value(movie_section[movie], tag_1, class_1, tag_2, class_2, find_,location))
            else:
                data_list.append(self.text_value(movie_section[movie], movie_section, tag_1, class_1, find_))

            data_list = re.sub(r'[\]\[\'\"]', '', str(data_list))
            data_list = data_list.split(", ")
            print(data_list)
        return data_list

    @staticmethod
    def filter_name(movie_title, movie_name, soup, flag):
        title_name = str(movie_title).lower()
        print(title_name)
        movie_name_temp = (str(movie_name).lower().strip())
        print(movie_name_temp)
        if (title_name.find(movie_name_temp)) == -1:
            print("Filter this movie!(NAME)")
            flag = False
        else:
            print("The movie is NOT Filter by name")
            if soup.find('a', class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color ipc-link--launch') is None:
                print("The movie is NOT development")
            else:
                print("Filter this movie!(development)")
                flag = False
        return flag

    def extract_all_attribute(self, movie_name, link_movie):
        all_attribute = []
        flag = True
        html_page = urllib.request.urlopen(link_movie)
        soup = BeautifulSoup(html_page, "html.parser")
        movie_title = self.extract_attribute(soup, 'div', 'TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt',
                                             'h1', "", True, 2)
        if self.filter_name(movie_title, movie_name, soup, flag):
            all_attribute.append(movie_title)
            genre = self.extract_attribute(soup, 'a', 'GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt',
                                           '', '', False, 0)
            all_attribute.append(genre)
            mpaa_rating = self.extract_attribute(soup, 'span', 'TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex',
                                                 '', '', False, 0)

            print(mpaa_rating[0])
            if mpaa_rating[0].isdigit():
                mpaa_rating.remove(mpaa_rating[0])
                print(mpaa_rating)
            all_attribute.append(mpaa_rating)
            movie_duration = self.extract_attribute(soup, 'ul', 'ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt',
                                                    'li', 'ipc-inline-list__item', True, 0)
            print(movie_duration[-1])
            if movie_duration[-1].isdigit() or movie_duration[-1].isalpha():
                movie_duration = ""
            else:
                min_str = "min"
                h_str = "h"
                if movie_duration[-1].find(min_str) and movie_duration[-1].find(h_str):
                    movie_duration = movie_duration[-1]
                else:
                    if movie_duration[-1][-1].find(h_str):
                        temp_runtime = movie_duration[-1].replace("h", "")
                        if temp_runtime.isdigit():
                            movie_duration = movie_duration[-1]
                        else:
                            movie_duration = ""
                    else:
                        movie_duration = ""
            all_attribute.append(movie_duration)

            director = self.extract_attribute(soup, 'div', 'ipc-metadata-list-item__content-container', 'a',
                                              'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link',
                                              True, 1)
            all_attribute.append(director)
            str_actors = self.extract_attribute(soup, 'div', 'ipc-metadata-list-item__content-container',
                                                'a', 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link',
                                                True, 0, 2)
            all_attribute.append(str_actors)
            return all_attribute
        else:
            return

