"""
BACKGROUND INFORMATION:
You are provided a dataset which has information on what images contain.
This dataset is used to train an image classification model: the model predicts a single class of what it thinks is in each image. Ideally, the model performs
very well on all different classes: we want the model to be fair and
unbiased.

SITUATION:
The company needs to ship their best 'image classification' model in a few weeks, and
wants you to analyze how well the model performs. The goal is to get a good idea
of where the model performs well and where the model does not perform well, with
a goal of providing specific, actionable data for the model architects and
trainers (R&D) to work with, to improve the model before the deadline.

Your job:
Provide actionable information to R&D exposing where the model fails and suggest
ways that the model could be improved. Focus on using data to back you up!

Parameters:
- Use anything in the standard default python library
- May not use any libraries that need to be installed via pip, such as pandas, scikit, etc.
- Use any internet resources you need to aid in your analysis

Files:
- labels_and_predictions.json: Labels and predictions by the model. Two keys at top level: 
   - 'labels': Each String in this List represents the label applied to the image at that index
   - 'predictions': Each string in this list represents the prediction of the model of the image at that index

Todo:
1. Load the data (the path to data is provided)
2. Calculate the distribution of classes in the ground truth labels; do the same for predictions
3. Calculate the overall accuracy of the model (out of all images, how many did the model correctly classify?)
4. Calculate precision, recall, and f1 for each of the classes
5. Compute the confusion matrix
6. Based off of all the data, 
   - Which classes does the model do well on?
   - Which classes does the model do poorly on?
   - How would you suggest improving the model, simply through data (i.e. not "magically" improve the architecture, or train for more iterations, etc.)
   - How would you ensure that the model performs equally as well on all classes?
"""

DATA_PATH = '/home/coderpad/data/labels_and_predictions.json'
import json
from collections import Counter

# Opening JSON file
with open(DATA_PATH) as json_file:
    data = json.load(json_file)
    print(data.keys())

# * 2.Get the distributions
pred_counts = Counter(data['predictions'])
labels_counts = Counter(data['labels'])
# * Normalize the counts.
total_pred = sum([count for _, count in pred_counts.items()])
total_labels = sum([count for _, count in labels_counts.items()])

pred_counts = {c: count/total_pred for c, count in pred_counts.items()}
labels_counts = {c: count/total_pred for c, count in labels_counts.items()}

print(f"{pred_counts=}\n{labels_counts=}")

# * 3. Accuracy = TP / all
tp_count = 0
for pred, label in zip(data['predictions'], data['labels']):
    if pred == label:
        tp_count += 1
acc = tp_count / total_labels
print(f"Accuracy: {acc}")

# * 4. Precision = TP / (TP + FP)
# * Recall = TP / (TP + FN)
for cls in set(data['labels']):
    _tp_count = 0
    _fp_count = 0
    _fn_count = 0
    for pred, label in zip(data['predictions'], data['labels']):
        # if pred != cls: continue
        if label == cls and pred != cls:
            _fn_count += 1

        if pred == cls and pred == label:
            _tp_count += 1
        elif pred == cls and label != cls:
            _fp_count += 1
    prec = _tp_count / (_fp_count+_tp_count)
    recall = _tp_count / (_fn_count+_tp_count)
    print(f"Class {cls}, Precision={prec: .3f}")
    print(f"Class {cls}, Recall={recall: .3f}")
    print(f"Class {cls}, F1={2 / (1/prec + 1/recall): .3f}")
    print()
        
# * 5. Confusion matrix
## Label      A  !A
## Predict   TP, FP
## 

# labels:  A B C
# A        9 5 
# B
# C

matrix = {cls: {} for cls in set(data['labels'])}
for pred, label in zip(data['predictions'], data['labels']):
    count = matrix[pred].get(label, 0)
    matrix[pred][label] = count + 1
print(matrix)