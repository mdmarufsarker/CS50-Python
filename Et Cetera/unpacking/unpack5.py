def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# using dictionary
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

