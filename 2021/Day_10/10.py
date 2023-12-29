import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def sum_syntax_error_score(data):
    points = {')':3, ']':57, '}':1197, '>':25137}
    closed = {'}':'{', ']':'[', ')':'(', '>':'<'}
    score = 0
    for s in data:
        stack = []
        for c in s:
            if c in closed:
                # found incorrect closing character
                if stack and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    score += points[c]
                    break
            # append open character
            else:
                stack.append(c)
    return score

data = parse_data(file)
print(f"The sum of syntax error scores is {sum_syntax_error_score(data)}.")

def get_incomplete(data):
    closed = {'}':'{', ']':'[', ')':'(', '>':'<'}
    corrupted = set()
    for i,s in enumerate(data):
        stack = []
        for c in s:
            if c in closed:
                # found incorrect closing character
                if stack and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    corrupted.add(i)
                    break
            # append open character
            else:
                stack.append(c)
    incomplete = []
    for i, s in enumerate(data):
        if i in corrupted: continue
        incomplete.append(s)
    return incomplete

def get_sequences(incomplete):
    closed = {'}':'{', ']':'[', ')':'(', '>':'<'}
    sequences = []
    for s in incomplete:
        stack = []
        for c in s:
            if c in closed:
                # found incorrect closing character
                if stack and stack[-1] == closed[c]:
                    stack.pop()
            # append open character
            else:
                stack.append(c)
        sequences.append(stack[:])
    return sequences

def get_middle_score(sequences):
    points = {'(':1, '[':2, '{':3, '<':4}
    scores = []
    for s in sequences:
        score = 0
        for c in s[::-1]:
            score = (score * 5)  + points[c]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

incomplete = get_incomplete(data)
sequences = get_sequences(incomplete)

print(f"The middle score is {get_middle_score(sequences)}.")