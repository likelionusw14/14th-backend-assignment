class Member:
    def __init__(self, name):
        self.name = self._validate_name(name)

    @staticmethod
    def _validate_name(name):
        cleaned = name.strip()
        if not cleaned:
            raise ValueError("이름은 비어 있을 수 없습니다.")
        return cleaned

    def to_display_line(self):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다.")


class Lion(Member):
    def __init__(self, name, track, cohort):
        super().__init__(name)
        self.track = self._validate_track(track)
        self.cohort = self._validate_cohort(cohort)

    @staticmethod
    def _validate_track(track):
        cleaned = track.strip()
        if not cleaned:
            raise ValueError("트랙은 비어 있을 수 없습니다.")
        return cleaned

    @staticmethod
    def _validate_cohort(cohort):
        cleaned = cohort.strip()
        if not cleaned:
            raise ValueError("기수는 비어 있을 수 없습니다.")
        if not (cleaned.endswith("기") and cleaned[:-1].isdigit() and int(cleaned[:-1]) > 0):
            raise ValueError("기수 형식이 올바르지 않습니다. 예: 1기")
        return cleaned

    def to_display_line(self):
        return f"- 🦁 아기사자 : {self.name} | {self.track} | {self.cohort}"


class Staff(Member):
    def to_display_line(self):
        return f"- 🧑‍🏫 운영진 : {self.name} | 운영진"


class SortPolicy:
    def sort(self, members):
        raise NotImplementedError("하위 정책에서 구현해야 합니다.")


class RegistrationOrderPolicy(SortPolicy):
    def sort(self, members):
        return list(members)


class MemberPrinter:
    def __init__(self, sort_policy):
        self.sort_policy = sort_policy

    def print_members(self, members):
        print("\n📋 멤버 목록")
        sorted_members = self.sort_policy.sort(members)

        if not sorted_members:
            print("- 등록된 멤버가 없습니다.")
            return

        for member in sorted_members:
            print(member.to_display_line())


class MemberRegistry:
    def __init__(self):
        self._members = []

    def add(self, member):
        self._members.append(member)

    def all(self):
        return list(self._members)


def print_menu():
    print("📌 기능을 선택하세요")
    print("1️⃣  아기사자 등록")
    print("2️⃣  운영진 등록")
    print("3️⃣  전체 출력")
    print("4️⃣  종료")


def register_lion(registry):
    name = input("🦁 이름: ")
    track = input("📚 트랙: ")
    cohort = input("🎓 기수: ")

    try:
        lion = Lion(name, track, cohort)
    except ValueError as error:
        print(f"⚠️  {error}")
        return

    registry.add(lion)
    print("✅ 아기사자가 등록되었습니다.")


def register_staff(registry):
    name = input("🧑‍🏫 이름: ")

    try:
        staff = Staff(name)
    except ValueError as error:
        print(f"⚠️  {error}")
        return

    registry.add(staff)
    print("✅ 운영진이 등록되었습니다.")


def show_all_members(registry, printer):
    printer.print_members(registry.all())


def run():
    registry = MemberRegistry()
    printer = MemberPrinter(RegistrationOrderPolicy())
    actions = {
        "1": lambda: register_lion(registry),
        "2": lambda: register_staff(registry),
        "3": lambda: show_all_members(registry, printer),
    }

    while True:
        print_menu()
        choice = input("👉 선택: ").strip()

        if choice == "4":
            print("👋 프로그램을 종료합니다.")
            break

        action = actions.get(choice)
        if action is None:
            print("⚠️  올바른 번호를 입력해주세요.\n")
            continue

        action()
        print()


if __name__ == "__main__":
    run()
