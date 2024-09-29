emptySet = set()
print(emptySet)
print(type(emptySet))

s = set()
s.add(5)
s.add(5)
s.add(1)
s.add(3)
print(s)

s2 = {1,2,4,5,66,6,6,6,6,0}
print(s2)

s3 = {1,2,4,5,"Geet",True}
print(s3)

s4 = {0,1,True,False,1,2,0,-3} # Since True == 1 and False == 0 , thus they will be ignored whichever comes first
print(s4)

s4.remove(0) # must be a member of set
print(s4)
s4.discard(-3) # if not a member do nothing
s4.discard(-6) # if not a member do nothing
print(s4)

print(s3.uni)