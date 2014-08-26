from classes import *
import random
import math

def calc_mismatch(shooter, defender, pr):
    int_mis = 2*shooter.int_s - defender.int_d
    mid_mis = 2*shooter.mid_s - (defender.out_d + defender.int_d)/2
    out_mis = 2*shooter.out_s - defender.out_d
    if pr==1: print(int_mis + mid_mis + out_mis)
    return int_mis + mid_mis + out_mis

def detect_mismatch(offense, defense, pr):
    pg_diff = calc_mismatch(offense.pointg, defense.pointg, pr)
    sg_diff = calc_mismatch(offense.shootg, defense.shootg, pr)
    sf_diff = calc_mismatch(offense.smallf, defense.smallf, pr)
    pf_diff = calc_mismatch(offense.powerf, defense.powerf, pr)
    cn_diff = calc_mismatch(offense.center, defense.center, pr)
    matches = [pg_diff, sg_diff, sf_diff, pf_diff, cn_diff]
    return matches

def draft_generate(num_players):
    player_list = []
    first_names_list = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.",
                  "J.", "K.", "L.", "M.", "N.", "O.", "P.", "Q.", "R.",
                  "S.", "T.", "U.", "V.", "W.", "X.", "Y.", "Z."]
    last_names_list = ["James", "Bryant", "Iverson", "Bird", "Baddie",
                       "Vanderbilt", "Notgood", "DaBest", "McGrady",
                       "Bud", "Swag", "Jam", "Rockafella", "Snipes", "Durant",
                       "Jordan", "Dogg", "Carter", "Wayne", "Tang", "Jones",
                       "Jesus", "Hooplife", "Buckets", "Curry", "Splash",
                       "Dunkins", "Jumpson"]
    player_name_set = generate_name_set(num_players, first_names_list, last_names_list)

    for name in player_name_set:
        position = math.ceil(random.random() * 5)
        player_list.append(generate_player(position, 0, name))
    return player_list

def draft_start(player_list, num_opponents):
    opponents_list = []
    for i in range(num_opponents):
        opponents_list.append(ai_opponent())
    player_team = team.empty()
    draft_pick = 1
    direction = 1
    for i in range(5):
        count = 0
        print("NAME:        | HT|WGT|AG|SP|IN|MD|OT|PS|HD|ST|BL|ID|OD|RB|")
        for x in player_list:
            count+=1
            x.print_ratings(0)
            if count == 10:
                print("NAME:        | HT|WGT|AG|SP|IN|MD|OT|PS|HD|ST|BL|ID|OD|RB|")
                count = 0
        for k in range(num_opponents + 1):
            if draft_pick == 1:
                #get player selection
                successful_selection = False
                while True:
                    player_selection_name = input("who u want: ")
                    for player in player_list:
                        if player.name.lower() == player_selection_name.lower():
                            player_team.add_player(player)
                            player_list.remove(player)
                            successful_selection = True
                            draft_pick += direction
                            break
                    if successful_selection: break
                    else: print("pick a real name idiot")
            elif draft_pick > 1 and draft_pick <= num_opponents + 1:
                opponents_choice = opponents_list[draft_pick - 2].select_player(player_list)
                opponents_list[draft_pick - 2].ai_team.add_player(player_list.pop(opponents_choice), i+1)
                draft_pick += direction
        direction = -direction
        if draft_pick == 0:
            draft_pick = 1
        elif draft_pick == num_opponents + 2:
            draft_pick = num_opponents + 1
        input("Press Enter to continue...")
        
    opp_teams = []
    for ai in opponents_list:
        opp_teams.append(ai.get_team())

    return player_team, opp_teams

def find_rebounder(team): #who shall receive the rebounding blessing?
    cenreb = random.random()*team.center.rebounding*1.2
    powreb = random.random()*team.powerf.rebounding*1.1
    smfreb = random.random()*team.smallf.rebounding
    shgreb = random.random()*team.shootg.rebounding*0.9
    ptgreb = random.random()*team.pointg.rebounding*0.8
    listreb = [cenreb, powreb, smfreb, shgreb, ptgreb]
    listreb.sort()
    if listreb[4]==cenreb:
        team.center.stats_reb += 1
        return team.center
    elif listreb[4]==powreb:
        team.powerf.stats_reb += 1
        return team.powerf
    elif listreb[4]==smfreb:
        team.smallf.stats_reb += 1
        return team.smallf   
    elif listreb[4]==shgreb:
        team.shootg.stats_reb += 1
        return team.shootg
    else:
        team.pointg.stats_reb += 1
        return team.pointg

