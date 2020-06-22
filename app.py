from flask import Flask
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():

    content = request.data
    ans = request.get_json()
    result = content.decode("utf-8")
    print('To jest result: {}'.format(result))
    return "Hello World! and answert: {}".format(result)



if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=4444)
