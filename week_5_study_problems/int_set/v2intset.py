class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
    
    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)
    
    def intersect(self, other):
        """Find common integers in two sets and return a new object"""
        common_numbers = set(self.vals) & set(other.vals)
        intersection = intSet()

        for number in common_numbers:
            intersection.insert(number)
        return intersection

    def __len__(self):
        """Returns the number of elements in an instance"""
        return len(self.vals)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


set1 = intSet()
set2 = intSet()

set1.insert(1)
set1.insert(2)

set2.insert(2)
set2.insert(3)
set2.insert(4)

print(set1.intersect(set2))
print(len(set2))