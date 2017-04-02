# Stage3 - DATA

In this directory, we host the original .csv files and ones created through the
stage3 process as indicated in the project stage step [here](https://sites.google.com/site/anhaidgroup/courses/cs-838-spring-2017/project-description/stage-3)


Our goal in this stage is to match two files on movie title-year. Specifically,
we aim to create a matcher that achieves precision of at least 90% and recall
as high as possible.

##Contents Details

**Due to the size of these files, the full csv files will instead be available on our project
website for download
[here](https://sites.google.com/site/cs838datascienceprojectmovie/). We apologize for the inconvenience. In this repository, we have only included the first 100 observations of each of these for illustration purposes.**

- **A**: *movie1_stage3.csv*
  - Number of tuples in A: 5043
  - Attributes of focus:
    - *id* = unique identifier for each movie
    - *title* = movie title
    - *year* = year associated with the movie
- **B**: *movie2_stage3.csv*
  - Number of tuples in B: 27,278
  - Attributes of focus:
    - *movieId* = unique identifier for each movie
    - *title* = movie title
    - *year* = movie year
- Number of tuples in AxB: 137,562,954
- **C**: *candidate_pairs.csv*
  - this file is a csv that contains all of the tuple pairs that survive the
    blocking step
- **G**: *gold.csv*
  - this file is our golden data, which contains true movie-year matches which
    we have verified.
  - this was created by randomly sampling 500 tuples and then labeling them as
    either 1 for match or 0 for no match under the variable *label*
- **I**: *setI.csv*
  - training set
- **J**: *setJ.csv*
  - testing set


