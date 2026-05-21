def register_lion(lions):
    name = input("🦁 이름을 입력하세요: ").strip()
    track = input("📚 트랙을 입력하세요: ").strip()
    generation = input("🎓 기수를 입력하세요: ").strip()
    
    lion_info = {
        "이름": name,
        "트랙": track,
        "기수": generation
    }
    lions.append(lion_info)
    print("✅ 아기사자가 등록되었습니다.")

def search_by_name(lions):
    search_name = input("🔍 검색할 이름을 입력하세요: ").strip()
    found = False
    
    for lion in lions:
        if lion["이름"] == search_name:
            print("\n📋 검색 결과")
            print(f"이름: {lion['이름']}")
            print(f"트랙: {lion['트랙']}")
            print(f"기수: {lion['기수']}")
            found = True
            break
            
    if not found:
        print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.")

def view_by_track(lions):
    search_track = input("📂 조회할 트랙을 입력하세요: ").strip()
    print(f"\n📋 {search_track} 트랙 아기사자 명단")
    
    found = False
    for lion in lions:
        if lion["트랙"] == search_track:
            print(f"- {lion['이름']} ({lion['기수']})")
            found = True
            
    if not found:
        print("해당 트랙에 등록된 아기사자가 없습니다.")

def main():
    lions = []
    
    while True:
        print("\n기능을 선택하세요")
        print("1. 아기사자 등록")
        print("2. 이름으로 검색")
        print("3. 트랙으로 조회")
        print("4. 종료")
        
        choice = input("선택: ").strip()
        
        if choice == "1":
            register_lion(lions)
        elif choice == "2":
            search_by_name(lions)
        elif choice == "3":
            view_by_track(lions)
        elif choice == "4":
            print("📌 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()