
from flask import Flask, request, jsonify, render_template,redirect,url_for
import sqlite3

app = Flask(__name__)

# Create a basic SQLite database for storing employees
def init_db():
    with sqlite3.connect('employee.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS employees
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         Name TEXT, 
                         department TEXT, 
                         salary INTEGER)''')
@app.route('/')
def home():
    # Fetch all employees from the database
    with sqlite3.connect('employee.db') as conn:
        employees = conn.execute('SELECT * FROM employees').fetchall()
    return render_template('lib.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    Name = request.form['Name']
    department = request.form['department']
    salary = int(request.form['salary'])
    with sqlite3.connect('library.db') as conn:
        conn.execute('INSERT INTO employees (Name, department, salary) VALUES (?, ?, ?)', (Name, department, salary))
    return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update_employee():
    employee_id = int(request.form['id'])
    Name = request.form['Name']
    department = request.form['department']
    salary = int(request.form['salary'])
    with sqlite3.connect('library.db') as conn:
        conn.execute('UPDATE employees SET Name = ?, department = ?, salary = ? WHERE id = ?', (Name, department, salary, employee_id))
    return 'employee updated successfully!'

@app.route('/delete', methods=['POST'])
def delete_employee():
    employee_id = int(request.form['id'])
    with sqlite3.connect('library.db') as conn:
        conn.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    return 'employee deleted successfully!'

@app.route('/search', methods=['GET'])
def search_employees():
    search_query = request.args.get('query', '')
    with sqlite3.connect('library.db') as conn:
        results = conn.execute('SELECT * FROM employees WHERE Name LIKE ? OR department LIKE ?', (f'%{search_query}%', f'%{search_query}%')).fetchall()
    return jsonify(results)


init_db()
app.run(port=9001)














































