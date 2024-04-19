from flask import Blueprint, render_template, request, session

menuBP = Blueprint('menu', __name__)


@menuBP.route('/uicerMenu', methods=['GET'])
def uicerMenu():
    if request.method == 'GET':
        uicername = session.get('name')
        return render_template('UICerPage.html',uicername = uicername)
@menuBP.route('/alumniMenu', methods=['GET', 'POST'])
def alumniMenu():
    if request.method == 'GET':
        alumniname = session.get('name')
        return render_template('alumni.html', alumniname = alumniname)
@menuBP.route('/adminMenu', methods=['GET', 'POST'])
def adminMenu():
    if request.method == 'GET':
        admname = session.get('name')
        print(admname)
        return render_template('admin.html', admname = admname)


