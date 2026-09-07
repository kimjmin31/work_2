books = []


def register_book():
	"""도서를 등록한다."""
	
	title = input("도서 제목: ").strip()
	author = input("저자: ").strip()

	if not title or not author:
		print("제목과 저자를 모두 입력해야 합니다.")
		return

	books.append({"title": title, "author": author, "rented": False})
	print("도서가 등록되었습니다.")


def show_books(book_list=None):
	"""전체 도서 또는 검색 결과를 출력한다."""
	items = books if book_list is None else book_list

	if not items:
		print("등록된 도서가 없습니다.")
		return

	print("\n번호 | 도서명 | 저자 | 대여 상태")
	print("-" * 45)
	for number, book in enumerate(items, 1):
		status = "대여 중" if book["rented"] else "대여 가능"
		print(f"{number} | {book['title']} | {book['author']} | {status}")


def search_book():
	keyword = input("검색할 도서명 또는 저자: ").strip().lower()
	if not keyword:
		print("검색어를 입력해야 합니다.")
		return

	results = [
		book for book in books
		if keyword in book["title"].lower() or keyword in book["author"].lower()
	]
	show_books(results)


def select_book(action):
	if not books:
		print("등록된 도서가 없습니다.")
		return

	show_books()
	try:
		number = int(input(f"{action}할 도서 번호: "))
		if not 1 <= number <= len(books):
			raise ValueError
	except ValueError:
		print("올바른 도서 번호를 입력하세요.")
		return

	book = books[number - 1]
	if action == "대여":
		if book["rented"]:
			print("이미 대여 중인 도서입니다.")
		else:
			book["rented"] = True
			print("도서가 대여 처리되었습니다.")
	else:
		if not book["rented"]:
			print("대여 중이 아닌 도서입니다.")
		else:
			book["rented"] = False
			print("도서가 반납 처리되었습니다.")


def main():
	while True:
		print("\n===== 도서 관리 프로그램 =====")
		print("1. 도서 등록")
		print("2. 전체 도서 조회")
		print("3. 도서 검색")
		print("4. 도서 대여")
		print("5. 도서 반납처리")
		print("6. 종료")

		choice = input("메뉴를 선택하세요: ").strip()

		if choice == "1":
			register_book()
		elif choice == "2":
			show_books()
		elif choice == "3":
			search_book()
		elif choice == "4":
			select_book("대여")
		elif choice == "5":
			select_book("반납")
		elif choice == "6":
			print("프로그램을 종료합니다.")
			break
		else:
			print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
	main()
