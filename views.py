from app import app
import controllers


@app.route('/')
def hello_world():
    return 'Привет'


@app.route('/xrates')
def view_rates():
    return controllers.get_all_rates()
