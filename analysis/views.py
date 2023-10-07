from flask import render_template, request
from . import app
from .root_finding import *
from .integration import *

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/usage')
def usage():
    return render_template('usage.html')

@app.route('/bisection-method', methods=['POST', 'GET'])
def bisection():
    if request.method == 'POST':
        func = request.form['function']
        interval = request.form['interval'].split(',')
        TOL = float(request.form['TOL'])
        result, eq = bisect(func, interval[0], interval[1], TOL)
        return render_template('bisection.html', data={'result': result, 'equation':eq})
    return render_template('bisection.html', data=None)

@app.route('/fixed-point', methods=['POST', 'GET'])
def fixed_point():
    if request.method == 'POST':
        func = request.form['function']
        initial = request.form['initial']
        TOL = float(request.form['TOL'])
        result, eq = fixed_point_iteration(func, initial, TOL)
        return render_template('fixed-point.html', data={'result': result, 'equation':eq})
    return render_template('fixed-point.html', data=None)

@app.route('/newton', methods=['POST', 'GET'])
def newton():
    if request.method == 'POST':
        func = request.form['function']
        derivative = request.form['derivative']
        checked = request.form.get('option')            # Check if the check-box is selected. If it is, user wants Modified Newton's Method.
        initial = request.form['initial']
        TOL = float(request.form['TOL'])
        if checked == "on":
            second_derivative = request.form['second_derivative']
            result, eq, df, ddf = modified_newton(func, derivative, second_derivative, initial, TOL)
            return render_template('newton.html', data={'modified_newton':True, 'result': result, 'equation':eq, 'derivative': df, 'ddf': ddf})
        else:
            result, eq, df = newton_raphson(func, derivative, initial, TOL)
            return render_template('newton.html', data={'result': result, 'equation':eq, 'derivative': df})
    return render_template('newton.html', data=None)

@app.route('/secant-method', methods=['POST', 'GET'])
def secant():
    if request.method == 'POST':
        func = request.form['function']
        points = request.form['initial_points'].split(',')
        TOL = float(request.form['TOL'])
        result, eq = secant_method(func, points[0], points[1], TOL)
        return render_template('secant.html', data={'result': result, 'equation':eq})
    return render_template('secant.html', data=None)

@app.route('/muellers-method', methods=['POST', 'GET'])
def muellers():
    if request.method == 'POST':
        func = request.form['function']
        points = request.form['initial_points'].split(',')
        TOL = float(request.form['TOL'])
        result, eq = muellers_method(func, points[0], points[1], points[2], TOL)
        return render_template('muellers.html', data={'result': result, 'equation':eq})
    return render_template('muellers.html', data=None)

@app.route('/aitkens-method', methods=['POST', 'GET'])
def aitkens():
    if request.method == 'POST':
        func = request.form['function']
        point = request.form['initial_point']
        iterations = int(request.form['iter'])
        result, eq = aitkens_method(func, point, iterations)
        return render_template('aitkens.html', data={'result': result, 'equation':eq})
    return render_template('aitkens.html', data=None)

@app.route('/steffensens-method', methods=['POST', 'GET'])
def steffensens():
    if request.method == 'POST':
        func = request.form['function']
        point = request.form['initial_point']
        TOL = float(request.form['TOL'])
        result, eq = steffensens_method(func, point, TOL)
        return render_template('steffensens.html', data={'result': result, 'equation':eq})
    return render_template('steffensens.html', data=None)

@app.route('/composite-trapezoidal', methods=['POST', 'GET'])
def composite_trapezoidal():
    if request.method == 'POST':
        func = request.form['function']
        llimit = request.form['llimit']
        print(llimit)
        ulimit = request.form['ulimit']
        print(ulimit)
        n = request.form['n']
        result, eq = trapezoidal(func, llimit, ulimit, n)
        return render_template('trapezoidal.html', data={'result': result, 'equation':eq})
    return render_template('trapezoidal.html', data=None)