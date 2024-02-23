import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Function write the correct answer giving in the appropriate place
def answer_guessed(answer, x_pos, y_pos):
    t = turtle.Turtle()
    t.penup()  # Lift the pen up to move without drawing
    t.goto(x_pos, y_pos)
    font_setup = ("Arial", 10, "normal")  # You can customize the font
    t.write(answer, font=font_setup)
    t.hideturtle()


def capitalize_words(sentence):
    if sentence is not None:
        words = sentence.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
    else:
        return None


def get_user_input(prompt):
    return screen.textinput(title=f"{score}/50 States correct", prompt=prompt)


def over():
    t = turtle.Turtle()
    t.penup()
    t.goto(0, 220)
    t.write(f"GAME OVER !\nStates Guessed : {score}", font=("Courier", 20, "bold"), align="center")
    t.hideturtle()


data = pandas.read_csv("50_states.csv")
game_over = False
score = 0
answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")
# Record the correct guesses
correct_guesses = []

while not game_over:

    # Convert both user input and data to lowercase for case-insensitive comparison
    capitalize_answer_state = capitalize_words(answer_state)

    if capitalize_answer_state == "Exit":
        break

    if capitalize_answer_state in data["state"].values and capitalize_answer_state not in correct_guesses:
        # Keeping track of the score
        score += 1
        correct_guesses += [capitalize_answer_state]
        coordinates = data[data["state"] == capitalize_answer_state]
        x = int(coordinates["x"].iloc[0])
        y = int(coordinates["y"].iloc[0])
        answer_guessed(capitalize_answer_state, x, y)
        answer_state = get_user_input("What's another state name?")
    elif capitalize_answer_state not in data["state"].values:
        game_over = True
        over()
    else:
        answer_state = get_user_input(f"You've already guessed {capitalize_answer_state}!\nTry another state.")

screen.exitonclick()
