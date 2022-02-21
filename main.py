from flask import Flask, render_template, redirect, url_for, request



app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/detail')
def detail():
    return render_template('portfolio-details.html')

@app.route('/detail-app2')
def detail_app2():
    return render_template('portfolio-details-app2.html')

@app.route('/detail-app3')
def detail_app3():
    return render_template('portfolio-details-app3.html')

@app.route('/detail-web1')
def detail_web1():
    return render_template('portfolio-details-web1.html')

@app.route('/detail-web2')
def detail_web2():
    return render_template('portfolio-details-web2.html')

@app.route('/detail-web3')
def detail_web3():
    return render_template('portfolio-details-web3.html')

@app.route('/detail-data')
def detail_data():
    return render_template('portfolio-details-data-analysis.html')

if __name__ == "__main__":
    app.run(debug=True)