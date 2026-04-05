class Member:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("이름이 비어있습니다.")
        self.name = name

    def get_info(self):
        raise NotImplementedError

class Lion(Member):
    def __init__(self, name, track, generation):
        super().__init__(name)
        if not track.strip() or not generation.strip():
            raise ValueError("트랙이나 기수 정보가 누락되었습니다.")
        self.track = track
        self.generation = generation

    def get_info(self):
        return f"🦁 아기사자 : {self.name} | {self.track} | {self.generation}"

class Staff(Member):
    def get_info(self):
        return f"🧑‍🏫 운영진 : {self.name} | 운영진"

def display_all_members(members):
    print("\n📋 멤버 목록")
    if not members:
        print("등록된 멤버가 없습니다.")
        return
    for member in members:
        print(f"- {member.get_info()}")

def main():
    members = []
    
    while True:
        print("\n📌 기능을 선택하세요")
        print("1️⃣  아기사자 등록")
        print("2️⃣  운영진 등록")
        print("3️⃣  전체 출력")
        print("4️⃣  종료")
        
        choice = input("👉 선택: ").strip()

        if choice == "1":
            try:
                name = input("🦁 이름: ").strip()
                track = input("📚 트랙: ").strip()
                gen = input("🎓 기수: ").strip()
                members.append(Lion(name, track, gen))
                print("✅ 아기사자가 등록되었습니다.")
            except ValueError as e:
                print(f"⚠️  {e}")

        elif choice == "2":
            try:
                name = input("🧑‍🏫 이름: ").strip()
                members.append(Staff(name))
                print("✅ 운영진이 등록되었습니다.")
            except ValueError as e:
                print(f"⚠️  {e}")

        elif choice == "3":
            display_all_members(members)

        elif choice == "4":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()