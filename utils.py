import csv
import os

def save_to_csv(path, data, fieldnames):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    file_exists = os.path.isfile(path)

    with open(path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

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
