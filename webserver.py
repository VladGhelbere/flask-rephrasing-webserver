from flask import Flask, flash, redirect, url_for, render_template, request, session
import os
import words_master as words_master

wm = words_master.words_master()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/home/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        if request.form['submit_button']:
            output_text = wm.change_words_simplified(request.form['input_text'])
            if len(output_text) >= 1500:
                flash('Given text should be less than 1500 characters.')
                return render_template("index.html",highlight_h="active")
            elif output_text == '':
                flash('Given text cannot be empty.')
                return render_template("index.html",highlight_h="active")
            else:
                return render_template("index.html",highlight_h="active",input_text=request.form['input_text'],output_text=output_text)
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
