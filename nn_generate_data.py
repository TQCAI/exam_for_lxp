import numpy as np
from pathlib import Path
import random as rd
import numpy.random as nd

def forward(x,W,b):
    return W.dot(x)+b

def generate(n_bound,m_bound,data_bound):
    n=rd.randint(1,n_bound)
    m=rd.randint(1,m_bound)
    x=nd.randint(0,data_bound,(n,1))
    b=nd.randint(0,data_bound,(m,1))
    W=nd.randint(0,data_bound,(m,n))
    y=forward(x,W,b)
    return  n,m,x,W,b,y
# print("u")
for i in range(10):
    n,m,x,W,b,y = generate(100, 100, 10)
    def to_flat_list(a):
        a = a.flatten()
        a = a.tolist()
        return a
    y=to_flat_list(y)
    x=to_flat_list(x)
    b=to_flat_list(b)
    with open(f'nn_data/Test{i + 1:02}.in', 'w+') as f:
        print(n,m, file=f)
        print(*x, file=f)
        for row in W:
            row = to_flat_list(row)
            print(*row, file=f)
        print(*b, file=f)

    with open(f'nn_data/Test{i+1:02}.ans','w+') as f:
        print(*y,file=f)



    