def generate_league(league_size):
    league = []
    team_prefixes = ["Mc", "Un", "Not", "Big", "Tiny", "Giant", "Red", "Blue",
                     "Neon", "Swaggish", "White", "Black", "Last", "Best", "Worst"]
    team_suffixes = ["Armadillos", "Lumberjacks", "Killas", "Dicks", "Diamonds",
                     "Senators", "Warriors", "Heat", "Bulls", "Tech Support",
                     "Ballers", "Rioters", "Mofos", "Nazis", "Klansmen"]
    team_names = generate_name_set(league_size, team_prefixes, team_suffixes)
    for name in team_names:
        league.append(generate_team(name, 1))
    return league

def generate_name_set(size, first_names_list, last_names_list=None):
    player_name_set = set()
    if last_names_list is not None:
        if size > len(first_names_list) * len(last_names_list):
            raise KeyError('Don\'t have enough names')
        while len(player_name_set) < size:
            player_name_set.add(random.choice(first_names_list) + " " + random.choice(last_names_list))
    else:
        if size > len(first_names_list):
            raise KeyError('Don\'t have enough names')
        while len(player_name_set) < size:
            player_name_set.add(random.choice(first_names_list))
    return player_name_set

#player needs
#GENERAL: height-weight-speed-age
#OFFENSE: inside-midrange-outside-passing-handling
#DEFENSE: steal-block-intd-outd-rebounding
def generate_player(pref_pos, pr, name="Generic"):
    #default values
    height     = 78 #6'6"
    weight     = 180
    speed      = 75
    age        = 25
    int_s      = 75
    mid_s      = 75
    out_s      = 75
    passing    = 75
    handling   = 75
    steal      = 75
    block      = 75
    int_d      = 75
    out_d      = 75
    rebounding = 75
    if pref_pos==1: #point guard
        if pr==1: print("\nPOINT GUARD")
        height -= random.randint(3, 6)
        weight -= random.randint(0, 30)
        speed += random.randint(5, 10)
        int_s -= random.randint(8, 16)
        mid_s += random.randint(0, 10) - 5
        out_s += random.randint(0, 10) - 5
        passing += random.randint(0, 10)
        handling += random.randint(0, 10)
        steal += random.randint(0, 10) - 2
        block -= random.randint(20, 40)
        int_d -= random.randint(8, 16)
        out_d += random.randint(0, 10) - 5
        rebounding -= random.randint(10, 30)
    elif pref_pos==2: #shooting guard
        if pr==1: print("\nSHOOTING GUARD")
        height += random.randint(0, 4) - 3
        weight += random.randint(0, 30) - 15
        speed += random.randint(0, 6)
        int_s += random.randint(0, 16) - 8
        mid_s += random.randint(0, 13) - 5
        out_s += random.randint(0, 13) - 5
        passing += random.randint(0, 10) - 3
        handling += random.randint(0, 10) - 2
        steal += random.randint(0, 10) - 5
        block -= random.randint(10, 30)
        int_d -= random.randint(5, 10)
        out_d += random.randint(0, 10) - 5
        rebounding -= random.randint(5, 15)
    elif pref_pos==3: #small forward
        if pr==1: print("\nSMALL FORWARD")
        height += random.randint(0, 6) - 2
        weight += random.randint(0, 40) - 10
        speed += random.randint(0, 16) - 8
        int_s += random.randint(0, 20) - 8
        mid_s += random.randint(0, 20) - 10
        out_s += random.randint(0, 20) - 10
        passing += random.randint(0, 20) - 10
        handling += random.randint(0, 20) - 10
        steal += random.randint(0, 20) - 10
        block += random.randint(0, 15) - 5
        int_d += random.randint(0, 15) - 5
        out_d += random.randint(0, 15) - 5
        rebounding += random.randint(0, 15) - 5
    elif pref_pos==4: #power forward
        if pr==1: print("\nPOWER FORWARD")
        height += random.randint(1, 7)
        weight += random.randint(20, 60)
        speed += random.randint(0, 15) - 15
        int_s += random.randint(0, 20) - 5
        mid_s += random.randint(0, 16) - 8
        out_s += random.randint(0, 12) - 6
        passing += random.randint(0, 20) - 20
        handling += random.randint(0, 20) - 20
        steal += random.randint(0, 20) - 20
        block += random.randint(0, 20) - 5
        int_d += random.randint(0, 20) - 5
        out_d += random.randint(0, 10) - 8
        rebounding += random.randint(0, 20) - 5
    elif pref_pos==5: #center
        if pr==1: print("\nCENTER")
        height += random.randint(2, 12)
        weight += random.randint(40, 80)
        speed += random.randint(0, 20) - 30
        int_s += random.randint(5, 15)
        mid_s += random.randint(0, 20) - 20
        out_s += random.randint(0, 30) - 45
        passing += random.randint(0, 20) - 40
        handling += random.randint(0, 30) - 40
        steal += random.randint(0, 30) - 40
        block += random.randint(5, 15)
        int_d += random.randint(5, 15)
        out_d += random.randint(0, 20) - 30
        rebounding += random.randint(5, 15)
    #choose 5(?) of these "attributes" to make a player. Some are good, some bad, some funny
    list_attributes = ["Passer", "Offensive Weapon", "Blocker", "Tall", "Short", "On-ball Defense", "Rebounder", "Fumbler", "Fatty", "Slow", "No Threes", "Dunker", "Defensive Liability", "Offensive Liability",
                       "Mid-range Specialist", "The Whole Package", "The Wall", "3pt Specialist", "Two-way inside", "Two-way outside"]
    num_att = 0
    tries = 0
    gained_attributes = []
    while num_att<5 or tries>10:
        att = random.randint(0, len(list_attributes)-1)
        gained_attributes.append(list_attributes[att])
        num_att+=1
    for a in gained_attributes:
        if pr==1: print(a)
        if a=="Passer":
            passing += random.randint(10, 15)
        elif a=="Offensive Weapon":
            out_s += random.randint(0, 10)
            mid_s += random.randint(10, 15)
            int_s += random.randint(10, 15)
        elif a=="Blocker":
            block += random.randint(10, 15)
        elif a=="Tall":
            height += random.randint(4,8)
        elif a=="Short":
            height -= random.randint(3,5)
        elif a=="On-ball Defense":
            steal += random.randint(5, 10)
            out_d += random.randint(5, 10)
        elif a=="Rebounder":
            rebounding += random.randint(10, 15)
            height += random.randint(0, 2)
        elif a=="Fumbler":
            passing -= random.randint(10, 15)
            handling -= random.randint(10, 15)
        elif a=="Fatty":
            weight += random.randint(50, 100)
        elif a=="Slow":
            speed -= random.randint(20, 40)
            if speed<0: speed=0
        elif a=="No Threes":
            out_s -= random.randint(20, 30)
        elif a=="Dunker":
            int_s += random.randint(15, 20)
        elif a=="Defensive Liability":
            steal -= random.randint(5, 10)
            block -= random.randint(5, 10)
            int_d -= random.randint(5, 10)
            out_d -= random.randint(5, 10)
        elif a=="Offensive Liability":
            int_s -= random.randint(5, 10)
            out_s -= random.randint(5, 10)
            mid_s -= random.randint(5, 10)
        elif a=="Mid-range Specialist":
            mid_s += random.randint(12, 17)
        elif a=="The Whole Package":
            steal += random.randint(2, 4)
            block += random.randint(2, 4)
            int_d += random.randint(2, 4)
            out_d += random.randint(2, 4)
            int_s += random.randint(2, 4)
            out_s += random.randint(2, 4)
            mid_s += random.randint(2, 4)
            passing += random.randint(2, 4)
        elif a=="The Wall":
            int_d += random.randint(12, 17)
            block += random.randint(6, 12)
        elif a=="3pt Specialist":
            out_s += random.randint(12, 17)
            mid_s -= random.randint(5, 15)
            int_s -= random.randint(5, 15)
            passing -= random.randint(5, 15)
        elif a=="Two-way inside":
            int_s += random.randint(8, 12)
            int_d += random.randint(8, 12)
        elif a=="Two-way outside":
            out_s += random.randint(8, 12)
            out_d += random.randint(8, 12)
            
    return bbplayer(name, height, weight, speed, age, int_s, mid_s, out_s, passing, handling, steal, block, int_d, out_d, rebounding)

