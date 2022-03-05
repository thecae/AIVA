import wolframalpha
from recognize_generate import *

client = wolframalpha.Client('JUT65U-PHRVWRHQTH')


def wolfram_search_query(query):
    results = client.query(query)
    generate_audio(results)
