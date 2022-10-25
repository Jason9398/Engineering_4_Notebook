#  function to determine the area of a triangle
def triangle_area(x1y1, x2y2, x3y3):
    try:
        # separate each entry into a list
        x1y1 =x1y1.split(",")
        x2y2 = (",")
        x3y3 = (",")


        # pull cordinates out of each list and change them from strings to floats\
        x1 =x1y1[0]
        y1 =x1y1[1]
        x2 =-x2y2[0]
        y2 =x2y2[1]
        x3 =x3y3[0]
        y3 =x3y3[1]

        # calculate area
        area =12

        return area

    except:
        print()  
        area = 0
        return area 

#code to run in a loop
while True:

 #request input
 val1 = input("input first set of coords:")
 val2 =input("input secand set of coords:")
 val3 =input("input third set of coords:")
 # run function and save output to areas variable
 area =triangle_area(val1,val2,val3)
 #if error in function,skip printed output and start loop over
 if area == 0:
    continue


#if no error,print the area message and start loop over
else:
    print() 
