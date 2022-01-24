


1st package: 
# [Classification-Evaluation-Metrics](https://pypi.org/project/Cls-Evaluation/0.0.1/)

### Basic metrics for evaluating classification results

[![PyPI version](https://badge.fury.io/py/0.0.1.svg)](https://badge.fury.io/py/0.0.1) [![Python 3.7.7](https://img.shields.io/pypi/pyversions/python-gitlab.svg)](https://www.python.org/downloads/release/python-360/)
## Functionalities

- Calculate True positive, true negative, false positive and false negative
- Accuracy calculates the number of times classifier predicts correctly.
- F1 score: Harmonic mean of precision and recall.
- Precision: What % of predicted Positive aspects are actually Positive?
- Recall: How many actual Positives are correctly classified?
- False dicovery rate (FDR)
  

## Methods
* Confusion matrix
* Accuracy
* F1 Score
* Precision 
* Recall
* FDR

## Installation


Install the dependencies from setup.py.

```sh
pip install Cls-Evaluation==0.0.1
```
## Simple Demo


```ruby
from setuptools import setup, find_packages
import Cls_evaluation as cl
conf_matrix = cl.confusion_matrix([1,0,0,1,1,0],[0,1,0,1,1,1])

print("Accuracy", cl.acc(conf_matrix))
print("Precision",cl.precision(conf_matrix))
print("Recall",cl.recall(conf_matrix))
print("F1 score", cl.F1(conf_matrix))
print("FDR",cl.FDR(conf_matrix))

Accuracy 0.5
Precision 0.5
Recall 0.6666666666666666
F1 score 0.5714285714285714
FDR 0.5
```

## License
OSI Approved :: MIT License

## Intended Audience
Education

## Reference

Scikit learn (https://scikit-learn.org/stable/)
