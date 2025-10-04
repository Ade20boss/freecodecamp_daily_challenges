def is_pangram(sentence, letters):
    sentence_list = []
    sentence = ' '.join(sentence).lower()
    for i in sentence:
        if i.isalpha():
            sentence_list.append(i)
    sentence = ''.join(sentence_list)
    letters = letters.lower()
    count_letters = len(letters)
    count_sentence = len(sentence)
    for i in letters:
        if i not in sentence:
            return False
        if i in sentence:
            if sentence.count(i) > letters.count(i):
                extra1 = letters.count(i)
                extra = sentence.count(i)
                count_sentence -= extra
                count_letters -= extra1
                continue
            count_letters -= 1
            count_sentence -= 1
    if count_sentence == 0 and count_letters == 0:
        return True
    else:
        return False

print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))
