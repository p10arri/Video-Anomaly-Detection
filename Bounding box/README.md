# BOUNDING BOX

Once the anomalies are extracted from the data, the bounding_box.py file draws the bounding boxes associated to each anomaly in all images inputes.

## Functions of bounding_box.py

+ compute_bbox(img): Returns the bounding box coordinates in (x,y,w,h) format for a given image (where img = cv2.imread(image_path))
+ compute_bbox_json(img_list, validation_file=False): Writes a json file containing all bounding box coordinates for the given images paths list (img_list  = [img_path1, img_path2, ...]) with the name 'detected_box.json'. If the validation json file is introduced it also returns the corresponding IoU score for each drawn bounding box. The json file has the following structure:
> {"directory_name": [boxes], [iou]}

# Trials

The trials directory contains all trial made for the generation of bounding_box.py. The bounding_box.ipynb shows how the bounding_box.py works.

