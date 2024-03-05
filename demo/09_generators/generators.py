
def myrange(start, end):
    pos = start
    while pos <= end:
        yield pos
        pos += 1

print([x for x in myrange(0, 5)])

def alphabet():
    pos = ord('A')
    end = ord('Z')
    while pos <= end:
        yield chr(pos)
        pos += 1

alphagen = alphabet()

print(alphagen.__next__())

