
# main.py
from flask import Flask, render_template, request, redirect, url_for
import backtesting_engine

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/backtest', methods=['POST'])
def backtest():
    # Extract form data
    parameters = request.form.to_dict()

    # Perform backtesting
    results = backtesting_engine.backtest(parameters)

    # Save the results for later retrieval
    session['results'] = results

    # Redirect to results page
    return redirect(url_for('results'))

@app.route('/results')
def results():
    # Retrieve the results from the session
    results = session.get('results')

    # Render the results page
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
