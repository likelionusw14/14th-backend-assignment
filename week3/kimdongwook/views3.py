from abc import ABC, abstractmethod

class Member:
    def __init__(self,name):
        if not name or not name.strip():
            raise ValueError('이름은 비어 있을 수 없습니다.')
        self.name=name.strip()

    def get_role(self):
        return '일반 멤버'
    
    def __str__(self):
        return f'{self.name}'
    
class Lion(Member):
    def __init__(self,name,track,generation):
        super().__init__(name)
        if not generation or not str(generation).isdigit():
            raise ValueError('기수는 비어 있거나 잘못된 값일 수 없습니다.')
        self.track=track
        self.generation=generation

    def get_role(self):
        return '아기사자'
    
    def __str__(self):
        return f'{self.get_role()}:{self.name}|{self.track}|{self.generation}기'
    
class Staff(Member):
    def get_role(self):
        return '운영진'
    
    def __str__(self):
        return f'{self.get_role()}:{self.name}|운영진'
    
class Sorting(ABC):
    @abstractmethod
    def sort(self,members):
        pass
class Namesort(Sorting):
    def sort(self,members):
        return sorted(members,key=lambda x:x.name)

class Generationssort(Sorting):
    def sort(self,members):
        return sorted(members,key=lambda x: getattr(x,'generation',0))

class DisplayManager:
    @staticmethod
    def display_members(members, strategy: Sorting):
        sorted_members = strategy.sort(members)
        print("\n 멤버 목록")
        for member in sorted_members:
            print(f"- {member}")

class ProgramManager:
    def __init__(self):
        self.members = []
        self.display_manager = DisplayManager()

    def run(self):
        while True:
            print('\n 기능을 선택하세요')
            print('1️⃣ 아기사자 등록 2️⃣ 운영진 등록 3️⃣ 전체 등록 4️⃣ 종료')
            choice=input('선택:')

            try:
                if choice=='1':
                    name = input(" 이름: ")
                    track = input(" 트랙: ")
                    gen = input(" 기수: ")
                    self.members.append(Lion(name, track, gen))
                    print(" 아기사자가 등록되었습니다.")

                elif choice == '2':
                    name = input(" 이름: ")
                    self.members.append(Staff(name))
                    print(" 운영진이 등록되었습니다.")

                elif choice == '3':
                    if not self.members:
                        print(" 등록된 멤버가 없습니다.")
                        continue
                    self.display_manager.display_members(self.members,Namesort())

                elif choice == '4':
                    print('프로그램을 종료합니다.')
                    break
                
                else:
                    print('잘못된 번호입니다.')

            except ValueError as e:
                print(e)

if __name__ == '__main__':
    app=ProgramManager()
    app.run()
