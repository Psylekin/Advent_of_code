import numpy as np
import pandas as pd
import re

# claims are structured like this: 
# Nr.,Startpoint horizont, startpoint vertical, length horizontal, length vertical

def connection_test():
    return 1

def overlap_counter(argument):
    counter = 0
    return counter

def clear_claim(dirtyClaim):
    editedClaim = dirtyClaim.replace(" ", "").lstrip("#")
    cleanClaim = re.sub(r"\D", ",", editedClaim)
    return cleanClaim

claimList = [line.rstrip('\n') for line in open('project1/input.txt')]
fabric = pd.DataFrame(int(0), index=np.arange(1, 1000), columns=np.arange(1000))


# Take a claim, add 1 to every number he claims
# Count for fields where the claimcounter is > 1

