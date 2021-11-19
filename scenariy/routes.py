from flask import Flask, render_template, request, redirect, Blueprint
from DB.database import work_with_db
from DB.sql_provider import SQLProvider
from access import group_permission_decorator

menu_app = Blueprint('menu', __name__, template_folder='templates')
provider = SQLProvider('scenariy/SQL/')

dbconfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user',
    'password': 'User2000!',
    'db': 'b_miles'
}

@menu_app.route('/menu')
@group_permission_decorator
def menu():
    return render_template('links.html')

@menu_app.route('/resume')
@group_permission_decorator
def resume():
    sql = provider.get('resume.sql')
    result = work_with_db(dbconfig, sql)

    if not result:
        return 'Not found'
    return render_template('result1.html', head = 'Отчет о начислении бонусных миль', list = result)
    return 'Invalid cursor'

@menu_app.route('/r_y', methods=['GET', 'POST'])
@group_permission_decorator
def r_y():
    if request.method == 'GET':
        return render_template('form1.html')
    else:
        year = request.form.get('year')

        if year:
            sql = provider.get('resume_year.sql', year=year)
            result = work_with_db(dbconfig, sql)
            if not result:
                return 'Not found'
            return render_template('result1.html', head='Отчет о продаже билетов за ' + year + ' год', list=result)
        return 'Invalid date or cursor'

@menu_app.route('/reit', methods=['GET', 'POST'])
@group_permission_decorator
def search_by_num():
    if request.method == 'GET':
        return render_template('form2.html')
    else:
        r_num = request.form.get('r_num')

        if r_num:
            sql = provider.get('reit.sql', r_num = r_num)
            result = work_with_db(dbconfig, sql)
            if not result:
                return 'Not found'
            return render_template('result1.html', head = 'Рейтинг пользователей, купивших билеты на рейс ' + r_num + ', по цене билета', list = result)
        return 'Invalid date or cursor'

@menu_app.route('/notick')
@group_permission_decorator
def never_buy():
    sql = provider.get('no_ticket.sql')
    result = work_with_db(dbconfig, sql)
    if not result:
        return 'Not found'
    return render_template('result1.html', head = 'Список зарегистрированных пользователей, никогда не покупавших билеты', list = result)

@menu_app.route('/empty_date', methods=['GET', 'POST'])
@group_permission_decorator
def empty_date():
    if request.method == 'GET':
        return render_template('form3.html')
    else:
        year = request.form.get('year')
        month = request.form.get('month')

        if year and month:
            sql = provider.get('empty_date.sql', year=year, month=month)
            result = work_with_db(dbconfig, sql)
            if not result:
                return 'Not found'
            return render_template('result1.html', head = 'Список зарегистрированных пользователей, не покупавших билеты за ' + month + '.' + year, list=result)
        return 'Invalid date or cursor'

@menu_app.route('/most_often', methods=['GET', 'POST'])
@group_permission_decorator
def most_often():
    if request.method == 'GET':
        return render_template('form4.html')
    else:
        year = request.form.get('year')
        month1 = request.form.get('month1')
        month2 = request.form.get('month2')
        num = request.form.get('num')

        if year and month1 and month2 and num:
            sql = provider.get('most_often.sql', year=year, month1=month1, month2=month2, num=num)
            result = work_with_db(dbconfig, sql)
            if not result:
                return 'Not found'
            return render_template('result1.html', head = 'Пользователи, чаще всего покупавшие билеты с '+month1+' по '+month2+' месяца '+year+' года', list=result)
        return 'Invalid date or cursor'
