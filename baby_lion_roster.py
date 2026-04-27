def collect_lion_names():
    lion_names = []

    while True:
        name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ").strip()

        if name.lower() == "q":
            print("\n📌 이름 입력을 종료합니다.")
            break

        if not name:
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
            continue

        lion_names.append(name)
        print(f"✅ '{name}' 이(가) 등록되었습니다.")

    return lion_names


def print_lion_names(lion_names):
    print("\n📋 현재 아기 사자 명단입니다.")

    if not lion_names:
        print("🦁 등록된 아기 사자가 없습니다.")
        return

    for index, name in enumerate(lion_names, start=1):
        print(f"🦁 {index}. {name}")


def main():
    print("🦁 아기 사자 명단 관리 프로그램입니다.")
    names = collect_lion_names()
    print_lion_names(names)


if __name__ == "__main__":
    main()
