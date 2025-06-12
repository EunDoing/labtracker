# 🧪 LabTracker

---

## 📌 개발 목적

LabTracker는 반복적인 실험 데이터 기록과 정리를 간편하게 자동화하기 위해 개발된 CLI 기반 소프트웨어입니다.  
사용자가 직접 실험명을 입력하고, 날짜, 조건, 결과를 기록하면, 프로그램이 데이터를 자동으로 CSV에 저장하고  
마크다운 형식의 리포트를 생성해 실험 과정을 체계적으로 관리할 수 있도록 돕습니다.
실험을 자주 하는 학과의 친구가 실험 기록 정리에 어려움을 겪는 것을 보고 누구나 쉽게 실험 정보를 기록하고
관리할 수 있는 도구를 만들고자 하여 해당 프로그램을 만들게 되었습니다.

---

## ⚙️ 상세 기능

- CLI(명령줄 인터페이스) 환경에서 실험 데이터 입력
- 입력값(실험명, 날짜, 조건, 결과)을 CSV 파일로 저장
- 기존 데이터가 있을 경우 이어서 자동 누적 저장
- 저장된 CSV 데이터를 바탕으로 Markdown 리포트 생성
- GitHub Actions를 통한 리포트 자동 업데이트

---

## 🔁 입출력 형태

### 입력

- 사용자 입력 항목:  
  - 실험명 (예: "CNT 복합체 실험")  
  - 날짜 (예: "2025-06-13")  
  - 실험 조건 (예: "3wt% CNT, 150도")  
  - 결과 요약 (예: "전도도 증가 확인됨")

### 출력

- `/data/experiments.csv`  
  → 모든 실험 기록을 누적 저장하는 CSV 파일

- `/reports/summary.md`  
  → 실험 기록 전체를 표 형태로 요약한 마크다운 파일

---
## 💻 실행 방법 (Step-by-Step Guide)

### 1️⃣ 저장소 클론

```bash
git clone https://github.com/본인아이디/labtracker.git
cd labtracker
```

---

### 2️⃣ 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

> 설치되는 주요 라이브러리:
> - `pandas` : CSV 파일 처리
> - `tabulate` : Markdown 표 생성

---

### 3️⃣ 폴더 구조 확인 / 생성

아래 두 개의 폴더는 프로그램 실행 전에 **반드시 존재해야 합니다.**

| 폴더명 | 용도 |
|--------|------|
| `data/` | 실험 데이터를 저장하는 폴더 (`experiments.csv`) |
| `reports/` | 마크다운 리포트가 생성되는 폴더 (`summary.md`) |

#### ✅ 생성 방법

```bash
mkdir data
mkdir reports
```

또는 파일 탐색기에서 직접 폴더를 만들어도 됩니다.

---

### 📁 폴더 배치 예시

```
labtracker/               ← 최상위 폴더
├── labtracker.py         ← 메인 실행 파일
├── utils.py              ← CSV 저장 및 리포트 생성 함수
├── requirements.txt      ← 필요한 패키지 목록
├── README.md             ← 설명 문서
├── data/                 ← 실험 기록 저장
│   └── experiments.csv   ← [자동 생성됨]
├── reports/              ← 리포트 저장
│   └── summary.md        ← [자동 생성됨]
```

> **주의:** `data/`와 `reports/`는 반드시 `labtracker.py`와 같은 폴더 위치에 있어야 합니다.  
> 다른 경로에 있을 경우 프로그램이 파일을 찾지 못해 오류가 발생할 수 있습니다.

---

### 4️⃣ 프로그램 실행

```bash
python labtracker.py
```

실행하면 다음과 같은 메뉴가 표시됩니다:

```
🧪 LabTracker 시작!
1. 실험 기록
2. 리포트 생성
선택 (1 or 2):

---

### 🔄 GitHub Actions 자동화 (선택사항)

- `main` 브랜치에 push하거나
- GitHub Actions 탭에서 수동 실행 시

`summary.md` 리포트가 자동으로 갱신되고 저장소에 반영됩니다.

---
