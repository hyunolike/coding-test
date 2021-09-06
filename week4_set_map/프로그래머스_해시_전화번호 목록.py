def solution1(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    
    for n1 in phone_book:
        for n2 in phone_book:
            if n1 == n2[:len(n1)] and n1 != n2:
                answer = False
                return answer
    
    return answer

def solution2(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True


from collections import defaultdict
def solution3(phone_book):
    hash_map = defaultdict(int)
    
    for p in phone_book:
        hash_map[p] += 1
    
    for phone_number in phone_book:
        tmp = ''
        for t in phone_number:
            tmp += t
            if tmp in hash_map.keys() and tmp != phone_number:
                return False
    
    return True