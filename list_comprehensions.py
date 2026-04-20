weights = []
for i in range(1,11) :
    w =int(input())
    weights.append(w)
healthy = [w for w in weights if 60 <= w <= 80 ]
print(healthy)