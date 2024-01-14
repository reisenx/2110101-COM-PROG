#import h1, m1 and s1 as integer variable
#Initial time is in this format h1 : m1 : s1
h1=int(input())
m1=int(input())
s1=int(input())

#import h2, m2 and s2 as integer variable
#Final time is in this format h2 : m2 : s2
h2=int(input())
m2=int(input())
s2=int(input())

#Convert the hours, minutes and second into only seconds
#Example 01:20:30 is equal to 4,830 seconds
t1=(h1*3600)+(m1*60)+s1
t2=(h2*3600)+(m2*60)+s2

#Find the difference between initial time and final time in seconds
#Need to plus 24 hours before subtracting to make sure that there's no negative results
#And need to modulo with 24 hours to make sure that the results won't exceed 24 hours
dt=((24*3600)+t2-t1)%(24*3600)

#Convert from seconds into the format dh:dm:dt
dh=dt//3600
dt=dt-(dh*3600)
dm=dt//60
dt=dt-(dm*60)
ds=dt

#Output
print(str(dh)+":"+str(dm)+":"+str(ds))