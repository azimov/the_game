import click
import time
from tqdm import tqdm
import random
import sys


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
        """
        @KanyeWest
        Mark Zuckerberg invest 1 billion dollars into Kanye West Ideas
        """,

        """
        @KanyeWest
        I hate when I'm on a flight and I wake up with a water bottle next to me like oh 
        great now I gotta be responsible for this water bottle
        """,

        """
        @ ShaneWarne
        When I turned 36 I realised - the likelihood is that in four years time I'll be 40.
        """,

        """
        @ Morty
        I wish that incest porn had a more mainstream audience. You know, for a friend.
        """,

        """
        @DonaldTrump
        Despite the negative press covfefe
        """,

        """
        @ConnorMcGreggor
        These custom-made suits aren’t cheap. This solid gold pocket watch, three people died making this watch.
        I need to put people away.
        I need those big fights. I’m going to end up in debt pretty fast.
        """
    ]

    choice = random.randint(0, len(tweets) -1)
    click.echo(tweets[choice])


def screen(background, text, wait_time=2.0, clear=True):

    if clear:
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

scrumpy_bg = """
>> {}









"""


def scrumpy_echo(command):
    print("\n>> ", end="")
    for char in command:
        wait = random.uniform(0, 0.5)
        print(char, end="")
        sys.stdout.flush()
        time.sleep(wait)
    screen(scrumpy_bg.format(command), [], 0)


class CoffeCounter(object):

    def __init__(self, limit=10):
        self.count = 0
        self.limit = limit

    def add_count(self, disp_screen):
        self.count += 1

        if self.count > self.limit:
            screen(bomb, [
                "You drank too much coffee.",
                "You have died.",
                "Because you did not lived to pass on your knowledge, much of humanity perished in a nuclear holocaust"
            ])
            click.pause()
            screen(bomb, [
                "Thankfully, this was only a simulation",
                "Just try to be more careful next time.",
                "Please go back and try again",
            ])
            click.pause()

            exit()



        screen(disp_screen,
            [
            "You have had {} coffees today.".format(self.count),
            "This makes you work faster, but remember drinking too much coffee will end badly"
            ], 0
        )
        click.pause()

coffee_counter = CoffeCounter()