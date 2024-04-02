info = {
    'distance' : 0,
    'speed' : 5,
    'time' : 3
}
def route_info(info):
    if ('distance' in info) and (type(info['distance']) != float) and (info['distance'] != 0):
        print (f"The distance is {info['distance']} kilometers")
    elif info.get('time') and info.get('speed'):
        print (f"The distance is {info['speed'] * info['time']} kilometers")
    else:
        print ('No info available')

route_info(info)
