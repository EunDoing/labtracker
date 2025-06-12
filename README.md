# 🧪 LabTracker
2443765 AI학과 은수인

**LabTracker**는 CLI에서 실험 데이터를 입력하면 자동으로 CSV에 저장하고,  
하루가 지나면 GitHub Actions를 통해 Markdown 리포트를 자동 생성하는 실험 기록 관리 프로그램입니다.

---

## 📌 개발 목적

LabTracker는 반복적인 실험 데이터 기록과 정리를 간편하게 자동화하기 위해 개발된 CLI 기반 소프트웨어입니다.  
사용자가 직접 실험명을 입력하고, 날짜, 조건, 결과를 기록하면, 프로그램이 데이터를 자동으로 CSV에 저장하고  
마크다운 형식의 리포트를 생성해 실험 과정을 체계적으로 관리할 수 있도록 돕습니다.
실험을 자주 하는 학과의 친구가 실험 기록 정리에 어려움을 겪는 것을 보고 누구나 쉽게 실험 정보를 기록하고
관리할 수 있는 도구를 만들고자 하여 해당 프로그램을 만들게 되었습니다.


⸻

## 🧩 주요 기능
	•	실험 정보 입력 (CLI)
	•	실험 내용 자동 CSV 저장 (data/experiments.csv)
	•	Markdown 형식 리포트 생성 (reports/summary.md)
	•	GitHub Actions로 매일 자정 자동 리포트 업데이트

⸻

## 🔄 입출력 형태

입력은 CLI에서 수행되며, 출력은 파일로 저장됩니다.

입력 항목:
	•	실험명, 날짜, 조건, 결과

출력 위치:
	•	data/experiments.csv (누적 저장)
	•	reports/summary.md (요약 리포트)

출력 방식:
	•	수동 생성: 메뉴에서 2번 선택
	•	자동 생성: GitHub Actions에서 매일 자정 자동 실행

⸻

## 📁 폴더 구조

labtracker/
├── data/experiments.csv ← 실험 데이터
├── reports/summary.md ← 자동 생성 리포트
├── labtracker.py ← 메인 실행 파일
├── utils.py ← 저장/리포트 함수
├── requirements.txt ← 설치용 패키지 목록
└── .github/workflows/report.yml ← 자동화 설정

참고: 샘플 파일이 들어 있어 직접 실행해보지 않아도 구조 확인 가능

## ▶️ 실행 방법
	1.	Python 3.8+ 설치
	2.	다음 명령어로 패키지 설치
→ pip install -r requirements.txt
(필요 패키지: pandas, tabulate)
	3.	python labtracker.py 실행
메뉴 선택:
	•	1 → 실험 기록
	•	2 → 리포트 생성

⸻

## 🧷 기타

GitHub 주소: https://github.com/EunDoing/labtracker
