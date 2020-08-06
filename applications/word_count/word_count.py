def word_count(s):
    # Your code here
    # create an array of all characters to ignore
    ignore = [
        '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{',
        '}', '(', ')', '*', '^', '&', '\t', '\r', '\n'
    ]

    # start a count
    cache = {}
    # if a character from the ignore array is present in the string replace it with white space
    for character in ignore:
        s = s.replace(character, ' ')

    # split the newly cleaned & lowercase string by white space
    split_string = s.lower().split(' ')

    # iterate through the new split string
    for word in split_string:
        # if the word is an empty space, skip it
        if word == '':
            pass
        # if the word isn't present in cache then add it
        elif word not in cache:
            cache[word] = 1
        # otherwise increment
        else:
            cache[word] += 1
    print(cache)
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            'This is a test of the emergency broadcast network. This is only a test.'
        ))
