import random
from optparse import OptionParser
games = []
f = open("games.txt", "r+")
for line in f:
    games.append(line)
print games
def main(argv):
    parser = OptionParser()
    parser.add_option("-d", "--delete", action="store_true", default=False, dest="delete",
                      help="Delete game from the list")
    parser.add_option("-s", "--show", action="store_true", default=False, dest="show",
                      help="Show all games in the list")
    parser.add_option("-a", "--add", action="store_true", default=False, dest="add",
                      help="Add a game to the list")
    (options, args) = parser.parse_args(sys.argv[1:])

    if options.delete:
        delete()
    elif options.show:
        show()
    elif options.add:
        add()
    else:
        pick()

def pick():
    print games[random.randint(1,len(games))]

def delete():
    print "What game?"
    game = raw_input()
    print game

def add():
    print "What game?"
    game = raw_input()
    games.write(game)
    games.write("\n")

def show():
    print games