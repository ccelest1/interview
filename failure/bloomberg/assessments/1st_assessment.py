"""
we are given sentences per page
(1) return page occurrences per page, no discussion about words occurring multiple times on single page
(2) then return order of frequencies sorted
"""


def sort_freqs(pages):
    tracker = {}
    freq = {}
    for i in range(len(pages)):
        page = pages[i][0]
        words = pages[i][1].split(" ")
        for word in words:
            if word not in tracker:
                tracker[word] = []
            tracker[word].append(page)
            freq[word] = len(tracker[word])

    sortedf = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sortedf


input1 = [("page1", "is a page ten ten ten"), ("page2", "is a book ten ten")]
print(sort_freqs(input1))
