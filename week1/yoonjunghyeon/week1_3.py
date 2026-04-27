class Member:
    def __init__(self, name: str):
        self.name = name

class Lion(Member):
    def __init__(self, name: str, track: str, num: str):
        super().__init__(name)
        self.track = track
        self.num = num

    def role(self):
        return ('🦁 아기사자')
    
    def get_info(self):
        return f'{self.name} | {self.track} | {self.num}'

class Staff(Member):
    def __init__(self, name: str):
        super().__init__(name)
    
    def role(self):
        return "🧑 운영진"

    def get_info(self):
        return f'{self.name} | 운영진'
    
class Manager:
    def __init__(self):
        self.members : list[Member] = []

    def add_member(self, memeber = Member):
        if not self.members:
            raise ValueError('내용이 비었습니다.')
        self.members.append(memeber)
    
    def get_list(self):
        print('\n📋 멤버 목록')
        for m in self.members:
            print(f'- {m.role()} : {m.get_info()}')

class Main:
    def __init__(self):
        self.manager = Manager()

    def explain_program(self):
        print('\n📌 기능을 선택하세요')
        print('1️⃣ 아기사자 등록')
        print('2️⃣ 운영진 등록')
        print('3️⃣ 전체 출력')
        print('4️⃣ 종료')

    def run(self):
        while True:
            self.explain_program()
            try:
                choice = int(input('👉선택: '))
                if choice == 1:
                    member = Lion(
                        input('🦁이름: '),
                        input('📚트랙: '),
                        input('🎓기수: ')
                    )
                    self.manager.add_member(member)
                    print('✅아기사자가 등록되었습니다.')
                elif choice == 2:
                    member = Staff(input('🧑🏫 이름: '))
                    self.manager.add_member(member)
                    print('✅운영진이 등록되었습니다.')
                elif choice == 3:
                    self.manager.get_list()
                elif choice == 4:
                    break
                else :
                    print('⚠️ 올바른 번호를 입력해주세요')
            except ValueError as e:
                print(e)
                continue

if __name__ == ('__main__'):
    main = Main()
    main.run()