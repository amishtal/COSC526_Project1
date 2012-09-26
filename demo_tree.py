#!/usr/bin/python
#
# Script to demonstrate the CART-like DT classifier from
# Chapter 7 of "Programming Collective Intelligence" by
# T. Segaran, O'Reilly, (c) 2007
#
import treepredict
import fileinput


train_data, test_data = fileinput.loadDataset(1)

tree=treepredict.buildtree(train_data, gain_threshold=0.009)


for row in test_data:
    actual    = row[-1]
#    print row
    predicted = treepredict.classify(row, tree)
    

    print 'Actual:', actual, 'Predicted:', predicted

# Let's see what it looks like...
#print "\nFinal tree...\n"
treepredict.printtree(tree)

# Produce a png of the tree
#treepredict.drawtree(tree,jpeg="sample_tree.jpg")
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
