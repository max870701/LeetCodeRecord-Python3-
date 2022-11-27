import queue

def levelTraverse(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)

    while not q.Empty():
        size = q.qsize()
        
        for i in range(size):
            current = q.get()

            if current.left is not None:
                q.put(current.left)
            if current.right is not None:
                q.put(current.right)
