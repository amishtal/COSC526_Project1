COSC 526 Project 1 MovieLens Decision Tree
Liu Liu, Aaron Mishtal, Hannah Woo
Fall 2012

Script Execution:
We have 5 files for demo_tree. 
Denise, please set global attribute at the top of fileinput.py to the absolute path to your data set.


Tree modification:
- fileinput.py will read in the training data and test data to create a list of lists with all attributes.
- created an attribute filter to change what attributes are being passed to the build tree function for consideration
- implemented 2 stopping criteria in buildtree explained in the "stopping criteria" section.

Stopping Criteria:
1) Early termination via minimum threshold for gain:
Our group first attempted to implement an early termination strategy to our tree building function by adding a minimum threshold for the best gain.  In the default provided scripts, the best gain had to above 0.  We attempted to hard code some higher values such as 0.1.  However,  this modification immediately terminated tree building after the first iteration because the first split only has a gain of 0.009.  Hence, we opted to start the minimum threshold at 0 and increment this value by some small interval with each recursive call of the tree build function thereby increasing stringency of splitting with each treebuilding iteration. The disadvantage of a minimum threshold stems from the nature of a greedy algorithm where gain may reach a relative minimum and stop the treebuilding even though the subsequent splits could have led to very high gains.

We found that this strategy improves classification rates of the test data.  We tested 10 different values between 0 and 10e-9 for the increment and found that using an incrementing minimum provided better classification rates than a fixed minimum threshold at 0 for all 5 test data sets. The best classification rates were provided by the following values for gain_increment.   
u1: 0.001
u2: 0.01
u3: 0.0001 
u4: 1e-05
u5: 0.01


2) Early termination via minimum number of instances in best sets:
This is to prevent the treebuilder from essentially splitting "hairs" and creating nodes that are ill supported by the training data.  In the default provided scripts, the best sets were chosen without any consideration of how small or large the best sets were as long as they weren't empty.  A printout of best sets' lengths showed that these sets were sometimes only 1,2 instances each.  Any subbranch based on less than three instances is too negligible of a split when training upon 20,000 instances. The buildtree function was modified to accept an instance_minimum variable that will cause splitting to stop once the node has reached some minimum threshold determined by the user. The disadvantage of this approach is that forcing splitting to stop at a set threshold can lead to nodes with high entropy (poorly classified nodes).

Justification:
Our initial pass through the datasets removed the following columns of values from consideration because they are nominal values unique or almost unique for each instance in the data: zipcode, timestamp, movie title, IMDb URL.  UserID and movieID were also excluded after mapping the information into one consolidated list of lists of user info, movie id and rating.
 
We noticed entries in the movie information data were missing attribute values.  Some of these values were inconsequential as we planned to exclude those columns, but movie dates were missing as well.  We elected to exclude movie dates for all movies to forgo the challenge of trying to represent the missing values.  

We binned the ratings from a 5-class problem to a 2-class one, because we saw that most of the training and testing data was rating 4.  Therefore, guessing 4 for all instances led to ~34% classification rate.  Our 3-class decision tree immediately improved the classification rate.  However, we also tried a 2-class problem and found that provided the best classification rates at 60% .  This is 10% better than random guess of 50%, but more interestingly, it is better than a always guessing class 1(which is 54% of the total data for u1). This is better probabilities than the other larger class problems.   This is still a valuable classification because we find out with more confidence if a rating will be good or bad.  

When classifying the test data, we broke ties by choosing one the classes by random probability. 

Usage of attributes

Based on previous studies, some attributes are eliminated from the data set (however, information like movie title, URL, zip code, etc are still considered in the final attribute usage). By analyzing the distribution of the users' gender, age and the movies' genre according to ratings, We reached a conclusion: users' gender and age have different correlations with ratings in respect of different users, which indicate that they are helpful to distinguish the different user' characteristics. Furthermore, when it comes to genre, we thought it might be redundant if we use all those different genres. We found that for those total 18 genres, only several of them have the averaged ratings noticably different from the rest. Thus we might only have to manipulate those genres that are more instrumental to describe the characteristics of a movie. And actually it does help the performance of the decision trees.
u1:
u2:
u3:
u4:
u5:


Contributions
Liu Liu: I conducted some analysis on attributes of the users and movies using python and MS EXCEL. Also I and Aaron worked on implementing the usage of the attributes in the fileinput script.
 
Aaron Mishtal: The main coder and debugger

Hannah Woo: I worked with Aaron to create fileinput script to consolidate the training and testing data with the movie and user information.  I added stopping criteria into the treepredict script and wrote the section describing those 2 strategies. 




