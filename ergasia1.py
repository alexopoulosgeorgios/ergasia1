while True:
    x = int(input("Give the beginning of space: "))
    y = int(input("Give the end of space: "))
    list=[[x,y]]
    while True:
	
        print("If you finish inserting spaces, enter it twice '0'")
	
        x = int(input("Give the beginning of space: "))
        y = int(input("Give the end of space: "))
	
        if x<y:
            list.append([x,y])
        elif x>y:
            print("Error, please try again!")
        elif x==0 and y==0:        
            break	

    list.sort()

    sum = int(list[0][1]-list[0][0])


    for i in range(1,len(list)):
    
        if list[i][0]>list[i-1][1]:
            sum+= (list[i][1]-list[i][0])
        else:
            if list[i][1]>list[i-1][1]:
                sum= sum + (list[i][1]-list[i-1][1])
		
    print( 'The sum of the lengths of the intervals is: ' , sum)
    print("Press 'ENTER' to retrieve a list.")
    answer=str(input())
    if answer!="": 
        break
