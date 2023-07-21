import functions

from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    cars=functions.load()
    total_cars=len(cars)
    return render_template("index.html", cars=cars, total_cars=total_cars)

@app.route('/add')
def add():
    car_name=request.args["car_name"]
    made_year=request.args["made_year"]
    color=request.args["color"]
    car_number=request.args["car_number"]
    driver_name=request.args["driver_name"]
    last_visit=request.args["last_visit"]
    last_check=request.args["last_check"]
    functions.add(car_name=car_name, made_year=made_year, color=color, car_number=car_number, driver_name=driver_name, last_visit=last_visit, last_check=last_check)
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    car_number=request.args["car_number"]
    functions.delete(car_number)
    return redirect(url_for('home'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        car_name=request.form["car_name"]
        made_year=request.form["made_year"]
        color=request.form["color"]
        car_number=request.form["car_number"]
        driver_name=request.form["driver_name"]
        last_visit=request.form["last_visit"]
        last_check=request.form["last_check"]
        functions.update(car_name, made_year, color, car_number, driver_name, last_visit, last_check)
        return redirect(url_for('home'))
    else:
        car_name=request.args["car_name"]
        made_year=request.args["made_year"]
        color=request.args["color"]
        car_number=request.args["car_number"]
        driver_name=request.args["driver_name"]
        last_visit=request.args["last_visit"]
        last_check=request.args["last_check"]
        return render_template("update.html", car_name=car_name, made_year=made_year, color=color, car_number=car_number, driver_name=driver_name, last_visit=last_visit, last_check=last_check)

@app.route('/search')
def search():
    query=request.args["query"]
    print('query = ',query)
    results=functions.search(query=query)
    total_cars=len(results)
    return render_template("index.html", cars=results, total_cars=total_cars)

@app.route('/find')
def find():
    car_name=request.args["car_name"]
    from_year=request.args["from_year"]
    till_year=request.args["till_year"]
    color=request.args["color"]
    car_number=request.args["car_number"]
    driver_name=request.args["driver_name"]
    last_visit_from=request.args["last_visit_from"]
    last_visit_till=request.args["last_visit_till"]
    last_check_from=request.args["last_check_from"]
    last_check_till=request.args["last_check_till"]
    results=functions.find(car_name, from_year, till_year, color, car_number, driver_name, last_visit_from, last_visit_till, last_check_from, last_check_till)
    total_cars=len(results)
    return render_template("index.html", cars=results, total_cars=total_cars)

# Запускаем сервер разработки Flask
if __name__ == '__main__':
    app.run()