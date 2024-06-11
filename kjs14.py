def kiosk():
    menu = ["냉면", "볶음밥", "피자", "짜장면"]

    while True:
        try:
            print("메뉴:")
            for i, item in enumerate(menu, 1):
                print(f"{i}. {item}")

            choice = int(input("메뉴 번호를 선택하세요: "))

            if choice < 1 or choice > len(menu):
                raise IndexError("잘못된 번호입니다.")

            print(f"선택한 메뉴: {menu[choice - 1]}")
            break  # 올바른 선택이므로 루프 종료

        except ValueError:
            print("숫자를 입력해주세요.")

        except IndexError:
            print("메뉴에 없는 번호입니다. 다시 입력해주세요.")


kiosk()