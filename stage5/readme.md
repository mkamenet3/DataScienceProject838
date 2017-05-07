# Stage 5 - Insights

The goal of this project is to do some data analysis on the integrated and
cleaned table, to infer insights. 


## Details

The goal is to create:

- a CSV file storing Table E, the integrated table which is the output of project stage 4. 
- a pdf file that discusses the following issues: 
  - Statistics on Table E: specifically, what is the schema of Table E, how many tuples are in Table E? Give at least four sample tuples from Table E. 
  - What was the data analysis task that you wanted to do? (Example: we wanted to know if we can use the rest of the attributes to accurately predict the value of the attribute loan\_repaid.) For that task, describe in detail the data analysis process that you went through. 
  - Give any accuracy numbers that you have obtained (such as precision and recall for your classification scheme).  
  - What did you learn/conclude from your data analysis? Were there any problems with the analysis process and with the data? 

If you have more time, what would you propose you can do next? 


## What's in the folder

We follow the format of the previous stage:

- **DATA** directory: contains csv (first 100) of the final integreated Table
  E (from stage 4).
- **CODE** diretory: contains a jupyter notebook that goes through the analysis


Due to the size of the data, in the **DATA** directory, we only present the
first 100 observations. The full data set can be found on our website
[here]<https://sites.google.com/site/cs838datascienceprojectmovie/>

## Insights

Our initial insights on this dataset:

- data for 2015 appears to incomplete (anomaly year)
- more information is needed on how data was collected. Early 2000's data show much fewer movies being made. Is this an artificat of the selection criteria in creating the dataset or is that accurate?
- boost in movies coming out between 2008 - 2013
- largest group by genre is drama, followed by romance-comedy; action-adventure is a smaller portion than expected
- The highest grossing movie in the dataset is Avatar followed by Avengers. Least grossing movies are Pride and The Hire:Chosen
- It looks like there has been a slight uptick in fmaily-children films and and also fantasy/scifi. 
- romance-comedy and family-children appear to be the genres which vary the least in terms of gross sales.
- No correlation identified between gross sales and facebook likes/imdb score nor imdb_score and facebook likes.
- There appears to be no relationship between imdb_score and grossnum until 2012 and later, when there is a reasonable positive relationship between the two.
- cast_total_facebook_likes on average have been steadily increasing, giving evidence to our earlier theory that much of this can be driven by the increasing prominence and use of IMDB as a review website and database. 

Details about insights along with challenges and future work can be found in **Analysis.ipynb** inside the ```CODE``` folder. Please visit our website for more details.


