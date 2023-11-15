from flask import Flask, request, jsonify
# import requests
app = Flask(__name__)
print('flask server initializing')

@app.route('/test_api',methods=['GET'])
def test_api():
    # json_data = request.get_json()
    reply = {
        "SESSION-TITLE": "BTP in a Nutshell"
    }
    return jsonify(reply)

if __name__ == "__main__":
    from waitress import serve
    print('server is up')
    serve(app, host="0.0.0.0", port=8080)
    
