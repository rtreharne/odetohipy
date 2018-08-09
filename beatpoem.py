"""
This code has been adapted from the original blog article published by Elliot Hauser. https://blog.trinket.io/writing-poetry-in-python/
"""

from random import choice, randint
import pyttsx3;

class Poem:

    def __init__(self):
        self.adjectives = "create striving excite learning radiant bright ecstatic young adaptable driving running joining".split()
        self.verbs = "explores inspires imagines returns wriggles grows stares drives smiles raps".split()
        self.nouns = "life science art confident data beauty research impact knowledge Python all Bees Beekeepers HiPy Liverpool code skill community September keyboard wifi honey sky sunlight".split()
        self.poem = self.beat_poem()

    def print_poem(self):
        print(self.poem)

    def beat_poem(self):

        poem = ""

        for x in range(randint(2,2)):
            words1 = " ".join([choice(self.adjectives) + ", ", choice(self.adjectives)])
            words2 = " ".join([choice(self.nouns), choice(self.verbs)])
            words3 = " ".join([choice(self.nouns), choice(self.nouns), choice(self.adjectives), choice(self.nouns)])


            for i in range(randint(2,4)):
                words = choice([words1, words2, words3])
                line = " "*randint(0, 40 - len(words)) + words
                poem += line + "\n"



                if x % 7 ==0:
                    words4 = " ".join(["the " + choice(self.adjectives), choice(self.nouns), choice(self.verbs)])
                    #poem += " ".join(words4) + "\n"
                    poem += words4 + "\n"


                if x % 3 ==0:

                    poem += choice(self.nouns) + "\n"
                    poem += ""*5 + choice(self.nouns) + "\n"
                    poem += " "*5 + "the " + choice(self.nouns) +"!" + "\n"

        return poem

    def speak(self):

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 100)
        engine.setProperty('voice', voices[2].id)
        engine.say(self.poem)
        engine.runAndWait()

if __name__ == "__main__":
    poem = Poem()
    print(poem.poem)
    poem.speak()
