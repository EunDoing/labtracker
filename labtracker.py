# labtracker.py

def main():
    print("📌 실험 기록 시작!")
    name = input("🧪 실험명: ")
    date = input("📅 날짜 (YYYY-MM-DD): ")
    condition = input("⚙ 실험 조건: ")
    result = input("📝 결과 요약: ")

    print("\n✅ 입력된 실험 정보:")
    print(f" - 실험명: {name}")
    print(f" - 날짜: {date}")
    print(f" - 조건: {condition}")
    print(f" - 결과: {result}")

if __name__ == "__main__":
    main()