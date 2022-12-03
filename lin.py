import matplotlib.pyplot as plt

def train(x,y):
    n=len(x)
    sx=0
    sy=0
#sum of x
    for i in range(0,len(x)):
        sx=sx+x[i]

# sum of y
    for i in range(0,len(y)):
        sy=sy+y[i]

#sum square x
    ssx=0
    for i in range(0,len(x)):
        s=x[i]**2
        ssx=ssx+s

#mul of xany
    r=0
    for i in range(0,len(x)):
        xy=x[i]*y[i]
        r=r+xy     
    print("your model Trained ")    
    j=sx*sx
    k=ssx*n
    l=sy*sx
    m=r*n
    o=j-k
    p=l-m
    b=p/o
    a=sx*b
    d=sy-a
    g=d/n
    return g , b

def predict(z,g,b):
     return g+b*z
     

def fit(a,b,x,y,q,m):
    w=list()
    for i in range(0,len(x)):
         n=predict(x[i],a,b)
         w.insert(i, n)
         
    plt.xlabel(q)
    plt.ylabel(m)
    plt.scatter(x, y)
    plt.plot(x, w, color='green')
  
    plt.show()
def sct(x,y,q,w):
    plt.scatter(x, y,)
    plt.xlabel(q)
    plt.ylabel(w)
    plt.show()

