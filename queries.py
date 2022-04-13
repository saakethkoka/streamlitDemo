from databaseConfig import cursor, mysql_connection



def addComment(comment):
    cursor.execute('INSERT INTO comments (comment) VALUES("' + str(comment) + '")')
    mysql_connection.commit()


def getComments():
    cursor.execute("SELECT * FROM comments")
    list = cursor.fetchall()
    comment_list = []
    for comment in list:
        comment_list.append(comment[0])
    return comment_list
