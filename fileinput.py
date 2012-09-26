#flag=[age, gender, occupation, zip code, action, adventure, animation, children's, comedy, crime,
#documentary, drama, fantasy, film-noir, horror, musical, mystery, romance, sci-fi,
#thriller, war, western, rating]
lenflag=0
flag = [1, # Age
        0, # Gender
        0, # Occupation
        0, # Zip Code
        0, # Title
        0, # Release Date
        0, # Unknown (always blank)
        0, # URL
        0, # Unknown (a genre)
        0, # Action
        0, # Adventure
        0, # Animation
        0, # Children's
        0, # Comedy
        0, # Crime
        0, # Documentary
        0, # Drama
        0, # Fantasy
        0, # Film-noir
        0, # Horror
        0, # Musical
        0, # Mystery
        0, # Romance
        0, # Sci-fi
        0, # Thriller
        0, # War
        0, # Western
        1] # Rating

def readfiles(fname,splitter):

    def f(word):
        if type(word) is str:
            return word.strip()
        else:
            return word

    fileIn = open(fname, 'r')
    data=[map(f,line.split(splitter)) for line in fileIn]
    fileIn.close()
    print 'There are '+ str(len(data))+ ' records'
    return data


def createDictionary(dataIn, cleanfun):

    dictionary={}

    i=0
    while i<len(dataIn):
        dictionary[str(i+1)] = cleanfun(dataIn[i])
        i+=1
    
    print 'Dictionary has ' + str(len(dictionary)) + ' items.'
    

    return dictionary


def listFilter(listIn):
    def f(x):
        return x[1]

    return [x[0] for x in filter(f, zip(listIn, flag))]


def replaceIDs(dataIn,userDict,movieDict):

    dataOut=[]
    for row in dataIn:
        userID=row[0]
        movieID=row[1]
        rating=row[2]    
        newList = []
        newList.extend(userDict[userID])
        newList.extend(movieDict[movieID])
        newList.append(rating)
        dataOut.append(listFilter(newList))

    return dataOut


def cleanmoviedata(listIn):
    
    listOut = listIn[1:]
    for n in range(0,19):
            if flag[3+n] == 1:
                    listout.append(listIn[5+n])
#    newList.extend(dataIn[5:24])
    return listOut


def cleanuserdata(listIn):

    listOut = []
    #listOut.append(int(listIn[1]))
    #listOut.extend(listIn[2:])
    if flag[0] == 1:
            listOut.append(int(listIn[1]))
    if flag[1] == 1:
            listOut.append(listIn[2])
    if flag[2] == 1:
            listOut.append(listIn[3])
    return listOut


def loadDataset(num):
    trainbase = readfiles('MovieLens/u' + str(num) + '.base', '\t')
    testbase  = readfiles('MovieLens/u' + str(num) + '.test', '\t')

    movielist = readfiles('MovieLens/u.item','|')
    userlist  = readfiles('MovieLens/u.user','|')

    moviedictionary = createDictionary(movielist, cleanmoviedata)
    userdictionary  = createDictionary(userlist, cleanuserdata)

    trainSet = replaceIDs(trainbase, userdictionary, moviedictionary)
    testSet = replaceIDs(testbase, userdictionary, moviedictionary)

    return trainSet, testSet
           
             

# Read in the file to turn into lists of lists.
# Pass it the file name and the character to split by.
#training1 = readfiles('u1.base','\t')
#movielist = readfiles('u.item','|')
#userlist  = readfiles('u.user','|')

# Make the dictionaries
#moviedictionary = createDictionary(movielist,cleanmoviedata)
#userdictionary  = createDictionary(userlist,cleanuserdata)

# Make your final list with all the IDs replaced
#goodlist=replaceIDs(training1,userdictionary,moviedictionary)
