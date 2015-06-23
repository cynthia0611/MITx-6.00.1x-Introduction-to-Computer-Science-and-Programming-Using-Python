def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
Towers(3,'f','t','s')
##s : spare
##f : from
##t : to


##t f s
##0 3 0
##------
##1 2 0
##1 1 1
##0 1 2
##1 0 2
##1 1 1
##2 1 0
##3 0 0
