# file = open('not_correct.txt', 'a', encoding='utf-8')
file = open('not_correct.txt', 'r+', encoding='utf-8')

# n = [str(i) for i in range(3123)]
# s = ''.join(n)
print(file.read())

file.close()

print('-' * 10)


def create_file_with_numbers(n):
    open(f'range_{n}.txt', 'w').writelines(''.join(map(str, range(1, n + 1))))


# create_file_with_numbers(100)

print('-' * 10)

from string import punctuation


def longest_word_in_file(file_name):
    text = open(file_name, 'r+', encoding='utf-8').read()
    for i in punctuation:
        text = text.replace(i, '')
    text = text.split()
    m = max([len(i) for i in text])
    return [i for i in text if len(i) == m][-1]


print(longest_word_in_file('range_100.txt'))

print('-' * 10)


def technical_and_two_digit_sums(file_name):
    with open(file_name, 'r', encoding='utf-8') as text:
        text = text.read()
        text = text.split()
        print(text)
        text = [i for i in text if i.isdigit()]
        print(len([int(i) for i in text if len(str(i)) == 3]))
        print(sum([int(i) for i in text if len(str(i)) == 2]))


technical_and_two_digit_sums('numbers.txt')
