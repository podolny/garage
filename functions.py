from classes import Cars
import pickle

def load():
    try:
        with open("cars.pickle", "rb") as f:
            cars=pickle.load(f)
            return cars
    except:
        return []

def add(car_name:str="car_name", made_year:int="made_year", color:str="color", car_number:str="car_number", driver_name:str="driver_name", last_visit:str="last_visit", last_check:str="last_check"):
    cars=load()
    cars.append(Cars(car_name=car_name, made_year=made_year, color=color, car_number=car_number, driver_name=driver_name, last_visit=last_visit, last_check=last_check))
    with open("cars.pickle", "wb") as f:
        pickle.dump(cars, f)       

def save(cars:list):
    with open("cars.pickle", "wb") as f:
        pickle.dump(cars, f)

def delete(car_number):
    cars=load()
    for car in cars.copy():
        if car.car_number==car_number:
            cars.remove(car)
    save(cars)

def update(car_name, made_year, color, car_number, driver_name, last_visit, last_check):
    delete(car_number)
    add(car_name, made_year, color, car_number, driver_name, last_visit, last_check)

def search(query):
    cars=load()
    list_of_dicts = [car.__dict__ for car in cars]
    results=[]
    for car in list_of_dicts:
        for value in car.values():
            if query in str(value):
                results.append(car)
                break
    return results    

from datetime import date, timedelta, datetime

def find(car_name, from_year, till_year, color, car_number, driver_name, last_visit_from, last_visit_till, last_check_from, last_check_till):
    cars=load()
    list_of_dicts = [car.__dict__ for car in cars]
    results=[]
    for car in list_of_dicts:
        if car_name == car.get('car_name') or car_name == "":
            if from_year != "":
                f_y = int(from_year)
            else:
                f_y = 1950
            if till_year != "":
                t_y = int(till_year)
            else:
                t_y = date.today().year
            made_year = car.get('made_year')
            print('f_y - ', f_y, type(f_y))
            print('t_y - ', t_y, type(t_y))
            print('made_year - ', made_year, type(made_year))
            if f_y <= made_year <= t_y:
                if color == car.get('color') or color == "":
                    if car_number == str(car.get('car_number')) or car_number == "":
                        if driver_name == car.get('driver_name') or driver_name == "":
                            if last_visit_from != "":
                                l_v_f = datetime.strptime(last_visit_from, "%Y-%m-%d")
                            else:
                                l_v_f = datetime.strptime("01/01/1900", "%d/%m/%Y")
                            if last_visit_till != "":
                                l_v_t = datetime.strptime(last_visit_till, "%Y-%m-%d")
                            else:
                                l_v_t = datetime(date.today().year, date.today().month, date.today().day)
                            last_visit = datetime.strptime(car.get('last_visit'), "%d/%m/%Y")
                            if l_v_f <= last_visit <= l_v_t:

                                if last_check_from != "":
                                    l_c_f = datetime.strptime(last_check_from, "%Y-%m-%d")
                                else:
                                    l_c_f = datetime.strptime("01/01/1900", "%d/%m/%Y")
                                if last_check_till != "":
                                    l_c_t = datetime.strptime(last_check_till, "%Y-%m-%d")
                                else:
                                    l_c_t = datetime(date.today().year, date.today().month, date.today().day)
                                last_check = datetime.strptime(car.get('last_check'), "%d/%m/%Y")
                                if l_c_f <= last_check <= l_c_t:
                                    results.append(car)
    return results 

import random


def generate_random_cars(count):
    car_brands = [
    "Toyota",
    "Honda",
    "Ford",
    "Chevrolet",
    "Volkswagen",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Nissan",
    "Hyundai",
    "Kia",
    "Volvo",
    "Subaru",
    "Mazda",
    "Lexus",
    "Jeep",
    "Land Rover",
    "Porsche",
    "Ferrari",
    "Lamborghini"
]
    colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Gray",
    "Silver",
    "Orange",
    "Purple",
    "Brown",
    "Pink",
    "Gold",
    "Beige",
    "Teal",
    "Navy",
    "Magenta",
    "Turquoise",
    "Lime",
    "Cyan"
]

    owner_names = [
    "Noam Levi",
    "Maya Cohen",
    "Yair Mizrahi",
    "Tamar Biton",
    "Eitan Dayan",
    "Shira Azulay",
    "Itai Cohen",
    "Noya Ben-David",
    "Adi Avrahami",
    "Liel Hakim",
    "Yael Cohen",
    "Omer Ben-Zvi",
    "Or Tal",
    "Nir Levy",
    "Talia Cohen",
    "Tomer Baruch",
    "Hadar Mor",
    "Nadav Harel",
    "Liora Weiss",
    "Guy Cohen"
]
    
    current_year = date.today().year

    for _ in range(count):
        car_year = random.randint(1970, current_year)
        car_brand = random.choice(car_brands)
        color = random.choice(colors)
        license_plate = ''.join(random.choices('0123456789', k=6))
        owner_name = random.choice(owner_names)
        last_service_date = date.today() - timedelta(days=random.randint(1, 365))
        last_maintenance_date = (last_service_date - timedelta(days=random.randint(1, 365))).strftime("%d/%m/%Y")
        last_service_date = last_service_date.strftime("%d/%m/%Y")
        
        add(car_brand, car_year, color, license_plate, owner_name, last_service_date, last_maintenance_date)

#generate_random_cars(20)


