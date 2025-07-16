# Practice 1:

def myFunc():
    print("Hello world")
myFunc()

# Practice 2:
if __name__ == '__main__':
    # If this code is excuted by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)

# Output:
# Hello world
# __main__