import click
import time
from tqdm import tqdm
import random

import numpy as np
import gnuplotlib as gp


def processing():
    click.secho("Processing...", blink=True)
    for _ in tqdm(range(100)):
        time.sleep(0.1 * random.random())


def get_multichoice(question, choices):
    """
    :param question: string
    :param choices: list of choices
    :return:
    """
    click.secho(question)
    for i, choice in enumerate(choices):
        click.secho("{} : {}".format(i, choice))

    response = click.prompt("Select your answer : ")
    return response


def check_twitter():
    """
    For when the user selects to check twitter instead of getting to work
    :return:
    """
    tweet = ""
    click.echo(tweet)



title_text = """ 

"""

time.sleep(5)
click.clear()


click.secho(
    title_text,
    blink=True,
    color="red",
)

name = click.prompt("Please enter your name")

click.clear()

click.secho("Hello {}, welcome to genome scale modelling the game. A game about genome scale modelling. \n".format(name) +
            "My name is COMPUTER 43 I am the benevolent AI sent to help you learn.")

time.sleep(3)

mood = click.prompt("How are you feeling today?")

processing()

click.clear()

click.secho("Sorry for the delay. Unfortunatley, due to budget cuts EMPATHY was not included in my programming. " +
            "My programmers sincerely hopes that {} is not one of the bad emotions".format(mood)
)
time.sleep(2)
click.echo("\n\n")

click.secho("This game is a text based adventure game. It requires dedication and involves FULL ROLEPLAY")
answer = click.prompt("Do you understand what this means?")

while answer not in ["Yes", "yes", "y", "Y", "YES"]:
    click.clear()
    click.secho("Hmmm, it seems that you are capable of replying and yet too stupid to play this game. \n")
    answer = click.prompt("Do you understand what this means?")

click.secho("Good, I am glad that you are willing to commit yourself to this task.")
time.sleep(3)
click.clear()

click.secho("It is early in the morning. 11:30am. \n"
            "You have arrived at your desk.")
time.sleep(5)
click.clear()

click.secho('''


::::==========:::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::=========::::::.---------------.:::::::::::::::::::::::::::::::
:::=============::::::| .-----------. |:::::::::::::::::::::::::::::
::::==========::::::::| | === == == | |:::::::::::::::::::::::::::::::::
::::==========::::::::| | 260 ED OO | |:::::::::::::::::::::::::::::::
:::::::=========='::::| |  urgent!  | |:::::::::::::::::::::::::::::
:::===========::::::::| |___________| |::::::((;):::::::::::::::::::::
""""============""""""|___________oo__|"")"""";(""""""""""""""""""""""
  ==========='           ___)___(___,o  (   .---._
     ===========        |___________| 8  \  |TEA|_)    .+-------+.
  ===========                     o8o8    ) |___|    .' |_______| `.
    =============      __________8___    (          /  /         \  \
 |\`==========='/|   .'= --------- --`.   `.       |\ /           \ /|
 | "-----------" |  / ooooooooooooo  oo\   _\_     | "-------------" |
 |______I_N______| /  oooooooooooo[] ooo\  |=|     |_______OUT_______|
                  / O O =========  O OO  \ "-"   .-------,
                  `""""""""""""""""""""""'      /~~~~~~~/
_______________________________________________/_   ~~~/_______________


''')
time.sleep(3)
click.clear()

click.secho("You have been tasked with the process of building a model for the organism Clostridum autoethanogenum")
click.secho("In a moment this text will disappear and you will be asked to spell 'autoethanogenum'")
time.sleep(5)
autoethanogenum = ""


click.clear()

autoethanogenum = click.prompt("How do you spell 'autoethanogenum'?")
processing()

if autoethanogenum != "autoethanogenum":
    click.secho("It might be a hard life {}".format(name))
else:
    click.secho("Good job.")

time.sleep(2)