def generate_team(name, pr):
    gen_team = team(name, generate_player(1, 0), generate_player(2, 0), generate_player(3, 0), generate_player(4, 0), generate_player(5, 0))
    if pr==1:
        print("\n")
        gen_team.print_team_ratings()
    return gen_team
    
def intelligent_pass(who_poss, offense, defense, matches):
    sorted_matches = sorted(matches)
    weighted = 2
    tot_m = matches[0]**weighted + matches[1]**weighted + matches[2]**weighted + matches[3]**weighted + matches[4]**weighted
    sel_target = random.randint(0, int(tot_m))
    if sel_target < sorted_matches[4]**weighted:
        target = sorted_matches[4]
    elif sel_target < (sorted_matches[4]**weighted + sorted_matches[3]**weighted):
        target = sorted_matches[3]
    elif sel_target < (sorted_matches[4]**weighted + sorted_matches[3]**weighted + sorted_matches[2]**weighted):
        target = sorted_matches[2]
    elif sel_target < (sorted_matches[4]**weighted + sorted_matches[3]**weighted + sorted_matches[2]**weighted + sorted_matches[1]**weighted):
        target = sorted_matches[1]
    else:
        target = sorted_matches[0]
    
    if target == matches[0]: #pg target of pass
        return offense.pointg
    elif target == matches[1]: #sg target of pass
        return offense.shootg
    elif target == matches[2]: #sf target of pass
        return offense.smallf
    elif target == matches[3]: #pf target of pass
        return offense.powerf
    elif target == matches[4]: #cn target of pass
        return offense.center

