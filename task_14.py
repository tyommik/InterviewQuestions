""" вывод слов в обратном порядке. Слова разделены пробелами """

def string_reverse(input_string):
    words = input_string.split(" ")
    return " ".join([word[::-1] for word in words[::-1]])

print(string_reverse('Hello world'))