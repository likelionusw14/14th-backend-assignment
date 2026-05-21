class InputException(Exception): pass
class InputNullException(InputException): pass
class InputDuplicateException(InputException): pass
class NotExistListName(InputException): pass
class NotExistList(InputException): pass

class Lion:
    def __init__(self , name, track, num):
        self.name = name
        self.track = track
        self.num = num

    def make_dict(self):
        return {
            "name": self.name,
            "track": self.track,
            "num" : self.num,
        }

class Manager:
    def __init__(self):
        self.lion_list = []

    def result_message(self):
        print('\n📋 검색 결과')

    def add_lion_info(self, name, track, num):
        self.add_filter(name, track, num)
        lion = Lion(name, track, num)
        self.lion_list.append(lion.make_dict())
    
    def search_by_name(self, lion_name):
        self.search_name_filter(lion_name)
        self.result_message()
        result = [item for item in self.lion_list if item['name'] == lion_name ]
        for item in result:
            print(f'이름: {item['name']}')
            print(f'트랙: {item['track']}')
            print(f'기수: {item['num']}')

    def search_by_tn(self, lion_track, lion_num):
        self.search_tn_filter(lion_track, lion_num)
        self.result_message()
        result = [item for item in self.lion_list if item['track'] == lion_track and item['num'] == lion_num]
        for item in result:
            print(f' - {item['name']} ({item['track']}, {item['num']})')

    def add_filter(self, name, track, num):
        if not name or not track or not num:
            raise InputNullException('⚠️ 내용이 비었습니다. 다시 입력하세요.')
        if any(item['name'] == name for item in self.lion_list):
            raise InputDuplicateException('⚠️ 이름이 중복되었습니다.')
    
    def search_name_filter(self, name):
        if not any(item['name'] == name for item in self.lion_list):
            raise NotExistListName('⚠️ 해당 이름의 아기사자를 찾을 수 없습니다.')
    
    def search_tn_filter(self, track, num):
        if not track or not num:
            raise InputNullException('⚠️ 내용이 비었습니다. 다시 입력하세요.')
        if not any(item['track'] == track and item['num'] == num for item in self.lion_list):
            raise NotExistList('⚠️ 조건에 맞는 아기사자가 없습니다.')

class MainApp:
    def __init__(self):
        self.manager = Manager()
    
    def guide_message(sefl):
        print('\n기능을 선택하세요')
        print('1. 아기사자 등록')
        print('2. 이름으로 검색')
        print('3. 트랙 + 기수로 조회')
        print('4. 종료')

    def exit_message(self):
        print('📌 프로그램을 종료합니다.')

    def run(self):

        while True:
            self.guide_message()
            try:
                choice = input('선택: ')
                if choice == '1':
                    name_input = input('🦁 이름을 입력하세요: ')
                    track_input = input('📚 트랙을 입력하세요: ')
                    num_input = input('🎓 기수를 입력하세요: ')
                    self.manager.add_lion_info(name_input,track_input,num_input)
                    print(f'✅ {name_input}가 등록되었습니다.')
        
                elif choice == '2':
                    search_name = input('🔍 검색할 이름을 입력하세요: ')
                    self.manager.search_by_name(search_name)

                elif choice == '3':
                    search_track = input('📁 조회할 트랙을 입력하세요: ')
                    search_num = input('🎓 조회할 기수를 입력하세요: ')
                    self.manager.search_by_tn(search_track, search_num)

                elif choice =='4':
                    self.exit_message()
                    break
                    
            except InputException as e:
                print(e)
                continue

if __name__ == "__main__":
    main = MainApp()
    main.run()

