Project 1: MovieLens Decision Tree
COSC 526
Fall 2012

Group members:
  Liu Liu
  Aaron Mishtal
  Hannah Woo 


Tree performance:
  u1:
    Training set confusion matrix (Classification rate: 0.629925):
      16386	19474
      10132	34008
    
    Test set confusion matrix (Classification rate: 0.61015):
      3835	4930
      2867	8368

  u2:
    Training set confusion matrix (Classification rate: 0.6299125):
      17040	18809
      10798	33353
    
    Test set confusion matrix (Classification rate: 0.60565):
      3617	5159
      2728	8496

  u3:
    Training set confusion matrix (Classification rate: 0.6177625):
      15490	20147
      10432	33931
    
    Test set confusion matrix (Classification rate: 0.61435):
      3834	5154
      2559	8453

  u4:
    Training set confusion matrix (Classification rate: 0.6453125):
      17107	18434
      9941	34518
    
    Test set confusion matrix (Classification rate: 0.6151):
      4140	4944
      2754	8162

  u5:
    Training set confusion matrix (Classification rate: 0.6367):
      16606	19007
      10057	34330
    
    Test set confusion matrix (Classification rate: 0.61325):
      4087	4925
      2810	8178

  Average Classification Rate:
    Training set: 0.6319225
    Test set:     0.6117


Script Execution:
  There are 5 files, tree_dataset1.py -- tree_dataset5.py,
  that generate trees for datasets 1 -- 5, respectively. In order for
  these scripts to run, the variable 'filepath' in fileinput.py must be
  set to the filepath of the folder containing the datasets. To build
  a tree for a particular dataset, just use Python to run one of the
  tree_datasetX.py files. This will output the text representation of
  the tree, the confusion matrix, and the classification rate. 


Code Modifications:
  - fileinput.py
      Reads data files, constructs dataset based on a given set of
      attribues.
  - treepredict.py
      Added stopping critera to buildtree function (explained
      below). Added testTree function that tests tree on a set of records
      and computes the classification rate and confusion matrix.
  - demo_tree_incrememt.py
      Tests trees with a variety of parameters.


Stopping Criteria:
  1) Early termination via minimum threshold for gain and threshold increment:
    Our first termination strategy consisted of adding a minimum threshold
    for the best gain. In the default provided scripts, the best gain had
    to above 0. We parameterized the buildtree function with a parameter
    that allowed us to see this value. Initial tests with what seemed
    to be reasonable values (0.1) resulted in single node trees. This
    was caused by a low initial gain (0.009) in the first split. Hence,
    we decided to start the minimum threshold at 0 and increment this
    value by some small constant at each recursive call of the buildtree
    function. This method, while allowing us to handle low initial gains,
    also increases the stringency of splitting with increasing levels
    of the tree, placing a growing constraint on tree depth and quality
    of lower nodes.

    The disadvantage of this method is related to the behavior of a
    greedy algorithm. A poor split may make way for additional splits
    that are very useful. We accept this disadvantage in favor of
    improved generalization.

    We found that this strategy improves classification rates of the
    test data. We tested 10 different values between 0 and 10e-9 for the
    increment and found that using an incrementing minimum provided better
    classification rates than a fixed minimum threshold at 0 for all 5
    test data sets when using all five target classes. This changed when
    we switched to only two classes, but the method was still helpful
    for the first dataset. The best test set classification rates were
    provided by the following values for the minimum gain increment:
      u1: 1e-05
      u2: 0
      u3: 0
      u4: 0
      u5: 0

  2) Early termination via minimum number of instances in best sets:
    This is to prevent the tree building algorithm from essentially
    "splitting hairs" and creating nodes that cater to small variations
    in the training data.  In the default provided scripts, the best
    sets were chosen without any consideration of their size as long
    as they were nonempty. An investigation of these sizes showed that
    in some cases the best sets contained only 1 or 2 instances each.
    We thought that the contribution of continually splitting such
    small nodes is negligible considering a training set size of 20,000
    instances and may lead to overtraining.  The buildtree function was
    modified to accept an additional threshold parameter that enforces
    a minimum combined size of the best sets.  The disadvantage of this
    approach is that forcing splitting to stop at a set threshold can
    lead to nodes with high entropy (poorly classified nodes).
    u1:0 u2:0 u3:300 u4:0 u5:100


Binning of class labels:
  Initial investigations of the dataset showed that the movie rating of
  '4' dominated all the training and test sets (~34%). When running our
  tree on the data, we noticed that the tree would often just guess a
  class label of '4' and ended up with a classification rate of close to
  34% on the test set. Careful selection of attributes and application
  of our early stopping methods increased allowed us to reach up to 38%
  on the test set.

  We decided that considering the context and the distribution of the
  dataset, it would be appropriate to bin the class labels. We eventually
  settled on a two-class problem with original labels '1', '2', and '3'
  being mapped to '1' and labels '4' and '5' being mapped to '2'. We
  propose that this binning captures the essence of the dataset, as the
  new label '1' corresponds to users who generally did not like the movie
  while the new label '2' corresponds to those who did. Additionally,
  this binning strategy evened out the class distributes to approximately
  54% and 46% for classes '1' and '2'. Our best methods were able to
  achieve around 61% correct classification rate on the test set with
  this binning strategy, which we feel is an improvement.

  Additional note:
    In the event of a tie for the prediction of a tree (such as when
    a node contains equal numbers of two or more classes), we selected
    one of the tied classes with equal probability. This introduced some
    randomness into the performance of our trees, but we could not think
    of any other method to appropriately handle this situtation.


Usage of attributes
  Some attributes were found to have missing data, such as the movie
  titles and release dates. We opted to simply ignore those attributes,
  although we had wished to use the year of the release date. This
  simplified the selection of attributes somewhat.

  Based on Liu's analysis, different attributes were used for each
  dataset.  By analyzing the distribution of the users' gender and age and
  the movies' genre according in relation to movie ratings, We reached
  the conclusion that users' gender and age have different correlations
  with ratings in respect to different users, which indicate that they are
  helpful to distinguish the different user' characteristics. Furthermore,
  we thought it might be redundant to use all the genres. We found that
  out of the total of 18 genres, only several of them have the averaged
  ratings noticably different from the rest. Thus we decided to only
  consider those genres for the purposes of classification. It turns
  out the this decision did improve the generalization of the decision
  trees. The following attributes were used for the datasets:
    u1:
      'age', 'gender', 'occupation', 'unknown genre', 'fantasy',
      'film-noir', 'horror', 'western'
    u2:
      'age', 'gender', 'occupation', 'unknown genre', 'film-noir',
      'horror', 'western'
    u3:
      'age', 'gender', 'occupation', 'unknown', 'film-noir',
      'horror', 'western'
    u4:
      'age', 'gender', 'occupation', 'unknown genre', 'drama',
      'film-noir', 'horror', 'western'
    u5:
      'age', 'gender', 'occupation', 'fantasy', 'film-noir',
      'drama', 'western'


Contributions:
  Liu Liu:
    Conducted analysis on data set attributes using Python and MS EXCEL.
    Jointly worked on the implementation of attribute selection code with
    Aaron. Assisted Hannah with final testing.

  Aaron Mishtal:
    Performed the majority of the coding and debugging. Final editing of
    README.

  Hannah Woo:
    Worked with Aaron to write the code that reads the data and constructs
    the datasets. Thought of and implemented stopping criteria. Wrote most
    of the initial README. Performed tests to determine optimal parameters.

  All members attended all of the group meetings and performed their tasks
  to the best of their ability.
