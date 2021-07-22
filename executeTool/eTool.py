from bs4 import BeautifulSoup
#import pandas as pd
import requests
#import webbrowser
import urllib.request
import re
import bs4



search_term = input('Enter Search IMDb by typing a word or phrase in the search box at the top of this page:') #input search_term Movie
urlS = "https://www.imdb.com/find?q="+str(search_term)+"&s=tt&ttype=ft&ref_=fn_ft" #Create a search URL
#webbrowser.open(urls, new=2)
url = urlS.replace(" ", "")


def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def prepend(list, str):
    str += '{0}'
    list = [str.format(i) for i in list]
    return list

#Database of all relevant pages by search.
arr = []
webS = "https://www.imdb.com/"
html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a', attrs={'href': re.compile("^/title/tt")}):
    arr = arr + [link.get('href')]

arr = list(dict.fromkeys(arr))
all_link = prepend(arr, webS)
for x in range(len(all_link)):
    all_link[x].replace(" ", "")

#Open a writing file located in 'movies.txt'
ob = open('movies.txt', "a", encoding='utf-8')

#Go through all the links and filter according to the requirements (see README.text)
for indexM in range(len(all_link)):
    #For name movie
    movP = all_link[indexM]
    print(indexM)
    html_page = urllib.request.urlopen(movP)
    soup = BeautifulSoup(html_page, "html.parser")
    movies = soup.findAll('div', class_='TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt')
    title = [movie.find('h1').text for movie in movies]
    tit = (str(title[0])).lower()
    print(tit)
    titS = (str(search_term).lower().strip())
    print(titS)
    if(tit.find(titS)) == -1:
        print("Filter this movie!")
        continue
    else:
        print("The title of the movie is appropriate")
        if soup.find('a', class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color ipc-link--launch') is None:
            print("no")
            with open('./movies.txt', "a", encoding='utf-8') as f:
                f.write(str(title[0]) + "|")
        else:
            continue
        # For genders movie
        genders = soup.findAll('a', class_='GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt')
        for i in range(len(genders)):
            if i != 0 and i < len(genders):
                with open('./movies.txt', "a", encoding='utf-8') as f:
                    f.write(",")
            #print(genders[i].text)
            with open('./movies.txt', "a", encoding='utf-8') as f:
                f.write(genders[i].text)
        with open('./movies.txt', "a", encoding='utf-8') as f:
            f.write("|")
        # For MPAA Rating movie
        mpaaRating = soup.findAll('span', class_='TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex')
        for j in range(len(mpaaRating)):
            if mpaaRating[j].text.isdigit():
                print("num" + mpaaRating[j].text)
            else:
                print(mpaaRating[j].text)
                with open('./movies.txt', "a", encoding='utf-8') as f:
                    f.write(mpaaRating[j].text)
        with open('./movies.txt', "a", encoding='utf-8') as f:
            f.write("|")
        # For Runtimes movie
        runtimes = soup.find('ul', {"class": "ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt"})  # Use dictionary to pass key : value pair
        runtime = runtimes.find_all('li', class_='ipc-inline-list__item')
        for t in runtime:
            #print(t.get_text())
            subRunT1 = "min"
            subRunT2 = "h"
            if str(t.get_text()).isdigit() or str(t.get_text()).isalpha():
                print("isdigit Or isalpha - Next...")
                #print(str(runtime[t]))
            else:
                if str(t.get_text()).find(subRunT1) or str(t.get_text()).find(subRunT2):
                    #print(str(t.get_text()))
                    with open('./movies.txt', "a", encoding='utf-8') as f:
                        f.write(str(t.get_text()))
        with open('./movies.txt', "a", encoding='utf-8') as f:
            f.write("|")
        # For directors movie
        directors = soup.find('div', {"class": "ipc-metadata-list-item__content-container"})  # Use dictionary to pass key : value pair
        director = directors.find_all('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
        count = 0;
        for d in director:
            print(d.get_text())
            if count > 0 and count < len(director):
                with open('./movies.txt', "a", encoding='utf-8') as f:
                    f.write(",")
            with open('./movies.txt', "a", encoding='utf-8') as f:
                f.write(str(d.get_text()))
            count = count + 1
        with open('./movies.txt', "a", encoding='utf-8') as f:
            f.write("|")

        # For stars movie
        stars = soup.findAll('ul', class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
        counter = 0;
        for s in stars:
             if (counter > 0) and (counter < 2):
                 star = s.find_all('a',  class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
             counter = counter + 1

        count = 0;
        for s in star:
            #print("hhhh")
            #print(s.get_text())
            if (count > 0) and (count < len(star)):
                with open('./movies.txt', "a", encoding='utf-8') as f:
                    f.write(",")
            with open('./movies.txt', "a", encoding='utf-8') as f:
                f.write(str(s.get_text()))
            count = count + 1

    with open('./movies.txt', "a", encoding='utf-8') as f:
        f.write("\n")
ob.close()
