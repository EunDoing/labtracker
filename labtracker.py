# labtracker.py
from utils import save_to_csv

def main():
    print("📌 실험 기록 시작!")
    name = input("🧪 실험명: ")
    date = input("📅 날짜 (YYYY-MM-DD): ")
    condition = input("⚙️ 실험 조건: ")
    result = input("📝 결과 요약: ")

    print("\n✅ 입력된 실험 정보:")
    print(f" - 실험명: {name}")
    print(f" - 날짜: {date}")
    print(f" - 조건: {condition}")
    print(f" - 결과: {result}")

    data = {
        '실험명': name,
        '날짜': date,
        '조건': condition,
        '결과': result
    }

    save_to_csv('data/experiments.csv', data, fieldnames=['실험명', '날짜', '조건', '결과'])
    print("💾 CSV 저장 완료! (data/experiments.csv)")

if __name__ == "__main__":
    main()