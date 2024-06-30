from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    if request.method == 'POST':
        name = request.form['name']
        student_number = request.form['student_number']
        email = request.form['email']
        grades = request.form['grades']
        satisfaction = request.form['satisfaction']
        suggestions = request.form['suggestions']
        # Process the data or save it to a file
        with open('data.txt', 'a') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Student Number: {student_number}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Grades: {grades}\n")
            f.write(f"Satisfaction: {satisfaction}\n")
            f.write(f"Suggestions: {suggestions}\n")
            f.write('---\n')
        return 'Form Submitted'
    return render_template('data_collection.html')

if __name__ == '__main__':
    app.run(debug=True)