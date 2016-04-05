from collections import Counter
def winner(left, right):
    """
    >>> winner("AD 2D 3D 4D 5D", "6D 7D 8D 9D JD")
    'left'
    >>> winner("6D 7D 8D 9D JD", "AD 2D 3D 4D 5D")
    'right'
    >>> winner("6D 7D 8D 9D TD", "2D 3D 4D 5D JD")
    'right'
    >>> winner("2D 6D 4D 5D JH", "3D 7D 8D 9D TD")
    'right'
    >>> winner("2D 6D 4D 5D JH", "3D 7D 8D 9D TH")
    'left'
    >>> winner("2D 6D 4D 5D JH", "3D 3H 8D 9D TH")
    'right'
    """
    if not flush(left) and flush(right):
        return "right"
    elif num_pairs(right) > 0:
        return "right"
    elif max_rank(right) > max_rank(left):
        return "right"
    else:
        return "left"

def num_pairs(hand):
    """
    >>> num_pairs("3D 6D 4D 5D JH")
    0
    >>> num_pairs("3D 3H 4D 5D JH")
    1
    >>> num_pairs("2D 2H 4D 5D JH")
    1
    """
    c = Counter(hand[::3])
    return list(c.values()).count(2)

def flush(hand):
    """
    >>> flush("2D 6D 4D 5D JH")
    False
    >>> flush("3D 7D 8D 9D TD")
    True
    """
    return len(set(hand[1::3])) == 1
        

def max_rank(hand):
    """
    >>> max_rank("6D 7D 8D 9D TD")
    10
    >>> max_rank("2D 3D 4D 5D JD")
    11
    """
    ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }
    rank = 0
    for char in hand[::3]:
        rank = max(rank, ranks[char])
    return rank
