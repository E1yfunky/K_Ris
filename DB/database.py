from pymysql import connect
from pymysql.err import OperationalError
from pymysql.err import InterfaceError


class UserDatabase:

    def __init__(self, config: dict):
        self.config = config
        self.conn = None

    def __enter__(self):
        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except OperationalError as err:
            if err.args[0] == 1045:
                print('Неверный логин и пароль, повторите подключение')
            if err.args[0] == 2003:
                print('Неверно введен порт или хост для подключения к серверу')
            if err.args[0] == 1049:
                print('Такой базы данных не существует')
            return None
        except UnicodeEncodeError as err:
            print('Были введены символы на русском языке')
            return None

    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_value:
            if exc_value == 'Курсор не был создан':
                print('Курсор не создан')
            elif exc_value.args[0] == 1064:
                print('Синтаксическая ошибка в запросе!')
            elif exc_value.args[0] == 1146:
                print('Ошибка в запросе! Такой таблицы не существует.')
            elif exc_value.args[0] == 1054:
                print('Ошибка в запросе! Такого поля не существует.')
        if self.conn is not None:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        return True

def work_with_db(dbconfig, _SQL):
    with UserDatabase(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не был создан')
        else:
            cursor.execute(_SQL)
            schema = [column[0] for column in cursor.description]
            result = []
            for str in cursor.fetchall():
                result.append(dict(zip(schema, str)))
            return result