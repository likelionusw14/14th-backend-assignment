def register_lions():
    lion_list = []

    while True:
        name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ").strip()

        if name.lower() == 'q':
            print("\n📌 이름 입력을 종료합니다.")
            break

        if not name:
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
            continue

        lion_list.append(name)
        print(f"✅ '{name}' 이(가) 등록되었습니다.")

    return lion_list

def display_lions(lion_list):
    print("\n📋 현재 아기 사자 명단입니다.")
    
    if not lion_list:
        print("입력된 명단이 없습니다.")
    else:
        for index, name in enumerate(lion_list, 1):
            print(f"🦁 {index}. {name}")

def main():
    lions = register_lions()
    display_lions(lions)

if __name__ == "__main__":
    main()