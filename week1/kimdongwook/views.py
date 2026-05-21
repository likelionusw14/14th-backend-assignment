from django.shortcuts import render


def get_valid_lion_name():
    while True:
        user_input = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
        
        if not user_input.strip():
            print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
            continue
            
        return user_input.strip()


def collect_lion_names():
    names_list = []
    
    while True:
        name = get_valid_lion_name()
        
        if name.lower() == 'q':
            print("\n📌 이름 입력을 종료합니다.")
            break
            
        names_list.append(name)
        print(f"✅ '{name}' 이(가) 등록되었습니다.")
        
    return names_list


def display_lion_list(lions):
    print("\n📋 현재 아기 사자 명단입니다.")
    for i, name in enumerate(lions, start=1):
        print(f"🦁 {i}. {name}")

def main():
    lion_names = collect_lion_names()

    display_lion_list(lion_names)
    
    print("\n프로그램이 정상적으로 종료되었습니다.")

if __name__ == "__main__":
    main()

# Create your views here.

