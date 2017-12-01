# Final_Checkin.py
#  by: Ran LI (UIN_655284071)
# A program that sorts the movie list by its release year

import csv # to read csv files

# define a function to sort the movies by its release year
def releaseyr(year):
    file = open('movielist.csv','r')
    file.close()
    reader = csv.reader(file)
    movielist = list(reader)
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    # from the enumerate, the tile is the second one; and the year is the eighth one
    titlelist = []
    for movie in movielist:
        if movie[8] == str(year):
            title = movie[2]
            titlelist.append(title)
            finaltitlelist = '\n'.join(titlelist)
    # store the result into a txt file
    output_name_format = 'Moives_in_#.txt'
    output_name = output_name_format.replace('#',str(year))
    output = open(output_name,'w')
    output.write(finaltitlelist)
    output.close()

# to get a list of movies released in each year from 1972 to 2016
yrlist = [1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
for year in yrlist:
    releaseyr(year)
