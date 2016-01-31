def numberWordCount():
    singles = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    singlesCount = 0
    for word in singles:
        singlesCount += len(word)

    tenCount = len('ten')

    multTens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    multTensCount = 0
    for word in multTens:
        multTensCount += len(word)

    teens = ['eleven', 'twelve', 'thir', 'four', 'fif', 'six', 'seven', 'eigh', 'nine']
    teensCount = 0
    for word in teens:
        teensCount += len(word)
    teensCount += len('teen') * 7

    doublesCount = 10*multTensCount + tenCount + teensCount
    
    andCount = len('and')

    hundredCount = len('hundred')
    
    thousandCount = len('oneThousand')

    allCount = 190*singlesCount + 10*doublesCount + 891*andCount + 900*hundredCount + thousandCount

    return allCount

print(numberWordCount())
    
    
    
