print("Demonstration of *ARGS\n\n")

def add(a, *args):
    su=a
    print("My First Variable:"+str(a))
    print("\nEntered Numbers\n")
    for arg in args:
        print("->"+str(arg))
    for arg in args:
        su=su+arg
    print("\nThe Sum is:"+str(su))
    
add(1,2,3,4,5,5,6)

print("\n\nDemonstration of **KWARGS")
    
def dic(**dictionary):
    print("\n")
    for key,value in dictionary.items():
        print(key+":"+value)
        
dic(first="LetsUpgrade", Middle="is", Last="Great!!!")
