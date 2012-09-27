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

tree=treepredict.buildtree(train_data,gain_increment=0,gain_threshold=0,instance_minimum=1)

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
    
    
# Let's see what it looks like...
#print "\nFinal tree...\n"
#treepredict.printtree(tree)


# Produce a png of the tree
print '\nPrinting tree image...'
treepredict.drawtree(tree,jpeg="sample_tree.jpg")


# For group homework, modify "buildtree" function so that it stops
# when a threshold value on entropy is no longer satisfied. It should
# accept a minimum gain parameter and stop dividing the branch if
# this condition is not met.  Pruning the tree will not be used in
# this cas.
