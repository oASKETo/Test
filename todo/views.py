# from django.shortcuts import render
# from .models import Todo
# from math import sin, cos, radians, acos
# from geopy.geocoders import Nominatim


#     #По идее должен передавать данные из бд в функцию

# EARTH_RADIUS_IN_KM = 6.371

# def adresPost(adres):
#     distance = 0
#     i=0
#     geolocator = Nominatim()
#     location = geolocator.geocode(adres)

#     latitude1 = radians(location.latitude)
        
#     while i < 5:
#             delta_long = radians(location.longitude - Todo.long)
            
#             cos_x = (
#                 sin(latitude1) * sin(location.longitude) +
#                 cos(latitude1) * cos(location.longitude) * cos(delta_long)
#             )
                
#             distanceTemp = acos(cos_x) * EARTH_RADIUS_IN_KM #В стринг наверное нужно
#             if i==0:
#                 distance = distanceTemp
#             if distanceTemp < distance:
#                 distance = distanceTemp
#             i+=1


#     if(distance > 8): #а тут скорее всего distance к целочисленному привести
#         return "В вашу область не возим"
#     else:
#         return "Вам привезут из " + Todo.adres
    

        

      
