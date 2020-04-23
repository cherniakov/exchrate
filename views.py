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


@app.route("/update/<int:from_currency>/<int:to_currency>")
@app.route("/update/all")
def update_xrates(from_currency=None, to_currency=None):
    return controllers.UpdateRates().call(from_currency, to_currency)


@app.route("/logs")
def view_logs():
    return controllers.ViewLogs().call()
