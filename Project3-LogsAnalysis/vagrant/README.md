# Logs Analysis Project

Third project in the Udacity Full Stack Nanodegree.

In this project, an internal reporting tool is created using the information from the database to discover what kind of articles the site's readers like.

The report will answer the following three questions:

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

In order to run this project, the following is required:

- A virtual machine. I use VirtualBox, which can be found here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
- A development environment to run inside the virtual machine. I use Vagrant, which can be found here: https://www.vagrantup.com/
- Go into the Project3-LogsAnalysis directory and run the command ```vagrant up```
- After the virtual machine has loaded, sign in using ```vagrant ssh```
- ```cd``` into the vagrant directory with the command ```cd /vagrant```
- Download and unzip newsdata.sql inside the vagrant directory, from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
- While in the vagrant directory and and use the command ```psql -d news -f newsdata.sql```
- Connect to the database using ```psql -d news```
- Create the following views: 

```CREATE VIEW path_views AS
SELECT path, COUNT(*) AS views 
FROM log where status = '200 OK' GROUP BY log.path ORDER BY views desc;```

```CREATE VIEW article_views AS 
SELECT articles.author, articles.title, path_views.views 
FROM path_views 
RIGHT JOIN articles on path_views.path like ('/article/' || articles.slug);```

```CREATE VIEW errors_log AS 
SELECT time::date as date, COUNT(case when status = '404 NOT FOUND' then 1 end) AS error, 
COUNT(*) AS total_requests FROM log GROUP BY date ORDER BY date;```

- And lastly, to run the program, use the following command: ```python logsanalysis.py```
