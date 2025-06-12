import csv
import os

def save_to_csv(filename, data, fieldnames):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def generate_markdown_report(csv_file, output_file):
    import pandas as pd

    if not os.path.exists(csv_file):
        print("⚠️ CSV 파일이 없습니다. 먼저 실험 데이터를 입력해주세요.")
        return

    df = pd.read_csv(csv_file)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 🧪 실험 기록 리포트\n\n")
        f.write(f"총 {len(df)}개의 실험이 기록되었습니다.\n\n")

        for idx, row in df.iterrows():
            f.write(f"## 실험 {idx+1}: {row['실험명']}\n")
            f.write(f"- 📅 날짜: {row['날짜']}\n")
            f.write(f"- ⚙️ 조건: {row['조건']}\n")
            f.write(f"- 📝 결과: {row['결과']}\n\n")

    print(f"✅ 리포트 생성 완료: {output_file}")