from collections import Counter

n = int(input())

books = []

for _ in range(n):
  book = input()
  books.append(book)

books.sort()

print(*list(zip(*Counter(books).most_common(1)))[0])
