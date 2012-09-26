
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


def createDictionary(dataIn,cleanfun):

    dictionary={}

    i=0
    while i<len(dataIn):
        dictionary[str(i+1)] = cleanfun(dataIn[i])
        i+=1
    
    print 'Dictionary has ' + str(len(dictionary)) + ' items.'
    

    return dictionary

 
def replaceIDs(dataIn,dictIn,dictIn2):

    dataOut=[]
    for row in dataIn:
        userID=row[0]
        movieID=row[1]
        rating=row[2]    
        newList = []
        newList.extend(dictIn[userID])
        newList.extend(dictIn2[movieID])
        newList.append(rating)
        dataOut.append(newList)

    return dataOut


def cleanmoviedata(dataIn):
    
    newList = []
    newList.extend(dataIn[5:24])
    return newList


def cleanuserdata(dataIn):

    newList = []
    newList.append(int(dataIn[1]))
    newList.extend(dataIn[2:4])
    return newList


def loadDataset(num):
    trainbase = readfiles('MovieLens/u' + str(num) + '.base', '\t')
    testbase  = readfiles('MovieLens/u' + str(num) + '.test', '\t')

    movielist = readfiles('MovieLens/u.item','|')
    userlist  = readfiles('MovieLens/u.user','|')

    moviedictionary = createDictionary(movielist,cleanmoviedata)
    userdictionary  = createDictionary(userlist,cleanuserdata)

    return replaceIDs(trainbase,userdictionary,moviedictionary), \
           replaceIDs(testbase,userdictionary,moviedictionary)
             

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
