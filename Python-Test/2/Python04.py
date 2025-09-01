# Create a set of numbers {1,2,3,4,5} and another {4,5,6,7,8}.
# Print their union, intersection, and difference.
import subprocess
import time

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
subprocess.run("cls", shell=True)
time.sleep(0.2)
print("\n\n","Union : ",set1.union(set2),"\n\n")
print("\n\n","Intersection : ",set1.intersection(set2),"\n\n")
print("\n\n","Difference : ",set1.difference(set2),"\n\n")
