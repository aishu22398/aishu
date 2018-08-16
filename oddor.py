a=raw_input()
a=a.split()
frst=int(a[0])
sec=int(a[1])
for i in range(frst+1,sec):
    if(i%2==1):
        print i,
