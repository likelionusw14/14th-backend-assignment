baby_lions = []

while True:
    print("\n기능을 선택하세요")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료")
    
    choice = input("선택: ")

    if choice == '1':
        name = input("이름을 입력하세요: ")
        track = input("트랙을 입력하세요: ")
        gen = input("기수를 입력하세요: ")
        
        lion_info = {
            "name": name,
            "track": track,
            "gen": gen
        }
        baby_lions.append(lion_info)
        print("✅ 아기사자가 등록되었습니다.")

    elif choice == '2':
        search_name = input("검색할 이름을 입력하세요: ")
        found = False
        
        for lion in baby_lions:
            if lion["name"] == search_name:
                print("\n검색 결과")
                print(f"이름: {lion['name']}")
                print(f"트랙: {lion['track']}")
                print(f"기수: {lion['gen']}")
                found = True
                break
        
        if not found:
            print("해당 이름의 아기사자를 찾을 수 없습니다.")

    elif choice == '3':
        search_track = input("조회할 트랙을 입력하세요: ")
        print(f"\n📋 {search_track} 트랙 아기사자 명단")
        
        found = False
        for lion in baby_lions:
            if lion["track"] == search_track:
                print(f"- {lion['name']} ({lion['gen']})")
                found = True
        
        if not found:
            print("해당 트랙에 등록된 아기사자가 없습니다.")

    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("1~4번 중 하나를 선택해주세요")