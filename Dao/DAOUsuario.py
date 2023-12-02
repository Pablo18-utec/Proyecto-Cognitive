import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )

    def read(self,id):
        con =DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM usuario order by nombre asc")
            else:
                cursor.execute("SELECT * FROM usuario where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(email,password) VALUES(%s, %s)", (data['email'],data['password'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario set email = %s, password =%s where id = %s", (data['email'],data['passowrd'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM usuario where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()