import re
wordtodigit = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',}
# TODO: get rid of above somehow?!?!?

print(sum([int((re.findall(f"(?=(\\d|{'|'.join(wordtodigit.keys())}))", line)[0] if re.findall(f"(?=(\\d|{'|'.join(wordtodigit.keys())}))", line)[0].isdigit() else wordtodigit[re.findall(f"(?=(\\d|{'|'.join(wordtodigit.keys())}))", line)[0]]) + (re.findall(f"(?=(\\d|{'|'.join(wordtodigit.keys())}))", line)[-1] if re.findall(f"(?=(\\d|{'|'.join(wordtodigit.keys())}))", line)[-1].isdigit() else wordtodigit[re.findall(f"(?=(\\d|{'|'.join(wordtodigit.keys())}))", line)[-1]])) for line in open('input.txt').readlines()]))