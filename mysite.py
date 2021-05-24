from flask import Flask

app = Flask(__name__)

@app.route("/")
def Welcome_to_codeplateau():
    return "<p>Welcome to CodePlateau</p>"

@app.route("/About_us")
def About_us():
    return "<p>About us</p>"

@app.route("/Home")
def Home ():
    return "<p>Home</p>"

@app.route("/Contact_us")
def Contact_us():
    return "<p>Contac us</p>"

@app.route("/Products")
def Products():
    return "<p>Products</p>"

@app.route("/Services")
def Services():
    return "<p>Services</p>"