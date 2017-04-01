# Stage3 - CODE

This folder contains the notebook **cs838stage3.ipynb**. This notebook has all
of our work as well as results. We use the python module
*py_entitymatching* to match on movie title-year.

### Summary of results

We first used the overlap blocker to black on attribute year. This resulted in
3,288,743 candidate tuples. 

Based on the objectives of the stage, we find that we are able to train
a logistic regression matcher using 10-fold cross validation that achieves the required precision (at least
90\%) and the highest possible recall. Specifically we are able to minimize the
type II error rate such that there are no false negatives and only 2 false
positives in our final testing set. Precision is reached to 96.55\%, recall is
at 100\%, and F1 is at 98.25\%.

An error analysis of misclassification shows us that there appears to be
a consistent error in that some movie titles are a year off between A and B.
This is likely due to the definition of movie year (perhaps release year versus
year filmed). This was not mentioned in our data source. When considering
debugging based on this, we were concerned that without knowing the source of
the error or reason for error, we may accidently bias the sample if we allow
a window (perhaps within 1 or 2 years). We leave this
for further exploration.



