# VIDEO ANOMALY DETECTION
[This project is part of the course in 364.021/2/41/42/43/44/45, UE Computer Vision of JKU.]

The idea of this project is to develop an unsupervised video anomaly detection system for a surveillance dron. 

# DATA
[The data is provided by the teachers of the course. ]
The dron has 10 cameras where there is defined central camera. For each camera we are given 7 frames, thus we are working with 70 images per sample. They are defined as follows:
+ f = {1,2,3,4,5,6,7} where 3 is the center frame
+ c = {B01,B02, B03, B04, B05, G01, G02, G03, G04, G05} where B01 is the center camera

For the training, valdiation and test we are given the following number of image sets (each set has 70 images):
+ 26 for training 
+ 11 for validation 
+ 13 test 

All data is located in data_Wisar. Each data sample is defined as follows: data_WiSAR\data\set type\set number\f-c.png (i.e:  data_WiSAR\data\train\train-1-0\0-B01.png)

# GOAL
The goal is to obtain bounding boxes in the 13 central pictures of the test set.

# STRUCTURE OF THE PROBLEM

# PAPERS

Here all the papers we have used for the project.
  - Unsupervised Pixel-wise Hyperspectral Anomaly Detection via Autoencoding Adversarial Networks [https://arxiv.org/pdf/2101.08827.pdf]
  - Ensemble and Random Collaborative Representation-Based Anomaly Detector for Hyperspectral Imagery[https://arxiv.org/pdf/2101.01976.pdf]
