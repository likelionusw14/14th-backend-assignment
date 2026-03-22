def register_lion(lion_list):
    name = input("🦁 이름을 입력하세요: ")
    track = input("📚 트랙을 입력하세요: ")
    generation = input("🎓 기수를 입력하세요: ")

    lion_info = {
        "name": name,
        "track": track,
        "generation": generation
    }
    
    lion_list.append(lion_info)
    print("✅ 아기사자가 등록되었습니다.\n")

def search_by_name(lion_list):
    search_name = input("🔍 검색할 이름을 입력하세요: ")
    found = False
    
    for lion in lion_list:
        if lion["name"] == search_name:
            print("\n📋 검색 결과")
            print(f"이름: {lion['name']}")
            print(f"트랙: {lion['track']}")
            print(f"기수: {lion['generation']}\n")
            found = True
            break  
    if not found:
        print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.\n")


def filter_by_track(lion_list):
    search_track = input("📂 조회할 트랙을 입력하세요: ")
    matching_lions = [lion for lion in lion_list if lion["track"] == search_track]
    
    print(f"\n📋 {search_track} 트랙 아기사자 명단")
    if matching_lions:
        for lion in matching_lions:
            print(f"- {lion['name']} ({lion['generation']})")
    else:
        print("- 등록된 아기사자가 없습니다.")
    print()  


def main():
    lion_list = []  
    
    while True:
        print("기능을 선택하세요")
        print("1. 아기사자 등록")
        print("2. 이름으로 검색")
        print("3. 트랙으로 조회")
        print("4. 종료")
        
        choice = input("선택: ")
        
        if choice == '1':
            register_lion(lion_list)
        elif choice == '2':
            search_by_name(lion_list)
        elif choice == '3':
            filter_by_track(lion_list)
        elif choice == '4':
            print("📌 프로그램을 종료합니다.")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 1~4 사이의 숫자를 입력해주세요.\n")

if __name__ == "__main__":
    main()