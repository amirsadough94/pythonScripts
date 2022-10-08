l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c']


def myZip(*input_data):
    seq = [list(s) for s in input_data]
    res = []
    while all(seq):
        res.append(tuple(s.pop(0) for s in seq))
    return res


def myPad(*input_data, **kargs):
    pad = kargs.get("pad", None)
    seq = [list(s) for s in input_data]
    res = []
    while any(seq):
        res.append(tuple(s.pop(0) if s else pad for s in seq))
    return res


def myPad_gen(*input_data, **kargs):
    pad = kargs.get("pad", None)
    seq = [list(s) for s in input_data]
    while any(seq):
        yield tuple(s.pop(0) if s else pad for s in seq)


print(list(myPad_gen(l1, l2, pad='?')))
