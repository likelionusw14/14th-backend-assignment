def menu() :
    print("\n기능을 선택하세요")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료\n")
    number = int(input("선택 : "))
    return number

lionlist = []

def get_lion():
    babylion = {} #딕셔너리 생성~!
    babylion["이름"] = input("🦁 이름을 입력하세요:")
    babylion["트랙"] = input("📚 트랙을 입력하세요:")
    babylion["기수"] = input("🎓 기수를 입력하세요:")
    lionlist.append(babylion) #중요중요 리스트에 추가
    print("✅ 아기사자가 등록되었습니다.\n")

def sreach_name():
    name = input("🔍 검색할 이름을 입력하세요:")
    for lion in lionlist: #lionlist라는 리스트에 lion이라는 딕셔너리요소를 하나씩 꺼내서!
        if lion["이름"] == name : #lionlist에 lion이 있을 때
            print("이름:",lion["이름"])
            print("트랙:",lion["트랙"])
            print("기수:",lion["기수"])
            return #찾으면 함수 종료
        print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.\n")

def sreach_track():
    track = input("🔍 조회할 트랙을 입력하세요:")
    for lion in lionlist : #해당되는 lion의 값이 계속 나오게 반복
        if lion["트랙"] == track :
            print("-",lion["이름"],"("+lion["기수"]+")")

while(1) :
    number = menu()
    if number == 1: 
        get_lion() 
    elif number == 2: 
        sreach_name()
    elif number == 3: 
        sreach_track()
    else: 
        print("📌 프로그램을 종료합니다.")
        break
