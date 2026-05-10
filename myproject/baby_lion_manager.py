class Member:
    role_name = "멤버"
    icon = "👤"
    role_priority = 99

    def __init__(self, name):
        self.name = self._validate_name(name)

    @staticmethod
    def _validate_name(name):
        cleaned_name = name.strip()
        if not cleaned_name:
            raise ValueError("이름은 비어 있을 수 없습니다.")
        return cleaned_name

    def detail(self):
        raise NotImplementedError

    def display_text(self):
        return f"- {self.icon} {self.role_name} : {self.name} | {self.detail()}"

    def sort_key(self):
        return self.name


class Lion(Member):
    role_name = "아기사자"
    icon = "🦁"
    role_priority = 0

    def __init__(self, name, track, cohort):
        super().__init__(name)
        self.track = self._validate_track(track)
        self.cohort = self._validate_cohort(cohort)

    @staticmethod
    def _validate_track(track):
        cleaned_track = track.strip()
        if not cleaned_track:
            raise ValueError("트랙은 비어 있을 수 없습니다.")
        return cleaned_track

    @staticmethod
    def _validate_cohort(cohort):
        cleaned_cohort = cohort.strip()
        if cleaned_cohort.endswith("기"):
            cleaned_cohort = cleaned_cohort[:-1].strip()

        if not cleaned_cohort.isdigit() or int(cleaned_cohort) <= 0:
            raise ValueError("기수는 1 이상의 숫자여야 합니다.")

        return f"{int(cleaned_cohort)}기"

    def detail(self):
        return f"{self.track} | {self.cohort}"


class Staff(Member):
    role_name = "운영진"
    icon = "🧑‍🏫"
    role_priority = 1

    def detail(self):
        return "운영진"


class MemberSortPolicy:
    def sort(self, members):
        raise NotImplementedError


class RoleThenNameSortPolicy(MemberSortPolicy):
    def sort(self, members):
        return sorted(
            members,
            key=lambda member: (member.role_priority, member.sort_key()),
        )


class MemberDisplayPolicy:
    def display(self, members):
        raise NotImplementedError


class ConsoleMemberDisplayPolicy(MemberDisplayPolicy):
    def display(self, members):
        print("\n📋 멤버 목록")

        if not members:
            print("- 등록된 멤버가 없습니다.")
            return

        for member in members:
            print(member.display_text())


class MemberManager:
    def __init__(self, sort_policy, display_policy):
        self.members = []
        self.sort_policy = sort_policy
        self.display_policy = display_policy

    def add_member(self, member):
        self.members.append(member)

    def show_members(self):
        sorted_members = self.sort_policy.sort(self.members)
        self.display_policy.display(sorted_members)


class BabyLionConsoleApp:
    def __init__(self):
        self.member_manager = MemberManager(
            RoleThenNameSortPolicy(),
            ConsoleMemberDisplayPolicy(),
        )
        self.is_running = True
        self.actions = {
            "1": self.register_lion,
            "2": self.register_staff,
            "3": self.show_all_members,
            "4": self.stop,
        }

    @staticmethod
    def print_menu():
        print("📌 기능을 선택하세요")
        print("1️⃣  아기사자 등록")
        print("2️⃣  운영진 등록")
        print("3️⃣  전체 출력")
        print("4️⃣  종료")

    def register_lion(self):
        name = input("🦁 이름: ").strip()
        track = input("📚 트랙: ").strip()
        cohort = input("🎓 기수: ").strip()

        try:
            lion = Lion(name, track, cohort)
        except ValueError as error:
            print(f"⚠️ {error}")
            return

        self.member_manager.add_member(lion)
        print("✅ 아기사자가 등록되었습니다.")

    def register_staff(self):
        name = input("🧑‍🏫 이름: ").strip()

        try:
            staff = Staff(name)
        except ValueError as error:
            print(f"⚠️ {error}")
            return

        self.member_manager.add_member(staff)
        print("✅ 운영진이 등록되었습니다.")

    def show_all_members(self):
        self.member_manager.show_members()

    def stop(self):
        print("👋 프로그램을 종료합니다.")
        self.is_running = False

    def run(self):
        while self.is_running:
            self.print_menu()
            choice = input("👉 선택: ").strip()
            action = self.actions.get(choice)

            if action is None:
                print("⚠️ 올바른 번호를 입력해주세요.")
            else:
                action()

            print()


def main():
    BabyLionConsoleApp().run()


if __name__ == "__main__":
    main()
