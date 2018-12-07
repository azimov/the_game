import click
import time
from utils import processing, check_twitter, office

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

dirs = ["""
        Directed by James Gilbert
""",
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
"""
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

click.secho("Good, I am glad that you are willing to commit yourself to this task.")
time.sleep(3)
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
processing()

click.clear()
click.secho(office)

if autoethanogenum != "autoethanogenum":
    click.secho("It might be a hard life {}".format(name))
else:
    click.secho("Good job.")

time.sleep(2)

click.secho("Level one complete.", blink=True)
click.pause()
click.clear()

click.secho(office)
click.echo("You are now about to enter the ScrumPy metabolic simulation simulator...")
click.pause()
click.clear()


protein = """
MSILNVKNVNHGFGDRAIFEDVSFRLLKGEHVGLVGANGEGKSTFMSIITGKLMPDEGTIEWSNNVRVGYMDQHASLQKG
KTIKDVLKDAFKYLFDMEANMMEITDKMAEASEDELQKLLDEMGTIQDTLDNNDFYVIDVKIEEVAKGLGITDIGLDKDV
ADLSGGQRTKVLLAKLLLQKPDILLLDEPTNYLDEVHIEWLKRYLNDFENAFILISHDIPFLNSVINVIYHIDNRKLTRY
AGDYDNFMRVYEANKKQVEAAYERQQQEIAKLKDFVARNKARVATTGMARARQKQLDKMDIIEKTQEKPKPEFNFKTART
SGKLIFETKDLVVGYDSPLSKPLNLTMERGQKIALVGANGLGKTTLLKSLLGKIKPISGDVELGDYQYIGYFEQEIKEAN
DKTCIEEVWEEFPAYTQYEVRAALAKCGLTTKHIESKVMVLSGGEQAKVRLCKLINNETNILILDEPTNHLDVDAKDELK
RALKEYRGSILLVCHEPEFYKDVVTDVWNCEEWTTKIY
"""

click.echo("In a moment you will be shown a protein sequence. That you have to identify.")
time.sleep(2)
click.clear()
click.echo(protein)
time.sleep(2)
click.clear()
gene_name = click.prompt("What is the name of this gene?")

click.echo("")

import nicole
import vanisha
import credits