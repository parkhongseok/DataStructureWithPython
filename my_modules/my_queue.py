class myQueue:
    #빈 큐와, 거짓으로 삭제된 요소의 번호를 저장할 맨 앞 인덱스 초기화
    def __init__(self) :
        self.queue = []
        self.frontIndex = 0
    # 거짓 길이 반환
    def __len__(self):
        return len(self.queue) - self.frontIndex
    # frontIndex부터 끝까지 리스트를 복사하여 문자열로 반환 비효율적인 부분인듯.. 
    def __iter__(self):
        for i in range(self.frontIndex, len(self.queue)):
            yield self.queue[i]
    def __str__(self):
        return '['+', '.join(str(i) for i in self)+']'
    #제너레이터를 통해 frontIndex부터 큐의 요소를 반환
            
            
    # 새로운 값을 맨 끝에 삽입
    def enqueue(self, item) : 
        self.queue.append(item)
    # 실제로 삭제하는 게 아니라, 시작 인덱스만 늘리는 방식으로 구현
    def dequeue(self) : 
        if self.frontIndex == len(self.queue) :
            print("*** myQueue.dequeue : Queue is empty ***")
        else :
            self.frontIndex += 1
            return self.queue[self.frontIndex - 1]
    
            

# ToDo 메모리 낭비 개선
# 1. 적당한 시점에 리스트 비우기
# 2. 리스트가 참조하는 주소값 자체를 Frontindex로 변경하여 메모리 복사 과정 없이 리스트 관리(파이썬에서 가능한가?) => 자바에선 불가능
# 3. 또는 원형 큐, 연결리스트를 이용