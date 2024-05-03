import pprint

def image_caption_combination_search(mq):
    settings = {
        "treat_urls_and_pointers_as_images": True,
        "model": "open_clip/ViT-B-32/laion2b_s34b_b79k",
    }

    mq.delete_index("my-first-multimodal-index")
    mq.create_index("my-first-multimodal-index", **settings)

    mq.index("my-first-multimodal-index").add_documents(
        [
            {
                "Title": "Flying Plane",
                "caption": "An image of a passenger plane flying in front of the moon.",
                "image": "https://raw.githubusercontent.com/marqo-ai/marqo/mainline/examples/ImageSearchGuide/data/image2.jpg",
            },
            {
                "Title": "Red Bus",
                "caption": "A red double decker London bus traveling to Aldwych",
                "image": "https://raw.githubusercontent.com/marqo-ai/marqo/mainline/examples/ImageSearchGuide/data/image4.jpg",
            },
            {
                "Title": "Horse Jumping",
                "caption": "A person riding a horse over a jump in a competition.",
                "image": "https://raw.githubusercontent.com/marqo-ai/marqo/mainline/examples/ImageSearchGuide/data/image1.jpg",
            },
        ],
        # note that captioned_image must be a tensor field
        tensor_fields=["captioned_image"],
        # Create the mappings, here we define our captioned_image mapping
        # which weights the image more heavily than the caption - these pairs
        # will be represented by a single vector in the index
        mappings={
            "captioned_image": {
                "type": "multimodal_combination",
                "weights": {"caption": 0.3, "image": 0.7},
            }
        },
    )

    # Search this index with a simple text query
    results = mq.index("my-first-multimodal-index").search(
        q="Give me some images of vehicles and modes of transport. I am especially interested in air travel and commercial aeroplanes."
    )

    print("Query 1:")
    pprint.pprint(results)

    # search the index with a query that uses weighted components
    results = mq.index("my-first-multimodal-index").search(
        q={
            "What are some vehicles and modes of transport?": 1.0,
            "Aeroplanes and other things that fly": -1.0,
        }
    )
    print("\nQuery 2:")
    pprint.pprint(results)

    results = mq.index("my-first-multimodal-index").search(
        q={"Animals of the Perissodactyla order": -1.0}
    )
    print("\nQuery 3:")
    pprint.pprint(results)
