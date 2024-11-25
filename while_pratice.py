print("  x ", end="")
for x in range(1,10):
    print(" %2d "%x,end="")
print()

for x in range(1,10):
    print(" %2d "%x, end="")
    for y in range(1,10):
        print(" %2d "%(x*y),end="")
    print()