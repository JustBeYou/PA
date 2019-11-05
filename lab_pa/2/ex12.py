sir = input()
oglindit = sir[::-1]

def op(sir1, sir2):
    while sir1[-1] == sir2[0]:
        print ("{} <op> {} = ".format(sir1, sir2), end='')
        c = sir1[-1]
        while sir1 != '' and sir1[-1] == c:
            sir1 = sir1[:-1]
        while sir2 != '' and sir2[0] == c:
            sir2 = sir2[1:]
        if sir1 == "" or sir2 == "":
            break

    ret = sir1 + sir2
    print ("{} + {} = {}".format(sir1, sir2, ret))
    return ret

ret1 = op(sir, oglindit)
ret2 = op(oglindit, sir)
