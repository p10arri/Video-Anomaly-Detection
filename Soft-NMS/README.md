# SOFT-NMS
Non-maximum suppression is an integral part of the object detection pipeline. First, it sorts all detection boxes on the basis of their scores. The detection box M with the maximum score is selected and all other detection boxes with a significant overlap (using a pre-defined threshold) with M are suppressed. This process is recursively applied on the remaining boxes. Soft-NMS is an algorithm which decays the detection scores of all other objects as a continuous function of their overlap with M.

Here is the pseudo-code of the algorithm displayed:

![pseudo-code](https://user-images.githubusercontent.com/92929846/146601937-cc97a877-0439-40a7-abfc-69e47d45aa22.PNG)


Non-maximum suppression starts with a list of detection boxes B with scores S. After selecting the detection with the maximum score M, it removes it from the set B and appends it to the set of final detections D. It also removes any box which has an overlap greater than a threshold Nt with M in the set B. This process is repeated for remaining boxes B. boxes B with scores S. After selecting the detection with the maximum score M, it removes it from the set B and appends it to the set of final detections D. It also removes any box which has an overlap greater than a threshold Nt with M in the set B. This process is repeated for remaining boxes B.

The pruning step in the Soft-NMS algorithm can be written as a re-scoring function as follows,

![pruning-step](https://user-images.githubusercontent.com/92929846/146602688-9fef59f0-7e96-489f-a84d-3a42da91b999.PNG)

Hence, Soft-NMS sets a function threshold while deciding what should be kept or decreased from the neighborhood of M.
