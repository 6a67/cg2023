import numpy as np

center = [4,2,-6,1]

points = []

for x in [4,-4]:
    for y in [4,-4]:
        for z in [4,-4]:
            point = [center[0]+x, center[1]+y, center[2]+z, center[3]]
            print(point)
            points.append(point)

print("="*40)

p_std_matrix = np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,-1,0]])

points = np.array(points)

dehomogenized = []

for p in points:
    print("Multiply")
    print(p_std_matrix)
    print("with")
    print(p)
    print("to get")
    newp = np.matmul(p_std_matrix, p)
    print(newp)
    print("Dehomogenize to get")
    newp = newp/newp[3]
    print(newp)
    dehomogenized.append(newp)
    print("="*20)


print("="*40)

print("Dehomogenized points:")

for d in dehomogenized:
    print(d)

# show points in 2D graph
import matplotlib.pyplot as plt

x = []
y = []

for d in dehomogenized:
    x.append(d[0])
    y.append(d[1])

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.axis('equal')
plt.grid(True)

plt.plot([x[0],x[1]],[y[0],y[1]], color='r')
plt.plot([x[0],x[2]],[y[0],y[2]], color='r')
plt.plot([x[0],x[4]],[y[0],y[4]], color='r')
plt.plot([x[1],x[3]],[y[1],y[3]], color='r')
plt.plot([x[1],x[5]],[y[1],y[5]], color='r')
plt.plot([x[2],x[3]],[y[2],y[3]], color='r')
plt.plot([x[2],x[6]],[y[2],y[6]], color='r')
plt.plot([x[3],x[7]],[y[3],y[7]], color='r')
plt.plot([x[4],x[5]],[y[4],y[5]], color='r')
plt.plot([x[4],x[6]],[y[4],y[6]], color='r')
plt.plot([x[5],x[7]],[y[5],y[7]], color='r')
plt.plot([x[6],x[7]],[y[6],y[7]], color='r')

plt.scatter(x,y)
plt.show()