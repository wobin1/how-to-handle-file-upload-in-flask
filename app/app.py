from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, ALL, UploadSet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ALL_DEST'] = 'static/uploaded_files'

all = UploadSet('all', ALL)
configure_uploads(app, all)


class MyForm(FlaskForm):
    all = FileField('all')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        filename = all.save(form.all.data)
        return f'Filename: {filename}'
    return render_template('index.html', form = form)

if __name__==('__main__'):
    app.run(debug=True)



