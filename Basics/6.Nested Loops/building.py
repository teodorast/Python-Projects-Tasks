number_of_floors = int(input())
number_of_rooms = int(input())

for current_floor in range(number_of_floors, 0, -1):
    
    for current_room in range(0,number_of_rooms):
        
        if current_floor == number_of_floors:
            print("L{0}{1} ".format(current_floor,current_room), end= "")
        elif current_floor%2==0:
            print("O{0}{1} ".format(current_floor,current_room), end= "")
        elif current_floor%2==1:
            print("A{0}{1} ".format(current_floor,current_room), end= "")
        current_room+=1
    current_floor+=1
    print("")








    
     
        


    





            
        

         
 