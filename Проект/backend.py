import http

from flask import jsonify, redirect, session
from flask_restful import Resource
from validate_email import validate_email
from models import database
from models.users_reg import Reg
from models.users_data import Data
from models.page_data import PData
from create_secret_email import create_secret_email_or_number
from create_code import create_code
from replace import replacce
from phonenumbers import is_valid_number

from code_sender import send_mail, send_sms


class Registration_Api(Resource):
    def post(self, email_or_number):
        code = create_code()
        if validate_email(email_or_number):
            db_sess = database.create_session()
            email_exist = db_sess.query(Reg.email).filter(Reg.email == email_or_number)
            send_mail(email_or_number, code, False)
        else:
            return 'Такой почты не существует'

        if is_valid_number(email_or_number):
            db_sess = database.create_session()
            number_exist = db_sess.query(Reg.email).filter(Reg.email == email_or_number)
            send_sms(email_or_number, f"Здравствуйте! Код подтверждения регистрации {email_or_number} - {code}.")
        else:
            return 'Такого номера не существует'

        if number_exist or email_exist:

            # conn = http.client.HTTPConnection("ifconfig.me")
            # conn.request("GET", "/ip")
            # session['logged'] = '0'
            # session['IP'] = str(conn.getresponse().read()).replace('b', '').replace("'", '').strip()
            # conn.close()

            user_reg = Reg(code_ver=code, email=email_or_number)
            db_sess.add(user_reg)
            db_sess.commit()
            id_ver = int(replacce(*db_sess.query(Reg.id).filter(Reg.email == email_or_number)))
            db_sess.close()
            return jsonify({'status': 'ok', 'id_ver': id_ver})
        else:
            return 'Такая почта уже зарегистрирована'
        db_sess.close()


class Verirfication_Api(Resource):
    def post(self, id_ver, code):
        db_sess = database.create_session()
        code_db = replacce(*db_sess.query(Reg.code_ver).filter(id == id_ver))
        if code == int(code_db):
            return jsonify({'status': 'ok'})
        else:
            return 'Неверный код'


class Registartion_data_Api(Resource):
    def post(self):
        # conn = http.client.HTTPConnection("ifconfig.me")
        # conn.request("GET", "/ip")
        # if session['IP'] == str(conn.getresponse().read()).replace('b', '').replace("'", '').strip():

        error = exam_password(form.password.data, form.pass_exam.data)
        if type(error) == bool:
            hashed_password = set_password(form.password.data)
            name = form.name.data
            surname = form.surname.data
            created_data = datetime.datetime.now()
            db_sess = database.create_session()
            email = replacce(str(*db_sess.query(Reg.email).filter(Reg.id == id_ver)))
            user_data = Data(name=name, surname=surname, created_date=created_data, user_id=id_ver,
                             hashed_password=hashed_password)
            avatar = f'/static/image/{email}/avatar.jpeg'
            status = 'Я пользуюсь Boot'
            page_data = PData(status=status, avatar=avatar, page_id=id_ver)
            direc = PATH_DIC + '/' + email
            os.mkdir(direc)
            shutil.copy('static/image/avatar.jpeg', f'static/image/{email}')
            db_sess.add(user_data)
            db_sess.add(page_data)
            db_sess.commit()
            db_sess.close()
            return redirect(f'/page/{id_ver}')

    elif form.submit.data:
            error = 'Введите данные'