from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def root():
    print(session)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_language'] = request.form['language']
    session['user_comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)