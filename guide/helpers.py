def neighbors(sequence):
    for i in range(len(sequence) - 1):
        yield sequence[i:i+2]

assert(list(neighbors('AABB')) == ['AA', 'AB', 'BB']) 
