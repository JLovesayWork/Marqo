from Scripts.Examples.marqo_book_example import run_marqo_book_example, get_example_book, get_index_stats, perform_lexical_search
from Scripts.Examples.multi_modal_search import image_search_animal, search_using_image
from Scripts.Examples.weighted_query import weighted_search
from Scripts.Examples.search_multimodal_combination import image_caption_combination_search

def process_simple_scripts(mq):
    
    run_marqo_book_example(mq)
    get_example_book(mq)
    get_index_stats(mq)
    perform_lexical_search(mq)

    # Multi modal and cross modal search

    image_search_animal(mq)
    search_using_image(mq)

    # Weighted Search

    weighted_search(mq)
    
    # Multi Modal Combination Search
    
    image_caption_combination_search(mq)
    

