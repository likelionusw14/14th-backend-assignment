class Member:
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("⚠️ 이름은 비어 있을 수 없습니다.")
        self.name = name
    def get_role(self):
        pass

    def get_info(self):
        pass

class Lion(Member):
    def __init__(self, name, track, generation):
        super().__init__(name)
        if not generation or not generation.strip():
            raise ValueError("⚠️ 기수는 비어 있을 수 없습니다.")
        self.track = track
        self.generation = generation

    def get_role(self):
        return "🦁 아기사자"

    def get_info(self):
        return f"{self.name} | {self.track} | {self.generation}"

class Staff(Member):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "🧑‍🏫 운영진"

    def get_info(self):
        return f"{self.name} | 운영진"

class NameSortStrategy:
    def sort(self, members):
        return sorted(members, key=lambda x: x.name)

class MemberPrinter:
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy

    def display(self, members):
        print("\n📋 멤버 목록")
        if not members:
            print("- 등록된 멤버가 없습니다.")
            return
        
        # 정렬 정책에 따라 리스트 정렬
        sorted_members = self.sort_strategy.sort(members)
        for m in sorted_members:
            # 다형성 활용: m이 Lion인지 Staff인지 묻지 않고 동일한 메서드 호출
            print(f"- {m.get_role()} : {m.get_info()}")
        print()

class MembershipManager:
    def __init__(self):
        self.members = []
        self.printer = MemberPrinter(NameSortStrategy()) 

    def run(self):
        while True:
            print("📌 기능을 선택하세요")
            print("1️⃣  아기사자 등록\n2️⃣  운영진 등록\n3️⃣  전체 출력\n4️⃣  종료")
            choice = input("👉 선택: ")

            try:
                if choice == '1':
                    self._add_lion()
                elif choice == '2':
                    self._add_staff()
                elif choice == '3':
                    self.printer.display(self.members)
                elif choice == '4':
                    print("👋 프로그램을 종료합니다.")
                    break
                else:
                    print("⚠️ 잘못된 번호입니다.\n")
            except ValueError as e:
                print(e, "\n")

    def _add_lion(self):
        name = input("🦁 이름: ")
        track = input("📚 트랙: ")
        gen = input("🎓 기수: ")
        new_lion = Lion(name, track, gen)
        self.members.append(new_lion)
        print("✅ 아기사자가 등록되었습니다.\n")

    def _add_staff(self):
        name = input("🧑‍🏫 이름: ")
        new_staff = Staff(name)
        self.members.append(new_staff)
        print("✅ 운영진이 등록되었습니다.\n")


if __name__ == "__main__":
    manager = MembershipManager()
    manager.run()