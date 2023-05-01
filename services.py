import pymysql

def registerUser(payload):
    try:
        con = pymysql.connect(host='127.0.0.1', user='root', password='Abhi@2001')
        dbCursor = con.cursor()
        try:
            query = 'create database pythonactivity'
            dbCursor.execute(query)
            query = 'use pythonactivity'
            dbCursor.execute(query)
            query = 'create table appusers(id int auto_increment primary key not null, userName varchar(50), email varchar(50), address varchar(50), password varchar(50))'
            dbCursor.execute(query)

        except:
            query = 'use pythonactivity'
            dbCursor.execute(query)
        
        query = 'select * from appusers where email=%s'
        dbCursor.execute(query, (payload["email"]))

        row = dbCursor.fetchone()

        if(row != None):
            return "User already exists !"
        else:
            query = 'insert into appusers(userName,email,address,password) values(%s,%s,%s,%s)'
            dbCursor.execute(query, (payload["userName"],payload["email"],payload["address"],payload["password"]))
            con.commit()
        
        dbCursor.close()
        con.close()
    except Exception as e:
        print("Error:", e)
        raise e
    
def loginUser(payload):
    try:
        con = pymysql.connect(host='127.0.0.1', user='root', password='Abhi@2001')
        dbCursor = con.cursor()
        
        query = 'use pythonactivity'
        dbCursor.execute(query)

        query = 'select * from appusers where email=%s and password=%s'
        dbCursor.execute(query, (payload["email"], payload["password"]))

        rowData = dbCursor.fetchone()

        if(rowData == None):
            return "Invalid Credentials !"
        else:
            print("rowData:", rowData)
            return rowData
        
        # dbCursor.close()
        # con.close()
    except Exception as e:
        print("Error:", e)
        raise e

def updateUser(payload):
    try:
        con = pymysql.connect(host='127.0.0.1', user='root', password='Abhi@2001')
        dbCursor = con.cursor()
        
        query = 'use pythonactivity'
        dbCursor.execute(query)

        print("Payload", payload)
        query = "UPDATE appusers set userName=%s, email=%s, address=%s where id=%s"
        dbCursor.execute(query, (payload["userName"], payload["email"], payload["address"], payload["id"]))
        con.commit()

        query = 'select * from appusers where id=%s'
        dbCursor.execute(query, (payload["id"]))

        updatedRow = dbCursor.fetchone()

        if(updatedRow == None):
            return "Updation Failed !"
        else:
            print("updatedRow:", updatedRow)
            return updatedRow
        
    except Exception as e:
        print("Error:", e)
        raise e

def deleteUser(payload):
    try:
        con = pymysql.connect(host='127.0.0.1', user='root', password='Abhi@2001')
        dbCursor = con.cursor()
        
        query = 'use pythonactivity'
        dbCursor.execute(query)

        query = "delete from appusers where id=%s"
        dbCursor.execute(query, (payload[0]))
        con.commit()
        
        query = 'select * from appusers where id=%s'
        dbCursor.execute(query, (payload[0]))

        deletedRow = dbCursor.fetchone()

        if(deletedRow == None):
            return "User Deleted Successfully"
        else:
            return "User Deletiton Failed !"
        
    except Exception as e:
        print("Error:", e)
        raise e
