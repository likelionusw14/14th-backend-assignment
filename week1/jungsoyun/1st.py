# 1. 처리: 유효성 검사 로직 (공백 및 빈 값 확인)
def is_valid_input(name):
    return name.strip() != ""

# 2. 입력: 데이터 수집 로직
def input_names():
    lions = []
    while True:
        name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 'q' 입력): ")

        # 종료 조건 확인
        if name.lower() == 'q':
            print("\n📌 이름 입력을 종료합니다.")
            break

        # 유효성 검사 및 처리 분기
        if is_valid_input(name):
            lions.append(name.strip())
            print(f"✅ '{name.strip()}' 이(가) 등록되었습니다.")
        else:
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
            
    return lions

# 3. 출력: 저장된 데이터 출력 로직
def display_lion_list(lion_list):
    print("\n📋 현재 아기 사자 명단입니다.")
    
    if not lion_list:
        print("입력된 이름이 없습니다.")
    else:
        for i, name in enumerate(lion_list, start=1):
            print(f"🦁 {i}. {name}")
    
    print("\n프로그램을 종료합니다.")

# 4. 실행 흐름 제어 (Main flow)
def main():
    print("🦁 아기 사자 명단 관리 프로그램입니다.")
    
    # [입력 및 처리]
    lions_list = input_names()
    
    # [출력]
    display_lion_list(lions_list)

# 프로그램 시작점
if __name__ == "__main__":
    main()
