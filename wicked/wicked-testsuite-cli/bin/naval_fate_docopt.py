"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -h | --help
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
  --boludo     Boludo Mode.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)


    try:
        # Parse arguments, use file docstring as a parameter definition
        arguments = docopt.docopt(__doc__)

        # Count is a mandatory option, caps is optional
        caps = arguments['--boludo']

            # In the definition, we expect one or more TEXT parameters
            # Each parameter is a word, or a text in quotes: "something like this"
            # If the user forgets about the quote, the program would print only "something"
            # Thus, we merge all the specified parameters with space
        text = ' '.join(arguments['TEXT'])
        if(caps):
            #print text.upper()
            print("Boludo!")
        else:
            print text

    # Handle invalid options
    except docopt.DocoptExit as e:
        print e.message


#def imprime(self):
#    texto = "y vos sos un boludo"

#    return texto