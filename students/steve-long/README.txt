
Python code for UWPCE-PythonCert class, written by Steve Long

The following is an update of the verification test. The original was
not aware of version 3.8.



import sys
print("This is NOT my first python program")

print("UW Python210 version verification\nModified from original script on 2020.09.09")

version = sys.version_info
version_string = "{}.{}".format(version.major, version.minor)
if version.major == 3:
    if version.minor not in (6, 7, 8):
        print("You should be running version 3.6, 3.7, or 3.8")
    else:
        print("You are running python{} -- all good!".format(version_string))
else:
    print("You need to run Python 3!")
    print("This is version: {}".format(version_string))