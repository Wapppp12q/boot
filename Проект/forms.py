from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, StringField, PasswordField


class RegisterForm(FlaskForm):
    email = EmailField('Введите вашу почту')
    submit = SubmitField('Отправить код')
    entrance = SubmitField('Уже зарегистрированы?')


class VerifForm(FlaskForm):
    code_str = StringField('Письмо отправлено')
    submit = SubmitField('Отправить код')


class DataForm(FlaskForm):
    name = StringField('Имя:')
    surname = StringField('Фамилия:')
    password = PasswordField('Введите пароль:')
    pass_exam = PasswordField('Подтвердите пароль:')
    submit = SubmitField('Готово')


class Recovery(FlaskForm):
    email = EmailField('Введите почту, на которую зарегистрирован аккаунт:')
    submit = SubmitField('Отправить код')


class RDataForm(FlaskForm):
    password = PasswordField('Пароль')
    pass_exam = PasswordField('Поторите пароль')
    submit = SubmitField('Сохранить пароль')





class Entrance(FlaskForm):
    email = EmailField('Почта:')
    password = PasswordField('Пароль:')
    rec = SubmitField('Забыли пароль?')
    submit = SubmitField('Войти')
    reg = SubmitField('Регистрация')


class SearchForm(FlaskForm):
    pass


class PeopleForm(FlaskForm):
    pass
