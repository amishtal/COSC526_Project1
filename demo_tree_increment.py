#!/usr/bin/python
import sys
sys.path.append('/usr/local/cellar/pil/1.1.7/lib/python2.7/site-packages/PIL/')

# Script to demonstrate the CART-like DT classifier from
# Chapter 7 of "Programming Collective Intelligence" by
# T. Segaran, O'Reilly, (c) 2007
#
import treepredict
import fileinput
import Image
import ImageDraw


# If the last parameter is set to 0, then all attributes other than 'age' and 'war' would be used.

train_data, test_data = fileinput.loadDataset(5, ['age', 'fantasy','film-noir', 'horror', 'western'], 1)


def testing_gain_increments(increments=[]):
  classresults={}
  
  for increment in increments:
    tree=treepredict.buildtree(train_data,gain_increment=increment,gain_threshold=0,instance_minimum=1)

    trainConfMat, crTrain = treepredict.testTree(train_data, tree)
    print 'Training set confusion matrix (Classification rate:', crTrain,'):'
    for row in trainConfMat:
      print '\t'.join(map(lambda x:str(x), row))

    print ''
  
    testConfMat, crTest  = treepredict.testTree(test_data,  tree) 
    print 'Test set confusion matrix (Classification rate:', crTest,'):'
    for row in testConfMat:
      print '\t'.join(map(lambda x:str(x), row))

    print ''

    
    classresults[increment]=[crTest]

  return classresults

increments=[0]

for i in xrange(1,10):
  x=10**(-i)
  increments.append(x)

print 'Increments to be tested and passed to gain_increments',increments
accuracyTest=testing_gain_increments(increments)
#print accuracyTest
values=accuracyTest.keys()
values.sort(cmp=lambda a,b:cmp(accuracyTest[a],accuracyTest[b]))
print 'Increment value with best classification rate was ',values[-1]

# Let's see what it looks like...
#print "\nFinal tree...\n"
treepredict.printtree(treepredict.buildtree(train_data,gain_increment=values[-1],gain_threshold=0,instance_minimum=1))

# Produce a png of the tree
treepredict.drawtree(tree,jpeg="sample_tree.jpg")
#print "\npng of tree generated using PIL (Python Imaging Library) modules.\n"

# Let's classify an incoming record of '(direct), USA, yes, 5' ...
#incoming = ['(direct)','USA','yes',5]
#print "Prediction of new record: ",treepredict.classify(incoming,tree)

# Finally, what does pruning do with say a mingain = 0.9 ?
#print "\nPruned tree...\n"
#treepredict.prune(tree,0.9)
#treepredict.printtree(tree)

# For group homework, modify "buildtree" function so that it stops
# when a threshold value on entropy is no longer satisfied. It should
# accept a minimum gain parameter and stop dividing the branch if
# this condition is not met.  Pruning the tree will not be used in
# this cas.
