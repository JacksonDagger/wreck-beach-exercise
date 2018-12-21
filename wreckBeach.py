def wreckMain(stair, stamina):
    return wreckRecursive(stair, stamina, -1)


def wreckRecursive(stair, stamina, index):
    length = len(stair)
    if index >= length:
        return stamina

    maxStamina = wreckRecursive(stair, stamina-stair[index+1], index+1)
    if index+1 < length:
        tempStamina = wreckRecursive(stair, stamina-stair[index+2]-1, index+2)
        if tempStamina > maxStamina:
            maxStamina = tempStamina
    if index+2 < length:
        tempStamina = wreckRecursive(stair, stamina-stair[index+3]-2, index+3)
        if tempStamina > maxStamina:
            maxStamina = tempStamina
    return maxStamina

