
                                                  #Break statement


# The break statement is used to exit a loop prematurely, regardless of the loop's condition.
# It can be used in both for and while loops.
# When the break statement is encountered, the loop is terminated immediately, and control is transferred to the next statement following the loop.
# # Syntax:
# # break
#
# # Example:

i=1
while i < 20:
    print(i)
    if i == 10:
        break
    i=i+1

print("Loop terminated at i =", i)

#output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Loop terminated at i = 10
