class Subsets:

    def __int__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2

    def unique(self):
        return "Unique Subsets are ", self.set1.intersection(self.set2)


# Set Literal - {} or set([])

obj = Subsets()
obj.set1 = {4, 7, 5, 1, 2, 4, 8, 5}
obj.set2 = {2, 4, 3, 5, 3, 2, 5, 8, 9}

print(obj.unique())
