import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def heading():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


random_number = random.randint(0, 9)
print(random_number)


@app.route("/<int:number>")
def match_the_number(number):
    print(random_number)
    if number == random_number:
        return ("<h1 style='color: green'>You found me! 🙂<h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWgyMnVqd2pxZnphZzc4djEwMGg1NzV2cD"
                "FheW1pY2g4N3pteXZsMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/t3sZxY5zS5B0z5zMIz/giphy"
                "-downsized-large.gif'>")
    elif number < random_number:
        return ("<h1 style='color: red'>Too low, try again! 🤔</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExazdxend5eGowbTI5N3BlejZ0bXJreW1idDNhZzdycj"
                "Azdzg0OTk4OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MZQkUm97KTI1gI8sUj/giphy.gif'>")
    else:
        return ("<h1 style='color: blueviolet'>Too high, try again! 🤔</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXBwY2I0b3doNjljeHBrbjd2YWg5MGw1NHZien"
                "B4ZGVidmh6YWdjMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3D4HBmyRdlPotgeZbu/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)
