from my_modules.tree.my_node import Node
class BinaryTree:
    def __init__(self, key=None):
        self.root = Node(key)
        self.size = 0 if self.root.key is None else 1
        self.height = 0
    
    def __len__(self):
        return self.size

    # 이터러블 제너레이터
    def __iter__(self):
        yield from self._preorder(self.root)
        
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
                lines.append(f"───── {node}(h={node.height})")
            else:
                lines.append(prefix + ("├──── " if is_left else "└──── ") + f"{node}(h={node.height})")
                
            if node.left or node.right:
                if node.left:  # 왼쪽 자식이 있는 경우
                    lines.extend(self._build_tree_structure(node.left, prefix + ("│     " if not is_root and is_left else "      "), True, False))
                else:  # 왼쪽 자식이 없으면 None을 출력
                    lines.append(prefix + ("│     " if not is_root and is_left else "      ") + "├──── None")
                    
                if node.right:  # 오른쪽 자식이 있는 경우
                    lines.extend(self._build_tree_structure(node.right, prefix + ("│     " if not is_root and is_left else "      "), False, False))
                else:  # 오른쪽 자식이 없으면 None을 출력
                    lines.append(prefix + ("│     " if not is_root and is_left else "      ") + "└──── None")
        return lines

    def __str__(self):
        return  "\n".join(self._build_tree_structure(self.root))
    
    # 인스턴스 메서드
    def insertLeft(self, Node, NewNode):
        Node.left = NewNode
        NewNode.parent = Node
        self.size += 1
        self.updateHeight(Node)
        
    def insertRight(self, Node, NewNode):
        Node.right = NewNode
        NewNode.parent = Node
        self.size += 1
        self.updateHeight(Node)
        # 루트노드가 None인 경우에 대한 예외처리는 상속받은 메서드에서 구현함

    # 노드 v의 높이를 수정
    def updateNodeHeight(self, v):
        # v가 존재한다면,
        if v:
            # 해당 노드의 자식이 존재하는지 검사 후, 자식 중에 더 깊이 뻗어있는 자식을 선택해서 현재 높이를 업데이트
            l = v.left.height if v.left else -1
            r = v.right.height if v.right else -1
            # 최대 높이를 가진 자식보단 본인이 한칸 더 크니까
            v.height = max(l, r) + 1

    # v부터 root가지 올라가면서 모든 노드 정보 업데이트
    # 노드를 삽입할 때마다 호출한다면, 언제나 리프노드부터 루트까지 존재하는 높이들을 업데이트 가능
    def updateHeight(self, v):
        # v가 루트노드에 도달할때까지 
        while v != None:
            # 높이를 갱신하고, 부모노드로 현재노드 이동
            self.updateNodeHeight(v)
            v = v.parent
        self.updateTreeHeight()

    def updateTreeHeight(self):
        if self.root.key is not None:
            self.height = self.root.height
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
        
    def printInfo(self, msg=None):
        if msg is not None:
            print("*** " + msg + " ***")
        print(self)
        self.info()