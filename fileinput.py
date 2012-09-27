#flag=[age, gender, occupation, zip code, action, adventure, animation, children's, comedy, crime,
#documentary, drama, fantasy, film-noir, horror, musical, mystery, romance, sci-fi,
#thriller, war, western, rating]
lenflag=0


# Takes a list of attribute names and a flag (0 or 1).
# If the flag is set (== 1) then the given attributes
# will be set to 1 in the returned list and all others
# will be set to 0. Otherwise, the given attributes will
# be set to zero and all others to 1. An exception is
# that the last attribute (rating) will always be set to
# one

attributeDict = {
  'age'           : 0,
  'gender'        : 1,
  'occupation'    : 2,
  'zip code'      : 3,
  'title'         : 4,
  'release date'  : 5,
  'unknown'       : 6,
  'url'           : 7, 
  'unknown genre' : 8,
  'action'        : 9,
  'adventure'     :10,
  'animation'     :11,
  'childrens'     :12,
  'comedy'        :13,
  'crime'         :14,
  'documentary'   :15,
  'drama'         :16,
  'fantasy'       :17,
  'film-noir'     :18,
  'horror'        :19,
  'musical'       :20,
  'mystery'       :21,
  'romance'       :22,
  'sci-fi'        :23,
  'thriller'      :24,
  'war'           :25,
  'western'       :26,
  'rating'        :27
}

def createAttributeFlags(attributeList, keep):
    flags= [not keep, # Age
            not keep, # Gender
            not keep, # Occupation
            not keep, # Zip Code
            not keep, # Title
            not keep, # Release Date
            not keep, # Unknown (always blank)
            not keep, # URL
            not keep, # Unknown (a genre)
            not keep, # Action
            not keep, # Adventure
            not keep, # Animation
            not keep, # Children's
            not keep, # Comedy
            not keep, # Crime
            not keep, # Documentary
            not keep, # Drama
            not keep, # Fantasy
            not keep, # Film-noir
            not keep, # Horror
            not keep, # Musical
            not keep, # Mystery
            not keep, # Romance
            not keep, # Sci-fi
            not keep, # Thriller
            not keep, # War
            not keep, # Western
            not keep] # Rating

    for attribute in attributeList:
        flags[ attributeDict[attribute.lower()] ] = keep

    flags[-1] = 1

    return flags


def readfiles(fname,splitter):

    def f(word):
        if type(word) is str:
            return word.strip()
        else:
            return word

    fileIn = open(fname, 'r')
    data=[map(f,line.split(splitter)) for line in fileIn]
    fileIn.close()
#    print 'There are '+ str(len(data))+ ' records'
    return data


def createDictionary(dataIn, cleanfun):

    dictionary={}

    i=0
    while i<len(dataIn):
        dictionary[str(i+1)] = cleanfun(dataIn[i])
        i+=1
    
#    print 'Dictionary has ' + str(len(dictionary)) + ' items.'
    

    return dictionary


def listFilter(listIn, keepList):
    def f(x):
        return x[1]

    return [x[0] for x in filter(f, zip(listIn, keepList))]


def replaceIDs(dataIn,userDict,movieDict, attributeFlags):

    ratingDict = {'1':'1', '2':'1', '3':'1', '4':'2', '5':'2'}

    dataOut=[]
    for row in dataIn:
        userID=row[0]
        movieID=row[1]
        rating=row[2]    
        newList = []
        newList.extend(userDict[userID])
        newList.extend(movieDict[movieID])
        newList.append(ratingDict[rating])
        dataOut.append(listFilter(newList, attributeFlags))

    return dataOut


def cleanmoviedata(listIn):
    
    listOut = listIn[1:]
    return listOut


def cleanuserdata(listIn):

    listOut = []
    listOut.append(int(listIn[1]))
    listOut.extend(listIn[2:])
    return listOut


def loadDataset(num, attributes=[], keep=0):
    print 'Loading dataset', num
    if keep:
        print '  Keeping attributes', attributes
    else:
        print '  Ignoring attributes', attributes
    print ''

    attributeFlags = createAttributeFlags(attributes, keep)

    trainbase = readfiles('MovieLens/u' + str(num) + '.base', '\t')
    testbase  = readfiles('MovieLens/u' + str(num) + '.test', '\t')

    movielist = readfiles('MovieLens/u.item','|')
    userlist  = readfiles('MovieLens/u.user','|')

    moviedictionary = createDictionary(movielist, cleanmoviedata)
    userdictionary  = createDictionary(userlist, cleanuserdata)

    trainSet = replaceIDs(trainbase, userdictionary, moviedictionary, attributeFlags)
    testSet = replaceIDs(testbase, userdictionary, moviedictionary, attributeFlags)

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
