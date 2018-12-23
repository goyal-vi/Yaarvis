import wikipedia

def wikipedia_api():
    input_ = input("Topic: ")
    #input__ = input("Select the output mode: ")
    print(wikipedia.summary(input_))
