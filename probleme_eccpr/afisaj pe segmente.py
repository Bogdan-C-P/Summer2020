v=[]
while True:
    p=[]
    j=""
    x=input()

    if x == '\n':
        break
    for i in x:
        j+=i
    for c in j.split(","):
        p.append(c)
    y=0
    if p == ["1", "1", "1", "1", "1", "1", "0", "0"]:
        y="0"
    elif p == ["1", "1", "1", "1", "1", "1", "0", "1"]:
        y = "0."
    elif p== ["0","1","1","0","0","0","0","0"]:
        y="1"
    elif p== ["0","1","1","0","0","0","0","1"]:
        y="1."
    elif p == ["1","1","0","1","1","0","1","0"]:
        y="2"
    elif p == ["1","1","0","1","1","0","1","1"]:
        y="2."
    elif  p == ["1","1","1","1","0","0","1","0"]:
        y="3"
    elif  p == ["1","1","1","1","0","0","1","1"]:
        y="3."
    elif  p == ["0","1","1","0","0","1","1","0"]:
        y="4"
    elif  p == ["0","1","1","0","0","1","1","1"]:
        y="4."
    elif  p == ["1","0","1","1","0","1","1","0"]:
        y="5"
    elif  p == ["1","0","1","1","0","1","1","1"]:
        y="5."
    elif  p == ["1","0","1","1","1","1","1","0"]:
        y="6"
    elif  p == ["1","0","1","1","1","1","1","1"]:
        y="6."
    elif  p == ["1","1","1","0","0","0","0","0"]:
        y="7"
    elif  p == ["1","1","1","0","0","0","0","1"]:
        y="7."
    elif  p == ["1","1","1","1","1","1","1","0"]:
        y="8"
    elif  p == ["1","1","1","1","1","1","1","1"]:
        y="8."
    elif  p == ["1","1","1","1","0","1","1","0"]:
        y="9"
    elif  p == ["1","1","1","1","0","1","1","1"]:
        y="9."
    else:
        break
    v.append(y)

for i in v:
    print(i, end="")
