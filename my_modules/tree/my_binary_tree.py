from my_modules.tree.my_node import Node

class BinaryTree:
    def __init__(self, key=None):
        self.root = Node(key)
        self.size = 0 if self.root.key is None else 1

    # 이터러블 제너레이터
    def __iter__(self):
        yield from self._preorder(self.root)
        
    def __len__(self):
        return self.size
        
    def _preorder(self, node):
        if node:
            yield node
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _inorder(self, node):
        if node:
            yield from self._preorder(node.left)
            yield node
            yield from self._preorder(node.right)
            
    def _postorder(self, node):
        if node:
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)
            yield node
    
    def preorder(self):
        yield from self._preorder(self.root)
                
    def inorder(self):
        yield from self._inorder(self.root)

    def postorder(self):
        yield from self._postorder(self.root)

    # 트리 구조 생성
    def _build_tree_structure(self, node, prefix="", is_left=True, is_root=True):
        lines = []
        if node is not None:
            if is_root:
                lines.append(f"──── {node}(root)")
            else:
                lines.append(prefix + ("├── " if is_left else "└── ") + f"{node}")
                
            if node.left or node.right:
                if node.left:  # 왼쪽 자식이 있는 경우
                    lines.extend(self._build_tree_structure(node.left, prefix + ("│    " if not is_root and is_left else "     "), True, False))
                else:  # 왼쪽 자식이 없으면 None을 출력
                    lines.append(prefix + ("│    " if not is_root and is_left else "     ") + "├── None")
                    
                if node.right:  # 오른쪽 자식이 있는 경우
                    lines.extend(self._build_tree_structure(node.right, prefix + ("│    " if not is_root and is_left else "     "), False, False))
                else:  # 오른쪽 자식이 없으면 None을 출력
                    lines.append(prefix + ("│    " if not is_root and is_left else "     ") + "└── None")
        return lines
    
    def __str__(self):
        return  "\n".join(self._build_tree_structure(self.root))
    
    # 인스턴스 메서드
    def insertLeft(self, Node, NewNode):
        Node.left = NewNode
        NewNode.parent = Node
        self.size += 1
        # print(f"[DEBUG] insertLeft: Node {Node.key}, NewNode {NewNode.key}, Size {self.size}")

    def insertRight(self, Node, NewNode):
        Node.right = NewNode
        NewNode.parent = Node
        self.size += 1
        # print(f"[DEBUG] insertRight: Node {Node.key}, NewNode {NewNode.key}, Size {self.size}")
    # 깊이우선탐색으로 이진트리의 높이 계산
    
    def getHeight(self, node):
        # 기저 조건: 노드가 None이면 높이는 0
        if node is None:
            return 0
        # 왼쪽과 오른쪽 서브트리의 높이를 재귀적으로 계산
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)
        # 노드의 높이는 왼쪽과 오른쪽 서브트리의 높이 중 큰 값 + 1
        return max(left_height, right_height) + 1

    def updateTreeHeight(self):
        if self.root.key is not None:
            self.height = self.getHeight(self.root)   
        else : 
            self.height = 0  
        return self.height

    def info(self):
        print("=>  info")
        print("    - Number of Nodes | ", self.size)
        print("    - Tree Height     | ", self.updateTreeHeight())
        print("    - Preorder        | ", *(i for i in self))
        print("    - Inorder         | ", *(i for i in self.inorder()))
        print("    - Postorder       | ", *(i for i in self.postorder()), "\n")