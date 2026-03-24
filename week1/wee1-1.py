# 이름 입력
def print_Comment():
    while True:
        name = input("아기 사자 이름을 입력하세요 (종료하려면 q입력): ").strip()
        #공백일 경우
        if name == "":
            print("이름이 비었습니다. 다시 입력해주세요.") 
        # q 입력 시 
        elif name =='q':
            print("이름 입력을 종료합니다.")
            break
        # 이름 추가 시
        else:
            #이름 중복 검사
            if(name in names):
                print("이미 등록된 이름입니다. 다시 입력해주세요.")
            else:
                names.append(name)
                print(f"'{name}' 이(가) 등록되었습니다.")

# 아기 사자 명단 출력
def print_List(name):
    print("현재 아기 사자 명단입니다.")
    print(f"총 인원 수 : {len(names)}")
    for i in range(len(name)):
        print(f"{i+1}. {name[i]}")
        
names = []
print("아기 사자 명단 관리 프로그램입니다.")
print_Comment()
print_List(names)