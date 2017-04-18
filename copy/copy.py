# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

def copy_a_file(filename, filename2):
    text = open(filename, "w")
    t = text.readlines()
    text2 = open(filename2, "r")
    t2 = text2.readlines()
    text = text2
    text.close()
    text2.close()


print(copy_a_file("new.txt", "old.txt"))
