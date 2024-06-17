# This is the driver code that uses the hardwareSet class that you are writing.
import hardwareSet

# Create object hwSet1 of class hardwareSet with capacity of 250
hwSet1 = hardwareSet.hardwareSet()
print("Total capacity of units:", hwSet1.get_capacity())

hwSet1.initialize_capacity(250)
# print initial capacity units of hardware set 1
print("Total capacity of units:", hwSet1.get_capacity())

# print number of available units of hardware set 1
print("Number of available units:", hwSet1.get_availability())

# Create a list of two test items
test = [20, 300]
# Run the test for all items in the test list
for i in test:

    err = hwSet1.check_out(i)
    # if function returns error code 0, it means we were able to checkout requested number of units, else we were
    # not able to check out requested number of units
    if (err == 0):
        # print number of units available after checkout
        print("Number of units available after checking out",
              i, "units:", hwSet1.get_availability())
        # print number of checkout units
        print("Number of total checkedout units",
              hwSet1.get_capacity()-hwSet1.get_availability())
    else:
        # print number of units available after checkout
        print("Number of units available after checking out",
              i, "units:", hwSet1.get_availability())
        # print number of checkout units
        print("Number of total checkedout units",
              hwSet1.get_capacity()-hwSet1.get_availability())
        print("Could not check out requested number of units")

# checkin 180 units
err=hwSet1.check_in(180)
# print number of units available after checkin
if (err==0):
    print("Number of units available after checking in 180 units:",
    hwSet1.get_availability())
else:
    print("Could not check in ", 180, "units")

# checkin 100 units
err=hwSet1.check_in(180)
# print number of units available after checkin
if (err==0):
    print("Number of units available after checking in 100 units:",
    hwSet1.get_availability())
else:
    print("Could not check in ", 100,  "units")
    