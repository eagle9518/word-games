class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def load_words():
    with open('words.txt') as word_file:
        valid_words = set()
        for word in word_file:
            valid_words.add(word.replace("\n", "").lower())

    return valid_words

def wordhunt():
    root = TrieNode()
    res = set()

    def create_trie():
        for word in english_words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_word = True

    create_trie()

    def read_input():
        grid_input = input("Grid: ")
        grid = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid_input[4*i+j])
            grid.append(row)
        return grid

    grid = read_input()

    def graph_traversal():
        ROWs = 4
        COLs = 4

        def path(row, col, seen, node, word):
            if node.is_word and len(word) >= 3:
                res.add(word)

            if ((row, col) in seen or
                row < 0 or col < 0 or
                row >= ROWs or col >= COLs or
                grid[row][col] not in node.children):
                return
            
            letter = grid[row][col]
            seen_copy = seen.copy()
            seen_copy.add((row, col))

            dirs = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]]
            for x, y in dirs:
                path(row+x, col+y, seen_copy, node.children[letter], word + letter)



        for r in range(ROWs):
            for c in range(COLs):
                path(r, c, set(), root, "")

    graph_traversal()
    return list(res)


def anagrams():
    english_words = load_words()
    data = input("Enter Characters: ")
    res = set()

    cur = []
    def subsets(perm, index):
        if index >= len(perm):
            word = "".join(cur.copy())
            if len(word) >= 3 and word in english_words:
                res.add(word)
            return
        
        cur.append(perm[index])
        subsets(perm, index+1)
        cur.pop()
        subsets(perm, index+1)


    def permutations(c):
        if len(c) == 0:
            return [""]
        perms = permutations(c[1:])
        res = []
        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm
                perm_copy = perm_copy[:i] + c[0] + perm_copy[i:]
                res.append(perm_copy)
        return res
    
    for i in permutations(data):
        subsets(i, 0)
    
    return list(res)
    
    
if __name__ == '__main__':
    english_words = load_words()
    def run_anagrams():
        res = anagrams()
        res.sort(reverse=True, key=len)
        print(res)

    def run_wordhunt():
        res = wordhunt()
        res.sort(reverse=True, key=len)
        print(res)
    
    run_wordhunt()