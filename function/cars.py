def description_car(brand, model, **car_info):
    car_info['brand'] = brand
    car_info['model'] = model
    print(car_info)

description_car('bmw', 'x6')
description_car('audi', 'r8', fuel_type='electric', speed=210)