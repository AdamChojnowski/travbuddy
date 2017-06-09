from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('main_filter.html')

@app.route("/results")
def results_page():
    return render_template('results_filter.html', people=['jan', 'siemak'])

@app.route("/person/<id>")
def person_page(id):
    return render_template('person.html')

if __name__ == "__main__":
    app.run()