import spacy
import yaml
import random
from collections import Counter
nlp = spacy.load("en_core_web_sm")

def read_responses(path = 'responses.yml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)


def get_response(whinge, responses_dict):
    labels = [x.label_ for x in nlp(whinge).ents]
    count = Counter(labels)
    key = count.most_common()[0][0].lower() if len(count.most_common()) > 0 else "general"
    return random.choice(responses_dict.get(key, "general"))


if __name__ == "__main__":
    responses_dict = read_responses()
    print(get_response(input("Whine at me. Lay it on me... I'm listening: "), responses_dict))