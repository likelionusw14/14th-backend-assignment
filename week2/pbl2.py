# 아기사자 리스트 생성
lions = []

# 아기사자 등록
def add_lion():
    # 이름, 트랙, 기수 입력
    name = input("이름을 입력하세요 : ")
    track = input("트랙을 입력하세요 : ")
    generation = input("기수를 입력하세요 : ")

    # 공백 입력 방지
    if name == "" or track == "" or generation == "":
        print("모든 정보를 입력해야 합니다. 다시 시도해주세요.")

    # 중복 입력 방지
    for lion in lions:
        if lion["이름"] == name:
            print("이미 등록된 이름입니다. 다시 시도해주세요.")

    # 입력된 정보를 딕셔너리 형태로 저장하여 리스트에 추가
    lion = {"이름": name, "트랙": track, "기수": generation}
    lions.append(lion)

    print("아기사자가 등록되었습니다.")

# 아기사자 검색
def search_lion():
    name = input("검색할 이름을 입력하세요 : ")

    find_name = False

    # 이름이 일치하는 아기사자 정보 출력
    for lion in lions:
        if lion["이름"] == name:
            print("\n검색 결과")
            print(f"이름: {lion['이름']}\n트랙: {lion['트랙']}\n기수: {lion['기수']}")
            find_name = True

    # 해당 이름의 아기사자가 없는 경우
    if find_name == False:
        print("해당 이름의 아기사자를 찾을 수 없습니다.")

# 트랙으로 조회
def search_track():
    track = input("조회할 트랙을 입력하세요 : ")

    print(f"\n{track} 트랙 아기사자 명단")

    find_track = False
    
    # 해당 트랙의 아기사자 정보 출력
    for lion in lions:
        if lion["트랙"] == track:
            print(f"- {lion['이름']} ({lion['기수']})")
            find_track = True

    # 해당 트랙의 아기사자가 없는 경우
    if find_track == False:
        print("해당 트랙의 아기사자를 찾을 수 없습니다.")
    

while True:
    print("\n기능을 선택하세요.")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료")

    choice = input("선택 : ")

    if choice == "1":
        add_lion()
    elif choice == "2":
        search_lion()
    elif choice == "3":
        search_track()
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")