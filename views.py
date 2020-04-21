from flask import request
from app import app
import controllers


@app.route('/')
def hello_world():
    return 'Привет'


@app.route('/xrates')
def view_rates():
    return controllers.ViewAllRates().call()


@app.route('/api/xrates/<fmt>')
def api_rates(fmt):
    return f"Rates with format: {fmt}. Args: {request.args}"
