# List cs contains the N widths of the N columns of the chessboard
# List rs contains the N heights of the N rows of the chessboard
# Remember, board coloring starts with top left cell => WHITE
# and then alternates with BLACK as in a usual chessboard.
def white_black_areas(cs, rs):
   # return a 2-element tuple, (total_white_area, total_black_area)
    total_white_area=0
    total_black_area=0
    #you want to get the total area of both white and black
    #create separate lists for the total of the correct squares
    r_odd, r_even=sum(rs[::2]), sum(rs[1::2])
    c_odd, c_even=sum(cs[::2]), sum(cs[1::2])
    print("Columns and Rows: ",(r_odd, r_even), " and ", (c_even, c_odd))
    #print("Black Squares: ",(r_odd, c_odd))
    #white squares: c_odd * r_odd + r_even * c_even
    #black squares: c_odd * r_even + r_odd * c_even
    print("White Squares total: ",(c_odd * r_odd) + (r_even * c_even))
    print("Black Squares total: ",(c_odd * r_even) + (r_odd * c_even))
    total_white_area=(c_odd * r_odd) + (r_even * c_even)
    total_black_area=(c_odd * r_even) + (r_odd * c_even)
    check_area(total_white_area, total_black_area, cs, rs)
    return total_white_area,total_black_area

def check_area(white_area, black_area, cs, rs):
    print("Sum of cs and rs areas: ",sum(cs)*sum(rs))
    if(white_area + black_area == sum(cs)*sum(rs)):
        print(True)
        return
    print(False)
