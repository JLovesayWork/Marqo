import pprint

def image_search_animal(mq):
    settings = {
        "treat_urls_and_pointers_as_images": True,
        "model": "open_clip/ViT-B-32/laion2b_s34b_b79k",
    }
    mq.delete_index("my-multimodal-index")
    response = mq.create_index("my-multimodal-index", **settings)

    response = mq.index("my-multimodal-index").add_documents(
        [
            {
                "My_Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Hipop%C3%B3tamo_%28Hippopotamus_amphibius%29%2C_parque_nacional_de_Chobe%2C_Botsuana%2C_2018-07-28%2C_DD_82.jpg/640px-Hipop%C3%B3tamo_%28Hippopotamus_amphibius%29%2C_parque_nacional_de_Chobe%2C_Botsuana%2C_2018-07-28%2C_DD_82.jpg",
                "Description": "The hippopotamus, also called the common hippopotamus or river hippopotamus, is a large semiaquatic mammal native to sub-Saharan Africa",
                "_id": "hippo-facts",
            }
        ],
        tensor_fields=["My_Image"],
    )
    
    results = mq.index("my-multimodal-index").search("animal")
    
    print("\nMULTIMODAL IMAGE SEARCH")
    pprint.pprint(results)

def search_using_image(mq):
    results = mq.index("my-multimodal-index").search(
    "https://docs.marqo.ai/2.0.0/Examples/marqo.jpg"
    )
    
    print("\nSEARCH USING IMAGE")
    pprint.pprint(results)
