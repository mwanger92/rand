import os, json, sys
from tempfile import mkstemp
from shutil import move
from optparse import OptionParser
from pprint import pprint

rpgMeOld = open('rpgMe.txt', 'r+')
skills = {'str', 'dex', 'con', 'int', 'cha'}
def main(argv):
  if os.stat('rpgMe.txt').st_size == 0:
    print "Insert Name"
    name = raw_input()
    newSkills(name)
  else:
      parser = OptionParser()
      parser.add_option("-s", "--stats", action="store_true", default=False, dest="stats",
                        help="are you looking for your stats")
      parser.add_option("-e", "--edit", action="store_true", default=False, dest="edit",
                        help="edit your stats")
      (options, args) = parser.parse_args(sys.argv[1:])

      if options.stats:
          stats()
      elif options.edit:
          oldSkills()
      else:
          print "Please use any of the options -s or -e"

def stats():
    for line in rpgMeOld:
        my_dict = json.loads(line)
        print "Which stat would you like to see?"
        ans = raw_input()
        if ans != 'ac' and ans != 'cha' and 'a' in ans:
            pprint(my_dict)
        else:
            if ans in my_dict['obj']:
                pprint(my_dict['obj'][ans])
            pprint(my_dict[ans])

def oldSkills():
  newRpgMe = open('newRpgMe.txt', 'w+')
  print "Which Skill Will Be Changed"
  skiller = raw_input()
  for line in rpgMeOld:
    if skiller in line:
      if skiller in skills:
        print "What would you like to change " + skiller + " to?"
        value = raw_input()
        # Int = False
        # if not skiller == 'obj' and value:
        #     while not Int:
        #         print "Invalid value insert " + skiller
        #         value = raw_input()
        #         if value is int:
        #             print "hello"
        #             Int=True
        my_dict = json.loads(line)
        my_dict[skiller] = value
        print my_dict
        rpgMe = json.dumps(my_dict)
        newRpgMe.write(rpgMe)
      elif skiller == 'lvl':
        print "Congrats on leveling up!"
        my_dict = json.loads(line)
        my_dict[skiller] += 1
        print my_dict
        rpgMe = json.dumps(my_dict)
        newRpgMe.write(rpgMe)
      elif skiller == 'arc' or skiller == 'gld' or skiller == 'obj' or skiller == 'hp':
        if skiller == 'obj':
            print "Are you removing an object?"
            ans=raw_input()
            if 'y' in ans:
                print "ok"
                obj = {}
            elif 'n' in ans:
                print "Insert number of perks the object affects"
                num = int(raw_input())
                for j in range(0, num):
                    print "Insert the name of the perk"
                    name = raw_input()
                    print "Insert the affect on that perk"
                    stat = raw_input()
                    obj={'name':value, name:stat}
            my_dict = json.loads(line)
            my_dict[skiller] = obj
            print my_dict
            rpgMe = json.dumps(my_dict)
            newRpgMe.write(rpgMe)
        else:
            print "What would you like to add to " + skiller + "?"
            value = raw_input()
            # if not skiller == 'obj' and int(value):
            #     Int = False
            #     while not Int:
            #         print "Insert " + skiller
            #         value = raw_input()
            #         if int(value):
            #             Int=True
            my_dict = json.loads(line)
            my_dict[skiller] += value
            print my_dict
            rpgMe = json.dumps(my_dict)
            newRpgMe.write(rpgMe)
    else:
      newRpgMe.write(line)
  os.remove("rpgMe.txt")
  move("newRpgMe.txt", "rpgMe.txt")

def newSkills(name):
  info = {'str', 'dex', 'con', 'int', 'cha', 'lvl', 'ac', 'gld', 'obj', 'hp', 'city'}
  for i in info:
    print "Insert " + i
    value = raw_input()
    # print int(value)
    # if not i == 'obj' and int(value):
    #     Int = False
    #     while not Int:
    #         print "Insert " + i
    #         value = raw_input()
    #         if int(value):
    #             Int=True
    if i=='str':
        stre=value
    elif i=='dex':
        dex=value
    elif i=='con':
        con=value
    elif i=='int':
        inte=value
    elif i=='cha':
        cha=value
    elif i=='lvl':
        lvl=value
    elif i=='arc':
        arc=value
    elif i=='gld':
        gld=value
    elif i=='ac':
        ac=value
    elif i=='obj':
        print "Insert number of perks the object affects(right now only 1)"
        # num = int(raw_input())
        num = 1
        for j in range(0, num):
            print "Insert the name of the perk"
            perk = raw_input()
            print "Insert the affect on that perk"
            stat = raw_input()
            obj={'name':value, perk:stat}
    elif i=='hp':
        hp=value
    elif i=='city':
        city=value

  rpgMe = json.dumps({'name':name, 'str':stre, 'dex':dex, 'con':con, 'int':inte, 'cha':cha, 'city':city, 'hp':hp, 'obj':obj, 'ac':ac, 'gld':gld, 'lvl':lvl})
  rpgMeOld.write(rpgMe)

main(sys.argv[1:])
