import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import save_to_csv, generate_markdown_report

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "2":
        generate_markdown_report()
        return

    print("📌 실험 기록 시작!")
    name = input("🧪 실험명: ")
    date = input("📅 날짜 (YYYY-MM-DD): ")
    condition = input("⚙️ 실험 조건: ")
    result = input("📝 결과 요약: ")

    save_to_csv(name, date, condition, result)
    print("\n✅ 실험 정보가 저장되었습니다!")

if __name__ == "__main__":
    main()
