from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for CSRF protection and session management
app.config['SECRET_KEY'] = 'your_secret_key'

# Define a WTForms form class for the questionnaire
class QuestionnaireForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])  # Name input field
    course = StringField('Course', validators=[DataRequired()])  # Course input field
    short_answer = TextAreaField('Short-form Answer', validators=[DataRequired()], render_kw={"rows": 2})  # Short answer textarea
    long_answer = TextAreaField('Long-form Answer', validators=[DataRequired()], render_kw={"rows": 5})  # Long answer textarea
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[DataRequired()])  # Satisfaction level dropdown
    recommend = RadioField('Would you recommend this course to others?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])  # Recommendation radio buttons
    improvements = TextAreaField('Suggestions for Improvement', render_kw={"rows": 3})  # Suggestions textarea
    submit = SubmitField('Submit')  # Submit button

# Define route for the home page
@app.route('/')
def home():
    return render_template('home.html')  # Render home.html template

# Define route for the information page
@app.route('/information')
def information():
    return render_template('information.html')  # Render information.html template

# Define route for the data collection page with GET and POST methods
@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = QuestionnaireForm()  # Instantiate the form
    if form.validate_on_submit():  # Check if form is submitted and validated
        # Open a file to store the submitted data
        with open('data.txt', 'a') as f:
            # Write the form data to the file
            f.write(f"Name: {form.name.data}\n")
            f.write(f"Course: {form.course.data}\n")
            f.write(f"Short-form Answer: {form.short_answer.data}\n")
            f.write(f"Long-form Answer: {form.long_answer.data}\n")
            f.write(f"Satisfaction: {form.satisfaction.data}\n")
            f.write(f"Recommend: {form.recommend.data}\n")
            f.write(f"Improvements: {form.improvements.data}\n")
            f.write('---\n')  # Separator for entries
        return 'Form Submitted'  # Response after successful submission
    return render_template('data_collection.html', form=form)  # Render the data collection form

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode