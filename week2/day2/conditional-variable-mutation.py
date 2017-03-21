a = 24
out = 0

if a % 2 == 0:
    out = out
else:
    out += 1
print(out)

b = 2
out2 = ""

if 10 < b < 20:
    out2 = "Sweet!"
if b < 10:
    out2 = "More!"
if b > 20:
    out2 = "Less!"
print(out2)

c = 123
credits = 100
is_bonus = False

if credits >= 50 and is_bonus == False:
    c -= 2
if credits < 50 and is_bonus == False:
    c -= 1
if is_bonus == True:
    c = c
print(c)

d = 8
time = 120
out3 = ""

if d/4 == d//4 and time <= 200:
    out3 = "check"
if time > 200:
        out3 = "Time out"
if d/4 != d//4:
    out3 = "Run Forest Run!"
print(out3)
