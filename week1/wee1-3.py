# member 클래스
class Member:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("이름을 입력해 주세요.")
        self.name = name
    
#Lion 클래스
class Lion(Member):
    def __init__(self, name, track, gen):
        super().__init__(name)
        if not (gen.endswith("기") and gen[:-1].isdigit()):
            raise ValueError("기수 형식이 올바르지 않습니다 (예: 14기).")
        self.track = track
        self.gen = gen

    def get_role(self):
        return "아기사자"
    
    def get_info(self):
        return f"{self.role} : {self.name} | {self.track} | {self.gen}"
    
#Staff 클래스
class Staff(Lion):
    def get_role(self):
        return "운영진"
    
    def get_info(self):
        return f"{self.role} : {self.name} | get_role"
    

class print_member:
    def print(self, member):
        print(" 멤버 목록")
        for i in member:
            print(f"- {i.get_role()} : {i.get_info()}")

class sorted_name_member:
    def sort(self,member):
        return sorted(member, key =lambda x: x.name)


# 1. 아기사자 등록 
def add_lion(member):
    name = input("이름을 입력하세요: ").strip()
    track = input("트랙을 입력하세요: ")
    gen = input("기수를 입력하세요: ").strip()
    lion = Lion(name,track,gen)
    member.append(lion)
    print("아기사자가 등록되었습니다. \n")

def add_admin(member):
    name = input("이름: ").strip()
    admin = Member(Staff(name))
    print("운영진이 등록되었습니다!")


#출력  
def print_menu(member):
    while True:
        print("기능을 선택하세요")
        print("1.아기사자 등록")
        print("2.운영진 등록")
        print("3.전체 출력")
        print("4.종료")

        choice = input("선택: ")

        if choice == '1':
            add_lion(member)
        
        elif choice == '2':
            add_admin(member)
        
        elif choice == '3':
            print_member.print(sorted_name_member(member))
        
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break





member = []
print_menu(member)

