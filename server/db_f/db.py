import pymysql


class Database:
    def __init__(self):
        try:
            self.db = pymysql.connect(host='localhost',
                                      user='root',
                                      password='qwer1234',
                                      db='new_db',
                                      charset='utf8')
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        except Exception as m:
            print(m)
            self.db = pymysql.connect(host='localhost',
                                      user='root',
                                      password='qwer1234',
                                      charset='utf8')
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("CREATE DATABASE new_db;")
            q = "CREATE TABLE new_db.item (" \
                "idx int(255) NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                "input_1 varchar(255) DEFAULT NULL," \
                "input_2 varchar(255) DEFAULT NULL," \
                "input_3 varchar(255) DEFAULT NULL," \
                "Create_date varchar(255) DEFAULT NULL," \
                "Update_date varchar(255) DEFAULT NULL);"
            self.cursor.execute(q)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        self.db.commit()
        return row


Database = Database()
