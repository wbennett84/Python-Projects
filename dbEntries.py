#must import sqlite3 module
import sqlite3
#establish connection with/create database
connection = sqlite3.connect('test.db')

with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    connection.commit()
connection.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#scan through above tuble and find .txt files and insert them into the database
def findTxtfiles():
    for i in fileList:
        if i.endswith(".txt"):


            connection = sqlite3.connect('test.db')

            with connection:
                cur = connection.cursor()
                cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", \
                            (i,))
                connection.commit()
            connection.close()

#draw out the info from the table and print it to the screen
def printTxtfiles():
            
                connection = sqlite3.connect('test.db')

                with connection:
                    cur = connection.cursor()
                    cur.execute("SELECT col_fileName FROM tbl_files")
                    varFiles = cur.fetchall()
                    for item in varFiles:
                        msg = "File: {}".format(item[0])
                        print (msg)
                connection.close()


                

findTxtfiles()
printTxtfiles()


            









