print('아기 사자 명단 관리 프로그램입니다.')

names = []

register=False

while not register:
    print('아기 사자 이름을 입력하세요(종료하려면 q 입력):')
    register_input = input(':  ')
    

    if register_input == 'q':
        register = True
        print('===================')
        print('이름 입력을 종료합니다')
        print('===================')
        break
    elif register_input == '':
        print("이름이 비어있습니다. 다시 입력해주세요. ")
    else:
        names.append(register_input)
        print(f"'{register_input}'이(가) 등록되었습니다.")

print('현재 아기 사자 명단입니다')

i=1
for name in names:
    print(f'{i}.{name}')
    i +=1