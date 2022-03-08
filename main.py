from backend.wikipedia import wikipedia_search_query
from backend.wolframalpha import wolfram_search_query
from backend.recognize_generate import *
from backend.exceptions import *


def process_query(query):
    """
    process_query is the main driver for the AI.  This function passes the query
    across the various interfaces that are supported by the AI in search of an
    answer to the query provided.  As this AI becomes more advances, more interfaces
    will be offered in this section.

    :param query: The query entered from user.
    """
    if " ".join(query.split(" ")[0:2]).__contains__("what is"):
        query = " ".join(query.split(" ")[2, :])

    # catch clause for Wikipedia search query
    try:
        wikipedia_search_query(query)
        return
    except WikipediaReturnedVoid:
        generate_audio("Wikipedia returned no search results.")
    except WikipediaNetworkFail:
        generate_audio("Unable to connect to Wikipedia API.")

    # catch clause for Wolfram|Alpha search query
    try:
        wolfram_search_query(query)
        return
    except WolframReturnedVoid:
        generate_audio("Wolfram|Alpha returned no search results.")

    generate_audio("I could not find any information about that.")


def main():
    while True:
        search_query = listen()
        if search_query:
            process_query(search_query)
            break


if __name__ == '__main__':
    main()