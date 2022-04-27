# List cs contains the N widths of the N columns of the chessboard
# List rs contains the N heights of the N rows of the chessboard
# Remember, board coloring starts with top left cell => WHITE
# and then alternates with BLACK as in a usual chessboard.
def white_black_areas(cs, rs):
    # return a 2-element tuple, (total_white_area, total_black_area)
    total_white_area=0
    total_black_area=0
    #you want to get the total area of both white and black
    #to do this create two separate funcs to get each area
    pass
    total_white_area=do_white_area(cs,rs)
    total_black_area=do_black_area(cs,rs)
    check_area(total_white_area, total_black_area, cs, rs)
        
    return total_white_area,total_black_area

def do_white_area(cs, rs):
    area=[]
    #match white value columns to white row values
    for c in range(len(cs)):
        for r in range(len(rs)):
            #if you get an odd column, multiple it to odd row values
            #if you get an even column, multipy it to even row values.
            if((c+1)%2==0 and (r+1)%2==0):
                area.append(cs[c] * rs[r])
            elif((c+1)%2 > 0 and (r+1)%2 > 0):
                area.append(cs[c] * rs[r])
    #print("White Area: ",area)
    print("Sum: ", sum(area))
    return sum(area)

def do_black_area(cs, rs):
    area=[]
    #match black column values to black row values
    for c in range(len(cs)):
        for r in range(len(rs)):
            #if you get an odd column, multiple it to even row values
            #if you get an even column, multipy it to odd row values.
            if((c+1)%2==0 and (r+1)%2>0):
                area.append(cs[c] * rs[r])
            elif((c+1)%2 > 0 and (r+1)%2 == 0):
                area.append(cs[c] * rs[r])
    #print("Black Area: ",area)
    print("Sum: ", sum(area))
    return sum(area)

def check_area(white_area, black_area, cs, rs):
    print("Sum of cs and rs areas: ",sum(cs)*sum(rs))
    if(white_area + black_area == sum(cs)*sum(rs)):
        print(True)
        return
    print(False)