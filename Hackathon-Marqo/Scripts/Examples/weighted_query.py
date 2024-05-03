import pprint

def weighted_search(mq):
    mq.delete_index("my-weighted-query-index")
    mq.create_index("my-weighted-query-index")

    mq.index("my-weighted-query-index").add_documents(
        [
            {
                "Title": "Smartphone",
                "Description": "A smartphone is a portable computer device that combines mobile telephone "
                "functions and computing functions into one unit.",
            },
            {
                "Title": "Telephone",
                "Description": "A telephone is a telecommunications device that permits two or more users to"
                "conduct a conversation when they are too far apart to be easily heard directly.",
            },
            {
                "Title": "Thylacine",
                "Description": "The thylacine, also commonly known as the Tasmanian tiger or Tasmanian wolf, "
                "is an extinct carnivorous marsupial."
                "The last known of its species died in 1936.",
            },
        ],
        tensor_fields=["Description"],
    )

    # initially we ask for a type of communications device which is popular in the 21st century
    query = {
        # a weighting of 1.1 gives this query slightly more importance
        "I need to buy a communications device, what should I get?": 1.1,
        # This will lead to 'Smartphone' being the top result
        "The device should work like an intelligent computer.": 1.0,
    }

    results = mq.index("my-weighted-query-index").search(q=query)

    print("Query 1:")
    pprint.pprint(results)

    # now we ask for a type of communications which predates the 21st century
    query = {
        # a weighting of 1 gives this query a neutral importance
        "I need to buy a communications device, what should I get?": 1.0,
        # This will lead to 'Telephone' being the top result
        "The device should work like an intelligent computer.": -0.3,
    }

    results = mq.index("my-weighted-query-index").search(q=query)

    print("\nQuery 2:")
    pprint.pprint(results)
