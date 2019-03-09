"""
Homework02 exercise1  spam problem for CS 344 at Calvin College
@author: Chan kIm
@date: 03/08/2019
"""
import collections


class Spam:

    def __init__(self, bad, good):
        # merges lists in the list into one list.
        self.bad = []
        for i in bad:
            for j in i:
                self.bad.append(j)
        self.good = []
        for i in good:
            for j in i:
                self.good.append(j)
        # creates dictionaries - keys as texts in each list and values as the number of each text.
        # uses collections.Counter to count number of each text and to make a hash table.
        self.bad_hash = collections.Counter(self.bad)
        self.good_hash = collections.Counter(self.good)
        # counts the number of nonspam and spam messages.
        # In this case, there are two messages in each good and bad corpus.
        self.nbad = len(bad)
        self.ngood = len(good)
        # merge two dictionaries into one for prob
        merge = self.good_hash.copy()
        merge.update(self.bad_hash)
        prob = merge
        # calculates the probability that an email containing it is a spam
        # and stores the value
        for i in list(merge.keys()):
            g = 2 * self.good_hash[i]
            b = self.bad_hash[i]
            if g + b > 0:
                prob[i] = max(0.01, min(0.99, min(1.0, b / self.nbad)
                                        / (min(1.0, g / self.ngood)
                                        + min(1.0, b / self.nbad))))
            else:
                prob[i] = 0
        self.prob = prob

    def spam_filtering(self, corpus):
        prod = []
        never_seen = 0.4
        # compares the words in corpus to prob and stores the word's probabilities
        for i in corpus:
            if i in self.prob:
                prod.append(self.prob[i])
            else:
                prod.append(never_seen)
        prods = 1
        not_prods = 1
        # calculates the combined probability
        for i in prod:
            prods *= i
            not_prods *= (1 - i)
        calc = prods / (prods + not_prods)
        # treats mail as spam if a probability is more than 0.9
        if calc > 0.9:
            return print("The combined probability: " + str(calc) +
                         "\tThis is spam.\n")
        else:
            return print("The combined probability: " + str(calc) +
                         "\tThis isn't spam.\n")


if __name__ == '__main__':
    spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
    ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

    # Initialize the spam case
    spam = Spam(spam_corpus, ham_corpus)

    # test cases
    test1 = ["i", "spam"]
    test2 = ["do", "i", "like", "green", "eggs", "spam", "I", "do", "not", "like", "that", "spamiam", "but", "bacon"]
    test3 = ["do", "I", "like", "bacon", "tomato", "egg",  "and", "spam"]
    test4 = ["do", "i", "like", "spam"]
    spam.spam_filtering(test1)
    spam.spam_filtering(test2)
    spam.spam_filtering(test3)
    spam.spam_filtering(test4)
