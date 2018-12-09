from utils import *

response = None
wt = 2.0
while response not in ["A", "a"]:

    screen(scrumpy_bg.format(" "), [
        "You are in the  scrumpy simulator",
        "What do you do?",
        "A: Load model",
        "B: Check twitter",
        "C: Get a coffee"
    ], wait_time=wt)

    response = click.prompt("Select an action")

    if response in ["B", "b"]:
        check_twitter(scrumpy_bg.format(" "))
        click.pause()

    elif response in ["C", "c"]:
        coffee_counter.add_count(scrumpy_bg.format(" "))

    wt = 0.0

scrumpy_echo("load_model()")

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