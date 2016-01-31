def getNbrWaysToMakeChange(amount, pieces):
    piecesLen = len(pieces)
    if piecesLen == 1:
        return 1

    curNbr = 0
    while amount >= 0:
        curNbr += getNbrWaysToMakeChange(amount, pieces[1:])
        amount -= pieces[0]
    
    return curNbr