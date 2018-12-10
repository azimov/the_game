from utils import *

click.echo("Entering level 3")
time.sleep(2)

screen(office,
    [
        "It is the day of your viva.",
        "You have to leave to get to get there but there is a problem",
        "Your colleagues are distracting you...",
    ]
)
click.pause()

wt = 2.0
response = None


bg = office
screen(cat, [
    "A wild Vanisha appears",
    "How do you get passed?",
    "A: Tell her to go home for a nap",
    "B: Suggest a Trip to nandos",
    "C: Distract her with booze"
], wait_time=wt)

response = click.prompt("Select an action")

screen(cat, ["It turns out it was just an illusion", "She was never really at work."])
click.pause()


wt = 2.0
response = "B"

while response in ["B", "b"]:
    screen(horse, [
        "Nicole is feeling chatty",
        "You need to get passed before the time runs out",
        "What do you do?"
        "A: Tell her there is a new flavour of crisp in the vending machine",
        "B: Throw chocolate at her",
        "C: Give here your tinder to play with"
    ], wait_time=wt)


    response = click.prompt("Select an action")
    wt =0.0

    if response in ["B", "b"]:
        screen(horse, ["It doesn't work", "She eats the chocolate too fast"])
        click.pause()

screen(horse, ["It works, you manage to slip away"])

screen(moose, [
    "Shit, James in the way",
    "He never gets distracted... Right!?",
    "What do you do?",
    "A: Show him a Youtube video",
    "B: Ask him to check the cricket score",
    "C: Mention Brexit and try to leave while he rants."
], wait_time=wt)

response = click.prompt("Select an action")

screen(moose, ["Yeah, that was pretty easy"])
click.pause()

screen(fish, [
    "You have peaked Thomas' attention",
    "What do you do?",
    "A: Suggest getting a coffee",
    "B: Mention that Claudio asked a Thermodynamics question",
    "C: Say that Vanisha wants running tips"
], wait_time=wt)

response = click.prompt("Select an action")

screen(fish, ["It works", "Finally, you can get to your Viva!"])
click.pause()
click.clear()
processing("Awaiting viva result...")
processing("Checking with external examiner...")

screen(fireworks,
       ["CONGRATULATIONS! You did it", "Somehow"]
)
click.pause()