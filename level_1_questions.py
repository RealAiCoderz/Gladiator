from math import comb
import logger

#business logic for each question
q1_sql = "SELECT Team, count(Team) AS Count FROM Heroes GROUP BY Team"
q2_sql = "select Name from Heroes where (Weight > (select weight from heroes where Name=\"Spider-Man\")) and (height > (select Height from heroes where Name=\"Henery\"))"
q3_sql = "select Name from Heroes where (Games_played > 100) and (weight > (select weight from heroes where Name=\"Captain America\"))"
q4_sql = "select Name from Heroes where (height+weight+games_played > 350)"

#1.1  Probability of selection of 2 from Marvel and 3 from DC
def q1(res):
    res = dict(res)
    
    n_dc =res["DC"]
    n_marvel = res["Marvel"]
    
    ans = comb(n_marvel,3) * comb(n_dc,2) / comb((n_dc + n_marvel), 5)
    print("--PROBABILITY OF A TEAM WITH 2 FROM MARVEL AND 3 FROM DC = {:.3f}".format(ans))
    print("\n")
    
#1.2 All characters heavier than Spider-Man and taller than Henery
def q2(res):
    print("--STARS WHO ARE HEAVIER THAN SPIDERMAN AND TALLER THAN HENERY:")
    for elem in res:
        print(elem[0], end=', ')
    print("\n")

#1.3  All characters who have played more than 100 games and are heavier than Captain America
def q3(res):
    print("--STARS WHO HAVE PLAYED > 100 GAMES AND ARE HEAVIER THAN CAPTAIN AMERICA:")
    for elem in res:
        print(elem[0], end=', ')
    print("\n")

#1.4 All characters whose sum of stats > 350
def q4(res):
    print("--STARS WHOSE SUM OF STATS > 350:")
    for elem in res:
        print(elem[0], end=', ')
    print("\n")