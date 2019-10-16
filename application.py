from flask import Flask, jsonify, request
import pprint
from influxdb import InfluxDBClient


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('cs')
client.switch_database('cs')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


good_maps = ['de_cache', 'de_dust2', 'de_mirage', 'de_overpass', 'de_train', 'de_inferno', 'de_vertigo']

stats = {'kills': 0, 'deaths': 0}


@app.route('/', methods = ['POST'])
def post_json_handler():
    global stats
    content = request.get_json()
    pprint.pprint(content)
    if 'player' in content and 'map' in content:
        if content['map']['mode'] == "competitive" and content['map']['name'] in good_maps:
            player_stats = content['player']
            player_id = player_stats['steamid'] # TODO: add check for steamid, soft fail if not there
            match_stats = player_stats['match_stats']
            kills = match_stats['kills']
            deaths = match_stats['deaths']

            if kills > stats['kills']:
                point = {}
                point['measurement'] = "kills"
                point['fields'] = {"count": kills - stats['kills']} # TODO: add other fields, such as flashed
                point['tags'] = {"player": player_id} # TODO: add other tags, such as weapon
                client.write_points([point])
                stats['kills'] = kills
            elif deaths > stats['deaths']:
                point = {}
                point['measurement'] = "deaths"
                point['fields'] = {"count": deaths - stats['deaths']}
                point['tags'] = {"player": player_id}
                client.write_points([point])
                stats['deaths'] = deaths
            elif deaths < stats['deaths']:
                stats['kills'] = 0
                stats['deaths'] = 0
            elif kills + 2 < stats['kills']:
                stats['kills'] = 0
                stats['deaths'] = 0

    return 'JSON posted'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
