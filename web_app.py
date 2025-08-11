from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
from Simulation import Simulation

app = Flask(__name__)
simulation = Simulation()
simulation_thread = None

def _run_simulation(duration, initial_customers):
    simulation.set_sim_flag()
    simulation.initiate_simulation(duration, initial_customers)

@app.route('/', methods=['GET', 'POST'])
def index():
    global simulation_thread
    if request.method == 'POST':
        duration = int(request.form.get('duration', 30))
        initial_customers = int(request.form.get('initial_customers', 10))
        simulation_thread = Thread(target=_run_simulation, args=(duration, initial_customers))
        simulation_thread.start()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/stop', methods=['POST'])
def stop():
    global simulation_thread
    simulation.stop_simulation()
    if simulation_thread and simulation_thread.is_alive():
        simulation_thread.join()
        simulation_thread = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
