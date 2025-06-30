# 한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 자료

![Chrome Education](https://img.shields.io/badge/Chrome-Education-4285F4?style=for-the-badge&logo=googlechrome)
![Korean Language](https://img.shields.io/badge/Korean-Language-CD212A?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K)
![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-222222?style=for-the-badge&logo=github)
![Auto Build](https://img.shields.io/badge/Auto-Build-00D26A?style=for-the-badge&logo=githubactions)

> **수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로 — 디지털 도구 완전정복**

한글학교 선생님들을 위한 크롬 웹브라우저 활용 교육 자료입니다. 기초부터 고급까지 단계별로 구성되어 있으며, 실습 중심의 학습을 통해 디지털 도구를 효과적으로 활용할 수 있도록 도와드립니다.

## 🌟 주요 특징

- **📊 단계별 구성**: 기초 → 중급 → 고급 순서로 체계적인 학습
- **🎯 실습 중심**: 실제 한글학교 상황에 맞춘 실습 시나리오
- **🤖 자동화**: GitHub Actions를 통한 자동 빌드 및 배포
- **📱 반응형**: 모든 기기에서 최적화된 viewing 경험
- **🔄 지속 업데이트**: 소스 코드 변경 시 자동으로 새 버전 생성

## 🚀 빠른 시작

### 온라인으로 바로 보기

- **슬라이드 프레젠테이션**: [GitHub Pages에서 보기](https://linuxsw.github.io/chrome_lecture_for_korean_teacher/)
- **실습 워크북**: [PDF 다운로드](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/releases/latest)

### 로컬에서 실행하기

```bash
# 저장소 클론
git clone https://github.com/linuxsw/chrome_lecture_for_korean_teacher.git
cd chrome_lecture_for_korean_teacher

# Python 의존성 설치
pip3 install python-pptx

# 교육 자료 생성 (HTML, PDF, PPTX 모두 생성)
bash scripts/generate_materials.sh

# 개별 생성도 가능:
# HTML 슬라이드 및 인덱스만 생성
python3 scripts/generate_slides.py

# PowerPoint 프레젠테이션만 생성
python3 scripts/generate_pptx.py

# 결과물 확인
open output/index.html
```

## 📚 포함된 자료

### 1. 웹 슬라이드 프레젠테이션 (10개 슬라이드)

- **타이틀 슬라이드**: 교육 과정 소개
- **강의 개요**: 목표, 대상, 구성
- **기초 단계**: 크롬 브라우저 기본 기능
- **중급 단계**: 교육자용 확장프로그램 & 한글교육 특화 웹도구
- **고급 단계**: 구글 워크스페이스 연동 & AI 도구 활용
- **실습 시나리오**: 실제 상황 기반 실습 가이드
- **추가 자료**: 참고 링크 및 커뮤니티 정보
- **질문 및 연락처**: 지원 정보

### 2. PowerPoint 프레젠테이션 (PPTX)

- 오프라인 강의용 PowerPoint 파일
- 웹 슬라이드와 동일한 내용 구성
- 프로젝터 연결 및 인쇄 최적화
- 자동 생성되는 타임스탬프 파일명

### 3. 실습 워크북 (PDF)

- 단계별 실습 가이드
- 체크리스트 제공
- 실제 상황 기반 시나리오
- 문제 해결 가이드
- 한글 폰트 지원 (Noto Sans CJK KR)

### 4. 지원 문서

- 교육 도구 조사 자료
- 커리큘럼 설계 문서
- 기술 문서 및 API 가이드

## 🛠️ 프로젝트 구조

```
chrome_lecture_for_korean_teacher/
├── 📁 .github/workflows/     # GitHub Actions 워크플로우
│   ├── build-and-deploy.yml  # 자동 빌드 및 배포
│   └── release.yml           # 릴리스 생성
├── 📁 docs/                  # 문서 및 자료
│   ├── chrome_edu_workbook.md
│   ├── chrome_education_research.md
│   └── curriculum_design.md
├── 📁 scripts/               # 생성 스크립트
│   ├── generate_materials.sh # 통합 빌드 스크립트 (Bash)
│   ├── generate_slides.py    # HTML 슬라이드 생성 (Python)
│   └── generate_pptx.py      # PowerPoint 생성 (Python)
├── 📁 slides/                # 슬라이드 HTML 파일들
│   ├── title_slide.html
│   ├── course_overview.html
│   └── ... (10개 슬라이드)
├── 📁 assets/                # 이미지 및 자원
├── 📁 output/                # 생성된 결과물
└── 📄 README.md              # 이 파일
```

## 🔧 자료 생성 과정

### 1. 수동 생성 (로컬 환경)

#### 필요한 도구

- **Python 3.7+**: 스크립트 실행 환경
- **Bash shell**: 통합 빌드 스크립트 실행
- **pandoc + XeLaTeX**: PDF 생성 (한글 지원)
- **python-pptx**: PowerPoint 파일 생성

#### macOS에서 설치

```bash
# 1. Homebrew로 시스템 도구 설치
brew install pandoc
brew install --cask mactex  # XeLaTeX 포함

# 2. Python 패키지 설치
pip3 install python-pptx

# 3. 자료 생성 실행
bash scripts/generate_materials.sh

# 4. 결과 확인
ls -la output/
open output/index.html
```

#### Ubuntu/Debian에서 설치

```bash
# 1. 시스템 패키지 설치
sudo apt-get update
sudo apt-get install -y python3 python3-pip pandoc texlive-xetex

# 2. Python 패키지 설치
pip3 install python-pptx

# 3. 자료 생성 실행
bash scripts/generate_materials.sh

# 4. 결과 확인
ls -la output/
```

#### Windows에서 설치

```powershell
# 1. Chocolatey로 도구 설치 (관리자 권한)
choco install pandoc miktex

# 2. Python 패키지 설치
pip install python-pptx

# 3. 자료 생성 실행
bash scripts/generate_materials.sh

# 4. 결과 확인
dir output\
start output\index.html
```

### 2. 자동 생성 (GitHub Actions)

#### 트리거 조건

- `main` 또는 `master` 브랜치에 푸시
- Pull Request 생성
- 수동 실행 (workflow_dispatch)
- 태그 푸시 (릴리스 생성)

#### 자동화 프로세스

1. **소스 코드 체크아웃**
2. **환경 설정** (Python, 시스템 도구)
3. **의존성 설치**
4. **자료 생성 스크립트 실행**
5. **PDF 변환**
6. **GitHub Pages 배포**
7. **릴리스 생성** (태그 푸시 시)

## 📋 생성 스크립트 상세

### 통합 빌드 스크립트 (`scripts/generate_materials.sh`)

- 출력 디렉토리 초기화 및 설정
- 슬라이드 HTML 파일 검증 및 복사
- 순서별 파일명 변경 (01_title_slide.html 등)
- 이미지 및 문서 파일 복사
- PDF 워크북 생성 (pandoc + XeLaTeX)
- PowerPoint 프레젠테이션 생성
- 빌드 정보 및 메타데이터 생성

### HTML 슬라이드 생성 (`scripts/generate_slides.py`)

- 슬라이드 구성 정보 관리
- 메인 인덱스 페이지 생성 (index.html)
- 동적 생성일 표시 기능
- 빌드 메타데이터 생성 (build_info.json)
- PDF/PPTX 파일 자동 링크 연결

### PowerPoint 생성 (`scripts/generate_pptx.py`)

- 10개 슬라이드 자동 생성
- 웹 슬라이드와 동일한 내용 구성
- 타임스탬프 기반 파일명 생성
- 한글 텍스트 완전 지원
- 로깅 시스템으로 오류 추적

## 🤖 자동화 시스템

### GitHub Actions 워크플로우

#### 1. 빌드 및 배포 (`build-and-deploy.yml`)

```yaml
# 트리거: push to main/master, PR, manual
# 기능: 자료 생성 → GitHub Pages 배포
```

#### 2. 릴리스 생성 (`release.yml`)

```yaml
# 트리거: 태그 푸시 (v*)
# 기능: 자료 생성 → 패키징 → 릴리스 생성
```

### 자동 업데이트 프로세스

1. 소스 코드 수정 후 커밋
2. GitHub에 푸시
3. GitHub Actions 자동 실행
4. 새로운 자료 자동 생성
5. GitHub Pages 자동 업데이트
6. 사용자에게 최신 버전 제공

## 📁 생성된 파일 구조

빌드 완료 후 `output/` 디렉토리에 다음 파일들이 생성됩니다:

```
output/
├── 📄 index.html                           # 메인 인덱스 페이지
├── 📄 slides_index.html                    # 슬라이드 목록 페이지
├── 📊 chrome_education_slides_YYYYMMDD_HHMM.pptx  # PowerPoint 프레젠테이션
├── 📚 chrome_edu_workbook_YYYYMMDD_HHMM.pdf       # 실습 워크북 PDF
├── 📋 build_info.json                      # 빌드 정보 메타데이터
├── 🎯 01_title_slide.html                  # 개별 슬라이드 파일들
├── 🎯 02_course_overview.html              # (순서별로 01~10)
├── 🎯 03_basic_features.html
├── 🎯 04_extensions_intro.html
├── 🎯 05_korean_edu_tools.html
├── 🎯 06_advanced_collab.html
├── 🎯 07_ai_tools.html
├── 🎯 08_practice_scenarios.html
├── 🎯 09_resources.html
├── 🎯 10_qa_contact.html
├── 📁 images/                              # 슬라이드 이미지 파일들
└── 📄 *.md                                 # 문서 파일들 (복사본)
```

## 📥 다운로드 및 사용

### 온라인 사용

- **웹 버전**: https://linuxsw.github.io/chrome_lecture_for_korean_teacher/
- **직접 링크**: 각 슬라이드별 개별 접근 가능 (01_title_slide.html ~ 10_qa_contact.html)

### 로컬 빌드 후 사용

```bash
# 빌드 완료 후 브라우저에서 열기
open output/index.html          # macOS
start output/index.html         # Windows
xdg-open output/index.html      # Linux

# PowerPoint 파일 열기
open output/chrome_education_slides_*.pptx

# PDF 워크북 열기
open output/chrome_edu_workbook_*.pdf
```

### 오프라인 사용

1. **전체 패키지**: [최신 릴리스](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/releases/latest)에서 ZIP 파일 다운로드
2. **개별 파일**: 필요한 파일만 선택적 다운로드
3. **PDF 워크북**: 인쇄용 PDF 파일 제공

### 교육 현장 활용

- **웹 프레젠테이션**: `index.html`을 브라우저에서 열어 인터랙티브 슬라이드 사용
- **PowerPoint 강의**: `.pptx` 파일을 PowerPoint에서 열어 전통적인 프레젠테이션
- **프로젝터 연결**: 슬라이드를 프로젝터로 직접 투영
- **인쇄물 제작**: PDF 워크북을 인쇄하여 배포
- **온라인 수업**: 화면 공유를 통한 원격 교육
- **자율 학습**: 개별 학습자의 속도에 맞춘 학습

## 🔧 문제 해결

### 자주 발생하는 문제들

#### 1. PDF 생성 실패 (한글 깨짐)

```bash
# 문제: PDF에서 한글이 깨져서 나타남
# 해결: XeLaTeX와 한글 폰트 설치

# macOS
brew install --cask mactex
sudo tlmgr install collection-langcjk

# Ubuntu/Debian
sudo apt-get install texlive-xetex texlive-lang-cjk
sudo apt-get install fonts-noto-cjk

# 폰트 확인
fc-list | grep -i noto
```

#### 2. PowerPoint 생성 실패

```bash
# 문제: python-pptx 모듈을 찾을 수 없음
# 해결: 패키지 설치 확인

pip3 install python-pptx
# 또는
pip install python-pptx

# 설치 확인
python3 -c "import pptx; print('python-pptx 설치 완료')"
```

#### 3. 빌드 스크립트 실행 권한 오류

```bash
# 문제: Permission denied
# 해결: 실행 권한 부여

chmod +x scripts/generate_materials.sh
bash scripts/generate_materials.sh
```

#### 4. 생성일이 표시되지 않는 문제

```bash
# 문제: index.html에서 생성일이 {datetime.now()...} 형태로 표시
# 해결: Python 스크립트 실행 확인

python3 scripts/generate_slides.py
```

### 로그 확인 방법

```bash
# PPTX 생성 로그 확인
cat pptx_generator.log

# 빌드 과정 상세 로그
bash -x scripts/generate_materials.sh
```

## 🔄 업데이트 및 기여

### 자료 업데이트

```bash
# 새로운 버전 태그 생성 (자동 릴리스)
git tag v1.1.0
git push origin v1.1.0

# 일반 업데이트 (자동 빌드)
git add .
git commit -m "Update educational materials"
git push origin main
```

### 기여 방법

1. **이슈 제기**: 개선 사항이나 버그 신고
2. **Pull Request**: 직접 수정 사항 제안
3. **피드백**: 교육 현장에서의 사용 경험 공유

## 📊 기술 스택

### 프론트엔드

- **HTML5**: 슬라이드 구조
- **CSS3**: 스타일링 (Tailwind CSS)
- **JavaScript**: 인터랙티브 요소 (Chart.js, D3.js)
- **Font Awesome**: 아이콘
- **Google Fonts**: 한글 폰트 (Noto Sans KR)

### 백엔드/도구

- **Python 3.7+**: 스크립트 및 자동화
- **python-pptx**: PowerPoint 파일 생성
- **Bash**: 시스템 스크립트
- **Pandoc + XeLaTeX**: 한글 지원 PDF 생성

### 인프라

- **GitHub**: 소스 코드 관리
- **GitHub Actions**: CI/CD 파이프라인
- **GitHub Pages**: 웹 호스팅
- **GitHub Releases**: 파일 배포

## 🎯 교육 목표 및 효과

### 학습 목표

- 크롬 브라우저의 교육적 활용 능력 향상
- 디지털 도구를 통한 수업 효율성 증대
- 온라인 협업 및 자료 관리 역량 강화
- AI 도구 활용을 통한 교육 혁신

### 기대 효과

- **수업 준비 시간 단축**: 효율적인 자료 수집 및 정리
- **학생 참여도 향상**: 인터랙티브한 수업 환경 구축
- **협업 강화**: 교사 간, 교사-학생 간 원활한 소통
- **지속적 성장**: 최신 교육 기술 트렌드 적응

## 🌐 관련 링크

### 공식 자료

- [Google Chrome 도움말](https://support.google.com/chrome)
- [Chrome 웹 스토어](https://chrome.google.com/webstore)
- [Google Workspace for Education](https://edu.google.com)

### 한글교육 자료

- [스터디코리안넷](https://study.korean.net)
- [국립국어원 한국어교수학습샘터](https://kcenter.korean.go.kr)
- [재미한국학교협의회 (NAKS)](https://www.naks.org)

### 커뮤니티

- [한글학교 교사 네트워크](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/discussions)
- [교육 기술 포럼](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/issues)

## 📞 지원 및 문의

### 기술 지원

- **GitHub Issues**: [문제 신고 및 기능 요청](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/issues)
- **GitHub Discussions**: [질문 및 토론](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/discussions)

### 연락처

- **개발자**: Seungweon Park (linuxsw@gmail.com)
- **저장소**: https://github.com/linuxsw/chrome_lecture_for_korean_teacher

## 📄 라이선스

이 프로젝트는 교육 목적으로 자유롭게 사용, 수정, 배포할 수 있습니다.

### 사용 조건

- **교육 목적**: 한글교육 및 교사 연수에 자유 사용
- **비상업적 사용**: 영리 목적 사용 시 사전 연락
- **출처 표기**: 자료 사용 시 출처 명시 권장

## 🙏 감사의 말

이 교육 자료는 전 세계 한글학교 선생님들의 헌신적인 노력에서 영감을 받아 제작되었습니다. 한글교육의 디지털 혁신을 위해 함께 노력하는 모든 분들께 감사드립니다.

---

<div align="center">

**🌟 더 나은 한글교육을 위한 여러분의 디지털 여정을 응원합니다! 🌟**

[![GitHub stars](https://img.shields.io/github/stars/linuxsw/chrome_lecture_for_korean_teacher?style=social)](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/linuxsw/chrome_lecture_for_korean_teacher?style=social)](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/network/members)

</div>
