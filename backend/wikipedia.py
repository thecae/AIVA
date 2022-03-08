import wikipediaapi
from backend.recognize_generate import *
from backend.exceptions import *

wikipedia = wikipediaapi.Wikipedia('en')


def wikipedia_search_query(query):
    """
    This function implements the Wikipedia API to generate results to most "what is" questions.
    It registers with the publicly-available API and enters the entire query and sifts for results.
    The function then passes the processor to two sub-functions, depending on the results achieved;
    if multiple results were found based on a broad search query, it asks for more clarification.
    Otherwise, it controls flow to a single-response function which then parses the article results.

    :param query: The search query input from user
    """
    page_result = wikipedia.page(query)
    if page_result.text.split('\n')[0].__contains__('Traceback (most recent call last)'):
        raise WikipediaNetworkFail
    if page_result.exists():
        if page_result.text.split('\n')[0].__contains__('may refer to'):
            process_multiple_results(page_result)
        else:
            process_single_result(page_result)
            return
    else:
        # generate_audio("I could not find any information on " + page_result.title + ".")
        raise WikipediaReturnedVoid


def process_multiple_results(page_result):
    """
    This function deals with multiple result search queries, based on the results of the
    wikipedia_search_query() function.  It catches multiple results based on keywords in
    the search results, indicating that multiple results show up. This function asks for
    more clarification from the user using the listen() function and re-sends it to be
    processed.

    :param page_result: The WikipediaPage result object
    """
    generate_audio("I couldn't quite narrow down what you mean by " + page_result.title + ".")
    generate_audio("Can you please provide a bit more clarification?")

    specified_query = listen()

    if not specified_query.__contains__(page_result.title):
        wikipedia_search_query(page_result.title + specified_query)
    else:
        wikipedia_search_query(specified_query)


def process_single_result(page_result):
    """
    This function processes single-page results, meaning that only one article was returned
    based on the input query.  The function then parses for the best output to provide to
    the user based on the question and sends it for output.

    Right now the processor is really lazy and uses the summary object in the WikipediaPage
    class, which is just the first few sentences of the article.

    :param page_result: The WikipediaPage result object.
    """
    generate_audio(page_result.summary)
