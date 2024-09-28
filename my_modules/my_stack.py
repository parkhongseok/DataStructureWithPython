class myStack:
    # 빈 스택을 초기화
    def __init__(self) -> None:
        self.stack = []
    # 리스트의 요소 맨 끝에 새로운 요소 삽입
    def push(self, item):
        self.stack.append(item)
    # 리스트의 가장 마지막 요소 삭제
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError :
            print("Stack is empty")
    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            print("Stack is empty")
        
    # 리스트 클래스에서 구현된 len()함수를 호출 후 반환
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)