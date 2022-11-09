from cloudant.client import Cloudant

#creating the Cloudant Database 
client = Cloudant.iam("1c7fdf42-123b-4b16-bc47-80c3130ce5d1-bluemix","MwmD6tzRaAiIW0QKPfYJ3nfm-8AQLki13-H1Rc14kQtr",connect=True)
database = client.create_database("bath4_database")

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if (__name__ == '__main__'):
    app.run(debug=True) 