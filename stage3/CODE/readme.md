# Stage3 - CODE

This folder contains the notebook **cs838stage3.ipynb**. This notebook has all
of our work as well as results. We use the python module
*py_entitymatching* to match on movie title-year.

### Summary of results

We first used the overlap blocker to block on attribute year. This resulted in
3,288,743 candidate tuples. 

Based on the objectives of the stage, we find that we are able to train
a logistic regression matcher using 10-fold cross validation that achieves the required precision (at least
90\%) and the highest possible recall. Specifically we are able to minimize the
type II error rate such that there are no false positives and only 1 false
negative in our final testing set. Precision is reached to 100\%, recall is
at 98.21\%, and F1 is at 99.1\%. 



### Timing
- overlap blocking step: 25.151411594869387
- get features step: 1.66341188046772
- extract features from I: 1.7220805879769614
- matching step - precision: 0.5405771328996707
- matching step - recall: 0.5123778116430913
- extract features from J: 0.9315263253015473
- ML matcher fit (logreg): 0.004608405979070085
- Prediction from ML Matcher: 0.0023624383898095402


