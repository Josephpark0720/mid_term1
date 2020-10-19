from wtforms import Form, StringField, TextAreaField

class SubmitForm(Form):
    title = StringField('Title')
    name = StringField('Name')
    content = TextAreaField('Content')
