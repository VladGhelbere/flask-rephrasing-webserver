from flask import Flask, redirect, url_for, render_template, request, session
import os
import words_master as words_master

wm = words_master.words_master()

app = Flask(__name__)
app.secret_key = os.getenv("app_SECRET_KEY")

@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/home/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        if request.form['submit_button']:
            output_text = wm.change_words_simplified(request.form['input_text'])
            return render_template("index.html",input_text=request.form['input_text'],output_text=output_text)
    else:
        return render_template("index.html",highlight_h="active")

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # do-nothing
        pass
    else:
        return render_template("contact.html",highlight_c="active")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)