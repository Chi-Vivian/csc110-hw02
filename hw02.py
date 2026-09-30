# ------------------------------------------------------
#        Name: Vivian Nguyen
#       Peers: 
#  References: 
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    user_x = input("Give me x: ")
    a = int(user_x)
    user_y = input("Give me y: ")
    b = int(user_y)
    return a,b
    #function reads user inputs in docstring, then convert them into ints,and return both variables

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult_result = a*b
    print("mult result:", mult_result)
    add_result = a+b
    print("add result:", add_result)
    return mult_result/add_result
    # function computes a*b and a+b, prints both of the results, and returns (a*b)/(a+b)

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("*" *16)
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("=" *16)
    #print top border of 16 asterisks, prints input values and multadd results, then print the bottom border of 16 equal signs

def main ():
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x,y = read_two_ints()
    #invoke read_two_ints() and unpack values into x and y
    
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x, y)
    #call compute_multadd(x,) and assigned the float output to xy_multadd

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x,y,xy_multadd)
    #call print_fancy with x, y, and xy_multadd to output final results

    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
