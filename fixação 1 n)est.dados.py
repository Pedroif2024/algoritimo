a=[]
for i in range(10):
    a.append(float(input(f"Degite a {i+1}°. temperatura em graus celsius:")))
a.sort()
print("a menor temperatura é:",a[0])
print("a maior temperatura é:",a[9])
print(f"a media das temperatura é:",sum[a]/10)