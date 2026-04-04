def menu():
  print("\n기능을 선택하세요")
  print("1. 아기사자 등록")
  print("2. 이름으로 검색")
  print("3. 트랙으로 조회")
  print("4. 종료")

lions = []

def add_lion(lions):
  name = input("이름을 입력하세요: ")
  track = input("트랙을 입력하세요: ")
  th = input("기수를 입력하세요: ")

  lion = {
    "name" : name,
    "track" : track,
    "th" : th
  }

  lions.append(lion)
  print("아기사자가 등록되었습니다.")

def search_name(lions):
  name = input("검색할 이름을 입력하세요: ")
  

  for lion in lions:
    if lion["name"] == name:
      print("\n검색 결과")
      print(f"이름: {lion['name']}")
      print(f"트랙: {lion['track']}")
      print(f"기수: {lion['th']}")
      return
    
    else:
      print("해당 이름의 아기사자를 찾을 수 없습니다.")

def search_track(lions):
  track = input("조회할 트랙을 입력하세요: ")

  print(f"{track} 트랙 아기사자 명단")

  for lion in lions:
    if lion["track"] == track:
      print(f"- {lion['name']} ({lion['th']})")
      return
    
    else:
      print("해당 트랙에 아기사자가 없습니다.")


while True:
  menu()
  select = input("선택: ")

  if select == "1":
    add_lion(lions)
  elif select == "2":
    search_name(lions)
  elif select == "3":
    search_track(lions)
  elif select == "4":
    print("프로그램을 종료합니다.")
    break
  else:
    print("올바른 번호를 입력해주세요.")
    continue

