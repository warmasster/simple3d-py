# simple3d-py
Library to make simple 3d objects

# How to use simple3d
In order to use it you will need numpy,
fist you have to import simple3d

in your code:
 ```
import simple3d as d3
 ```
then you need to call the simple3d class and the Cube function (The only one avilable in this moment) and store it in a variable

in your code:
 ```
simple = d3.simple3d()
cube = simple.Cube(X size,Y size ,Z size, [Cords X,cords Y],D)
```
then a varible inside the simple object will store all the cordinates of the vertexes of the cube

Final Example:

```
import simple3d as d3
import numpy as np

// This will work as our screen
screen = np.empty((16,16), dtype="str")
screen[:] = ' '

// Creating the cube
simple = d3.simple3d()
cordscubo = simple.Cube(8,5,5, [5,5],20)

// Drawing the cube
for i in simple.vproyec:
    screen[i[0]][i[1]] = "#"
print(screen)
```

# To do list

+ Add edges to the cube
+ Add new 3d objects function
+ Add custom 3d object function
