from modules.wikipedia import wikipedia_search_query
from modules.wolframalpha import wolfram_search_query
from modules.recognize_generate import *


def process_query(query):
    if " ".join(query.split(" ")[0:2]).__contains__("what is"):
        query = " ".join(query.split(" ")[2, :])
    response = wikipedia_search_query(query)
    if not response:
        response = wolfram_search_query(query)
        if not response:
            generate_audio("I could not find any information about that.")


def main():
    while True:
        search_query = listen()
        if search_query:
            process_query(search_query)


if __name__ == '__main__':
    main()