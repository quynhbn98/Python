
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

def assign_truck_bag(bag_data, truck_data):
    output = []
    # your code here
    bags = {}
    for i, item in enumerate(bag_data):
        bags[item["dst_id"]] = [] # insert dst_id as key into dictionary
        a = [] # just bags' weight
        b = {} # map bag - weight
        for j in range(len(item["bag_export"])):
            a.append(item["bag_export"][j][1])
            b[item["bag_export"][j][0]] = item["bag_export"][j][1]
        bags[item["dst_id"]].append(a)
        bags[item["dst_id"]].append(b)

    trucks = { k : [] for k in list(bags.keys()) }
    for i in list(trucks.keys()):
        f = [] # just trucks' weight
        e = {} # map truck - weight
        for item in truck_data:
            if item["dst_id"] == i:
                f.append(item["remain_weight"])
                e[item["truck_plate"]] = item["remain_weight"]
        f = sorted(f, reverse = True)
        trucks[i].append(f)
        trucks[i].append(e)

    truck_map_bag = {}
    for  i in truck_data:
        truck_map_bag[i["truck_plate"]] = []

    for bag_dst in bags:
        for truck_dst in trucks:
            if bag_dst == truck_dst:
                while (min(trucks[truck_dst][0]) > min(bags[bag_dst][0]) and min(bags[bag_dst][0]) > 0) or sum(bags[bag_dst][0]) > 0:
                    bag = max(bags[bag_dst][0])
                    tempp = []
                    for i in trucks[truck_dst][0]:
                        if i > bag:
                            tempp.append(i)
                    if len(tempp) > 0:
                        truck = min(tempp)
                    else:
                        truck = min(trucks[truck_dst][0])
                    b_index = bags[bag_dst][0].index(bag)
                    t_index = trucks[truck_dst][0].index(truck)
                    x = get_key(bag,bags[bag_dst][1])
                    y = get_key(truck,trucks[truck_dst][1])
                    if bag <= truck and bag > 0 :
                        truck = (truck - bag)
                        trucks[truck_dst][1][y] = truck
                        trucks[truck_dst][0][t_index] = truck
                        bags[bag_dst][0][b_index] = 0
                        bags[bag_dst][1][x] = 0
                        truck_map_bag[y].append(x)
                    else: bags[bag_dst][0][b_index] = 0
    for i in truck_map_bag:
        z = {}
        z["truck_plate"] = i
        z["bags"] = truck_map_bag[i]
        output.append(z)

    # end your code here
    return output

assign_result = assign_truck_bag(truck_data=truck_data, bag_data=bag_data)
print(assign_result)