class Member:
    def __init__(self, name):
        if not name: 
            raise ValueError("이름이 비어있습니다. 이름을 다시 입력하세요.")
        self.name = name

    def get_role(self):
        return "멤버"

    def get_info(self):
        return f"{self.get_role()} : {self.name}"

class Lion(Member):
    def __init__(self, name, track, generation):
        if not track:
            raise ValueError("트랙이 비어있습니다.")
        if not generation or not generation.isdigit(): 
            raise ValueError("기수가 비어있거나 잘못된 값입니다.")
        
        super().__init__(name)
        self.track = track
        self.generation = int(generation)

    def get_role(self):
        return "아기사자"

    def get_info(self):
        return f"{self.get_role()} : {self.name} | {self.track} | {self.generation}기"

class Staff(Member):
    def get_role(self):
        return "운영진"

    def get_info(self):
        return f"{self.get_role()} : {self.name} | 관리자"

class NameSorter:
    def sort(self, members):
        return sorted(members, key=lambda x: x.name)

class ConsolePrinter:
    def display(self, members, sorter=None):
        print("\n--- 멤버 목록 ---")
        
        display_list = sorter.sort(members) if sorter else members
        
        if not display_list:
            print("등록된 멤버가 없습니다.")
            return

        for member in display_list:
            print("-", member.get_info())

members = []
printer = ConsolePrinter() # 출력 전담 객체 생성
name_sorter = NameSorter() # 정렬 전담 객체 생성

def add_lion():
    try:
        name = input("이름 : ")
        track = input("트랙 : ")
        gen = input("기수 : ")
        members.append(Lion(name, track, gen))
        print("등록 완료!")
    except ValueError as e:
        print(f"오류 : {e}")

def add_staff():
    try:
        name = input("이름 : ")
        members.append(Staff(name))
        print("등록 완료!")
    except ValueError as e:
        print(f"오류 : {e}")

while True:
    print("\n1. 아기사자 등록 | 2. 운영진 등록 | 3. 전체 출력(이름순) | 4. 종료")
    choice = input("선택 : ")

    if choice == "1":
        add_lion()
    elif choice == "2":
        add_staff()
    elif choice == "3":
        printer.display(members, sorter=name_sorter)
    elif choice == "4":
        break
    else:
        print("다시 선택하세요.")