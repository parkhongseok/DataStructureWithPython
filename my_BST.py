class Node:
    def __init__(self, key):
        self.key = key
        self.height = 0
        self.parent = None
        self.left = None
        self.right = None

    # preorder 방식으로 순회
    def __iter__(self):
        if self != None:
            if self.left != None:
                for leftSubTree in self.left:
                    yield leftSubTree
            yield self
            if self.right != None: 
                for rightSubTree in self.right:
                    yield rightSubTree

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = self.updateTreeHeight()
        
    def updateTreeHeight(self):
        self.height = max(i.height for i in self.root) if self.root != None else 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.root:
            return ("\n").join("h"+str(i.height)+" : "+str(i) for i in self.root)
        else:
            return "empty"

    def preorder(self, v):
        if v != None:
            print(v, end=" ")
            if v.left != None:
                self.preorder(v.left)
            if v.right != None:
                self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            if v.left != None:
                self.inorder(v.left)
            print(v, end=" ")
            if v.right != None:
                self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            if v.left != None:
                self.postorder(v.left)
            if v.right != None:
                self.postorder(v.right)
            print(v, end=" ")

    def findLocation(self, key):
        # 들어있는 자리를 찾거나, 내가 들어갈 자리를 확인 후, 부모를 호출(그래야 부모의 자식으로 연결할 수 있으니까)
        # 근데 애초에 빈 트리면 부모도 내자리도 아무것도 없으니 None
        if self.size == 0: return None
        # running tech을 사용하여, 어떤 노드 v와 v의 부모노드인 p를 동시에 찾는다.
        p = None 
        v = self.root
        # v가 None이 되면 
        while v:
            # key값이 일치하는 v를 찾았다면 반환
            if v.key == key:
                return v
            # 찾고자 하는 key가 v의 key값보다 크다면 오른쪽 탐색
            elif v.key < key:
                p = v
                v = v.right
            # 찾고자 하는 key가 v보다 작으면 왼쪽 탐색
            else:
                p = v
                v = v.left
        # while문을 빠져나왔다는 것은, 찾고자 하는 key를 가진 v가 존재하지 않고, 해당 노드가 들어갈 자리만 찾았다는 말
        # 따라서 v가 들어갈 수 있는 자리의 부모노드 반환
        return p
    
    # 사실 findLocation의 일정부분까지만 사용하면 search를 구현할 수 있지만, 코드의 재사용성을 위해 
    # 왜냐면 해당 노드를 찾는다고 해도, key값이 들어갈 자리의 부모를 찾기 위해 똑같은 걸 반복해야하니까.
    def search(self, key):
        #findLocation을 호출하여, 해당 key가 들어가있거나, 들어갈 자리의 부모노드를 호출(만약 아무것도 없으면 None)
        p = self.findLocation(key)
        if p and p.key == key:
            return p
        else: 
            return None
    # 노드 v의 높이를 수정
    def update_node_height(self, v):
        # v가 존재한다면,
        if v:
            # 해당 노드의 자식이 존재하는지 검사 후, 자식 중에 더 깊이 뻗어있는 자식을 선택해서 현재 높이를 업데이트
            l = v.left.height if v.left else -1
            r = v.right.height if v.right else -1
            # 최대 높이를 가진 자식보단 본인이 한칸 더 크니까
            v.height = max(l, r) + 1

    # v부터 root가지 올라가면서 모든 노드 정보 업데이트
    # 노드를 삽입할 때마다 호출한다면, 언제나 리프노드부터 루트까지 존재하는 높이들을 업데이트 가능
    def update_height(self, v):
        # v가 루트노드에 도달할때까지 
        while v != None:
            # 높이를 갱신하고, 부모노드로 현재노드 이동
            self.update_node_height(v)
            v = v.parent
        self.updateTreeHeight()
        
    def insert(self, key):
        p = self.findLocation(key)
        # 삽입이 가능한 경우 : 빈 노드에 첫 삽입이거나, 부모 노드가 반환된 경우
        if p == None or p.key != key:
            # print("검색 성공")
            newNode = Node(key)

            # 첫 삽입인 경우
            if p == None:
                # print("첫번째 삽입")
                self.root = newNode
            # 내가 들어갈 부모 노드를 찾은 경우
            else:
                # print("하나 이상의 노드가 존재하는 트리에 삽입 시도")
                newNode.parent = p
                # 부모보다 작은 값은 왼쪽에 삽입
                if p.key > key:
                    # print("왼쪽 자식에 연결")
                    p.left = newNode
                # 부모보다 큰 경우 오른쪽
                else:
                    # print("오른쪽 자식에 연결")
                    p.right = newNode
            self.size += 1
            self.update_height(newNode)
        # 삽입하고자 하는 key값이 이미 존재하는 경우
            return newNode   
        else:
            # print("이미 중복된 값이 존재")
            # 중복 허용 안한다면 none
            return None


    def deleteByMerging(self, key):
        x = self.search(key)
        if x == None: return None
        else: pass
        # 상황 : x를 삭제하려고 한다. (삭제할 노드를 x, x의 부모를 pt, x의 left를 a, right를 b라고 하자)
        a, b, pt = x.left, x.right, x.parent
        s = None
        # case1. a노드의 존재 유무 (x의 빈자리 쟁탈전)
        if a == None:
        # x자리에 올 노드를 c라고 부르자. (일종의 c를 두고 ab가 대결하는 구도) => a의 존재여부만 가림, b는 2차전에서 c존재 여부로 확인 
            c = b
            s = b
        else:
            # 왕좌를 차지한 a
            c = a
            # a의 가장 오른쪽 리프 노드를 찾기 위해 a의 암행어사 생성
            m = a
            # 그런 뒤에 a의 가장 오른쪽 리프노드 m을 찾고
            while m.right != None :
                m = m.right
            # b는 처절하게 m을 부모로 인정함
            if b != None:
                b.parent = m
            # b가 존재하거나 말거나, 암행어서 m은 (b를 자식으로 삼음)
            m.right=b
            s = m
        #왕좌에 앉기 게임의 1차전이 끝났고 이제 선대에게 인정받아야함
        
        # case2. 지울 노드가 root인지 여부
        if self.root != x:
            # 근데 만약 1차전에서 a도 없고 b도 없었다면 c는 None일 수도 있으니까 일단 살아있는지 확인해야함
            if c:
                # 선대를 자신의 부모로 인정함
                c.parent = pt
                # 부모도 새로운 왕을 인정함
                if  c.key < pt.key:
                    pt.left = c
                else:
                    pt.right = c
            # 근데 1차전에서 다 죽었다면 기존 x자리를 빈자리로 만들어야함
            else:
                if pt.left == x:
                    pt.left = c
                else:
                    pt.right = c  

        # 만약 지운 값이 root였다면?
        else:
            #  일단 루트 자리에 새로운 c가 옴
            self.root = c
            # c가 있다면 이전에 섬기던 왕 x를 잊고, 자신이 직접 왕이 되어야함(아무도 의지하지마..!
            if c: 
                c.parent = None
        self.size -= 1
        
        # a와 b가 모두 존재하는 경우, a의 암행어사로서, 가장 오른쪽 리프노드였던 b는 왼쪽 자식은 있었을 수도 있고, 오른쪽 자식은 없었다. (자신이 오른쪽 끝이니까)
        # 그렇다면 m의 오른자식으로 b를 붙였을 때, m의 높이 정보는 m.left와(있었다면) m.right(b를 포함한 자식들) 과 비교를 해서 쭉 root까지만 업데이트하면 된다.
        print("Unbalanced Point : ", s)
        self.update_height(s)
        return x
    
    def print_binary_tree_structure(self, node, prefix="", is_left=True):
        if node is not None:
            # 현재 노드 출력
            if self.root == node:
                print(prefix + "└── " + f"{node}(h={node.height})")
            else:
                print(prefix + ("├── " if is_left else "└── ") + f"{node}(h={node.height})")
            
            
            if node.left or node.right:
                if node.left:  # 왼쪽 자식이 있는 경우
                    self.print_binary_tree_structure(node.left, prefix + ("│    " if is_left else "     "), True)
                else:  # 왼쪽 자식이 없으면 None을 출력
                    print(prefix + ("│    " if is_left else "    ") + "└── None")
                    
                if node.right:  # 오른쪽 자식이 있는 경우
                    self.print_binary_tree_structure(node.right, prefix + ("│    " if is_left else "     "), False)
                else:  # 오른쪽 자식이 없으면 None을 출력
                    print(prefix + ("│    " if is_left else "     ") + "└── None")
                    
    def printInfo(self):
        print("\n=>  info")
        self.print_binary_tree_structure(self.root)
        # tree_structure = str(self).split("\n")  # __str__에서 나온 결과를 줄 단위로 나눔
        # for line in tree_structure:
        #     print("\n    - Tree Structure  | " + line, end="")  # 각 줄에 들여쓰기 추가
        print("\n    - Preorder        | ", end="")
        self.preorder(self.root)
        print("\n    - inorder         | ", end="")
        self.inorder(self.root)
        print("\n    - Tree height     | ", self.height)
        print("    - Number of Node  | ", self.size)