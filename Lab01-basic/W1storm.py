print(" *** Wind classification ***")
W = float(input("Enter wind speed (km/h) : "))
if(W>=0 and W<52):
    print("Wind classification is Breeze.")
elif(W>=52 and W<56):
    print("Wind classification is Depression.")
elif(W>=56 and W<102):
    print("Wind classification is Tropical Storm.")
elif(W>=102 and W<209):
    print("Wind classification is Typhoon.")
elif(W>=209):
    print("Wind classification is Super Typhoon.")
