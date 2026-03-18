def is_valid_input(name): # 유효성 검사
    return name.strip() != ""

def input_names(): # 이름 입력 함수
    lions = []
    while True:
        name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
        if name.lower() == 'q':
            print("\n📌 이름 입력을 종료합니다.")
            break
        if is_valid_input(name):
            lions.append(name)
            print(f"✅ '{name}' 이(가) 등록되었습니다.")
        else:
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
    return lions

def display_lion_list(lion_list): # 이름 출력 함수
    print("\n📋 현재 아기 사자 명단입니다.")
    if not lion_list:
        print("입력된 이름이 없습니다.")
    else:
        for i, name in enumerate(lion_list, start=1):
            print(f"🦁 {i}. {name}")
    print("\n프로그램을 종료합니다.")

def main():
    print("🦁 아기 사자 명단 관리 프로그램입니다.")
    lions_list = input_names()
    display_lion_list(lions_list)

if __name__ == "__main__":
    main()
