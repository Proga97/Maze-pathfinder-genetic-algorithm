import Tkinter as tk
import random
import time
import pygame as p
import random
import math

mutation_rate=10
increase_rate=0.1
complex=True
pop_size=200
black=((0,0,0))
fps=60
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
grid=[]
size=20
w=32
flag=0
mousepos=[]
space="udlr"
splen=len(space)
length=400
startx=0
starty=0
finishx=19
finishy=19
prev_steps=-1


def find_dupes(st):
    seen=[]
    for i in range(len(st)):
        if i in seen:
            k=gen_population(1,len(i))[0]
            if k not in st:
                st[i]=k
            else:
                st[i]=k[::-1]
        seen.append(i)
    return st

def get_numbers(currentx,currenty,steps):
    global prev_steps,mutation_rate,complex
    if complex==False:
        d = abs(finishy - currenty)
        d1 = abs(finishx - currentx)
        td = d + d1#+steps/((d+d1)*length)
        maxd = abs(finishy - starty) + abs(finishx - startx)
        if steps>prev_steps:
            prev_steps=steps


        return 100-int((float(td)/maxd) * 100)
    else:
        st=float(steps)/length
        d = abs(finishy - currenty)
        d1 = abs(finishx - currentx)
        td = d + d1  # +steps/((d+d1)*length)
        st=steps
        if steps>prev_steps:
            prev_steps=steps
            #complex=False
        return (float(st)/length)*100


def clear():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=="P":
                grid[i][j]=0

    grid[startx][starty]="P"
def fitness(player,gri):
    global mutation_rate
    board=gri

    #mutation_rate=10
    steps=0
    start=[startx,starty]
    currentx=startx
    currenty=starty
    visited=[]
    visited=[[currentx,currenty]]

    for i in range(len(player)):

            #print "STEPS",steps




        #print board
        k=player[i]
        steps+=1

        if k=='u':
            #print "UP"
            try:
                if board[currentx-1][currenty]==0 and [currentx-1,currenty] not in visited and currentx>=1:
                    #print "NO ERROR"
                    if currentx-1<0:
                        board[500][500]="p"
                    board[currentx][currenty]=0
                    board[currentx-1][currenty]='P'
                    currentx=currentx-1
                    #gridplayer(board)
                    #time.sleep(0.5)
                    visited.append([currentx,currenty])
                    mutation_rate-=increase_rate/(float(2))
                elif board[currentx-1][currenty]=="F" and currentx>=1:
                    clear()
                    return 100
                else:
                    clear()
                    mutation_rate+=increase_rate*5
                    return get_numbers(currentx,currenty,steps)

            except:
                clear()
                mutation_rate += increase_rate*5
                return get_numbers(currentx,currenty,steps)
        if k == 'd':
            #print "DOWN"
            try:
                if board[currentx+1][currenty ] == 0 and [currentx+1,currenty] not in visited:
                    #print "NO ERROR"
                    board[currentx][currenty] = 0
                    board[currentx+1][currenty] = 'P'
                    currentx = currentx + 1
                    #gridplayer(board)
                    #time.sleep(0.5)
                    visited.append([currentx, currenty])
                    #print "DOWN DONE"
                    mutation_rate -= increase_rate/(float(2))
                elif board[currentx+1][currenty] == "F":
                    #print "REACHED FINISH"
                    clear()
                    return 100
                else:
                    #"NO VALID DOWN"
                    mutation_rate += increase_rate*5
                    clear()

                    return get_numbers(currentx,currenty,steps)

            except Exception as e:
                #print e
                clear()
                mutation_rate += increase_rate*5
                return get_numbers(currentx, currenty,steps)
        if k == 'l':
            #print "LEFT"
            try:
                if board[currentx][currenty-1] == 0 and [currentx,currenty-1] not in visited and currenty>=1:
                    #print "NO ERROR"
                    if currenty-1<0:
                        board[500][500]="LOL"
                    board[currentx][currenty] = 0
                    board[currentx][currenty-1] = 'P'
                    currenty = currenty - 1
                    #gridplayer(board)
                    #time.sleep(0.5)
                    visited.append([currentx, currenty])
                    mutation_rate -= increase_rate/(float(2))
                elif board[currentx][currenty-1] == "F" and currenty>=1:
                    clear()
                    return 100
                else:
                    clear()
                    mutation_rate += increase_rate*5
                    return get_numbers(currentx,currenty,steps)

            except:
                clear()
                mutation_rate += increase_rate*5
                return get_numbers(currentx, currenty,steps)
        if k == 'r':
            #print "RIGHT"
            try:
                if board[currentx][currenty+1] == 0 and [currentx,currenty+1] not in visited:

                    board[currentx][currenty] = 0
                    board[currentx][currenty+1] = 'P'
                    currenty = currenty + 1
                    #gridplayer(board)
                    #time.sleep(0.5)
                    visited.append([currentx, currenty] )
                    mutation_rate -= increase_rate/(float(2))
                elif board[currentx][currenty+1] == "F":
                    clear()
                    return 100
                else:

                    clear()
                    mutation_rate += increase_rate*5
                    return get_numbers(currentx,currenty,steps)

            except:
                clear()
                mutation_rate += increase_rate*5
                return get_numbers(currentx, currenty,steps)
    mutation_rate += increase_rate*5
    return get_numbers(currentx,currenty,steps)


