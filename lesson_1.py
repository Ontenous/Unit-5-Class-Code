"""
Name: William Nathan
Date: 11/6/24
Topic: Functions
"""
from docutils.nodes import title
from s3fs.utils import title_case


def main():
    def sunny_message():
        print("Sandals would be a great footwear")

    def snowy_message():
        print("On a rainy day, galoshes would be better")

    def rainy_message():
        print("You'll need boots to keep your feet warm!")

    weather = input("What is the weather outside? (sunny, rainy, snowy) ")
    weather = title_case(weather)

    if weather == "Sunny":
        sunny_message()

    elif weather == "Snowy":
        snowy_message()
    elif weather == "Rainy":
        rainy_message()
    else:
        print("Incorrect input, please try again")


#if __name__ == "__main__":
    #main()





