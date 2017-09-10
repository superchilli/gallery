# -*-coding: utf-8-*-

from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField, PasswordField, BooleanField, FileField, \
    TextAreaField, SelectField, IntegerField, SelectMutipleField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, URL, Optionnal, NumberRange
from wtforms import ValidationError
from flask_wtform.file import FileField, FileAllowed, FileRequired
from wtforms.widgets import TextArea

from .. import photos
from ..models import User, Role


class SettingForm(Form):
    name=StringField('name', validators=[Length(0, 64)])
    location=StringField('city', validators=[Length(0, 64)])
    website=StringField('website', validators=[Length(0, 64), Optional()
                                           ], render_kw={"placeholder": "http://..."})
    about_me=TextAreaField('about me', render_kw={'rows': 8})
    like_public=BooleanField('public my likes')
    submit=SubmitField('submit')

    def validate_website(self, field):
        if field.data[:4] != "http":
            field.data="http://" + field.data

class EditProfileAdminForm(Form):
    email=StringField('email', validators=[DataRequired(), Length(1, 64),
                                         Email(message='Please enter correct email')])
    username=StringField('username', validators=[DataRequired(message='user name cannot be empty'), Length(1, 64),
                                             Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                    'username can only use, letters '
                                                    'numbers, dot and slash.')])
    confirmed=BooleanField('Comfirm')
    role=SelectField('Role', coerce=int)
    name=StringField('name', validators=[Length(0, 64)])
    location=StringField('city', validators=[Length(0, 64)])
    website=StringField('website', validators=[Length(0, 64), Optional()
                                           ], render_kw={"placeholder": "http://..."})
    about_me=TextAreaField('about me', render_kw={'rows': 8})
    like_public=BooleanField('public my likes')
    submit=SubmitField('submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices=[(role.id, role.name)
                           for role in Role.query.order_by(Role.name).all()]
        self.user=user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been used.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('The username has been used.')

class CommentForm(Form):
    body=TextAreaField('Comment', validators=[DataRequired(message='Content cannot be empty')],render_kw={'rows':5})
    submit=SubmitField('Submit')


class AddPhotoForm(Form):
    photo = FileField('Photo', validators=[FileRequired(),
                                         FileAllowed(photos, 'only photo files allowed')])
    submit=SubmitField('Submit')




