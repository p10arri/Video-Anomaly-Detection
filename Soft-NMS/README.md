# SOFT-NMS
Non-maximum suppression is an integral part of the object detection pipeline. First, it sorts all detection boxes on the basis of their scores. The detection box M with the maximum score is selected and all other detection boxes
with a significant overlap (using a pre-defined threshold) with M are suppressed. This process is recursively applied on the remaining boxes. Soft-NMS is an algorithm which decays the detection scores of all other objects
as a continuous function of their overlap with M.

Here is the pseudo-code of the algorithm displayed

![pseudo-code](https://user-images.githubusercontent.com/92929846/146601937-cc97a877-0439-40a7-abfc-69e47d45aa22.PNG)



