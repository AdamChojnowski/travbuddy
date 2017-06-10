from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('main_filter.html')

@app.route("/results")
def results_page():
    return render_template('results_filter.html', people=['Mark Twain', 'Mark Twain', 'Mark Twain'])

@app.route("/person/<id>")
def person_page(id):
    return render_template('person.html')

@app.route("/person/messages/<id>")
def person_message(id):
    return render_template('messages.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)