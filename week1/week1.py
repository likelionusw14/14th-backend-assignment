
print("아기 사자 명단 관리 프로그램입니다.")
User = []
UserInput = ""

def ShowUser():
    if len(User) == 0:
        print("등록된 아기사자 명단이 없습니다.")
    else:
        print("등록된 아기사자 명단:")
        for i in range(len(User)):
            print(f"{i+1}. {User[i]}")
           
while UserInput != "q":
    UserInput = input("아기사자 이름을 입력하세요 (종료하려면 q 입력): ")
    if UserInput == "":
        print("이름이 비어있습니다. 다시 입력해주세요.")
    elif UserInput == "q":
        print("이름 입력을 종료합니다.")
    else:
        User.append(UserInput)
        print(f"{UserInput}이(가) 등록되었습니다.")
  
  
ShowUser()
            



            