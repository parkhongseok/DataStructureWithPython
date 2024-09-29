class myQueue:
    #빈 큐와, 거짓으로 삭제된 요소의 번호를 저장할 맨 앞 인덱스 초기화
    def __init__(self) :
        self.queue = []
        self.frontIndex = 0
    # 새로운 값을 맨 끝에 삽입
    def enqueue(self, item) : 
        self.queue.append(item)
    # 실제로 삭제하는 게 아니라, 시작 인덱스만 늘리는 방식으로 구현
    # 놀고있는 공간이 실제 사용 공간보다 커지면, 실제로 데이터 삭제
    def dequeue(self) : 
        if self.frontIndex == len(self.queue) :
            print("Queue is empty")
        else :
            self.frontIndex += 1
            return self.queue[self.frontIndex - 1]
    
    # 길이 반환
    def __len__(self):
        return len(self.queue) - self.frontIndex
    # frontIndex부터 끝까지 리스트를 복사하여 문자열로 반환 비효율적인 부분인듯.. 
    def __str__(self):
        return str(self.queue[self.frontIndex:])
    #제너레이터를 통해 frontIndex부터 큐의 요소를 반환
    def __iter__(self):
        for i in range(self.frontIndex, len(self.queue)):
            yield self.queue[i]
            
''' ToDo 메모리 낭비 개선, 적당한 시점에 리스트 비우기 또는 리스트가 참조하는 주소값 자체를 Front
index로 변경하여 메모리 복사 과정 없이 매 시간 리스트 관리 '''
''' 또는 원형 큐, 연결리스트를 이용한 큐 개념 확장'''
