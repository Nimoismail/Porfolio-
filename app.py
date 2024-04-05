from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/link', methods=['POST'])
def submit():
    if request.method == 'POST':
        Resume = request.form['Resume']
        Research = request.form['Research']
        Personal = request.form['Personal']
        print(Resume, Research, Personal)

    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
