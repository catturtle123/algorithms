import bisect

def solution(words, queries):
    
    words_list = {}
    reverse_words_list = {}

    for i in words:
        reverse_word = i[::-1]
        word_len = len(i)
        if word_len in words_list:
            words_list[word_len].append(i)
            reverse_words_list[word_len].append(reverse_word)
        else:
            words_list[word_len] = [i]
            reverse_words_list[word_len] = [i[::-1]]

    for i in words_list.values():
        i.sort()

    for i in reverse_words_list.values():
        i.sort()

    result = []
    for i in queries:
        l = len(i)
        if l not in words_list:
            result.append(0)
            continue
        
        if i[0] != "?":
            a = i.replace("?", "a")
            z = i.replace("?", "z")

            start = bisect.bisect_left(words_list[l], a)
            end = bisect.bisect_right(words_list[l], z)

            result.append(end - start)

        else:
            a = i[::-1].replace("?", "a")
            z = i[::-1].replace("?", "z")

            start = bisect.bisect_left(reverse_words_list[l], a)
            end = bisect.bisect_right(reverse_words_list[l], z)

            result.append(end - start)


    return result