def create_pairs(pop):
    pai = []
    selected = []
    pop_score = []
    # print len(p),"CreatePairs"
    for i in pop:
        pop_score.append([i,fitness(i,grid)])

    pi = []
    # print len(pop_score),"After pop score"
    l=max(pop_score, key=lambda x:x[1])[1]

    # print len(pop_score),"pop score"
    p = sorted(pop_score, key=lambda x:x[1])
    # print len(p),"After sorting ascending"
    p = p[::-1]
    #print p, len(p)
    #print p[0]
    while (len(pai) * 2) < len(p):
        # print len(pai)
        if len(pi) == 2:
            pai.append(pi)

            pi = []
            continue
        for i in p:
            if len(pi) == 2:
                break
            #if i[0] not in selected:
                #k = random.randint(0, l)
                #if k <= i[1]:
            pi.append(i[0])
            selected.append(i[0])
    #print pai
    return pai



def crossover(pai):
    po = []
    global mutation_rate
    for i in pai:

        t = i
        x = t[0]
        y = t[1]
        tl = random.randint(0, len(x) - 1)
        l = len(x) / 2
        t1 = x[:l] + y[l:]
        t2 = x[l:] + y[:l]
        t3 = y[:l] + x[l:]
        t4 = y[l:] + x[:l]
        t5 = x[:tl] + y[tl:]
        t6 = x[tl:] + y[:tl]
        t7 = y[:tl] + x[tl:]
        t8 = y[tl:] + x[:tl]
        t9 = x
        t10 = y
        for j in range(1, len(x), 2):
            t11 = x[:j] + y[j] + x[j + 1:]
            t12 = y[:j] + x[j] + y[j + 1:]
            x = t11
            y = t12
        txf = {}
        txf[t1] = fitness(t1,grid)
        txf[t2] = fitness(t2,grid)
        txf[t3] = fitness(t3,grid)
        txf[t4] = fitness(t4,grid)
        txf[t5] = fitness(t5,grid)
        txf[t6] = fitness(t6,grid)
        txf[t7] = fitness(t7,grid)
        txf[t8] = fitness(t8,grid)
        txf[t9] = fitness(t9,grid)
        txf[t10] = fitness(t10,grid)
        txf[t11] = fitness(t11,grid)
        txf[t12] = fitness(t12,grid)
        for i in range(15 - len(txf)):
            tmp = ""
            tmp = gen_population(1)[0]
            txf[tmp] = fitness(tmp,grid)

        p = sorted(txf, key=txf.get)
        p = p[::-1]
        #print p
        flag = 0
        l = max(txf, key=lambda x: x[1])
        l=txf[l]
        for i in p:
            if flag>=2:
                break
            po.append(i)
            flag+=1
        #print l


    # print len(po),"Cross"

    po = find_dupes(po)
    return po


def mutations(pop):
    global complex
    global mutation_rate
    po = []

    print complex,"Complex",mutation_rate,prev_steps
    for i in pop:
        t = i
        for j in range(len(t)):
            k = random.randint(0, 100)
            if mutation_rate<1:
                mutation_rate=10
                complex=False
            if mutation_rate>20:
                mutation_rate=19
            if mutation_rate>10:
                complex=True
            #print mutation_rate,"MUTE"
            if k <= mutation_rate:
                x = random.randint(0, splen - 1)
                t = t[:j] + space[x] + t[j + 1:]
        po.append(t)
    # print len(po),"Mut"
    mutation_rate=0
    po = find_dupes(po)
    return po
def gen_population(size):
    pop=[]
    while len(pop)<size:
        temp=""
        for j in range(length):
            k=random.randint(0,splen-1)
            #print k
            temp += space[k]
            '''
            x=0
            y=0
            if space[k] == "u":
                y+=1
                temp[x][y]="P"
            if space[k] == "d":
                y-=1
                temp[x][y]="P"
            if space[k] == "r":
                x+=1
                temp[x][y]="P"
            if space[k] == "l":
                x-=1
                temp[x][y]="P"'''
        if temp not in pop:
            pop.append(temp)
    return pop


p.init()
Res=(1270,720)
screen=p.display.set_mode(Res)
clock = p.time.Clock()



