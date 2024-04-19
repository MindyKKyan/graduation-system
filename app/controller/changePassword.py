

from flask import request, Blueprint, render_template, session
from app.models.base import db
from app.models.uicer import UICer


changePasswordBP = Blueprint('changePassword', __name__)


@changePasswordBP.route("/changePassword", methods=['GET', 'POST'])
def changePassword(message=None, message2=None):
    if request.method == 'GET':
        name = session.get('name')
        return render_template('changePSW.html', name = name)
    else:
        username = session.get('name')
        oldPassword = request.form['oldPSW']
        newPassword = request.form['newPSW']
        confirmPassword = request.form['newPSW2']

        target = UICer.query.filter(UICer.name == username).first()
        #print("test")
        #print(target._password)


        if oldPassword != target._password:
            message = 'wrong old password'

            #print("test warning")
            #return render_template('changePSW.html', message='username or old password incorrect')
        if newPassword != confirmPassword:
            message2 = 'wrong confirm'

            #print("confirm warning")
            #return render_template('changePSW.html', message='confirm password need to be same as new password')

        #print(target._password)

        if message:
            return '<script> alert("username or old password incorrect");window.location.replace("/changePassword")</script>'

        if message2:
            return '<script> alert("confirm password need to be same as new password");window.location.replace("/changePassword")</script>'

        target._password = newPassword
        db.session.add(target)
        db.session.commit()
        return '<script> alert("password changed success. Please login again");window.location.replace("/")</script>'

