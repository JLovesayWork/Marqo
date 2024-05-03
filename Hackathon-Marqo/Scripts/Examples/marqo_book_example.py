import pprint

def run_marqo_book_example(mq):
    index_name = "my-first-index"
    mq.delete_index(index_name)
    mq.create_index(index_name, model="hf/e5-base-v2")

    mq.index("my-first-index").add_documents(
        [
            {
                "Title": "The Travels of Marco Polo",
                "Description": "A 13th-century travelogue describing Polo's travels",
            },
            {
                "Title": "Extravehicular Mobility Unit (EMU)",
                "Description": "The EMU is a spacesuit that provides environmental protection, "
                "mobility, life support, and communications for astronauts",
                "_id": "article_591",
            },
        ],
        tensor_fields=["Description"],
    )

    results = mq.index("my-first-index").search(
        q="What is the best outfit to wear on the moon?"
    )

    print("\nADD DOCUMENTS")
    pprint.pprint(results)
    
def get_example_book(mq):
    result = mq.index("my-first-index").get_document(document_id="article_591")
    
    print("\nGET DOCUMENT")
    pprint.pprint(result)
    
def get_index_stats(mq):
    results = mq.index("my-first-index").get_stats()
    
    print("\nINDEX STATS")
    pprint.pprint(results)
    
def perform_lexical_search(mq):
    result = mq.index("my-first-index").search("marco polo", search_method="LEXICAL")
    
    print("\nLEXICAL SEARCH")
    pprint.pprint(result)



