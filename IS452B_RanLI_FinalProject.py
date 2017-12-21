# IS452B_Final_Project.py
#  by: Ran LI (UIN_655284071)
# A program that sorts all the movies released in the U.S from 1972-2016

import csv,operator # to read & sort csv files

## PART.ONE
# define a function to sort the movies by its release year
def releaseyr(year):
    file = open('movielist.csv','r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    # from the enumerate, the tile is the second one; and the year is the eighth one
    titlelist = []
    for movie in movielist[1:]:
        title = movie[2]
        release_yr = movie[8]
        if release_yr == str(year):
            titlelist.append(title)
            finaltitlelist = '\n'.join(titlelist)
    # store the result into a txt file
    output_name_format = 'Moives_in_#.txt'
    output_name = output_name_format.replace('#',str(year))
    output = open(output_name,'w')
    output.write(finaltitlelist)
    output.close()

# define a function to get a list of all release years
def get_yr_list(filenm):
    file = open(filenm,'r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    yr_list =[]
    for movie in movielist[1:]:
        yr = movie[8]
        if yr != '????':
            if yr not in yr_list:
                yr_list.append(yr)
    return yr_list
# get the lists of movies released in each year based on the previous list of release years
yrlist = get_yr_list('movielist.csv')
for year in yrlist:
    releaseyr(year)

## PART.TWO
# define a function to sort movies by its ratings
def ratings(rating1,rating2,rating3,rating4,rating5):
    file = open('movielist.csv','r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    # from the enumerate, the tile is the second one; and the IMDb rating is the sixth one
    titlelist1 = []
    titlelist2 = []
    titlelist3 = []
    titlelist4 = []
    titlelist5 = []
    titlelist6 = []
    for movie in movielist[1:]:
        title = movie[2]
        rating = movie[6]
        if rating <= str(rating1):
            titlelist1.append(title)
            finaltitlelist1 = '\n'.join(titlelist1)
        elif str(rating1) < rating <= str(rating2):
            titlelist2.append(title)
            finaltitlelist2 = '\n'.join(titlelist2)
        elif str(rating2) < rating <= str(rating3):
            titlelist3.append(title)
            finaltitlelist3 = '\n'.join(titlelist3)
        elif str(rating3) < rating <= str(rating4):
            titlelist4.append(title)
            finaltitlelist4 = '\n'.join(titlelist4)
        elif str(rating4) < rating <= str(rating5):
            titlelist5.append(title)
            finaltitlelist5 = '\n'.join(titlelist5)
        elif rating > str(rating5):
            titlelist6.append(title)
            finaltitlelist6 = '\n'.join(titlelist6)
    # store the result into a txt file
    output_name_format1 = 'Moives_below_#.txt'
    output_name1 = output_name_format1.replace('#',str(rating1))
    output1 = open(output_name1,'w')
    output1.write(finaltitlelist1)
    output1.close()
    output_name_format2 = 'Moives_between_#-$.txt'
    output_name2 = output_name_format2.replace('#',str(rating1))
    output_name2f = output_name2.replace('$',str(rating2))
    output2 = open(output_name2f,'w')
    output2.write(finaltitlelist2)
    output2.close()
    output_name3 = output_name_format2.replace('#',str(rating2))
    output_name3f = output_name3.replace('$',str(rating3))
    output3 = open(output_name3f,'w')
    output3.write(finaltitlelist3)
    output3.close()
    output_name4 = output_name_format2.replace('#',str(rating3))
    output_name4f = output_name4.replace('$',str(rating4))
    output4 = open(output_name4f,'w')
    output4.write(finaltitlelist4)
    output4.close()
    output_name5 = output_name_format2.replace('#',str(rating4))
    output_name5f = output_name5.replace('$',str(rating5))
    output5 = open(output_name5f,'w')
    output5.write(finaltitlelist5)
    output5.close()
    output_name_format3 = 'Movies_above_#.txt'
    output_name6 = output_name_format3.replace('#',str(rating5))
    output6 = open(output_name6,'w')
    output6.write(finaltitlelist6)
    output6.close()

# to get a list of movies with ratings <=6.5, 6.5-7, 7-7.5, 7.5-8, 8-8.5, >8
ratings(6.5, 7, 7.5, 8, 8.5)

## PART.THREE
# define a function to sort the movies by directors
def director(dname):
    file = open('movielist.csv','r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    # from the enumerate, the tile is the second one; and the director is the fourth one
    titlelist =[]
    for movie in movielist[1:]:
        title = movie[2]
        directors = movie[4]
        if directors == dname:
            titlelist.append(title)
        finaltitlelist = '\n'.join(titlelist)
    # store the result into a txt file
    output_name_format = 'Moives_by_#.txt'
    output_name = output_name_format.replace('#',dname)
    output = open(output_name,'w')
    output.write(finaltitlelist)
    output.close()

# to get the lists of movies directed by my favorite directors
directorlist = ['Alfred Hitchcock','Steven Spielberg','James Cameron','Quentin Tarantino','James Mangold','Christopher Nolan',
                'Sam Raimi','Joe Johnston','Joss Whedon','Zack Snyder','Justin Lin','Nancy Meyers']
for directornm in directorlist:
    director(directornm)

## PART.FOUR
# define a function to sort the movies by its genres
def genre(gname):
    file = open('movielist.csv','r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    # from the enumerate, the tile is the second one; and the genre is the ninth one
    titlelist =[]
    for movie in movielist[1:]:
        title = movie[2]
        genres = str(movie[9]).split(',')
        for genrenm in genres:
            if genrenm == gname:
                titlelist.append(title)
        finaltitlelist = '\n'.join(titlelist)
    # store the result into a txt file
    output_name_format = '#_Moives.txt'
    output_name = output_name_format.replace('#',str(gname).capitalize())
    output = open(output_name,'w')
    output.write(finaltitlelist)
    output.close()

# define a function to get a list of all genres shown in the data
def get_genre_list(filenm):
    file = open(filenm,'r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    genrelist =[]
    for movie in movielist[1:]:
        genres = movie[9]
        genre = str(genres).split(',')
        for genrenm in genre:
            fgenrenm = genrenm.lstrip()
            if fgenrenm != '':
                if fgenrenm not in genrelist:
                    genrelist.append(fgenrenm)
    return genrelist

# to get the lists of movies categorized by different genres
genre_list = get_genre_list('movielist.csv')
for genrenm in genre_list:
    genre(genrenm)

## PART.FIVE
# to sort the original movie list on its ratings
infile = open('movielist.csv')
reader = csv.reader(infile)
next(reader) # not read the header which is the first row of the csv file
sortedlist = sorted(reader, key = operator.itemgetter(6))  # 6 specifies according to sixth column we want to sort
#now write the sorte result into new CSV file
outfile = open('sortedmovielist.csv','w')
csvout = csv.writer(outfile)
csvout.writerows(sortedlist)
outfile.close()

# define a function to obtain the top50 movies in different genres
def top50films(gnm):
    file = open('sortedmovielist.csv','r')
    reader = csv.reader(file)
    movielist = list(reader)
    file.close()
    #for column,tuple in enumerate(movielist[0]):
        #print(column,tuple)
    # from the enumerate, the tile is the second one; and the genre is the ninth one
    titlelist =[]
    for movie in movielist:
        if movie != []:
            title = movie[2]
            ratings = movie[6]
            genres = str(movie[9]).split(',')
            if ratings >= str(8):
                for genrenm in genres:
                    fgenrenm = genrenm.lstrip()
                    if fgenrenm == gnm:
                        titlelist.append(title)
        finaltitlelist = '\n'.join(titlelist[:50])
    # store the result into a txt file
    output_name_format = 'Top50_#_Moives.txt'
    output_name = output_name_format.replace('#',str(gnm).capitalize())
    output = open(output_name,'w')
    output.write(finaltitlelist)
    output.close()

# to get the lists of top50 movies of some of my favorite genres
genrelist = ['action','adventure','animation','comedy','crime','drama','mystery','romance','sci_fi']
for eachgenre in genrelist:
    top50films(eachgenre)
