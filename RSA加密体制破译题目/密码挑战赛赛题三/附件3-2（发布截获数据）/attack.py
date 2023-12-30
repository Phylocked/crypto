m, N, e, c = [], [], [], []
j = 0
filename = ['Frame' + str(i) for i in range(21)]
for i in range(21):
    fd = open(filename[i], 'r')
    m.append(fd.read())
    fd.close()
for frame in m:
    N.append(frame[0:256])
    e.append(frame[256:512])
    c.append(frame[512:768])
    print( 'Frame', j)
    print( 'N=', frame[0:256])
    print( 'e=', frame[256:512])
    print( 'c=', frame[512:768])
    print( '\n')
    j += 1

