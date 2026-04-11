class Member :
    def __init__ (self, name, track, num) :
        self.name = name
        self.track = track
        self.num = num

class Lion(Member) :
    def __init__ (self) :    
        name = input("🦁 이름:") 
        #임시 변수로 저장하고 부모한테 넘겨서 부모가 self.name처럼 저장
        #둘다 self.name으로 저장하면 중복됨. 사용X, 자식클래스는 그냥 임시 저장만
        if not name:
            raise ValueError("오류!! 이름을 다시 입력해주세요.")
        track = input("📚 트랙:") #1.먼저 이름, 트랙, 기수의 값을 받고
        num = input("🎓 기수:")
        num = num.replace("기","") #'기'를 빼고 num을 받음...
        if num == "":
            raise ValueError("기수를 입력해주세요.")
        try:
            num = int(num)
        except ValueError: #int("num") 변환을 실패하면 파이썬이 자동으로 ValueError를 발생시킴
            raise ValueError("기수에는 숫자를 입력해주세요.")
        if num <= 0:
            raise ValueError("기수는 양수여야 합니다.")
        super().__init__(name, track, num) #2. 그 값을 부모한테 전달함

    def get_info(self):
        return ('- 🦁 아기사자 : {0} | {1} | {2}기'.format(self.name,self.track,self.num))

class Staff(Member) :
    def __init__ (self) :
        name = input("🧑‍🏫 이름:")
        if not name:
            raise ValueError("오류!! 이름을 다시 입력해주세요.")
        super().__init__(name,track = "운영진", num = None)
        #Staff클래스에서 이름만 필요하더라도 super로 넘겨줄 때는 없는 건 None으로 넘겨줌.
        #super().__init__(name) <- 이렇게 적으면 안됨

    def get_info(self): #자기자신을 가르키는 self
        return(f'- 🧑‍🏫 운영진 : {self.name} | {self.track}')

class Printer:
    def print_all (self, members):
        for m in members:
            print(m.get_info())

babylion= []
all_staff= []


while (True) :

    print("📌 기능을 선택하세요\n1️⃣  아기사자 등록\n2️⃣  운영진 등록\n3️⃣  전체 출력\n4️⃣  종료")
    select = int(input("👉 선택:"))

    if select == 1:
        lion = Lion() #새로운 아기사자 객체 생성
        babylion.append(lion) #리스트 추가할 때는 무조건 append 쓰기
        print("✅ 아기사자가 등록되었습니다.\n")
    elif select == 2:
        staff = Staff()
        all_staff.append(staff)
        print('✅ 운영진이 등록되었습니다.\n')
    elif select == 3:
        printer = Printer() #새로운 printer 객체 생성
        print('📋 멤버 목록')
        printer.print_all(babylion)
        printer.print_all(all_staff)
        print('\n')
    else:
        print('👋 프로그램을 종료합니다.')
        break