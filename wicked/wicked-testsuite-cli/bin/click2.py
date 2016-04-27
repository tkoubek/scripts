import click


@click.command()
@click.option("--number",
              required=True,
              type=click.INT,
              help="print different output")
@click.option("--choice",
              type=click.Choice(['this', 'that']),
              help="print different output")
@click.option("--test", help="print different output")

def cli(number, choice, test):
    """Argument parsing example"""

    if test:
        print("Just testing, move along...")
    else:
        print("This is fo'realz!")

    if choice == 'this':
        print("Selected this")
    elif choice == 'that':
        print("Selected that")

    print("This is a number: %d" % number)