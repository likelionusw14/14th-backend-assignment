def collect_names():
    lion_names = []  # 아기 사자 이름을 저장할 변수 (자료형: 리스트)
    print("🦁 아기 사자 명단 관리 프로그램입니다.")
    
    while True: 
        user_input = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
        
        name = user_input.strip()
        if name == 'q':
            print("\n📌 이름 입력을 종료합니다.\n")
            break  
            
        elif name == "":  # 입력값이 비어 있거나 공백만 있는 경우
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
            
        else:
            lion_names.append(name)
            print(f"✅ '{name}' 이(가) 등록되었습니다.")
            
    return lion_names


def print_names(names):
    print("📋 현재 아기 사자 명단입니다.")
    
    # 전달받은 리스트가 비어있는지 확인하는 예외 처리
    if not names:
        print("등록된 아기 사자가 없습니다.")
        return
    for index, name in enumerate(names, start=1):
        print(f"🦁 {index}. {name}")


def main():
    collected_names = collect_names()
    print_names(collected_names)
    
if __name__ == "__main__":
    main()