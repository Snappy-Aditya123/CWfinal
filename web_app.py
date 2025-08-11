
from flask import Flask, render_template, request, jsonify

from threading import Thread
from Simulation import Simulation

app = Flask(__name__)
simulation = Simulation()
simulation_thread = None

def _run_simulation(duration, initial_customers):
    simulation.set_sim_flag()
    simulation.initiate_simulation(duration, initial_customers)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/start')
def start():
    global simulation_thread
    data = request.get_json() or {}
    duration = int(data.get('duration', 30))
    initial_customers = int(data.get('initial_customers', 10))
    simulation_thread = Thread(target=_run_simulation, args=(duration, initial_customers))
    simulation_thread.start()
    return '', 204


@app.post('/stop')

def stop():
    global simulation_thread
    simulation.stop_simulation()
    if simulation_thread and simulation_thread.is_alive():
        simulation_thread.join()
        simulation_thread = None
    return '', 204


@app.get('/state')
def state():
    return jsonify(simulation.get_lane_states())


if __name__ == '__main__':
    app.run(debug=True)

