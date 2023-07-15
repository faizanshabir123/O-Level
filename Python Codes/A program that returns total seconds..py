def main():
    racehours=int(0)
    print (racehours)
    racemins=int(0)
    print (racemins)
    racesec=int(0)
    print (racesec)
    totalseconds = 0
    print("enter time in hours, mins, secs")
    racehours = (input("input hours"))
    racemins = (input("input minutes"))
    racesec = (input("input seconds"))
    totalseconds = (3600*racehours) + (60*racemins) + (racesec)
    print (totalseconds)
    
main()
