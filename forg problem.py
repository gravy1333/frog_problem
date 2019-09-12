import random
while(1):
    #dist = input("Distence: ")
    #trials = input("trial number: ")
    #dist = int(dist)
    #trials = int(trials)
    jumps = 0
    dist = random.randint(1, 100)
    trials = 1000000
    print(dist)
    
    for tri in range(trials):
        pos = 0
        while(pos != dist):
            jump = random.randint((pos+1), dist)
            pos = jump
            jumps += 1
    
    avg = jumps / trials
    print(avg)