def playseason(teams_arr):
    itr = 0
    while itr < len(teams_arr):
        ttr = itr + 1
        while ttr < len(teams_arr):
            playgame(teams_arr[itr], teams_arr[ttr], 0, 0).wins += 1
            playgame(teams_arr[ttr], teams_arr[itr], 0, 0).wins += 1
            playgame(teams_arr[itr], teams_arr[ttr], 0, 0).wins += 1
            playgame(teams_arr[ttr], teams_arr[itr], 0, 0).wins += 1
            ttr += 1
        itr += 1
    
    print("\n")
    for t in teams_arr:
        print(t.name ,":", t.wins, "-", (t.pointg.stats_gms - t.wins))
        t.print_pergame_box()
        print("\n")
        
def playseries(team1, team2, numgames, prbox, prend):
    wins1 = 0
    wins2 = 0
    series_games = numgames
    toggle_home = True #have toggle to change arenas every game (maybe home adv l8r implement so this might matter)
    while numgames > 0:
        if toggle_home == True:
            toggle_home = False
            winner = playgame(team1, team2, 0, prbox)
            if winner==team1:
                wins1 += 1
            elif winner==team2: 
                wins2 += 1
        else:
            toggle_home = True
            winner = playgame(team2, team1, 0, prbox)
            if winner==team2:
                wins2 += 1
            elif winner==team1: 
                wins1 += 1
        numgames -= 1
    
    print("\n")
    print("Result of",series_games,"game series:",team1.name,"-",wins1,team2.name,"-",wins2,"\n")
    if prend == 1:
        print(team1.name,"-",wins1,"wins")
        team1.print_pergame_box()
        print("\n")
        print(team2.name,"-",wins2,"wins")
        team2.print_pergame_box()

