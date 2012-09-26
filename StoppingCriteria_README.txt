Stopping Criteria

1) Early termination via minimum threshold for gain:
Our group first attempted to implement an early termination strategy to our tree building function by adding a minimum threshold for the best gain.  In the provided scripts, the minimum threshold for gain was 0.  We attempted to hard code some higher values such as 0.1.  However,  this modification immediately terminated tree building after the first iteration because the first split only has a gain of 0.009.  Hence, we opted to start the minimum threshold at 0 and increment this value by some small interval with each recursive call of the tree build function thereby increasing stringency of splitting with each treebuilding iteration.  
