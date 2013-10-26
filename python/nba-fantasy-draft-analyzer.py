#! /usr/bin/python

def parse_espn():
    f_in = open('espn.txt')
    f_out = open('espn-players.txt', 'w')
    pick_num = 1;
    expert_map = {}
    expert_list = []
    for line in f_in:
        if line.startswith("<td><a href=\"javascript:newWin"):
            name = line.split(">")[2].split("<")[0]
            out_line = "%d %s" % (pick_num, name)
            #print(out_line)
            f_out.write(out_line + "\n")
            expert_map[name] = pick_num
            expert_list.append(name)
            pick_num += 1
            #raw_input()
    f_in.close()
    f_out.close()
    return expert_map, expert_list

def parse_yahoo():
    f_in = open('yahoo.txt')
    f_out = open('yahoo-players.txt', 'w')
    pick_num = 1;
    our_pick_map = {}
    our_pick_list = []
    for line in f_in:
        if "sports.yahoo.com/nba/players/" in line:
            name = line.split(">")[2].split("<")[0]
            out_line = "%d %s" % (pick_num, name)
            #print(out_line)
            f_out.write(out_line + "\n")
            our_pick_map[name] = pick_num
            our_pick_list.append(name)
            pick_num += 1
            #raw_input()
    f_in.close()
    f_out.close()
    return our_pick_map, our_pick_list

if __name__=='__main__':
    expert_map, expert_list = parse_espn()
    our_pick_map, our_pick_list = parse_yahoo()
    
    #find sleepers
    print("Player\tESPN\tOur draft\tDifference")
    for (expert_pos, player) in enumerate(expert_list, start=1):
        if player not in our_pick_map:
            print("%s\t%d\tn/a\tn/a" % (player, expert_pos))
        else:
            our_picked_pos = our_pick_map[player]
            underestimate = our_picked_pos - expert_pos
            if underestimate > 8:
                print("%s\t%d\t%d\t-%d" % (player, expert_pos, our_picked_pos, underestimate))
    
    #find overrated
    print("Player\tOur draft\tESPN\tDifference")
    for (our_pos, player) in enumerate(our_pick_list, start=1):
        if player not in expert_map:
            print("%s\t%d\tn/a\tn/a" % (player, our_pos))
        else:
            expert_pos = expert_map[player]
            overestimate = expert_pos - our_pos
            if overestimate > 8:
                print("%s\t%d\t%d\t%d" % (player, our_pos, expert_pos, overestimate))
                