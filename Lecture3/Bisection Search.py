## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/Week_2/videosequence:Lecture_3/
print("Please think of a number between 0 and 100!")
high = 100
low = 0
guessed = False

while not guessed:
    ans = (high + low)/2
    print("Is your secret number " + str(ans) + "? ")

    fbk = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if fbk == "h":
        high = ans
    elif fbk == "l":
        low = ans
    elif fbk == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
