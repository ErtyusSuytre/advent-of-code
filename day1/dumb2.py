print(sum([int(str([x.index(min(x)) for x in [[min(digit, word) for digit, word in zip([line.find(num) if num in line else len(line) for num in ['one','two','three','four','five','six','seven','eight','nine']],[line.find(num) if num in line else len(line) for num in ['1','2','3','4','5','6','7','8','9']])]]][0]+1)+str([x.index(min(x)) for x in [[min(digit, word) for digit, word in zip([line[::-1].find(num) if num in line[::-1] else len(line) for num in ['eno','owt','eerht','ruof','evif','xis','neves','thgie','enin']],[line[::-1].find(num) if num in line[::-1] else len(line) for num in ['1','2','3','4','5','6','7','8','9']])]]][0]+1)) for line in open('input.txt').readlines()]))