# 🧪 LabTracker

실험 기록을 손쉽게 관리할 수 있는 CLI 기반 실험 자동화 프로그램입니다.  
CSV 파일로 실험 데이터를 저장하고, 마크다운 형식의 요약 리포트를 자동으로 생성합니다.

---

## ✅ 주요 기능

- 실험명, 날짜, 조건, 결과 입력 기능  
- 입력된 실험 데이터를 `data/experiments.csv`에 저장  
- 마크다운 리포트(`reports/summary.md`) 자동 생성  
- GitHub Actions를 활용한 자동 리포트 생성 워크플로우 포함

---

## 💻 실행 방법

1. 이 저장소를 클론합니다:

```bash
git clone https://github.com/본인아이디/labtracker.git
cd labtracker
```

2. 필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

3. 프로그램을 실행합니다:

```bash
python labtracker.py
```

---

## 🗂️ 프로젝트 구조

```
labtracker/
├── labtracker.py              # 메인 실행 파일
├── utils.py                   # 저장 및 리포트 유틸 함수
├── data/
│   └── experiments.csv        # 실험 입력 데이터 저장 위치
├── reports/
│   └── summary.md             # 실험 요약 리포트 생성 위치
├── requirements.txt           # 설치 패키지 목록
├── .github/workflows/
│   └── report.yml             # 자동 리포트 생성 GitHub Action
└── README.md
```

---

## 🧪 예시 실행 화면

```
선택 (1 or 2): 1
🧪 실험명: CNT 복합체 실험
📅 날짜 (YYYY-MM-DD): 2025-06-13
⚙️ 실험 조건: 3wt% CNT, 150도
📝 결과 요약: 전도도 증가 확인됨
💾 CSV 저장 완료! (data/experiments.csv)
```

---

## 🔧 주의사항

- `data/`, `reports/` 폴더는 미리 생성해 주세요. (`.gitkeep`으로 포함됨)  
- 실행 후 리포트가 자동으로 생성되지 않으면 2번 메뉴에서 직접 생성할 수 있습니다.  
- GitHub Actions는 `main` 브랜치에서만 작동합니다.

---

## 📮 제작자

- 동아대 ＡＩ학과 ２４４３７６５ 은수인
- 과제 제출용
