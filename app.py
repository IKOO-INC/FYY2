from flask import Flask,redirect, render_template
from routes.admin import admin_bp
from routes.tracking import tracking_bp

app = Flask(__name__)

app.route('/')
def bsdchdf():
    return render_template('landing.html')

app.register_blueprint(admin_bp)
app.register_blueprint(tracking_bp)



if __name__ == "__main__":
    app.run(debug=True)
