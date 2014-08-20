from classes import *
import random

def draft(num_players):
    return 0

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
#player needs
#GENERAL: height-weight-speed-age
#OFFENSE: inside-midrange-outside-passing-handling
#DEFENSE: steal-block-intd-outd-rebounding

def generate_player(pref_pos):
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
        print("\nPOINT GUARD")
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
        print("\nSHOOTING GUARD")
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
        print("\nSMALL FORWARD")
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
        print("\nPOWER FORWARD")
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
        print("\nCENTER")
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
                       "Mid-range Specialist", "The Whole Package", "The Wall", "3pt Specialist"]
    num_att = 0
    tries = 0
    gained_attributes = []
    while num_att<5 or tries>10:
        att = random.randint(0, len(list_attributes)-1)
        gained_attributes.append(list_attributes[att])
        num_att+=1
    for a in gained_attributes:
        print(a)
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
            out_s += random.randint(15, 20)
            mid_s -= random.randint(5, 15)
            int_s -= random.randint(5, 15)
            passing -= random.randint(5, 15)
    return bbplayer("Generic", height, weight, speed, age, int_s, mid_s, out_s, passing, handling, steal, block, int_d, out_d, rebounding)

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
    
    while playing: #40min games
        if poss_home:
            hscore += run_play(home, away, prplay)
            poss_away = 1
            poss_home = 0
            gametime += 24 * random.random() / hspeed
        elif poss_away:
            ascore += run_play(away, home, prplay)
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

def run_play(offense, defense, prplay): #take it possession at time yo
    if prplay==1: print(offense.name, "have the ball.")
    passes = 0
    off_poss = 1
    who_poss = offense.pointg
    who_def  = defense.pointg
    assister = who_poss
    while off_poss == 1:
        passprob = who_poss.passing / who_poss.ovrshoot
        if random.random() * passprob > 0.2:
            #pass
            ifsteal = pot_steal(who_poss, who_def)
            if ifsteal == 1:
                #stolen
                if prplay==1: print(who_def.name, "has stolen the ball!")
                who_def.stats_stl += 1
                return 0
            pass_to = random.randint(1, 5)
            assister = who_poss
            if pass_to == 1:
                who_poss = offense.pointg
                who_def  = defense.pointg
            if pass_to == 2:
                who_poss = offense.shootg
                who_def  = defense.shootg
            if pass_to == 3:
                who_poss = offense.smallf
                who_def  = defense.smallf
            if pass_to == 4:
                who_poss = offense.powerf
                who_def  = defense.powerf
            if pass_to == 5:
                who_poss = offense.center
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
                    assister.stats_ass += 1
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

#def pass_or_shoot(who_poss, offense, defense):
def take_shot(shooter, defender, defense, assister, prplay): #return points of shot, 0 if miss
    #give assist bonus for having a good passer pass to you
    ass_bonus = 0
    if assister.name != shooter.name:
        ass_bonus = assister.passing / 20
    #block?
    if random.random() * (defender.block + (defender.height - shooter.height)) > 75 or random.random() < 0.005:
        #NOT IN MY HOUSE MOFO
        if prplay==1: print(defender.name,"has blocked",shooter.name,"!")
        shooter.stats_fga += 1
        defender.stats_blk += 1
        return 0
    if shooter.out_s * random.random() > 40 or (shooter.out_s > (shooter.int_s + shooter.mid_s) and random.random() > 0.25): #second part is where guy is clearly 3pt specialist, ie 25/50/99
        #3pt shot
        chance = (shooter.out_s / defender.out_d) * random.random() * 70 + ass_bonus + shooter.out_s/10 #70 norm multy
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
    elif shooter.mid_s * random.random() > 50: 
        #midrange jumper
        chance = (shooter.mid_s / defender.out_d) * random.random() * 80 + ass_bonus + shooter.mid_s/10 #80 norm multy
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
    else:
        #inside layup/dunk/etc
        chance = ((shooter.int_s / defender.int_d) * random.random() * 80) + ass_bonus + shooter.int_s/10 # - random.random()*((defense.center.int_d + defense.powerf.int_d + defense.smallf.int_d*0.75)/5)
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