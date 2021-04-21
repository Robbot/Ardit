import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))


def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead. Press Y for yes or N for no: ")
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist. Please double check it"


program_is_running = True

while program_is_running:
    word = input("Enter a word or Q if you want to finish: ").lower()
    if word == "q":
        print("The Program is exiting")
        exit()

    output = translate(word)

    if type(output) == list:
        for item in output:
            n = output.index(item)+1
            print(str(n)+"."+item)
    else:
        print(output)
