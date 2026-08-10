

    def levelOrder(self,root):
        from collections import deque

        queue = deque([root])

        while queue:
            node = queue.popleft()

            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
