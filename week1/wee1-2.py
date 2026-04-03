# 아기사자 등록
def add_lion(lion_list):
    name = input("이름을 입력하세요: ")
    track = input("트랙을 입력하세요: ")
    gen = input("기수를 입력하세요: ")

    lion = {"name": name, "track": track, "gen": gen}
    lion_list.append(lion)
    print("아기사자가 등록되었습니다. \n")

# 이름으로 검색
def search_lion(lion_list):
    found = False
    name = input("검색할 이름을 입력하세요: ")
    for lion in lion_list:
        if lion["name"] == name:
            print("검색 결과")
            print(f"이름: {lion['name']}")
            print(f"트랙: {lion['track']}")
            print(f"기수: {lion['gen']} \n")
            found = True
    
    if not found:
        print("해당 이름의 아기사자를 찾을 수 없습니다. \n")


# 트랙으로 조회
def retrieve_lion(lion_list):
    track = input("조회할 트랙을 입력하세요: ")
    print(f"{track} 트랙 아기사자 명단")

    for lion in lion_list:
        if track == lion["track"]:
            print(f"- {lion['name']} ({lion['gen']})")
    print()

def print_menu(lion):
    while True:
        print("기능을 선택하세요")
        print("1. 아기사자 등록")
        print("2. 이름으로 검색")
        print("3. 트랙으로 조회")
        print("4. 종료")  
        choice = input("선택: ")

        if choice == "1":
            add_lion(lion_list)
        elif choice == "2" :
           search_lion(lion_list)
        elif choice == "3":
            retrieve_lion(lion_list)
        elif choice =="4":
            print("프로그램을 종료합니다!")
            break


lion_list = [] 
print_menu(lion_list)