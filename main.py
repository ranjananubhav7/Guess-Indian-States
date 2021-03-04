import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian states game")
image = "ezgif.com-gif-maker.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("31_states.csv")
states = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

score = 0

while score < 31:
    user_answer = screen.textinput(title=f"{score}/31 correct states", prompt="What is the name of another state")
    if user_answer in states:
        score += 1
        x1 = x_cor[states.index(user_answer)]
        y1 = y_cor[states.index(user_answer)]

        new_state = turtle.Turtle()
        new_state.up()
        new_state.hideturtle()
        new_state.goto(x1, y1)
        new_state.write(user_answer, align="center", font=("Arial", 8, "normal"))

    else:
        print("not present")

screen.exitonclick()
