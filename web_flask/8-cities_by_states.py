#!/usr//bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_list():
    states = storage.all('State')
    cities = storage.all('City')
    return render_template(
        '8-cities_by_states.html',
        states=states,
        cities=cities)


@app.teardown_appcontext
def remove_session(self):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
