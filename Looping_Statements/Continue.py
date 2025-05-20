
                                                      #Continue statement


# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# It can be used in both for and while loops.
# When the continue statement is encountered, the remaining code in the loop for that iteration is skipped, and control is transferred to the next iteration of the loop.
# Syntax:
# continue


i=1
while i<10:
    i=i+1
    if i == 5:
        continue
    print(i)


#output
# 2
# 3
# 4
# 6
# 7
# 8
# 9
#10