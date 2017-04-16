# Stage 4 - Combining Data Into a Single Set


The goal of this project stage is to combine two tables. 


## Combining the Two Tables

- 1) Recall that in the previous  project stage you have performed entity matching between two tables A and B. Specifically, you have trained a matcher M. If you haven't already, now you need to apply matcher M to the set of candidate tuple pairs obtained after blocking on A and B, to obtain the set of all matches between A and B. 

- 2) Next, you should create the schema of a table E, which is the target table into which you will merge the two tables A and B. If tables A and B have identical schema, then table E has the same schema. Otherwise, the schema of table E will be the union of the schemas of tables A and B. 

- 3) Next, you will write a Python script to combine the tuples of tables A and B to create the tuples for table E. Note that we have discussed such a step several times in the class. This Python script will use the matches that you have created between the entities in Tables A and B. It will also have to decide on how to merge data between the two tables (using for example a set of merging rules). 

- 4) Finally, you execute this Python script to populate the table E. 

Note: In this step, if you want to add more data, such as combining a table D with tables A and B to create table E, that is fine too. 

## What Is Here


We follow the format of the previous stage where we have:

- **DATA** directory: contains csv (first 100 obs) storing Table E; set of matches between
  Tables A and B (first 100 obs)
- **CODE** directory: contains a jupyter notebook that goes through the
  matching process; python script that creates the schema for Table E and the
table itself.


Due to the size of the data, in the **DATA** directory, we only present the
first 100 observations. The full data set can be found on our website
[here]<https://sites.google.com/site/cs838datascienceprojectmovie/>

