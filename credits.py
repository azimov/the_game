import click
import time
from pygame import mixer
import os

if os.path.exists("baby.mp3"):
    mixer.init()
    mixer.music.load("baby.mp3")
    mixer.music.play()

SPEED = 0.5

click.echo("""

        Congratulations on making it to the end you have been awarded the rank of:
                                
                                DOCTOR

""")

click.echo(
    """
        GSM the game is an SBRC production.
        
    """
)
for i in range(100):
    click.echo()

with open("credits.txt") as credits:
    for line in credits:
        print(line + " ")
        time.sleep(SPEED)


click.pause()
