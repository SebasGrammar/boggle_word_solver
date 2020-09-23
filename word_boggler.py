class Tree():
    def __init__(self, letter = None):
        self.letter = letter
        self.children = {}
        self.leaf = False

    def __string__(self):
        print(self.children)

    def add(self, word):
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = Tree(letter)
            return self.children[letter].add(word)
        else:
            self.leaf = True
            return self

    def search(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]




example = Tree()
example.add("cow")
holder = ""
print(example.children)
for element in example.children:
    print(element)
    print(example.leaf)

example.search("o")


def main():
    print("Hello")

main()
