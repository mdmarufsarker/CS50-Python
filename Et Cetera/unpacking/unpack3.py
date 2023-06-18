def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# using list
coins = [100, 50, 25]

print(total(*coins), "Knuts")