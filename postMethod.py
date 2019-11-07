from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    data1 = content['first_value']
    data2 = content['second_value']
    result = int(data1) + int(data2)
    print(result)

    print(content)
    return 'JSON posted'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)