
# Crawler-Web
 The tool developed for Crawler Web by Nofet_Malca 
===================
The tool developed will accept a search term and then produce a file with information about the
movies with titles containing the search term.
The resulting file should contain one record for each movie, records shall be separated by a
new line.
Each record shall contain the following fields separated by vertical bar (|) :
1. Movie title
2. Genre : list of genre
3. MPAA rating. (R, PG-13, etc)
4. Movie duration
5. Director or list of directors if more than one (comma separated)
6. Star or list of stars ( comma separated )
Notes:
● Some movie titles are in the development phase. These should not be included in the
resulting file. See "The Lord Before the Rings"
● Some Movies lack some information. Maybe not rated yet, or duration is unknown ,etc. If
a field is missing you should output that as an empty field. See: "Skull Commandos"
● IMDb search facility is a fuzzy search:
       ○ Searching for "Elm" will also return:
            ■ Selma
            ■ Hotel Mumbai
            ■ Steel Magnolias
        The second & third results are obviously not desired and should be filtered out an
        and not included in the output file.

System-based program for crawler web using Python in Environment- PyCharm. 
The program performs Extracting data from the HTML of the site,
and saving some of the data as the output file in accordance with the requirements.
It uses urllib,requests,BeautifulSoup,re library for Extracting data.

### Installation

1. Install PyCharm 2019.1.2:
Make sure that latest version and installed for your machine or any environment that Python supports.
Refer hrefVS="https://www.jetbrains.com/pycharm/download/#section=windows" for installation. 

2. Install library : 
For import library installed on From the software in your machine.
Refer hrefOCv="https://www.youtube.com/watch?v=4KaCeqfm7VY&list=PLvv4vffx7Tzw21IrJxfoITlAO2CQtd09l&index=7"
Help how to download for installation.
 
### After Running the Program

1. Gets the name of a movie search word from the user. 
  
2. Finding the Search Page by input form user.

3. Find all the pages of the filtered movie list.

4. For-each Page:
    Filter pages according to 2 criteria
      1.  Filter by movie name.
      2. Filtering by movie titles are in development
	Create a file movies.text
	Perform data extraction from the particular page
	and insert them into the file if necessary.
5.Close the file.
Exit

###Sources of information

To using Beautiful Soup library:
1.
https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup
2.
https://towardsdatascience.com/web-scraping-101-in-python-35f8653b1c97


To using Urllib library:
1.https://www.guru99.com/accessing-internet-data-with-python.html



Help with bug fixes, highly recommend the sites:
1.
https://stackoverflow.com/
2.
https://www.geeksforgeeks.org/
3.
Just Google the error you made...

