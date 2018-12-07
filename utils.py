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


def check_twitter(screen=None):
    """
    For when the user selects to check twitter instead of getting to work
    :return:
    """

    if screen is not None:
        click.clear()
        click.echo(screen)

    tweets = [
        """"
        @KanyeWest
        Mark Zuckerberg invest 1 billion dollars into Kanye West Ideas
        """,
        """"
        @KanyeWest
        I hate when I'm on a flight and I wake up with a water bottle next to me like oh 
        great now I gotta be responsible for this water bottle
        """,

        """
        @ ShaneWarne
        When I turned 36 I realised - the likelihood is that in four years time I'll be 40.
        """

        """
        @ Morty
        I wish that incest porn had a more mainstream audience. You know, for a friend.
        """
    ]

    click.echo(random.choice(tweets))


def screen(background, text, wait_time=2.0):

    click.clear()
    click.echo(background)
    for t in text:
        click.echo(t)
        time.sleep(wait_time)


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

bomb = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
"""
