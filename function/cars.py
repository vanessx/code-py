def description_car(brand, model, **car_info):
    car_dic = {
        'brand': brand.title(),
        'model': model.title(),
    }
    for car, value in car_info.items():
        car_dic[car] = value
        
    return car_dic

my_car = description_car('bmw', 'x6')
print(my_car)

your_car = description_car('audi', 'r8', fuel_type='electric', speed=210)
print(your_car)