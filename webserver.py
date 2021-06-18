from flask import Flask, redirect, url_for, render_template, request, session
import os
import words_master as words_master

wm = words_master.words_master()

APP = Flask(__name__)
APP.secret_key = os.getenv("APP_SECRET_KEY")

@APP.route("/")
def index():
    return redirect(url_for("home"))

@APP.route("/home/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        if request.form['submit_button']:
            output_text = wm.change_words_simplified(request.form['input_text'])
            return render_template("index.html",input_text=request.form['input_text'],output_text=output_text)
    else:
        return render_template("index.html",highlight_h="active")

@APP.route("/contact/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # do-nothing
        pass
    else:
        return render_template("contact.html",highlight_c="active")

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000, debug=True)