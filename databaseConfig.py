import mysql.connector


username = 'admin'
password = 'Saketh12'
host = 'redditsentimentscraper.clx83lofg8ls.us-east-2.rds.amazonaws.com'
database = 'reddit'

mysql_connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
cursor = mysql_connection.cursor()