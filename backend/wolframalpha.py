import wolframalpha
from backend.recognize_generate import *
from backend.exceptions import *


def wolfram_search_query(query):
    """
    The Wolfram Search Query function implements the Wolfram API based on a uniquely generated
    App ID that is unique to the AIVA core program.  The API serves as a backend to making search
    queries primarily based on calculations and number computations that would be difficult to
    process within the program itself.  Outsourcing this computation provides faster service
    that returns more accurate answers.

    :param query: The query input by the user
    """

    try:
        client = wolframalpha.Client('JUT65U-PHRVWRHQTH')

        results = client.query(query)
        if results.get('@success'):
            result_expression = results.get('pod')[0].get('subpod').get('plaintext')
            answer = result_expression.split(' = ')[1]
            generate_audio(answer)
            return
        else:
            raise WolframReturnedVoid
    finally:
        raise WolframInvalidClient
