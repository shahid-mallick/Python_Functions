import math

def windchill():
    v= int(input("Enter the wind speed in Miles per hour    :  "))
    t= int(input("Enter the Air temperature in Faranheit    :  "))

    wchill = (13.12 + 0.6215 * t - 11.37 * math.pow ( v, 0.16) + 0.3965 * t * math.pow (v, 0.16))
    print ("The Windchill is", int(wchill,0))

    if (t > 50 or v > 120):
        print ("Please enter the valid number   :  ")
    else:
        print (wchill)


windchill()

