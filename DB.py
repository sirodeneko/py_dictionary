#!/depot/Python-2.5/bin/python
import sqlite3

class Sqlopen():
    def __init__(self):
        #链接数据库文件
        #如果数据库文件不存在，将新建一个，如果存在则打开此文件
        self.conn = sqlite3.connect('db/EDB.db')
        #创建一个Cursor
        self.cursor = self.conn.cursor()
        # 执行一条SQL语句，创建Ewordmap表:
        self.cursor.execute('create table if not exists Ewordmap (id integer primary key,name varchar(20),pronounce1 varchar(10),pronounce2 varchar(10),result1 varchar(40),result2 varchar(40),result3 varchar(40),result4 varchar(40),result5 varchar(40))')

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
    
    #增加单词
    def SetWord(self,word,pronounce,result):
        tableName='Ewordmap'

        word_f='"'+word+'"'
        pronounce_f=[]
        for index in range(2):
            if(index<len(pronounce)):
                pronounce_f.append('"'+pronounce[index]+'"')
            else:
                pronounce_f.append('null')
                
        result_f=[]
        for index in range(5):
            if(index<len(result)):
                result_f.append('"'+result[index]+'"')
            else:
                result_f.append('null')
        
        sql_cmd=r'insert into %s values (null,%s,%s,%s,%s,%s,%s,%s,%s)' %(tableName,word_f,pronounce_f[0],pronounce_f[1],result_f[0],result_f[1],result_f[2],result_f[3],result_f[4])
        
        # 继续执行一条SQL语句，插入一条记录:
        self.cursor.execute(sql_cmd)

    #查询单词
    def GetWord(self,word):

        tableName='Ewordmap'

        word_f='"'+word+'"'
            
        sql_cmd=r'select * from %s where name=%s' %(tableName,word_f)
        # 执行查询语句:
        self.cursor.execute(sql_cmd)
        
        # 获得查询结果集:
        values = self.cursor.fetchall()
        #print(values)
        return values
    
    #删除单词单词
    def DelWord(self,word):
        tableName='Ewordmap'
        
        word_f='"'+word+'"'

        sql_cmd=r'delete from %s where name=%s' %(tableName,word_f)
        
        # 继续执行一条SQL语句，插入一条记录:
        self.cursor.execute(sql_cmd)
    
    #修改单词
    def UpWord(self,word,pronounce,result):
        tableName='Ewordmap'

        # 先删除
        word_f='"'+word+'"'

        sql_cmd=r'delete from %s where name=%s' %(tableName,word_f)
        
        # 继续执行一条SQL语句，插入一条记录:
        self.cursor.execute(sql_cmd)

        word_f='"'+word+'"'
        pronounce_f=[]
        for index in range(2):
            if(index<len(pronounce)):
                pronounce_f.append('"'+pronounce[index]+'"')
            else:
                pronounce_f.append('null')
                
        result_f=[]
        for index in range(5):
            if(index<len(result)):
                result_f.append('"'+result[index]+'"')
            else:
                result_f.append('null')
        
        sql_cmd=r'insert into %s values (null,%s,%s,%s,%s,%s,%s,%s,%s)' %(tableName,word_f,pronounce_f[0],pronounce_f[1],result_f[0],result_f[1],result_f[2],result_f[3],result_f[4])
        
        # 继续执行一条SQL语句，插入一条记录:
        self.cursor.execute(sql_cmd)