for j in range(size):
    a=[]
    for i in range(size):

        a.append(0)
    grid.append(a)

grid[finishx][finishy]="F"
grid[startx][starty]="P"
#print grid



def gridf(grid):

    x = 64
    y = 64
    for row in grid:
        for col in row:
            box = p.Rect(x, y, w, w)
            p.draw.rect(screen, WHITE, box,1)
            #screen.blit(screen,box)
            p.draw.rect(screen, RED, (32*(startx+2),32*(starty+2),w,w))
            p.draw.rect(screen, GREEN, (32*(finishx+2), 32*(finishy+2), w,w))
            p.draw.rect(screen, GREEN, (736, 640, w+64, w))
            x = x + w
        y = y + w
        x = 64
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                p.draw.rect(screen, WHITE,(32*(j+2),32*(i+2),w,w))





def gridplayer(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "P":
                #print i,j
                p.draw.rect(screen, BLUE, ((j+2)*32, (i+2)*32, w, w))
                p.display.flip()

def clearboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "P":
                print i,j
                p.draw.rect(screen, WHITE, ((j + 2) * 32, (i + 2) * 32, w, w), 1)
                p.draw.rect(screen, black, ((j+2)*32, (i+2)*32, w, w))


    p.draw.rect(screen, BLUE, ((startx + 2) * 32, (starty + 2) * 32, w, w))
def draw_player(moves):
    currentx=startx
    currenty=starty
    #clearboard(grid)
    screen.fill(black)
    gridf(grid)
    for i in range(len(moves)):
        #print grid
        k=moves[i]
        if k=="u":
            if currentx>=1 and  grid[currentx-1][currenty]==0:
                grid[currentx-1][currenty]="P"
                currentx-=1
            else:
                gridplayer(grid)
                #clearboard(grid)
                return
        if k=="l":
            if currenty>=1 and grid[currentx][currenty-1]==0:
                grid[currentx][currenty-1] = "P"
                currenty-=1
            else:
                gridplayer(grid)
                #clearboard(grid)
                return
        if k == "r":
            if currenty <= size-2 and grid[currentx][currenty +1] == 0:
                grid[currentx][currenty + 1] = "P"
                currenty+=1
            else:
                gridplayer(grid)
                #clearboard(grid)
                return
        if k == "d":
            if currentx <= size-2 and grid[currentx+1][currenty ] == 0:
                grid[currentx+1][currenty] = "P"
                currentx+=1
            else:
                gridplayer(grid)
                #clearboard(grid)
                return
    gridplayer(grid)
    return
def run_algo():

    #s="rdruruuddddrduluuullrduurrulrurdluulrllllluluudul"
    #print fitness(s)
    count = 0
    for i in grid:
        for j in i:
            if j == 1:
                count += 1

    print count
    gen=0
    best_fitness=0
    best_dir=""
    avg=0
    players = gen_population(pop_size)
    while best_fitness<100:
        #print grid
        gen+=1
        pairs=create_pairs(players)
        children=crossover(pairs)
        children=mutations(children)
        for i in children:

            r=fitness(i,grid)
            #print r
            avg+=r
            #draw_player(i)
            #print r,i
            if r>best_fitness:
                best_fitness=r
                best_dir=i
        avg=float(avg)/len(children)
        #print best_fitness
        #print best_dir
        print avg
        avg=0
        draw_player(best_dir)

        #time.sleep(1)

        #print best_dir
        players=children

    #print fitness(player[0])
    draw_player(best_dir)
    #print best_dir
    #print gen

while 1:
    #print grid

    #gridplayer(grid# )
    if flag==1:

        flag=2

    if flag == 0:
        gridf(grid)
        flag=1

    #print LOL
    clock.tick(30)
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            mousepos= p.mouse.get_pos()
            x = mousepos[0] / 32
            y = mousepos[1] / 32
            try:
                if grid[y-2][x-2]==0:
                    grid[y-2][x-2]=1
                    x=x*32
                    y=y*32
                    box = p.Rect(x, y, w, w)
                    p.draw.rect(screen, WHITE, box)
                elif grid[y-2][x-2]==1:
                    grid[y - 2][x - 2] = 0
                    x = x * 32
                    y = y * 32
                    box = p.Rect(x, y, w, w)
                    p.draw.rect(screen, black, box)
                    p.draw.rect(screen, WHITE, box, 1)
            except:
                pass
            if mousepos[0] >= 736 and mousepos[0] <= 736+w+64 and mousepos[1] >= 640 and mousepos[1] <= 640+w:
                run_algo()
                #s="rrdddrrrrrdddd"
                #draw_player(s)
                #print "Done drawing"
            #print mousepos,x,y,grid

    p.display.flip()