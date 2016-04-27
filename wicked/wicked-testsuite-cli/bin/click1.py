import click

@click.command()
@click.option('--list', required=True,  help='List scenarios.')





def list():
    print("It's a list")
    click.echo('Fucking World!')





if __name__ == '__main__':
    list()