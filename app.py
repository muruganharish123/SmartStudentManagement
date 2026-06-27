from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/marks')
def marks():
    return render_template('marks.html')

@app.route('/fees')
def fees():
    return render_template('fees.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)