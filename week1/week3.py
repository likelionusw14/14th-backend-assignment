# 부모 클래스
class Member:
    def __init__(self, name):
        if not name:
            raise ValueError("이름이 필요합니다.")
        self.name = name

    def get_role(self):
        return self.role


class AddUser:
    def __init__(self, name, track):
        self.name = name
        self.track = track


class Printer:
    def print_member(self, member):
        raise NotImplementedError("하위 클래스에서 구현하세요.")


# 역할 영역
class Lion(Member):
    role = "아기사자"

    def __init__(self, name, track, generation):
        super().__init__(name)

        if not track:
            raise ValueError("트랙이 필요합니다.")
        if not generation or generation <= 0:
            raise ValueError("잘못된 기수입니다.")

        self.track = track
        self.generation = generation


class Staff(Member):
    role = "운영진"

    def __init__(self, name, track, position):
        super().__init__(name)

        if not track:
            raise ValueError("트랙이 필요합니다.")
        if not position:
            raise ValueError("포지션이 필요합니다.")

        self.track = track
        self.position = position


# 멤버 추가 영역
class AddLion(AddUser):
    def __init__(self, name, track, generation):
        super().__init__(name, track)

        if not generation or generation <= 0:
            raise ValueError("잘못된 값입니다.")
        self.generation = generation


class AddStaff(AddUser):
    def __init__(self, name, track, position):
        super().__init__(name, track)

        if not position:
            raise ValueError("포지션 필요")
        self.position = position


class MemberFactory:
    def create_lion(self, dto):
        return Lion(dto.name, dto.track, dto.generation)

    def create_staff(self, dto):
        return Staff(dto.name, dto.track, dto.position)


# 출력 영역
class LionPrinter(Printer):
    def print_member(self, member):
        print(f"[{member.get_role()}] 이름: {member.name} / 트랙: {member.track} / 기수: {member.generation}")


class StaffPrinter(Printer):
    def print_member(self, member):
        print(f"[{member.get_role()}] 이름: {member.name} / 트랙: {member.track} / 포지션: {member.position}")


class PrinterManager:
    def __init__(self):
        self.printers = {
            Lion: LionPrinter(),
            Staff: StaffPrinter()
        }

    def print_all(self, members):
        for member in members:
            printer = self.printers[type(member)]
            printer.print_member(member)

# 정렬 영역
class SortAllPolicy:
    def sort(self, members):

        def sort_key(m):
            # 아기사자
            if isinstance(m, Lion):
                return (
                    0,                 
                    m.generation,      
                    m.track,           
                    m.name             
                )

            # 운영진
            if isinstance(m, Staff):
                role_priority = {
                    "대표": 0,
                    "팀장": 1
                }

                priority = role_priority.get(m.position, 2)

                return (
                    1,         
                    priority,  
                    m.name
                )

        return sorted(members, key=sort_key)
   
# 메인
def main():
    members = []
    factory = MemberFactory()
    printer_manager = PrinterManager()
    sort_policy = SortAllPolicy()

    while True:
        print("\n===== 멤버 관리 프로그램 =====")
        print("1. 아기사자 추가")
        print("2. 운영진 추가")
        print("3. 전체 출력")
        print("4. 종료")

        choice = input("기능 선택: ").strip()

        try:
            if choice == "1":
                name = input("이름: ").strip()
                track = input("트랙: ").strip()
                generation = int(input("기수: ").strip())

                dto = AddLion(name, track, generation)
                lion = factory.create_lion(dto)
                members.append(lion)

                print("아기사자가 등록되었습니다.")

            elif choice == "2":
                name = input("이름: ").strip()
                track = input("트랙: ").strip()
                position = input("포지션(예: 대표, 팀장, 운영진): ").strip()

                dto = AddStaff(name, track, position)
                staff = factory.create_staff(dto)
                members.append(staff)

                print("운영진이 등록되었습니다.")

            elif choice == "3":
                if not members:
                    print("등록된 멤버가 없습니다.")
                else:
                    sorted_members = sort_policy.sort(members)
                    printer_manager.print_all(sorted_members)

            elif choice == "4":
                print("프로그램을 종료합니다.")
                break

            else:
                print("올바른 기능 번호를 입력하세요.")

        except ValueError as e:
            print(f"입력 오류: {e}")


if __name__ == "__main__":
    main()
    
