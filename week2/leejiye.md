백엔드 트랙 2주차 pbl 과제 제출 폴더입니다.
class Member:

    def __init__(self, name: str):

        self.name = name



class Lion(Member):

    def __init__(self, name: str, track: str, num: str):

        super().__init__(name)

        self.track = track  # 예: Django, SpringBoot

        self.num = num      # 예: 1기



    def role(self):

        return '🦁 아기사자'



    def get_info(self):

        return f'이름: {self.name}\n트랙: {self.track}\n기수: {self.num}'



class Manager:

    def __init__(self):

        self.members = []



    def add_member(self, member):

        self.members.append(member)



    def search_by_name(self, name):

        # 이름이 정확히 일치하는 멤버 찾기

        for member in self.members:

            if member.name == name:

                return member

        return None



    def filter_by_track(self, track):

        # 해당 트랙에 속한 멤버 리스트 반환

        return [m for m in self.members if isinstance(m, Lion) and m.track == track]



# --- 실행 로직 ---



manager = Manager()



while True:

    print("\n기능을 선택하세요")

    print("1. 아기사자 등록")

    print("2. 이름으로 검색")

    print("3. 트랙으로 조회")

    print("4. 종료")

    

    choice = input("선택 : ").strip()



    if choice == '1':

        name = input("🦁 이름을 입력하세요 : ").strip()

        track = input("📚 트랙을 입력하세요 : ").strip()

        num = input("🎓 기수를 입력하세요 : ").strip()

        

        new_lion = Lion(name, track, num)

        manager.add_member(new_lion)

        print("✅ 아기사자가 등록되었습니다.")



    elif choice == '2':

        search_name = input("🔍 검색할 이름을 입력하세요 : ").strip()

        result = manager.search_by_name(search_name)

        

        if result:

            print("\n📋 검색 결과")

            print(result.get_info())

        else:

            print(f"⚠️ 해당 이름의 아기사자를 찾을 수 없습니다.")



    elif choice == '3':

        search_track = input("📂 조회할 트랙을 입력하세요 : ").strip()

        results = manager.filter_by_track(search_track)

        

        print(f"\n📋 {search_track} 트랙 아기사자 명단")

        if results:

            for lion in results:

                print(f"- {lion.name} ({lion.num})")

        else:

            print("해당 트랙에 등록된 사자가 없습니다.")



    elif choice == '4':

        print("🚀 프로그램을 종료합니다.")

        break

    

    else:

        print("❌ 잘못된 선택입니다. 1~4 사이의 숫자를 입력해주세요.")
