print(" *** Wind classification ***")
W = float(input("Enter wind speed (km/h) : "))
if(W<0):
    print("!!!Wrong value can't classify.")
if(W>=0 and W<52):
    print("Wind classification is Breeze.")
if(W>=52 and W<56):
    print("Wind classification is Depression.")
if(W>=56 and W<102):
    print("Wind classification is Tropical Storm.")
if(W>=102 and W<200):
    print("Wind classification is Typhoon.")
elif(W>=209):
    print("Wind classification is Super Typhoon.")