def playgame(home, away, prplay, prbox): #home team, away team, print play-by-play (0 or 1), print box at end (0 or 1)
    if prbox==1: 
        print("\n")
        print(away.name, " @ ", home.name,"\n")
    
    #set possession
    poss_home, poss_away = tip_off(home, away, prplay)
    gametime = 0
    max_gametime = 2400
    hscore = 0
    ascore = 0
    hspeed = (home.pointg.speed + home.shootg.speed + home.smallf.speed) / 300
    aspeed = (away.pointg.speed + away.shootg.speed + away.smallf.speed) / 300
    playing = True
    
    matches_h = detect_mismatch(home, away, 0)
    for i in range(5):
        home.player_array[i].stats_tot_msm += matches_h[i]
    matches_a = detect_mismatch(away, home, 0)
    for i in range(5):
        away.player_array[i].stats_tot_msm += matches_a[i]
    
    while playing: #40min games
        if poss_home:
            hscore += run_play(home, away, matches_h, prplay)
            poss_away = 1
            poss_home = 0
            gametime += 24 * random.random() / hspeed
        elif poss_away:
            ascore += run_play(away, home, matches_a, prplay)
            poss_away = 0
            poss_home = 1
            gametime += 24 * random.random() / aspeed
        if gametime > max_gametime:
            gametime = max_gametime
            if hscore != ascore:
                playing = False
            else:
                if prplay==1: print("\n*** OVERTIME! ***\n")
                poss_home, poss_away = tip_off(home, away, prplay)
                max_gametime += 300
        if prplay==1: print("Gametime: ", int(gametime), " | ", home.name, ":", hscore, " ", away.name, ":", ascore,"\n")
    
    #print boxscore if desired
    if prbox==1:
        print("HOME ", home.name, ": ", hscore)
        home.print_box()
        print("\n")
        print("AWAY ", away.name, ": ", ascore)
        away.print_box()
    
    #do some stats management, like adding player stuff to their career totals
    home.game_reset_tstats()
    away.game_reset_tstats()
    
    #return winner
    if hscore > ascore:
        return home
    else: return away

def pot_steal(poss, stlr): #see if the pass is stolen, return 1 if it is
    if random.random() < 0.1: #only 10% of passes are "stealable"
        chance = random.random() * (stlr.steal - poss.handling*0.5)
        if chance > 30 or random.random() < 0.1:
            #stolen!
            return 1
        else: return 0
    else: return 0

def run_play(offense, defense, matches, prplay): #take it possession at time yo
    if prplay==1: print(offense.name, "have the ball.")
    passes = 0
    off_poss = 1
    who_poss = offense.pointg
    who_def  = defense.pointg
    assister = who_poss
    while off_poss == 1:
        #mismatch = calc_mismatch(who_poss, who_def, 0)
        if ((random.randint(0,6) + passes < 5) or (passes==0 and random.random()<0.97)) or (who_poss.passing*3 - who_poss.out_s - who_poss.mid_s - who_poss.int_s > 80 and random.random() < 0.9):
            #pass
            passes+=1
            ifsteal = pot_steal(who_poss, who_def)
            if ifsteal == 1:
                #stolen
                if prplay==1: print(who_def.name, "has stolen the ball!")
                who_def.stats_stl += 1
                return 0
            assister = who_poss
            who_poss = intelligent_pass(who_poss, offense, defense, matches)
            if who_poss == offense.pointg:
                who_def  = defense.pointg
            if who_poss == offense.shootg:
                who_def  = defense.shootg
            if who_poss == offense.smallf:
                who_def  = defense.smallf
            if who_poss == offense.powerf:
                who_def  = defense.powerf
            if who_poss == offense.center:
                who_def  = defense.center
        else:
            #shoot
            points = take_shot(who_poss, who_def, defense, assister, prplay)
            if points > 0:
                #made it!
                if assister == who_poss:
                    if prplay==1: print(who_poss.name, "made a", points, "pt shot")
                    return points
                else:
                    if assister.passing*random.random() + 50 > 75: assister.stats_ass += 1
                    if prplay==1: print(who_poss.name, "made a", points, "pt shot with an assist from", assister.name)
                    return points
            else:
                #rebounding, defenders have 3:1 advantage
                #weighted rebounding advantage calculator, maybe add height adv too l8r
                reb_adv = (defense.center.rebounding - offense.center.rebounding) + (defense.powerf.rebounding - offense.powerf.rebounding)*0.85 + (defense.smallf.rebounding - offense.smallf.rebounding)*0.7 + (defense.shootg.rebounding - offense.shootg.rebounding)*0.5 + (defense.pointg.rebounding - offense.pointg.rebounding)*0.25
                reb_adv *= 0.5
                if (random.random()*100 + reb_adv) > 25: #defensive reb
                    rebounder = find_rebounder(defense)
                    if prplay==1: print(rebounder.name,"grabs the defensive rebound!")
                    return 0
                else: #offensive reb
                    rebounder = find_rebounder(offense)
                    if prplay==1: print(rebounder.name,"snatches the offensive rebound!")
                    who_poss = rebounder
                    passes = 2

