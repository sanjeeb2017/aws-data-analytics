<img width="527" alt="image" src="https://user-images.githubusercontent.com/24868114/224403983-02f0a5ec-23bd-4087-a63e-309b6ce89370.png">

# Data Engineering – AWS S3 cost monitoring – Storage Lens

**Problem Statement :  How to monitor S3 bucket storage utilization.

Amazon S3 is an object storage service and one of the most popular services in AWS which offers of industry-leading scalability, data availability, security, and performance. Organizations can store and retrieve any amount of data from anywhere.
If an organization is using aws for their cloud service, AWS S3 is one of prefer storage solution. Some of the use cases of S3 are:
1.	Build an Enterprise Data Lake 
2.	Create a Disaster Recovery System for back up and restore data.
3.	Archive cold data for a long period to meet regulatory requirements
4.	Host a static website.
5.	Integrated with many cloud native solutions to provide storage option.

While you are store unlimited amount of data in S3, it is very important to monitor the storage of S3 and number of objects in S3 buckets. At end of the day every object storage occurred a cost. Organizations may not be able to quantify the storage cost when they have GB, TB data but when the data volume grow to PB’s S3 cost will be high.
For example, when you store 10 PB data (for big enterprise scale applications like data lake, lake house etc)  , you have to give 220K USD for UK region for storage. So it is very important to understand the usage of S3 bucket.

 

AWS S3 have a feature called “Storage lens” where you can create your own custom dashboard and monitor the usage of S3 objects. In this blog, we will create a dashboard using storage lens and see how it work.
To do the same. 
1.	Click on S3 in AWS management console. You can see the overall utilization of all your S3 buckets.
 
 <img width="509" alt="image" src="https://user-images.githubusercontent.com/24868114/224404212-4fb21a59-6547-4788-9fc9-485f6f972465.png">


2.	To create a Dashboard, click on the storage lens in the left panel. Click on Dashboard
3.	Click on Create Dashboard.
4.	Give the below details
•	Dashboard Name:  in this case we give the name as s3-bucket-usage-monitor
•	Home Region : Select the appropriate region, for us it is London region which is eu-west-2
•	Select Status as enable so that we can see the status of the dashboard.

<img width="476" alt="image" src="https://user-images.githubusercontent.com/24868114/224404274-2fc1e669-449a-4cd5-937e-cd445d835909.png">

 
5.	For Dashboard Scope, if you are having objects across regions, you can select the region, in our case we ONLY select London region as all our objects are store in London region and include all buckets in the region.
<img width="395" alt="image" src="https://user-images.githubusercontent.com/24868114/224404323-e750026a-ce66-4a02-8aba-6d8094e36a09.png">

 
6.	In the metrics section, select the Free metrices. A lot of key metrices are available under free metrices and that is more than enough to monitor usages of S3 buckets.
 
 <img width="492" alt="image" src="https://user-images.githubusercontent.com/24868114/224404368-75325581-ef63-4eb8-a086-72a1d7279851.png">

7.	You can export these metrices to an S3 path for further analytical usages, for our case we disabled this option. Finally click create dashboard.
 
<img width="473" alt="image" src="https://user-images.githubusercontent.com/24868114/224404410-d0ca1e8f-6e5e-4e90-b8df-f042b5a4df93.png">


8.	It will take 48 hours to have the charts ready.
 <img width="502" alt="image" src="https://user-images.githubusercontent.com/24868114/224404460-a860509b-5e8e-4035-b155-a4b9b041c5ed.png">


By default, AWS created a lens for you ( which cover all regions), if you want to use the default dashboard, that is fine as well. For any custom requirements like specific region or any rule we can create custom dashboard as well. Sample charts from default dashboard is :

<img width="482" alt="image" src="https://user-images.githubusercontent.com/24868114/224404550-7518a4da-41f8-4ff7-b14c-328a6e0966f7.png">


**Quick Tips: 
1.	Once you understood the usages, you can see which critical data is require for your use case and access pattern. If there are buckets and folders access pattern is unknown, better to use S3 intelligent tiering for cost saving.
2.	Many organizations and enable bucket versioning so that they can avoid the accidental deletion of the object, however ONLY critical data objects (which is difficult to recreate, scripts folder) versioning make sense. But use cases like Data lake when you are getting source data and processed the data and move to archive, you really DO NOT need versioning to the staging bucket.
3.	For files which needs to be stored for long term, better to define a life cycle management to Glacier storage, this can be set it up using Life cycle management policy. 

