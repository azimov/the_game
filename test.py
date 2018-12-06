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

screen(office,[])
processing("Loading...")