def take_shot(shooter, defender, defense, assister, prplay): #return points of shot, 0 if miss
    
    #give assist bonus for having a good passer pass to you
    ass_bonus = 0
    if assister != shooter:
        ass_bonus = assister.passing / 20
    
    #block?
    if random.random() * (defender.block + (defender.height - shooter.height)) > 80 or random.random() < 0.005:
        #NOT IN MY HOUSE MOFO
        if prplay==1: print(defender.name,"has blocked",shooter.name,"!")
        shooter.stats_fga += 1
        defender.stats_blk += 1
        return 0
    
    #select shot, use tendencies
    out_ten = 0
    mid_ten = 0
    int_ten = 0
    if shooter.out_s>50: out_ten = (shooter.out_s / defender.out_d) * shooter.out_s**1.2
    if shooter.out_s + 20 < shooter.mid_s or shooter.out_s + 20 < shooter.int_s: out_ten -= 200 #see if one stat is sig worse than other two so he never takes that shot
    out_ten += 3*(shooter.out_s - 75)
    
    if shooter.mid_s>50: mid_ten = (shooter.mid_s / (defender.out_d*0.5 + 0.5*defender.int_d)) * shooter.mid_s**1.2
    if shooter.mid_s + 20 < shooter.out_s or shooter.mid_s + 20 < shooter.int_s: mid_ten -= 200
    mid_ten += 3*(shooter.mid_s - 75)
    
    if shooter.int_s>50: int_ten = (shooter.int_s / defender.int_d) * shooter.int_s**1.2
    if shooter.int_s + 20 < shooter.out_s or shooter.int_s + 20 < shooter.mid_s: int_ten -= 200
    int_ten += 3*(shooter.mid_s - 75)
    
    if out_ten<0: out_ten=0
    if mid_ten<0: mid_ten=0
    if int_ten<0: int_ten=0
    tot_ten = out_ten + mid_ten + int_ten
    sel_shot = random.randint(0, int(tot_ten))
    
    if sel_shot < out_ten and out_ten!=0: #3point shot selected
        chance = (shooter.out_s / defender.out_d) * random.random() * 70 + ass_bonus + (shooter.out_s - 75)/3 #70 norm multy
        if chance > 60:
            #made it!
            shooter.stats_pts += 3
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            shooter.stats_3ga += 1
            shooter.stats_3gm += 1
            return 3
        else:
            if prplay==1: print(shooter.name, "misses from downtown!")
            shooter.stats_fga += 1
            shooter.stats_3ga += 1
            return 0
    
    elif sel_shot >= out_ten and sel_shot < int_ten and mid_ten!=0: #midrange jumper selected
        chance = (shooter.mid_s / (defender.out_d*0.5 + 0.5*defender.int_d)) * random.random() * 80 + ass_bonus + (shooter.mid_s - 75)/3 #80 norm multy
        if chance > 50:
            #made it!
            shooter.stats_pts += 2
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            return 2
        else:
            if prplay==1: print(shooter.name, "bricks the midrange jumper!")        
            shooter.stats_fga += 1
            return 0
    
    else: #inside layup/dunk/etc
        chance = ((shooter.int_s / defender.int_d) * random.random() * 80) + ass_bonus + (shooter.int_s - 75)/3 # - random.random()*((defense.center.int_d + defense.powerf.int_d + defense.smallf.int_d*0.75)/5)
        if chance > 50:
            #made it!
            if random.random() < 0.3:
                if prplay==1: print(shooter.name, "slams it down over", defender.name, "!")
            else:
                if prplay==1: print(shooter.name, "lays it in!")
            shooter.stats_pts += 2
            shooter.stats_fga += 1
            shooter.stats_fgm += 1
            return 2
        else:
            if prplay==1: print(shooter.name, "can't connect on the inside shot!") 
            shooter.stats_fga += 1
            return 0

def tip_off(home, away, prplay):
    poss = random.random()
    if poss > 0.5:
        poss_home = True
        poss_away = False
        if prplay==1: print(home.name, "wins the tip-off!")
    else:
        poss_away = True
        poss_home = False
        if prplay==1: print(away.name, "wins the tip-off!")
    return poss_home, poss_away
