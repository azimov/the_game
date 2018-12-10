from utils import *

click.echo("Entering level 2")
click.pause()

coffee_counter.count = 0

screen(office, [
    "It is the day of your thesis submission",
    "You have 3 hours before you need to submit",
    "But there is a problem",
    "You have lost your only copy!"
])

click.pause()

response = None
wt = 2.0
while response not in ["C", "c"]:
    bg = office
    screen(bg, [
        "What are you going to do?",
        "A: Tweet about it",
        "B: Try to rewrite it from scratch",
        "C: Conduct a ninja spy mission"
    ], wait_time=wt)

    response = click.prompt("Select an action")
    if response in ["A", "a"]:
        screen(bomb, [
            "Your constant use of social media has led the world down a dark path",
            "Following the nuclear war, little is left of humanity"
        ])
        click.secho("Please try again", blink=True)
        exit()
    elif response in ["b", "B"]:
        screen(bg, [
            "there isn't enough coffee in the world to get that done"
        ])
    wt = 0.0

click.clear()

wt = 2.0
response = None

while response not in ["A", "a", "b", "B", "c", "C"]:
    bg = office
    screen(bg, [
        "You dress as sterling Archer, drink 3 cocktails and begin Interrogating the entire SBRC."
        "After an intense investigation you feel that it must be between one of three people.",
        "Who is it?",
        "A: Nigel",
        "B: Thomas",
        "C: Sneaky bitch Nicole"
    ], wait_time=wt)

    response = click.prompt("Select an action")


if response in ["A", "a"]:
    screen(office,
           [
               "It was a bold move accusing Nigel.",
               "But he understands that you were stressed",
               "He actually thinks more of you for having the courage.",
               "Just don't do it again"
           ]
    )

elif response in ["B", "b"]:
    screen(office,
           [
               "Thomas laughs in your face and calls you a bloody stupid idiot",
               "He turns away and goes to get a coffee",
               "It is clear you are no longer friends"
           ]
    )

elif response in ["C", "c"]:
    screen(office,
           [
               "Nicole is in tears",
               "You didn't have to call her a sneaky bitch",
               "She promptly gets drunk and goes full Mansfield",
               "She C bombs the shit out of you until you cry"
           ]
    )
click.pause()
screen(office,
    [
        "As it turns, it was none of these people.",
        "You left it on the tram when you went to Clifton",
        "Thomas calls you a bloody idiot",
        "Somehow, you manage to submit on time."
    ]
)

click.secho("Level 2 complete", blink=True)
click.pause()