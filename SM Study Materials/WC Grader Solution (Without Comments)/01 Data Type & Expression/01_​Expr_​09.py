def str2hms(hms_str):
    h,m,s = hms_str.split(':')
    return int(h),int(m),int(s)

def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:] + ':' + ('0'+str(s))[-2:]

def to_sec(h,m,s):
    return (h*3600) + (m*60) + s

def to_hms(s) :
    h = s//3600
    s = s-(h*3600)
    m = s//60
    s = s-(m*60)
    return h,m,s

def diff(h1,m1,s1,h2,m2,s2):
    t1 = (h1*3600) + (m1*60) + s1
    t2 = (h2*3600) + (m2*60) + s2
    dt = ((24*3600) + t2 - t1) % (24*3600)
    dh = dt//3600
    dt = dt - (dh*3600)
    dm = dt//60
    dt = dt - (dm*60)
    ds = dt
    return dh,dm,ds

def main():
    hms_start = input()
    hms_end = input()
    h1,m1,s1 = str2hms(hms_start)
    h2,m2,s2 = str2hms(hms_end)
    dh,dm,ds = diff(h1,m1,s1,h2,m2,s2)
    time = hms2str(dh,dm,ds)
    print(time)

exec(input())