class Member:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("이름을 입력해 주세요.")
        self.name = name

class Lion(Member):
    def __init__(self, name, track, gene):
        super().__init__(name)
        if not gene.strip():
            raise ValueError("기수를 입력해 주세요.")
        self.track = track
        self.gene = gene

    def get_role(self):
        return "🦁 아기사자"

    def get_info(self):
        return f"{self.name} | {self.track} | {self.gene}"


class Staff(Member):
    def get_role(self):
        return "🧑‍🏫 운영진"

    def get_info(self):
        return f"{self.name} | 운영진"


class SimplePrintPolicy:
    def print(self, members):
        print("\n📋 멤버 목록")
        for m in members:
            print(f"- {m.get_role()} : {m.get_info()}")


class NameSortPolicy:
    def sort(self, members):
        return sorted(members, key=lambda m: m.name)


members = []
print_policy = SimplePrintPolicy()
sort_policy = NameSortPolicy()

while True:
    print("\n📌 기능을 선택하세요")
    print("1️⃣  아기사자 등록")
    print("2️⃣  운영진 등록")
    print("3️⃣  전체 출력")
    print("4️⃣  종료")
    choice = input("👉 선택: ")

    try:
        if choice == "1":
            members.append(Lion(input("🦁 이름: "), input("📚 트랙: "), input("🎓 기수: ")))
            print("✅ 아기사자가 등록되었습니다.")
        elif choice == "2":
            members.append(Staff(input("🧑‍🏫 이름: ")))
            print("✅ 운영진이 등록되었습니다.")
        elif choice == "3":
            print_policy.print(sort_policy.sort(members))
        elif choice == "4":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("⚠️ 올바른 번호를 입력해주세요.")
    except ValueError as e:
        print(e)
