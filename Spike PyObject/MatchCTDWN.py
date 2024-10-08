for x in range(45):
    time = int(input("How far is the match now???"))
    if time <= 45:
        print("------------------------------------------------------")
        print("...MATCH UPDATE...")
        print(str(time)+ " minutes")
        print("It is still first half... The match is still going on!")
        print("------------------------------------------------------")
        
    elif 45 < time  < 90:
        print("------------------------------------------------------")
        print("...MATCH UPDATE...")
        print(str(time)+ " minutes")
        print("It is second half... All the teams are back with much energy...!")
        print("------------------------------------------------------")
        
    elif time == 90:
        print("------------------------------------------------------")
        print("...MATCH UPDATE...")
        print(str(time)+ " minutes")
        print("BOOM... The match is done!!!")
        print("THANK YOU FOR YOUR TIME!!!")
        print("------------------------------------------------------")
        


