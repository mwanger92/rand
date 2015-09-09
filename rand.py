import random, sys, os
from shutil import move
from optparse import OptionParser
games = []
f = open("games.txt", "r+")
for line in f:
    games.append(line)
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
    newGames = open ("newGames.txt", "w+")
    print "What game?"
    game = raw_input()
    found = False
    for g in games:
        if g == game+"\n":
            found = True
        else:
            newGames.write(g)
    if found:
        print game + " was deleted"
        os.remove("games.txt")
        move("newGames.txt", "games.txt")
    else:
        print game + " not found"

def add():
    print "What game?"
    game = raw_input()
    f.write(game)
    f.write("\n")

def show():
    print games

main(sys.argv[1:])
