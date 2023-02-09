import numpy as np
import cmath

# these matrix values correspond to mess
# BIBC = np.array(
#     [
#     [1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0],
#     [0, 0, 1, 1, 0, 1],
#     [0, 0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, -1],
#     [0, 0, 0, 0, 0, 1],
#     ]
# )
# BCBV = np.array(
#     [
#     [0.279 + 0.015j, 0             , 0             ,              0, 0              , 0             ],
#     [0.279 + 0.015j, 0.444 + 0.439j, 0             ,              0, 0              , 0             ],
#     [0.279 + 0.015j, 0.444 + 0.439j, 0.864 + 0.751j,              0, 0              , 0             ],
#     [0.279 + 0.015j, 0.444 + 0.439j, 0.864 + 0.751j, 0.864 + 0.751j, 0              , 0             ],
#     [0.279 + 0.015j, 0.444 + 0.439j, 0             ,              0,  1.374 + 0.774j, 0             ],
#     [0             , 0             , 0.864 + 0.751j, 0.864 + 0.751j, -1.374 + 0.774j, 0.896 + 0.155j]
#     ]
# )
# print(np.matmul(BCBV,BIBC))

dlf = np.array([
        [0.279 + 0.015j, 0.279 + 0.015j, 0.279 + 0.015j, 0.279 + 0.015j, 0.279 + 0.015j ],
        [0.279 + 0.015j, 0.723 + 0.454j, 0.723 + 0.454j, 0.723 + 0.454j, 0.723 + 0.454j ],
        [0.279 + 0.015j, 0.723 + 0.454j, 1.587 + 1.205j, 1.587 + 1.205j, 0.723 + 0.454j ],
        [0.279 + 0.015j, 0.723 + 0.454j, 1.587 + 1.205j, 2.451 + 1.956j, 0.723 + 0.454j ],
        [0.279 + 0.015j, 0.723 + 0.454j, 0.723 + 0.454j, 0.723 + 0.454j, 2.097 + 1.228j ]
    ])
# print(dlf)

nodes = 6
branches = 5
p = np.array([0, 1572, 1936, 189, 1336])
q = np.array([0,  174,  312,  63,  112])
Vs = 11+0j #kV
V = np.empty(nodes-1,dtype=complex)
V.fill(Vs)
error = np.empty(nodes-1)
error.fill(1e9)
current = np.empty(nodes-1)
iter_count = 1

while(max(error)>1e-5):
    #compute load current at each node

    #compute [delta V]

    #update node voltage

    #compute error vector

    #keep printing the values obtained
