"""
UNSUPERVISED BOUNDING BOXES FOR COMPUTER VISION PROJECT

    This file takes a binary picture where the background should be in black and the anomaly in any desired color. The inputed 

    The compute_bbox returns the box coordinates in (x,y,w,h), so, in order to obtain the JSON file with all the detected box coordinates, 
    you need to use the compute_bbox_json, where the input is a list of all the images to detect.

"""
import matplotlib.pyplot as plt
import cv2
from utils import compute_IoU
import evaluate
import numpy as np
import json
import os

def compute_bbox(img):
    """
    Calculates the bounding boxes for the inputed image.
    Input: 
        +img = cv2.imread(img_path)
    Output: 
        +detected_boxes: box coordinates in (x,y,w,h) format
    """

    # # Display the images
    # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # plt.figure(figsize=(20, 18), dpi=80)
    # plt.imshow(rgb)
    # plt.title('Image to detect')
    # plt.show()

    # working over a copy
    img_ = img.copy()
    # convert to grayscale
    gray = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)

    # threshold
    thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]

    # get contours
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    detected_boxes = []
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        detected_boxes.append((x,y,w,h))
        cv2.rectangle(img_, (x, y), (x+w, y+h), (0, 255, 0), 2) # Draw green bounding boxes over the copied image
    #     print("x,y,w,h:",x,y,w,h)
    
    print('Box coordinates of detected objects (x,y,w,h):', detected_boxes)
    
    # # display image with bounding boxes
    # rgb_ =  cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    # plt.figure(figsize=(20, 18), dpi=80)
    # plt.imshow(rgb_)
    # plt.title('bounding boxes')
    # plt.show()



    return detected_boxes

def compute_bbox_json(img_list, validation_file=False):
    """
    Calculates the bounding boxes for all listed images.
    Input: 
        + img_list = [img_path1, img_path2, ...]
        + validation_file: (optional) json file for the validation. 
            True = IoU scores for each detected boxes are given
            False = There is no IoU score given
    """   
    
    for img_path in img_list:
        directory_name =  os.path.dirname(img_path) 

        img = cv2.imread(img_path)
        box = compute_bbox(img)

        # create directory for json file
        detected_box = {}
        detected_box[directory_name] = [box]

        # Check for validation
        if valdiation_file:
            validation_boxes = validation_file[directory_name]
            iou_scores = compute_IoU(box, validation_boxes) # matrix of IoU scores

            iou_ = np.zeros(iou_scores.shape[0])
            # Maximal IoU score corresponds to the given box
            for pos, row in enumerate(iou_scores):
                # IoU value = Index of non zero element in the row
                    iou_[pos]= max(row[np.nonzero(row)]) 
            # add IoU scores to the dictionary
            detected_box[directory_name].append(iou_)

        #writting the json file
        with open('detected_box.json', 'w') as f:
            json.dump(detected_box, f)
