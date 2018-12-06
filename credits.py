import click
import time

click.echo(
    """
        GSM the game is an SBRC production.
        
    """
)
for i in range(100):
    click.echo()

with open("credits.txt") as credits:
    for line in credits:
        click.echo(line)
        time.sleep(0.6)


click.pause()