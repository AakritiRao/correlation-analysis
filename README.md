# correlation-analysis

## Breakdown
We will be writing a script to automate analysis of question correlation.
Here's a high-level way of breaking down the parts of the scripts.



#### userBuckets.py

Functions for pulling and manipulating user buckets. 

###### Get "yes" and "no" user buckets
```
def getUserBuckets(ques_id):
    call sql query given a ques_id 
    return a dictonary with yes and no user buckets (amount), id, and total amount

```

###### Calculate the user buckets from the "yes" user bucket of the root question
```
def getUserBucketsYes(root, ques_id):
    call sql query given a root['id'] and ques_id
    return a dictonary with yes and no user buckets for ques_id, amount for each bucket, and q_id

```

###### Calculate the user buckets from the "no" user bucket of the root question
```
def getUserBucketsNo(root, ques_id):
    call sql query given a root['id'] and ques_id
     return a dictonary with yes and no user buckets for ques_id, amount for each bucket, and q_id

```

#### analysis.py
	
Function for the calculations behind the analysis. This will use functions from userBuckets.py

###### Calculate correlation for a ques_id given the "yes" user bucket of root question 
```
def calcCorrelationYes(root, ques_id):
    call and and save getUserBucketsYes(root, ques_id) in variable "quesBuckets"
    return dictonary with yesCorrelation: quesBuckets['yes#']/root['yes#'], noCorrelation: quesBuckets['no#']/root['yes#'], q_id

```

###### Calculate correlation for a ques_id given the "no" user bucket of root question 
```
def calcCorrelationYes(root, ques_id):
    call and and save getUserBucketsNo(root, ques_id) in variable "quesBuckets"
    return dictonary with yesCorrelation: quesBuckets['yes#']/root['no#'], noCorrelation: quesBuckets['no#']/root['no#'], q_id

```
    
	 
Let's just start from there. We can figure out how to piece everything together once we have these completed.

##dependencies (pip3)

xlsxwriter

mysql-connector





