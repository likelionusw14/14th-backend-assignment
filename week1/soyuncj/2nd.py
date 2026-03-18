def onboard_lion(lions) :
  name = input ("🦁 이름을 입력하세요: ")
  track = input ("📚 트랙을 입력하세요: ")
  gene = input ("🎓 기수를 입력하세요: ")
  lion = {
  "name": name,
  "track": track,
  "gene": gene}
  lions.append(lion)
  print(f"✅ '{name}' 아기사자가 등록되었습니다.")

def search_lion(lions):
  name = input ("🔍 검색할 이름을 입력하세요: ")
  for lion in lions:
    if lion["name"] == name:
      print("\n📋 검색 결과")
      print(f"이름: {lion['name']}")
      print(f"트랙: {lion['track']}")
      print(f"기수: {lion['gene']}")
      return
  print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.")

def track_filtering (lions):
  track = input ("📂 조회할 트랙을 입력하세요: ")
  results = [lion for lion in lions if lion["track"] == track]
  if not results:
    print(f"⚠️  '{track}' 트랙에 소속된 아기사자가 없습니다.")
  else:
    print(f"\n📋 {track} 트랙 아기사자 명단")
    for i, lion in enumerate(results, 1):
      print(f"{i}. {lion['name']} ({lion['gene']}기)")

def print_menu ():
    print("\n기능을 선택하세요")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료")

def main():
  lions = []
  while True:
    print_menu()
    choice = input ("선택: ")

    if choice == "1":
      onboard_lion(lions)
    elif choice == "2":
      search_lion(lions)
    elif choice == "3":
      track_filtering(lions)
    elif choice == "4":
        print("📌 프로그램을 종료합니다.")
        break
    else:
      print("⚠️  올바른 번호를 입력해주세요.")
      
if __name__ == "__main__":
    main()
