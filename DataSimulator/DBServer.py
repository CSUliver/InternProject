
#import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

# 打开数据库连接


# 使用cursor()方法获取操作游标

HOST = "47.98.214.197"
PORT = 3306
USER = "root"
PASSWD = "root"
DATABASE = "myproject"

class DBServer(object):

    def __init__(self):
        self.db = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, database=DATABASE, charset='utf8' )
        self.cursor = self.db.cursor()

    def execute(self, sql_cmd):
        self.cursor.execute(sql_cmd)
        self.db.commit()


if __name__ == "__main__":
    ds = DBServer()
    #ret = ds.execute("INSERT INTO scene_tempdata(device_id, `value`, addtime) VALUES ('1', '23.72', '2021-08-11 21:46:18.218992')")
    print(ret)