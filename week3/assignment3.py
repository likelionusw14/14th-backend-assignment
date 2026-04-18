class Member:

    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "멤버"
    
    #자식 클래스에서 오버라이딩 진행됨ㅁ
    def get_info(self):
        return f"self.name"

class Lion(Member):
    def __init__(self, name, track, generation):
        super().__init__(name)
        self.track = track
        self.generation = generation

    def get_role(self):
        return "아기사자"
    
    def get_info(self):
        return f"{self.name} / {self.track} / {self.generation}"
    
class Staff(Member):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "운영진"
    
    def get_info(self):
        return f"{self.name} / 운영진"

#리스트    
members = []

while True:
    print("\n 기능을 선택하세요")
    print("1 아기사자 등록")
    print("2 운영진 등록")
    print("3 전체 출력")
    print("4 종료")

    choice = input("선택: ")

    if choice == "1":
        name = input("이름: ")
        track = input("트랙: ")
        generation = input("기수: ")

        lion = Lion(name, track, generation)
        members.append(lion)

        print("아기사자가 등록되었습니다.")

    elif choice == "2":
        name = input("이름: ")

        staff = Staff(name)
        members.append(staff)

        print("운영진이 등록되었습니다")

    elif choice == "3":
        print("\n 멤버 목록")
        for m in members:
            print(f"- {m.get_role()} : {m.get_info()}")

    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
