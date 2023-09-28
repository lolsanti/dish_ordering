import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class SQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()

    def sql_query(self, query):
        answer = self.cur.execute(query)
        return answer.fetchall()

    def insert_into(self, table_name, params):
        values = ', '.join([f"'{str(i)}'" for i in params.values()])
        columns = ', '.join(params.keys())
        self.cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")

    def select_from(self, table_name, columns: list, where=None):
        columns = ', '.join(columns)
        query = f'SELECT {columns} FROM {table_name}'

        if where:
            where = ', '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f' WHERE {where}'

        return self.sql_query(query)


class LOGIN:
    def __init__(self, db_name, cur, con):
        self.db_name = db_name
        self.cur = cur
        self.con = con

    def register_user(self, username, password):
        try:
            existing_user = self.cur.execute("SELECT * FROM USER WHERE username = ?", (username,))
            if existing_user.fetchone():
                return "Користувач із таким іменем вже існує"

            self.cur.execute("INSERT INTO USER (username, password) VALUES (?, ?)", (username, password))
            self.con.commit()
            return None  # Реєстрація успішна

        except sqlite3.Error as e:
            return str(e)  # Помилка бази даних

    def login_user(self, username, password):
        try:
            # Пошук користувача з вказаним іменем і паролем
            user = self.cur.execute("SELECT * FROM User WHERE username = ? and password = ?", (username, password))
            user_data = user.fetchone()

            if user_data:
                # Якщо користувач знайдений, створюємо сесію
                session['username'] = user_data['username']
                return None  # Вхід успішний

            return "Невірне ім'я користувача або пароль"

        except sqlite3.Error as e:
            return str(e)  # Помилка бази даних

    def logout_user(self):
        try:
            # Знищення сесії користувача
            session.pop("username", None)  # Виправлено параметр "None"
            return None  # Вихід успішний
        except Exception as e:
            return str(e)