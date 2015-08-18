import sys, json
from pprint import pprint
from optparse import OptionParser
npcs = open('npcs.txt', 'r+')
def main(argv):
    parser = OptionParser()
    parser.add_option("-p", "--people", action="store_true", default=False, dest="people",
                      help="are you looking for a person")
    parser.add_option("-c", "--city", action="store_true", default=False, dest="place",
                      help="are you looking for a city")
    parser.add_option("-e", "--edit", action="store_true", default=False, dest="edit",
                        help="edit your stats")
    (options, args) = parser.parse_args(sys.argv[1:])

    if options.people:
        people()
    elif options.place:
        city()
    elif options.edit:
        edit()
    else:
        print "Please use any of the options -p or -c or -e"

def city():
    print "Insert City"
    city = raw_input()
    print "Are you looking for anyone in particular?"
    answer = raw_input()
    if 'y' in answer:
        print "Who?"
        name = raw_input()
        for line in npcs:
            if name in line:
                print line
    elif 'n' in answer:
        for line in npcs:
            if city in line:
                print line

def edit():
    npcs = open('npcs.txt', 'r+')
    for line in npcs:
        my_dict = json.loads(line)
        print my_dict['name']
    print "Who would you like to edit?"
    answer = raw_input()
    npcs = open('npcs.txt', 'r+')
    for line in npcs:
        my_dict = json.loads(line)
        if answer in my_dict['name']:
            print "What would you like to edit?"
            stat=raw_input()
            print stat

def people():
    print "Insert Name"
    name = raw_input()
    print "Insert City"
    city = raw_input()
    tester = name + "," + city
    npc_names=[]
    npcs_list=[]
    for line in  npcs:
        my_dict=json.loads(line)
        npc_names.append(my_dict["name"] + "," + my_dict["city"])
        npcs_list.append(my_dict)

    if tester in npc_names:
        print name + ' already exists in ' + city
        print npcs_list[npc_names.index(tester)]
    else:
        newSkills(name, city)

def newSkills(name, city):
    skills = {'str', 'dex', 'con', 'int', 'cha', 'hp', 'ocu'}
    for skill in skills:
        print "Insert " + skill
        value = raw_input()
        if skill=='str':
            str = value
        elif skill=='dex':
            dex = value
        elif skill=='con':
            con = value
        elif skill=='int':
            int = value
        elif skill=='cha':
            cha = value
        elif skill=='hp':
            hp = value
        elif skill=='ocu':
            ocu = value
    npc = json.dumps({'name':name, 'str':str, 'dex':dex, 'con':con, 'int':int, 'cha':cha, 'city':city, 'hp':hp, 'ocu':ocu})
    npcs.write(npc)
    npcs.write('\n')

main(sys.argv[1:])
