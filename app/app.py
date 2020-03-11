from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my Flask App!'

@app.route('/state', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
         data = request.json
         with open('state.json', 'w') as json_file:
            json.dump(data, json_file)
         return 'success'
    if request.method == 'GET':
        with open('state.json') as json_file:
            data = json.load(json_file)
        return data
    return 'bad request'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
