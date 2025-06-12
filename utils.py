import csv
import os

def save_to_csv(name, date, condition, result, path="data/experiments.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    is_new_file = not os.path.exists(path)

    with open(path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if is_new_file:
            writer.writerow(["실험명", "날짜", "조건", "결과"])
        writer.writerow([name, date, condition, result])

def generate_markdown_report(input_path="data/experiments.csv", output_path="reports/summary.md"):
    import pandas as pd
    if not os.path.exists(input_path):
        print("⚠️ CSV 파일이 없어 summary.md 생성 건너뜀")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 🧪 실험 기록 요약\n\n")
        f.write(df.to_markdown(index=False))
