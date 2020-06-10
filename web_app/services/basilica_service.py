# web_app/services/basilica_service.py



from basilica import Connection
import os
import basilica
from dotenv import load_dotenv


load_dotenv() # parse the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

connection = Connection(BASILICA_API_KEY)
print(type(connection))

#def basilica_api_client():
#    return basilica.Connection(BASILICA_API_KEY)


if __name__ == "__main__":
    
    embedding = connection.embed_sentence("HELLO WORLD")
    print(embedding) #>
    
    sentences = [
        "This is a sentence!",
        "This is a similar sentence",
        "I don't think this sentence is a very similar at all...",
    ]

    print(type(connection)) #> <basilica.Connection object at 0x102081b10>

    embeddings = list(connection.embed_sentences(sentences))
    for embed in embeddings:
        print("----------")
        print(embed) #> a list with 768 floats from -1 to 1
    # print(list(embeddings)) # [[0.8556405305862427, ...], ...]
