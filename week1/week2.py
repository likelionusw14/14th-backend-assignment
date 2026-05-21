def register_lion(lions):
    name = input("이름: ")
    track = input("트랙: ")
    generation = input("기수: ")

    lion = {
        "name": name,
        "track": track,
        "generation": generation
    }

    lions.append(lion)
    print("아기사자가 등록되었습니다.")


def search_by_name(lions, name):
    for lion in lions:
        if lion["name"] == name:
            return lion
    return None


def filter_by_track(lions, track):
    result = []

    for lion in lions:
        if lion["track"] == track:
            result.append(lion)

    return result


def print_lion(lion):
    print(f"이름: {lion['name']}, 트랙: {lion['track']}, 기수: {lion['generation']}")


def print_lions(lion_list):
    if not lion_list:
        print("출력할 아기사자 정보가 없습니다.")
        return

    for lion in lion_list:
        print_lion(lion)


def main():
    lions = []

    while True:
        print("1. 아기사자 등록")
        print("2. 이름 검색")
        print("3. 트랙 조회")
        print("4. 종료")
        choice = input("기능 번호를 선택하세요: ")

        if choice == "1":
            register_lion(lions)

        elif choice == "2":
            name = input("검색할 이름을 입력하세요: ")
            result = search_by_name(lions, name)

            if result:
                print("검색 결과:")
                print_lion(result)
            else:
                print("해당 이름의 아기사자를 찾을 수 없습니다.")

        elif choice == "3":
            track = input("조회할 트랙명을 입력하세요: ")
            result = filter_by_track(lions, track)

            if result:
                print("조회 결과:")
                print_lions(result)
            else:
                print("해당 트랙의 아기사자가 없습니다.")

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


main()

