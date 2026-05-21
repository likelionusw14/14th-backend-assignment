
class DataException(Exception):pass #Exception 부모 추상 클래스
class InvalidNullError(DataException): pass # 아무것도 입력하지 않았을 때
class InvalidDuplicateError(DataException): pass #중복된 이름을 입력햇을 때

class NameManager:
    def __init__(self):
        self.lions_list = []
    
    def add_lions(self, lion_info):
        if not lion_info:
            raise InvalidNullError('⚠️ 이름이 비어있습니다. 다시 입력하세요')
        
        if lion_info in self.lions_list:
            raise InvalidDuplicateError('⚠️ 이미 등록된 이름입니다.')
        
        self.lions_list.append(lion_info)


  
    def get_all_list(self): 
        return self.lions_list
    
  
    def count_all_list(self): 
        return len(self.lions_list)

class MainApp:
    def __init__(self):
        self.manager = NameManager()

    def explain_program(self):
        print('🦁 아기 사자 명단 관리 프로그램입니다.')

    def show_list(self):
        """등록된 명단을 번호와 함께 출력합니다."""
        for index,i in enumerate(self.manager.get_all_list(), start =1 ):
            print(f'🦁 {index}. {i}')

    def show_all_count(self):
        """"등록된 명단의 인원 수를 나타냅니다."""
        print(f'👥 총 인원 수 {self.manager.count_all_list()}')

    def exit_message(self):
        print('\n📌 이름 입력을 종료합니다.\n')
        print('📋 현재 아기 사자 명단입니다.')

    def run(self):
        self.explain_program()
        while True:
            try:
                name_input = input('✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ').replace(" ","")
                if name_input.lower() == 'q':
                    self.exit_message()
                    self.show_all_count()
                    self.show_list()
                    break
                self.manager.add_lions(name_input)
                print(f'{name_input}이(가) 등록되었습니다.')
            except DataException as e: # 전체 예외 처리 및 계속 입력 받음
                print(e)
                continue

if __name__ =='__main__':
    app = MainApp()
    app.run()

