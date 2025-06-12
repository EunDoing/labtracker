# labtracker.py (상단에 import 추가)
from utils import generate_markdown_report

def main():
    print("🧪 LabTracker 시작!")
    print("1. 실험 기록")
    print("2. 리포트 생성")
    choice = input("선택 (1 or 2): ")

    if choice == "1":
        name = input("🧪 실험명: ")
        date = input("📅 날짜 (YYYY-MM-DD): ")
        condition = input("⚙️ 실험 조건: ")
        result = input("📝 결과 요약: ")

        data = {
            '실험명': name,
            '날짜': date,
            '조건': condition,
            '결과': result
        }

        save_to_csv('data/experiments.csv', data, fieldnames=['실험명', '날짜', '조건', '결과'])
        print("💾 CSV 저장 완료! (data/experiments.csv)")

    elif choice == "2":
        generate_markdown_report('data/experiments.csv', 'reports/summary.md')
    else:
        print("❌ 잘못된 입력입니다.")