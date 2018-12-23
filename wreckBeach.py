import ISexception


def wreckMain(stair, stamina):
    maxstam = wreckRecursive(stair, stamina, -1)
    print(maxstam)
    if maxstam < 1:
        raise ISexception.InsufficientStaminaException
    return maxstam


def wreckRecursive(stair, stamina, index):
    length = len(stair)
    if index+1 >= length:
        return stamina

    maxStamina = wreckRecursive(stair, stamina-stair[index+1], index+1)
    if index+2 < length:
        tempStamina = wreckRecursive(stair, stamina-stair[index+2]-1, index+2)
    else:
        tempStamina=stamina-1

    if tempStamina > maxStamina:
        maxStamina = tempStamina

    if index+3 < length:
        tempStamina = wreckRecursive(stair, stamina-stair[index+3]-2, index+3)
    else:
        tempStamina=stamina-2

    if tempStamina > maxStamina:
        maxStamina = tempStamina
    return maxStamina

