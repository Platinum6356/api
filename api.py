from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users/', methods = ['GET'])
def ReturnUserInfo():
    id = request.args.get("id")
    id = int(id)

    users = {
        1: {
            "name": "Alex",
            "Age": "52"
        },
        2: {
            "name": "Vanek",
            "Age": "12"
        },
        3: {
            "name": "Sanya",
            "Age": "52"
        }
    }
    return jsonify(users[id])

if __name__ == "__main__":
    app.run(debug=True)