def print_menu():
    print("기능을 선택하세요")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료")


def register_lion(lions):
    name = input("🦁 이름을 입력하세요: ").strip()
    track = input("📚 트랙을 입력하세요: ").strip()
    cohort = input("🎓 기수를 입력하세요: ").strip()

    if not name or not track or not cohort:
        print("⚠️  이름, 트랙, 기수를 모두 입력해주세요.")
        return

    lion = {
        "이름": name,
        "트랙": track,
        "기수": cohort,
    }
    lions.append(lion)
    print("✅ 아기사자가 등록되었습니다.")


def find_lion_by_name(lions, target_name):
    for lion in lions:
        if lion["이름"] == target_name:
            return lion
    return None


def search_lion(lions):
    target_name = input("🔍 검색할 이름을 입력하세요: ").strip()
    lion = find_lion_by_name(lions, target_name)

    if lion is None:
        print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.")
        return

    print("\n📋 검색 결과")
    print(f"이름: {lion['이름']}")
    print(f"트랙: {lion['트랙']}")
    print(f"기수: {lion['기수']}")


def filter_lions_by_track(lions, target_track):
    return [lion for lion in lions if lion["트랙"] == target_track]


def show_lions_by_track(lions):
    target_track = input("📂 조회할 트랙을 입력하세요: ").strip()
    matched_lions = filter_lions_by_track(lions, target_track)

    if not matched_lions:
        print(f"⚠️  {target_track} 트랙의 아기사자가 없습니다.")
        return

    print(f"\n📋 {target_track} 트랙 아기사자 명단")
    for lion in matched_lions:
        print(f"- {lion['이름']} ({lion['기수']})")


def main():
    lions = []

    while True:
        print_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            register_lion(lions)
        elif choice == "2":
            search_lion(lions)
        elif choice == "3":
            show_lions_by_track(lions)
        elif choice == "4":
            print("📌 프로그램을 종료합니다.")
            break
        else:
            print("⚠️  올바른 번호를 입력해주세요.")

        print()


if __name__ == "__main__":
    main()
