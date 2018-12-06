import click
import time
from tqdm import tqdm
import random


def processing(text="Processing..."):
    click.secho(text, blink=True)
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


office ='''
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \                             | 
|     /  %%%%%%%%%%%%%%  \                            | 
|     ^^^^^^^^^^^^^^^^^^^^                            | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

'''