# importing modules
import turtle
import pandas

# setting screen and map
map_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)          # adding the image to the screen so that used by turtle object
map_turtle.shape(image)

# loading data file
data_file = pandas.read_csv('50_states.csv')
state_names = data_file.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    # getting answer from user input
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 States correct', prompt="What's another state name ?").title()

    if answer_state == 'Quit':
        missing_states = [state for state in state_names if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    # creating a turtle to goto a particular coordinate
    if answer_state in state_names:
        guessed_state.append(answer_state)
        t = turtle
        t.hideturtle()
        t.penup()
        state_data = data_file[data_file.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)








screen.exitonclick()
