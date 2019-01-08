import sys

def open_file(file_name, mode):
    try:
        f = open(file_name, mode)
    except IOError as a:
        print("błąd wejscia wyjscia")
        print(a)
        input("\nAby zakonczyc nacisnij ENTER!")
        sys.exit()
    else:
        return f

def next_line(f):
    line = f.readline()
    line = line.replace("/", "\n")
    return line

def next_block(f):
    category = next_line(f)

    question = next_line(f)

    anwers = []
    for i in range(4):
        answers[i] = next_line(f)

    correct = next_line(f)
    if correct:
        correct = correct[0]

    explanation = next_line(f)

    return category, question, answers, correct, explanation





