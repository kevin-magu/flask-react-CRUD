from config import mysql

class User:
    @staticmethod
    def create_user(first_name, last_name, email):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def update_user(user_id, first_name, last_name, email):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET first_name=%s, last_name=%s, email=%s WHERE id=%s", (first_name, last_name, email, user_id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete_user(user_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def get_all_users():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        return users
