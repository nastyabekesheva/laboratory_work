bintree = [[0, 4], [4, 2], [2, 1], [1, 3]]
visited = set()

def preorder(bintree):
    for i in bintree:
        if i[1] not in visited:
            if i[0] not in visited:
                print(i[0], end = " ")
                visited.add(i[0])
            print(i[1], end = " ")
            visited.add(i[1])

def postorder(bintree):
    for i in bintree[::-1]:
        if i[0] not in visited:
            if i[1] not in visited:
                print(i[1], end = " ")
                visited.add(i[1])
            print(i[0], end = " ")
            visited.add(i[0])
 
def main():
    preorder(bintree)
    print("\n")
    visited.clear()
    postorder(bintree)

main()
