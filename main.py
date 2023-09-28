from flask import Flask
from flask import request
from flask import request, redirect, url_for, render_template

from functions import SQLiteDB
from functions import LOGIN

app = Flask(__name__)
app.config['SECRET_KEY'] = '134734'


@app.route('/admin', methods=['GET', 'PUT', 'DELETE'])
def admin():
    return


@app.route('/admin/dishes', methods=['GET'])
def dishes():
    return


@app.route('/admin/dishes/add', methods=['POST'])
def dishes_add():
    return


@app.route('/admin/dishes/<dish_name>', methods=['GET', 'PUT', 'DELETE'])
def admin_dish_name():
    return


@app.route('/admin/current_orders', methods=['GET'])
def get_current_orders():
    return


@app.route('/admin/current_orders/<order_id>', methods=['GET', 'PUT'])
def order_id():
    return


@app.route('/admin/category_list', methods=['GET', 'POST'])
def category_list():
    return


@app.route('/admin/category_list/<category_name>', methods=['GET', 'DELETE'])
def category_name():
    return


@app.route('/admin/search', methods=['GET/POST'])
def amin_search():
    return


@app.route('/cart', methods=['GET', 'PUT'])
def cart():
    return


@app.route('/cart/order', methods=['POST'])
def cart_order():
    return


@app.route('/cart/add', methods=['POST', 'PUT'])
def cart_add():
    return


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def user():
    return


@app.route('/user/register', methods=['POST'])
def user_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = LOGIN("dish.db")
        registration_result = db.register_user(username, password)

        if registration_result is None:
            return redirect(url_for('user_sign_in'))  # Правильна назва функції
        else:
            return registration_result  # Повертаємо повідомлення про помилку

    return render_template('register.html')


@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():
    return


@app.route('/user/logout', methods=['GET', 'POST'])
def user_logout():
    return


@app.route('/user/restore', methods=['POST'])
def user_restore():
    return


@app.route('/user/orders', methods=['GET'])
def user_orders_history():
    return


@app.route('/user/orders/<order_id>', methods=['GET'])
def user_order(order_id: int):
    return


@app.route('/user/address', methods=['GET', 'POST'])
def user_address_list():
    return


@app.route('/user/address/<address_id>', methods=['GET', 'PUT', 'DELETE'])
def user_address(address_id: int):
    return


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    with SQLiteDB("dish.db") as db:
        if request.method == "POST":
            data = request.form.to_dict()
            data['ID'] = data["Dish_name"].replace('', '')
            data['Available'] = 1
            db.insert_into('Dishes', data)

        dishes = db.select_from('Dishes', ['*'])

    return render_template('menu.html', dishes=dishes)


@app.route('/menu/<cat_name>', methods=['GET'])
def menu_cat_name():
    return


@app.route('/menu/<cat_name>/<dish>', methods=['GET'])
def menu_cat_name_dish():
    return


@app.route('/menu/<cat_name>/<dish>/review', methods=['POST'])
def menu_review():
    return


@app.route('/menu/search', methods=['GET', 'POST'])
def menu_search():
    return


if __name__ == '__main__':
    app.run()
