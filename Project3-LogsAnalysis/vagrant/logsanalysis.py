import psycopg2

# Connect to the 'news' database
DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


def q1():
    """This function answers the first question: What are the most
       popular three articles of all time?

       The output is a list of the top three articles in order
       of views."""

    c.execute("""SELECT title, views
                 FROM article_views
                 ORDER BY views desc limit 3""")
    results = c.fetchall()

    print("1. What are the most popular three articles of all time?")
    for i in results:
        print("%s - %s views" % (i[0], i[1]))
    print("\n")


def q2():
    """This function answers the second question: Who are the most
       popular article authors of all time?

       The output is a list of the top authors in order of views."""

    c.execute("""SELECT authors.name, sum(article_views.views) AS views
                 FROM authors, article_views
                 WHERE authors.id = article_views.author
                 GROUP BY authors.id ORDER BY views desc""")
    results = c.fetchall()

    print("2. Who are the most popular article authors of all time?")
    for i in results:
        print("%s - %s views" % (i[0], i[1]))
    print("\n")


def q3():
    """This function answers the third question: On which days
       did more than 1% of requests lead to errors?

       The output is the date on which more than 1% of
       requests led to errors along with the error rate."""

    c.execute("""SELECT date, 100.0 * error/total_requests AS error_rate
                 FROM errors_log
                 WHERE 100.0 * error/total_requests > 1
                 ORDER BY error_rate desc""")
    results = c.fetchall()

    print("3. On which days did more than 1% of requests lead to errors?")
    for i in results:
        print("%s - %s%% errors" % (i[0], round(i[1], 2)))

if __name__ == "__main__":
    q1()
    q2()
    q3()

    db.close()
