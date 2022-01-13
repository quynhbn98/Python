# Optimize route of truck
# your have station infos include coordinates
# write a function give a list next station need to come (unorrdered)
# you need get optimize route (in order) that minimize truck total distances
# You can caculate distance by skyway (depend on lat, long of two points)
import geopy.distance
import itertools

station_infos = {
    657: {
        "station_id": 657,
        "station_name": "Kho Láng Hạ",
        "coor": (21.013561, 105.813030) # lat, long
    },
    105: {
        "station_id": 105,
        "station_name": "BC Trung Kính (HN)",
        "coor": (21.014479, 105.797630)
    },
    164: {
        "station_id": 164,
        "station_name": "Thường Tín",
        "coor": (20.824356, 105.881634)
    },
    361: {
        "station_id": 361,
        "station_name": "BC Thụy Khuê (HN)",
        "coor": (21.043394, 105.821611)
    },
    505: {
        "station_id": 505,
        "station_name": "Kho Phạm Văn Đồng",
        "coor": (21.075193, 105.7835495)
    },
}

def get_optimize_route(cur_station, next_stations):
    # optimize_route = []
    permutation_list = list(itertools.permutations(next_stations))
    possible_routes = []
    for item in permutation_list:
        a = list(item)
        a.insert(0,current_station)
        possible_routes.append(a)
    route_lengths = {}
    for i, route in enumerate(possible_routes):
        lenght = 0
        for j in range(len(route) - 1):
            prev_station = route[j]
            next_station = route[j+1]
            prev_coords = station_infos[prev_station]["coor"]
            next_coords = station_infos[next_station]["coor"]
            lenght = lenght + geopy.distance.distance(prev_coords, next_coords).km
        route_lengths[i] = lenght
    print(route_lengths)
    min_lenght_index = min(route_lengths, key=route_lengths.get)
    print(route_lengths[min_lenght_index])
    optimize_route = possible_routes[min_lenght_index]
    return optimize_route

current_station = 657
next_stations = [505, 361, 164] # list stations need to come unorrdered
my_route = get_optimize_route(cur_station=current_station, next_stations=next_stations)
print(my_route)