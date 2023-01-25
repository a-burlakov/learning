from collections import Counter


def codewars(text):
    text = ''.join([s if s.isalpha() or s == "'" else ' ' for s in text])
    words = ''.join([s for s in text.lower() if s.isalpha() or s in " '"]).split()
    words = filter(lambda word: not all([x == "'" for x in word]), words)
    return [s for s, a in Counter(words).most_common(3)]


result = codewars("AGU:/AGU?:!AGU_!/.;AGU::/ ;AGU;AGU:-;-:AGU. :AGU.__?,AGU;:_-AGU!: AGU;??AGU/.:!AGU.AGU .AGU/_/,:")
print(result)
result = codewars("  '''  ")
print(result)
