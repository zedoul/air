matrix = (
    (0, ('L','R','0')),
    (('L','0','R'), 0),
)
#matrix = (
#    (0, ('0'), ('L','R')),
#    (('L'),0,('0')),
#    (('R','L'),('0'),0),
#)

# v_from : int
# e_from : char ['L','R','0']
def linked_edge(v_from, e_from):
    assert(int == type(v_from))
    assert(e_from in ['L','R','0'])
    v_to = None
    e_to = None
    # connection information of v_from
    conns = [(index,connection) for (index,connection) in enumerate(matrix[v_from]) if connection != 0]
    for conn_ind, conn_e in conns :
        for e_i, e in enumerate(conn_e):
            if e == e_from :
                v_to = conn_ind
                e_to = matrix[v_to][v_from][e_i]
                break
    return v_to, e_to
    

v_from = 0
e_from = 'L'
v_to, e_to = linked_edge(v_from, e_from)

print v_to, e_to
#v_from = 0
#e_from_out = 2
#for b in enumerate(a[0]):
#    print b
#
#print conns
#(1, ('L', 'R', '0'))
#n = conns[0][1][e_from_out] #'0'
#
#v_to = conns[0][0]
#e_to = a[v_to][v_from]
#print e_to


