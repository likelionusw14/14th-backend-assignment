# 명단 선언
lions = []

# 명단 추가
def add_lion():
    name = input("아기 사자의 이름을 입력하세요 (종료하려면 q 입력): ")
    # 앞뒤 공백 제거
    name = name.strip() 

    # 입력된 이름이 'q'인 경우 함수를 종료
    if name == "q":
        print("\n이름 입력을 종료합니다.\n")
        return False
    
    # 공백일 경우 재입력 안내
    if name == "":
        print("이름이 비어있습니다. 이름을 다시 입력하세요.")
        return True
    
    # 중복된 이름이 있을 경우 재입력 안내
    if name in lions:
        print(f"{name}은(는) 이미 등록된 이름입니다. 다시 입력해주세요.")
        return True
    
    # 등록완료 안내
    lions.append(name)
    print(f"{name}이(가) 등록되었습니다.")
    return True

# 명단 출력
def show_lions():
    print("현재 아기 사자 명단입니다.")
    print(f"총 인원 수 : {len(lions)}")

    # 명단의 이름과 번호를 함께 출력
    for lion in lions:
        print(f"{lions.index(lion)+1}. {lion}")

print("아기 사자 명단 관리 프로그램입니다.")

# 메인
while True:
    value = add_lion()

    if value == False:
        break

show_lions()