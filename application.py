from flask import Flask, jsonify, request
import time
import pprint

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


stats = {}


@app.route('/', methods = ['POST'])
def post_json_handler():
    content = request.get_json()
    timestamp = time.time()
    pprint.pprint(content)
    print(timestamp)
    # if player kills > stats['kills'] (or deaths)
        # then insert a kill/death
    # elif deaths < stats['deaths'] reset both
    # elif kills goes down by more than one at a time, reset both



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)