# There are 7 bags will go to 657 and 4 bags will go to 505

bag_data = [
    {
        "dst_id": 657, # bag destination
        "bag_export": [
            (1001, 1), # (bag_order, weight)
            (1002, 0.7),
            (1003, 1.2),
            (1004, 4.4),
            (1005, 0.5),
            (1006, 4),
            (1007, 1.2)
        ]
    },
    {
        "dst_id": 505,
        "bag_export": [ (1008, 0.4), (1009, 1.2), (1010, 3), (1011, 4.3)]
    }
]

# There are 3 trucks: 2 trucks will go to 657, another truck will go to 505

truck_data = [
    {
        "truck_plate": "29H-123.43",
        "remain_weight": 5, # truck remain weight
        "dst_id": 657 # truck destination
    },
    {
        "truck_plate": "37B-142.33",
        "remain_weight": 7,
        "dst_id": 657
    },
    {
        "truck_plate": "30A-443.89",
        "remain_weight": 5,
        "dst_id": 505
    }
]

# You have to maximize truck capacity (least weight remaining) or number of bags on each truck or both
# Output will be something like this:

# assign_result = [
#     {
#         "truck_plate": "29H-123.43",
#         "bags": [1004, 1005]
#     },
#     {
#         "truck_plate": "37B-142.33",
#         "bags": [1006, 1003, 1007]
#     },
#     {
#         "truck_plate": "30A-443.89",
#         "bags": [1011, 1008]
#     },
# ]