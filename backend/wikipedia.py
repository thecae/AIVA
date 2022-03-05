import wikipediaapi
from recognize_generate import *

wikipedia = wikipediaapi.Wikipedia('en')


def wikipedia_search_query(query):
    page_result = wikipedia.page(query)
    if page_result.exists():
        if page_result.text.split('\n')[0].__contains__('may refer to'):
            process_multiple_results(page_result)
        else:
            process_single_result(page_result)
    else:
        print("I could not find any information on " + page_result.title + ".")


def process_multiple_results(page_result):
    generate_audio("I couldn't quite narrow down what you mean by " + page_result.title + ".")
    generate_audio("Can you please provide a bit more clarification?")
    specified_query = "Python Programming Language"
    if not specified_query.__contains__(page_result.title):
        wikipedia_search_query(page_result.title + specified_query)
    else:
        wikipedia_search_query(specified_query)


def process_single_result(page_result):
    generate_audio(page_result.summary)
