from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class QuestionnaireForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    short_answer = TextAreaField('Short-form Answer', validators=[DataRequired()], render_kw={"rows": 2})
    long_answer = TextAreaField('Long-form Answer', validators=[DataRequired()], render_kw={"rows": 5})
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[DataRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement', render_kw={"rows": 3})
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        with open('data.txt', 'a') as f:
            f.write(f"Name: {form.name.data}\n")
            f.write(f"Course: {form.course.data}\n")
            f.write(f"Short-form Answer: {form.short_answer.data}\n")
            f.write(f"Long-form Answer: {form.long_answer.data}\n")
            f.write(f"Satisfaction: {form.satisfaction.data}\n")
            f.write(f"Recommend: {form.recommend.data}\n")
            f.write(f"Improvements: {form.improvements.data}\n")
            f.write('---\n')
        return 'Form Submitted'
    return render_template('data_collection.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)