from utils import *


def screen(background, text, wait_time=2.0):

    click.clear()
    click.echo(background)
    for t in text:
        click.echo(t)
        time.sleep(wait_time)


screen(office, ["Hello this is Joshua"])
click.pause()
screen(office, [])
conf = click.confirm("Would you like to play a game?", default=True)

if not conf:
    screen(office, ["You have selected GLOBAL THERMO NUCLEAR WAR"])
    click.pause()

    screen(bomb, [
            "Nuclear war has ravaged the earth for nearly three decades",
            "Nobody knows how  or why the first bomb was dropped.",
            "You are one of the few remaining humans",
            ])
    click.pause()
    screen(bomb,
           ["The machines have lost.", "We are near there final base",
            "However, we have reason to believe that they are plotting something big"]
    )

screen(office,[])
processing("Loading...")