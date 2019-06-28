import numpy as np
import pandas as pd
import re
import time

# claims are structured like this: 
# Nr.,Startpoint horizont, startpoint vertical, width , hight

def connection_test():
    return 1

def clear_claim(dirtyClaim):
    editedClaim = dirtyClaim.replace(" ", "").lstrip("#")
    cleanClaim = re.sub(r"\D", ",", editedClaim).split(",")
    for index, value in enumerate(cleanClaim): cleanClaim[index] = int(value)
    return cleanClaim

def claim_fabric_piece(fabric,clearClaimList):
    for claim in clearClaimList:
        for width in range(claim[3]):
            for hight in range (claim[4]):
                fabric.iloc[claim[1] + width, claim[2] + hight] += 1
    return fabric

def count_overlapping_claims(fabric):
    return fabric[fabric > 1].count().sum()

def find_nonoverlapping_claim(fabric, claims):
    for claim in clearClaimList:
        claimFabric = claimedFabric.loc[claim[1] : claim[1] + claim[3], claim[2] : claim[2] + claim[4]]
        if count_overlapping_claims(claimFabric) == 0:
            return claim[0]

start = time.time()

claimList = [line.rstrip('\n') for line in open('advent_of_code/3/project1/input.txt')]
clearClaimList = list(map(lambda x: clear_claim(x) ,claimList))
fabric = pd.DataFrame(int(0), index=np.arange(1, 1000), columns=np.arange(1000))
claimedFabric = claim_fabric_piece(fabric, clearClaimList)

print(count_overlapping_claims(claimedFabric))
print(find_nonoverlapping_claim(fabric, clearClaimList))
print("{}".format(time.time() - start))