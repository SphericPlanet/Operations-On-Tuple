t = (1,"Gauransh",99.9, ["Maths","Science"],(98,97))
print(t)

print("First Element:",t[0])
print("Second Element:",t[1])
print("Nested Index:",t[3][1])


#Tuple Is Immutable
##t.append(1)
###t[0] = 2

print("Slicing:", t[4:5])

for i in t:
    print(i)