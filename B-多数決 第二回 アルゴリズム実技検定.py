vote = input()

a = vote.count("a")
b = vote.count("b")
c = vote.count("c")

if a > b:
    if a > c:
        print("a")
    else:
        print("c")
elif b > c:
    print("b")
else:
    print("c")