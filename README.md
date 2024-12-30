# DataStructures With Python
각 자료구조는 Jupyter Notebook 형식으로 코드와 함께 설명이 포함되어 있습니다. 

[한국외국어대학교 컴퓨터공학부 신찬수 교수님의 강의](https://www.youtube.com/@ChanSuShin)를 듣고 학습한 내용을 실습하는데 목적을 두고 있습니다. 감사합니다.




## 목록
#### Linear Data Structures
- [Stack](####Stack)
- Queue
- Deque
- Single Linked List
- Circular Doubly Linked List

#### Non-linear Data Structures
- Hash Table
- Binary Tree
- Heap
- Binary Search Tree
- AVL Tree



## 본문
### Linear Data Structures
  #### Stack
<pre>
<h1>
Stack
</h1>

                    [][][][][][][a] <- First in

                    [a][][][][][][] -> Last out



First In Last Out,FILO 형식으로 삽입 시 들어온 순서대로 데이터가 쌓이지만, 삭제 시 최근 들어온 순서부터 나가는 자료 구조
순차적으로 값이 삽입되며, 맨 끝값만 삭제 가능


<h1>
Stack Class
</h1>

- 필드
    

- 메서드 명세
    특수 메서드
    __init__    => 생성자 호출 시, 빈 리스트를 맴버 변수로 갖는 인스턴스 생성
    __len__     => len() 메서드를 호출하여, 리스트 클래스에서 구현한 __len__을 사용하여 리스트의 길이 호출한다.
    __str__     => 이를 구현하지 않으면, 리스트의 주소를 반환한다. 따라서 리스트 클래스에서 str()을 호출하여, 리스트 클래스에서 구현한 __str__을 사용한다.

    

    일반 메서드
    push(item)        => 리스트의 append 연산으로 맨 끝에 요소 삽입  
    pop         => pop 메서드를 통해, 가장 마지막 값 삭제
                    =>  텅 빈 경우 "Stack is empty" 메시지 반환
    top         => -1인덱스에 해당하는 값을 읽고, 해당 요소 반환
                    => 텅 빈 경우 "Stack is empty" 메시지 반환
</pre>

