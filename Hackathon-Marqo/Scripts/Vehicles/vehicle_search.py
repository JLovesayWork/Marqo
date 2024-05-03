import pprint

def search_vehicles(mq):
    # Search 1: Simple text query
    results = mq.index("simple-vehicle-index").search(
        q="I want a Toyota Corolla.",
        limit="1"
    )
    print("\nSearch 1:")
    pprint.pprint(results)

    # Search 2: Weighted components query
    results = mq.index("complex-vehicle-index").search(
        q={
            "Looking for Toyota vehicles": 1.0,
            "Prefer compact models": -0.5,
        },
        limit="3"
    )
    print("\nSearch 2:")
    pprint.pprint(results)
    
    # Search 3: Multimodal query (using a description)
    results = mq.index("multimodal-vehicle-index").search(
        q="https://th.bing.com/th/id/OIP.tn8nSDdBvDb_c0LL3Qu0gwHaEo?rs=1&pid=ImgDetMain",
        limit=1
    )
    print("\nSearch 3:")
    pprint.pprint(results)
    
    # Search 4: Multimodal query (looking for panoramic sunroof)
    results = mq.index("complex-vehicle-index").search(
        q={
            "I want a vehicle with a panoramic sunroof": 1.1
        },
        limit=1
    )
    print("\nSearch 4:")
    pprint.pprint(results)

    # Search 5: Multimodal query (looking for alloy wheels)
    results = mq.index("complex-vehicle-index").search(
        q={
           "I want a vehicle with alloy wheels": 1.5
        },
        limit=2
    )
    print("\nSearch 5:")
    pprint.pprint(results)
   
