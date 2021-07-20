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

@app.route('/', methods=['POST', 'GET'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        fname = all.save(form.all.data)
        return f'Name of file: {fname}'
    return render_template('home.html', form = form)

if __name__==('__main__'):
    app.run(debug=True)



