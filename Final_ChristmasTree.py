""" Final_ChristmasTree  """
def fff():
    """ Final_ChristmasTree  """
    aaa = int(input())
    bbb = int(input())
    num = 1
    numm = aaa-1
    ooo = 0
    while num <= aaa:
        print(" "*(numm)+"*"*((num*2)-1))
        if num == 1:
            ooo = numm-1
        numm -= 1
        num += 1
    for i in range(bbb):
        print(" "*(ooo)+"---")
fff()
