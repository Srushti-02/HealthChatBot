from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists', 'error')
        finally:
            conn.close()

    return render_template('signup.html')


# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/liver-test')
def liver_test():
    return render_template('liverchatbot.html')

@app.route('/process-input', methods=['POST'])
def process_input():
    data = request.get_json()

    # Example logic to generate a suggestion based on inputs
    bilirubin = float(data.get("Please enter your Bilirubin level:"))
    alp = float(data.get("Please enter your Alkaline Phosphatase (ALP) level:"))
    alt = float(data.get("Please enter your Alanine Aminotransferase (ALT) / SGPT level:"))
    ast = float(data.get("Please enter your Aspartate Aminotransferase (AST) / SGOT level:"))
    proteins = float(data.get("Please enter your Total Proteins / Albumin level:"))

    # Simple decision logic for example
    if alp>120 and alt>40 and ast>40:
        suggestion = "Fatty liver."
    elif bilirubin > 1.2 or alp > 120 or alt > 40 or ast > 40 or proteins < 6:
        suggestion = "Based on the provided values, there may be a risk of liver disease. Please consult with a healthcare provider for further evaluation."
    else:
        suggestion = "Your liver test results appear to be within the normal range. However, it's always best to consult with a healthcare provider for a full assessment."

    return jsonify({"suggestion": suggestion})

@app.route('/diabetes-test')
def diabetes_test():
    return render_template('diabeteschatbot.html')

@app.route('/kidney-test')
def kidney_test():
    return render_template('kidneychatbot.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)



#https://github.com/Srushti-02/HealthChatBot.git