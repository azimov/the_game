import click
import time
from utils import processing, check_twitter, office, screen, coffee_counter, scrumpy_bg, scrumpy_echo

title_text = """ 
              _____  ________  ___                
             |  __ \/  ___|  \/  |                
             | |  \/\ `--.| .  . |                
             | | __  `--. \ |\/| |                
             | |_\ \/\__/ / |  | |                
              \____/\____/\_|  |_/                
                                                  
                                                  
 _____ _   _  _____   _____   ___  ___  ___ _____ 
|_   _| | | ||  ___| |  __ \ / _ \ |  \/  ||  ___|
  | | | |_| || |__   | |  \// /_\ \| .  . || |__  
  | | |  _  ||  __|  | | __ |  _  || |\/| ||  __| 
  | | | | | || |___  | |_\ \| | | || |  | || |___ 
  \_/ \_| |_/\____/   \____/\_| |_/\_|  |_/\____/ 

"""

dirs = [
"""
            An SBRC production
""",
"""
        Story by James Gilbert, 
                Nicole Pearcy 
                    and Vanisha Patel
""",
"""
        A tale of love, loss, betrayal and ...
""",
"""
                     GROWTH.
""",
]


for d in dirs:
    click.clear()
    click.secho(
        title_text,
        blink=True,
        color="red",
    )
    click.secho(d)
    time.sleep(3)

click.pause()

click.clear()

processing("Loading...")

name = click.prompt("Please enter your name")

click.clear()

click.secho("Hello {}, welcome to genome scale modelling the game. A game about genome scale modelling. \n".format(name) +
            "My name is JOSHUA I am the FRIENDLY AI sent to help you LEARN.")

time.sleep(3)

mood = click.prompt("How are you feeling today?")

processing()

click.clear()
click.pause()

click.clear()
click.secho("Sorry for the delay. Unfortunatley, due to budget cuts EMPATHY was not included in my programming. ")
click.secho("My programmers sincerely hopes that {} is not one of the bad emotions".format(mood))

time.sleep(2)
click.echo("\n\n")

click.secho("This game is a text based adventure game. It requires dedication and involves FULL ROLEPLAY")
answer = click.prompt("Are you prepared to accept everything that this entails?")

while answer not in ["Yes", "yes", "y", "Y", "YES"]:
    click.clear()
    answer = click.prompt("Are you prepared to accept everything that this entails?")

click.secho("Excellent. This constitutes your informed consent.")
click.pause()
click.clear()

click.secho(office)
click.secho("It is early in the morning.")
time.sleep(2)
click.secho("11:30am.")
time.sleep(2)
click.echo("Tired and groggy, you have arrived at your desk.")
time.sleep(2)
click.echo("For some reason you are wearing a yellow shirt.")
time.sleep(2)
click.echo("Your thesis is due in 2 weeks.")
click.pause()

click.clear()
click.secho(office)
time.sleep(3)

click.secho("You have been tasked with the process of building a model for the organism Clostridum autoethanogenum")
time.sleep(2)
click.secho("In a moment this text will disappear and you will be asked to spell 'autoethanogenum'")
time.sleep(5)
autoethanogenum = ""


click.clear()

click.secho(office)
autoethanogenum = click.prompt("How do you spell 'autoethanogenum'?")
processing("Checking spelling...")
screen(office, [], 0)
processing("Loading database...")
screen(office, [], 0)
processing("Performing string equivalence test...")
screen(office, [], 0)
if autoethanogenum != "autoethanogenum":
    click.secho("It might be a hard life {}".format(name))
else:
    click.secho("Good job.")

time.sleep(2)
click.clear()

response = None
wt = 2.0
while response not in ["A", "a"]:

    screen(office, [
        "An email marked 'high importance' has arrived in your inbox. What do you do?",
        "A: Open the email",
        "B: Check twitter",
        "C: Get a coffee"
    ], wait_time=wt)

    response = click.prompt("Select an action")

    if response in ["B", "b"]:
        check_twitter(office)
        click.pause()

    elif response in ["C", "c"]:
        coffee_counter.add_count(office)

    wt = 0.0

click.clear()

click.secho(office)
click.echo("You see an email of high importance sent to your inbox")
click.pause()
processing("Loading email...")
click.clear()
processing("Setting fonts...")
click.clear()
processing("Adjusting text...")
click.clear()
click.secho("""
Dear {},

We really need you to get on with your important science.
Today we have found an emergency in our bioreactor that requires a genome scale model to solve.
The level of carbon monoxide in the system is too high and we're scared she's gonna blow.

Unfortunately our last modeller died trying to save us. 
She was working on a really important problem.

What is the expected growth rate of C aceto when growing on glucose?

Yours scincerely,
Sean Sampson
LanzarTak

""".format(name))

click.pause()

