
Data Engineering – Use Case – Read the file from S3 and Load it in RDS.
Problem Statement -  An organization received source systems data to an input landing. The requirement is to load the data to a relational database system so that BI reports can be developed. The average number of records in the file is 10000.
Solution:  Looking at the problem statement and file size, we are going to develop an event driven architecture to load the data. The solution steps.
1.	The input files are placed in S3 bucket.
2.	An event is triggered, which in turn 
3.	The lambda function extracts the file details from event context and load the data in RDS.
We are going to follow below solution architecture to solve this problem.




