# SOFT-NMS
Non-maximum suppression is an integral part of the object detection pipeline. First, it sorts all detection boxes on the basis of their scores. The detection box M with the maximum score is selected and all other detection boxes
with a significant overlap (using a pre-defined threshold) with M are suppressed. This process is recursively applied on the remaining boxes. Soft-NMS is an algorithm which decays the detection scores of all other objects
as a continuous function of their overlap with M.

![Pseudo-code](https://github.com/p10arri/Video-Anomaly-Detection/Soft-NMS/pseudo-code.png?raw=true)