response = None
wt = 2.0
while response not in ["A", "a"]:

    screen(office, [
        "Wow. Looks like you can't ignore this issue.",
        "What do you do?",
        "A: Enter scrumpy to find the solution",
        "B: Check twitter",
        "C: Get a coffee"
    ], wait_time=wt)

    response = click.prompt("Select an action")

    if response in ["B", "b"]:
        check_twitter(office)
        click.pause()

    elif response in ["C", "c"]:
        coffee_counter.add_count(office)

    wt = 0.0

click.secho(office)
click.echo("You are now about to enter the ScrumPy metabolic simulation simulator...")
click.secho("If you thought things were nerdy before...", blink=True)
click.pause()
click.clear()


# Get exact growth rate of C auto on glucose
response = None
wt = 2.0
while response not in ["A", "a"]:
    bg = scrumpy_bg.format(" ")
    screen(bg, [
        "You are in the  scrumpy simulator",
        "What do you do?",
        "A: Load model",
        "B: Check twitter",
        "C: Get a coffee"
    ], wait_time=wt)

    response = click.prompt("Select an action")

    if response in ["B", "b"]:
        check_twitter(bg)
        click.pause()

    elif response in ["C", "c"]:
        coffee_counter.add_count(bg)

    wt = 0.0

click.clear()
scrumpy_echo("load_model()")

response = None
wt = 2.0
while response not in ["A", "a"]:
    bg = scrumpy_bg.format("load_model()")
    screen(bg, [
        "You are in the  scrumpy simulator",
        "What do you do next?",
        "A: Set growth media and calculate growth rate",
        "B: Check twitter",
        "C: Get a coffee"
    ], wait_time=wt)

    response = click.prompt("Select an action")

    if response in ["B", "b"]:
        check_twitter(bg)
        click.pause()

    elif response in ["C", "c"]:
        coffee_counter.add_count(bg)

    wt = 0.0

click.echo("""
>> Infeasible
""")

response = None
wt = 2.0
blag = True
while response not in ["A", "a"]:

    screen(office, [
        "Looks like scrumpy is broken but you need an answer fast",
        "What do you do?",
        "A: Blag an answer",
        "B: Check twitter",
        "C: Get a coffee",
        "D: Try and get it working"
    ], wait_time=wt)

    response = click.prompt("Select an action")

    if response in ["B", "b"]:
        check_twitter(office)
        click.pause()

    elif response in ["C", "c"]:
        coffee_counter.add_count(office)

    elif response in ["D", "d"] and coffee_counter < 3:
        screen(office, [
            "You struggle to summon the motivation to work again",
            "Maybe coffee would help"
            ]
        )

        click.pause()
    elif response in ["D", "d"] and coffee_counter.count >= 3:
        screen(office, [
            "Again you load up the simulator",
            "You realise that your scrumpy spy file is broken",
            "Fixing this you get the answer"
            ]
        )
        scrumpy_echo("m.Solve()")
        click.echo("0.03")
        blag = False

    wt = 0.0

screen(office, ["You decide to send that email"])

if blag:
    pass
else:
    pass


# Error in code

# Fix bug, run again

# Send email - response
# "You saved the field of production of small quantities of solvents made from waste gasses in china"
# "good job"

# Kobashi mayru


protein = """
MSILNVKNVNHGFGDRAIFEDVSFRLLKGEHVGLVGANGEGKSTFMSIITGKLMPDEGTIEWSNNVRVGYMDQHASLQKG
KTIKDVLKDAFKYLFDMEANMMEITDKMAEASEDELQKLLDEMGTIQDTLDNNDFYVIDVKIEEVAKGLGITDIGLDKDV
ADLSGGQRTKVLLAKLLLQKPDILLLDEPTNYLDEVHIEWLKRYLNDFENAFILISHDIPFLNSVINVIYHIDNRKLTRY
AGDYDNFMRVYEANKKQVEAAYERQQQEIAKLKDFVARNKARVATTGMARARQKQLDKMDIIEKTQEKPKPEFNFKTART
SGKLIFETKDLVVGYDSPLSKPLNLTMERGQKIALVGANGLGKTTLLKSLLGKIKPISGDVELGDYQYIGYFEQEIKEAN
DKTCIEEVWEEFPAYTQYEVRAALAKCGLTTKHIESKVMVLSGGEQAKVRLCKLINNETNILILDEPTNHLDVDAKDELK
RALKEYRGSILLVCHEPEFYKDVVTDVWNCEEWTTKIY
"""

click.echo("Its a good thing you're here")
time.sleep(2)
click.echo("In a moment you will be shown a protein sequence that you have to identify.")
time.sleep(2)

click.clear()
click.echo(protein)
time.sleep(3)
click.clear()
gene_name = click.prompt("Name the gene")

screen(office, [])
processing("Checking gene name...")
screen(office, [])
processing("Loading NCBI blast...")
screen(office, [])
processing("Querying server...")
screen(office, [])
processing("Validating response...")

time.sleep(3)
click.secho("Actually, Its probably not that important. Lets just move on.")

click.secho("Level one complete.", blink=True)
click.pause()
click.clear()

import nicole
import vanisha
import credits