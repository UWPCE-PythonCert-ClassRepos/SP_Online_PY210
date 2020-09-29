import sys
print("This is my first python program")

version = sys.version_info
version_string = "{}.{}".format(version.major, version.minor)
if version.major == 3:
    if version.minor not in (6, 7):
        print("You should be running version 3.6 or 3.7")
    else:
        print("You are running python{} -- all good!".format(version_string))
else:
    print("You need to run Python 3!")
    print("This is version: {}".format(version_string))