# 並查集實現：https://www.nowcoder.com/practice/e7ed657974934a30b2010046536a5372
import sys

# 迭代  
def find(e):
    global father
    stack = []
    while e != father[e]:
        stack.append(e)
        e = father[father[e]]
    while stack:
        cur = stack.pop()
        father[cur] = e
    return e

# 遞迴
def find2(e):
    global father
    if e != father[e]:
        father[e] = find2(father[e])
    return father[e]

def isSameSet(a, b):
    return find(a) == find(b)

def union(a, b):
    global father
    global size
    a_father = find(a)
    b_father = find(b)
    if a_father != b_father:
        if size[a_father] <= size[b_father]:
            father[a_father] = b_father
            size[b_father] += size[a_father]
        else:
            father[b_father] = a_father
            size[a_father] += size[b_father]

def main():
    global father
    global size
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        n, m = map(int, input_buffer[line_index].strip().split())
        line_index += 1
        # 建立 father 和 size
        father = [i for i in range(n)]
        size = [1 for _ in range(n)]


        for _ in range(m):
            op, x, y = map(int, input_buffer[line_index].strip().split())
            line_index += 1

            if op == 1:
                output_buffer.append("Yes" if isSameSet(x, y) else "No")
            else:
                union(x, y)

    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()