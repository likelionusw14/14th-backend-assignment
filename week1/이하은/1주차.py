def get_names() :
    person = []
    while (1) :
        name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
        if name == 'q' :
            print("📌 이름 입력을 종료합니다. \n")
            break
        elif not name :
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
        else :
            person.append(name)
            print("✅ '", name ,"'이(가) 등록되었습니다.")

    return person

def out_names(person):
    print("📋 현재 아기 사자 명단입니다.")
    for i, name in enumerate(person,1) : #번호, 값 순서대로 꺼내기 i-> name
        print("🦁 %d."%i, name)

print("🦁 아기 사자 명단 관리 프로그램입니다.")
lionlist = get_names()
out_names(lionlist)