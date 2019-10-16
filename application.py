from flask import Flask, jsonify, request
import time
import pprint

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


stats = {'kills': 0, 'deaths': 0}


@app.route('/', methods = ['POST'])
def post_json_handler():
    global stats
    content = request.get_json()
    timestamp = time.time()
    pprint.pprint(content)
    print(timestamp)
    if 'player' in content:
        player_stats = content['player']
        match_stats = player_stats['match_stats']
        kills = match_stats['kills']
        deaths = match_stats['deaths']

        if kills > stats['kills']:
            pass
        elif deaths > stats['deaths']:
            pass
        elif deaths < stats['deaths']:
            stats['kills'] = 0
            stats['deaths'] = 0
        elif kills + 2 < stats['kills']:
            stats['kills'] = 0
            stats['deaths'] = 0


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    