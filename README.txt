Script Execution

Tree modification

Stopping Criteria
1) Early termination via minimum threshold for gain:
Our group first attempted to implement an early termination strategy to our tree building function by adding a minimum threshold for the best gain.  In the default provided scripts, the best gain had to above 0.  We attempted to hard code some higher values such as 0.1.  However,  this modification immediately terminated tree building after the first iteration because the first split only has a gain of 0.009.  Hence, we opted to start the minimum threshold at 0 and increment this value by some small interval with each recursive call of the tree build function thereby increasing stringency of splitting with each treebuilding iteration. The disadvantage of a minimum threshold stems from the nature of a greedy algorithm where gain may reach a relative minimum and stop the treebuilding even though the subsequent splits could have led to very high gains.

2) Early termination via minimum number of instances in best sets:
This is to prevent the treebuilder from essentially splitting "hairs" and creating nodes that are ill supported by the training data.  In the default provided scripts, the best sets were chosen without any consideration of how small or large the best sets were as long as they weren't empty.  A printout of best sets' lengths showed that the tree nodes were sometimes creating subbranches based on only 4-5 instances, meaning set1 and set2 were of 1,2 instances each.  Any subbranch based on less than three instances is too negligible of a split when training upon 20,000 instances. The buildtree function was modified to accept an instance_minimum variable that will cause splitting to stop once the node has reached some minimum threshold determined by the user. The disadvantage of this approach is that forcing splitting to stop at a set threshold can lead to nodes with high entropy (poorly classified nodes).

Justification




Contributions
Liu Liu:
 
Aaron Mishtal:

Hannah Woo: I worked with Aaron to create fileinput script to consolidate the training and testing data with the movie and user information.  I added stopping criteria into the treepredict script and wrote the section describing those 2 strategies.  



