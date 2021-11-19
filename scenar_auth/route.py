from flask import Blueprint, session, render_template, request
from access import group_permission_decorator
from DB.database import work_with_db
from DB.sql_provider import SQLProvider

auth_app = Blueprint('auth', __name__, template_folder='templates')
provider = SQLProvider('scenar_auth/SQL/')

dbconfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user',
    'password': 'User2000!',
    'db': 'b_miles'
}

@auth_app.route('/auth', methods=['GET', 'POST'])
@group_permission_decorator
def auth():
    if request.method == 'GET':
        return render_template('auth.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')


        sql = provider.get('auth.sql', login=login, password=password)
        result = work_with_db(dbconfig, sql)
        if not result:
            return render_template('auth_result.html', head='Invalid login or password')
        session['group_name'] = result[0]['group_acc']
        return render_template('auth_result.html', head='Logged in')