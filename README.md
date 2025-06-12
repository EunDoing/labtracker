# 🧪 LabTracker

**LabTracker**는 CLI에서 실험 데이터를 입력하면 자동으로 CSV에 저장하고,  
하루가 지나면 GitHub Actions를 통해 Markdown 리포트를 자동 생성하는 실험 기록 관리 프로그램입니다.

---

## 📌 개발 목적

LabTracker는 반복적인 실험 데이터 기록과 정리를 간편하게 자동화하기 위해 개발된 CLI 기반 소프트웨어입니다.  
사용자가 직접 실험명을 입력하고, 날짜, 조건, 결과를 기록하면, 프로그램이 데이터를 자동으로 CSV에 저장하고  
마크다운 형식의 리포트를 생성해 실험 과정을 체계적으로 관리할 수 있도록 돕습니다.
실험을 자주 하는 학과의 친구가 실험 기록 정리에 어려움을 겪는 것을 보고 누구나 쉽게 실험 정보를 기록하고
관리할 수 있는 도구를 만들고자 하여 해당 프로그램을 만들게 되었습니다.

---

## 📌 주요 기능

1. **실험 기록 입력** → CSV(`data/experiments.csv`)로 저장
2. **리포트 생성** → Markdown 리포트(`reports/summary.md`)로 출력
3. **자동 리포트 생성** → GitHub Actions가 매일 0시에 리포트를 새로 갱신

---

## ⚙️ 실행 방법

### ▶️ 실험 기록 입력
```bash
python labtracker.py
```
실행 후 `1` 입력 → 실험 정보 입력 → 자동 저장

### ▶️ 리포트 수동 생성
```bash
python labtracker.py
```
실행 후 `2` 입력 → `reports/summary.md` 생성됨

---

## 📁 폴더 구조 예시

```
labtracker/
├── data/
│   └── experiments.csv       ← 실험 데이터 저장
├── reports/
│   └── summary.md            ← 리포트 결과 저장
├── labtracker.py             ← 메인 실행 파일
├── utils.py                  ← 저장 및 리포트 유틸 함수
├── requirements.txt
└── .github/
    └── workflows/
        └── report.yml        ← GitHub Actions 자동 리포트 설정
---

## 📦 설치 필요 패키지

```bash
인
---
