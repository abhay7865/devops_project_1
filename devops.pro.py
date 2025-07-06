
from flask import Flask

app = Flask(_name_)

@app.route('/info')
def info():
    return "Heyy!! This is the info page."

@app.route('/phone') 
def phone():
    return "This is the phone page."

app.run(host='0.0.0.0', debug=True)