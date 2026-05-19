from flask import Flask, render_template, redirect, request

app = Flask(__name__)


contact = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contact)

@app.route('/add', methods=['POST', 'GET'])
def com():
    if request.method == "POST":
        name = request.form['Name']
        phone = request.form['phone']  # Corrected field name
        contact.append({'name': name, 'phone': phone})  # Consistent key names
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    if 0 <= id < len(contact):
        contact.pop(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
