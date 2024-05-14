from flask import request, jsonify
from config import app, mysql

@app.route("/contacts", methods=["GET"])
def get_contacts():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify({"contacts": users})


@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "Must include first name, last name, and email"}), 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "User created!"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"]) 
def update_contact(user_id):
    data = request.json
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "Must include first name, last name, and email"}), 400

    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET first_name=%s, last_name=%s, email=%s WHERE id=%s", (first_name, last_name, email, user_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "User info updated"}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Contact deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
