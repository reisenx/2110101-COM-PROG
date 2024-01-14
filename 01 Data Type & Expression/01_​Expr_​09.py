#Create str2hms(hms_str) function
#This function can convert a string in format "HH:MM:SS" to and 3 integers which are t[0],t[1],t[2]
def str2hms(hms_str):
    t=hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])

#Create hms2str(h,m,s) function
#This function can convert a 3 integers h,m,s to a string in the format HH:MM:SS
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:] + ':' + ('0'+str(s))[-2:]

#Create to_sec(h,m,s) function
#This function can convert the hours, minutes and second into only seconds
#Example 01:20:30 is equal to 4,830 seconds
def to_sec(h,m,s):
    return (h*3600)+(m*60)+s

#Create to_hms(s) function
#This function can convert seconds into hours, minutes and second
#Example 4,830 seconds is equal to 01:20:30
def to_hms(s) :
    h=s//3600
    s=s-(h*3600)
    m=s//60
    s=s-(m*60)
    return h,m,s

#Create diff(h1,m1,s1,h2,m2,s2) function
#This function can find difference between 2 times
#Input time is in the format h,m,s
#Output is also in the format h,m,s
def diff(h1,m1,s1,h2,m2,s2):
    t1=(h1*3600)+(m1*60)+s1
    t2=(h2*3600)+(m2*60)+s2
    dt=((24*3600)+t2-t1)%(24*3600)
    dh=dt//3600
    dt=dt-(dh*3600)
    dm=dt//60
    dt=dt-(dm*60)
    ds=dt
    return dh,dm,ds

#Create main() function
#This function can find difference between 2 times
#Input time is in the format HH:MM:SS
#Output is also in the format HH:MM:SS
def main():
    hms_start = input()
    hms_end = input()
    h1,m1,s1 = str2hms(hms_start)
    h2,m2,s2 = str2hms(hms_end)
    dh,dm,ds = diff(h1,m1,s1,h2,m2,s2)
    time = hms2str(dh,dm,ds)
    print(time)

#Execute the input string
exec(input())