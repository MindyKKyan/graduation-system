from flask import Blueprint, render_template, request, redirect, url_for, session

from sqlalchemy import and_

from app.models.admin import Admin
from app.models.uicer import UICer

loginBP = Blueprint('login', __name__)


@loginBP.route('/', methods=['GET', 'POST'])
def login(message=None,result1=None,result2=None,result3=None):
    if request.method == 'GET':
        return render_template('login.html')
    else:

        name = request.form.get('name')
        _password = request.form.get('password')
        role = request.form.get('identity')

        print(name, _password, role)


        if (name =='') or (_password=='') or (role==''):
            message ='Incomplete Input'
        elif role=='uicer':
            result1 = UICer.query.filter(and_(UICer.name == name, UICer._password == _password)).first()


        elif role=='alumni':
            result2 = UICer.query.filter(and_(UICer.name == name, UICer._password == _password)).first()


        elif role=='administrator':
            result3 = Admin.query.filter(and_(Admin.name == name, Admin._password == _password)).first()

        else:
            return "invalid operation"

        if message:
            return '<script> alert("Incomplete Input");window.location.replace("/")</script>'
            # return render_template('login.html',msg=message, status='error')
        if result1:
            if result1.role == 2:
                return '<script> alert("Wrong Role. Please try again");window.location.replace("/")</script>'
            print(result1.name)
            print(result1._password)
            session['name'] = result1.name
            session['role'] = result1.role
            return redirect(url_for('menu.uicerMenu'))
        elif result2:
            if result2.role == 1:
                return '<script> alert("Wrong Role. Please try again");window.location.replace("/")</script>'
            print(result2.name)
            print(result2._password)
            session['name'] = result2.name
            session['role'] = result2.role
            return redirect(url_for('menu.alumniMenu'))
        elif result3:
            print(result3.name)
            print(result3._password)
            session['name'] = result3.name
            session['role'] = result3.role
            return redirect(url_for('menu.adminMenu'))
        else:
            return '<script> alert("Wrong Name or Password or Role. Please try again");window.location.replace("/")</script>'

