# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

def copy_a_file(filename, filename2):
    try:
        text = open(filename, "r")
        t = text.read()
        text2 = open(filename2, "r")
        t2 = text2.read()
        text2 = open(filename2, "w")
        text2.write(t)
        text.close()
        text2.close()
    except TypeError:
        print("No destination is provided")

print(copy_a_file("new.txt", "old.txt"))
