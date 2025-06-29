# 설치 및 실행 가이드

이 가이드는 한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 자료를 로컬 환경에서 생성하고 실행하는 방법을 설명합니다.

## 🖥️ 시스템 요구사항

### 최소 요구사항
- **운영체제**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **메모리**: 4GB RAM
- **저장공간**: 1GB 여유 공간
- **인터넷**: 의존성 다운로드를 위한 인터넷 연결

### 권장 요구사항
- **운영체제**: Windows 11, macOS 12+, Ubuntu 20.04+
- **메모리**: 8GB RAM
- **저장공간**: 2GB 여유 공간

## 🛠️ 설치 방법

### 1. Ubuntu/Debian 계열

```bash
# 시스템 업데이트
sudo apt-get update

# 필수 패키지 설치
sudo apt-get install -y \
    git \
    python3 \
    python3-pip \
    pandoc \
    wkhtmltopdf \
    curl \
    wget

# Python 패키지 설치
pip3 install --user markdown weasyprint reportlab

# 저장소 클론
git clone https://github.com/linuxsw/chrome_lecture_for_korean_teacher.git
cd chrome_lecture_for_korean_teacher

# 실행 권한 부여
chmod +x scripts/*.sh scripts/*.py
```

### 2. CentOS/RHEL/Fedora 계열

```bash
# 시스템 업데이트
sudo yum update  # 또는 sudo dnf update (Fedora)

# 필수 패키지 설치
sudo yum install -y \
    git \
    python3 \
    python3-pip \
    pandoc \
    wkhtmltopdf \
    curl \
    wget

# Python 패키지 설치
pip3 install --user markdown weasyprint reportlab

# 저장소 클론
git clone https://github.com/linuxsw/chrome_lecture_for_korean_teacher.git
cd chrome_lecture_for_korean_teacher

# 실행 권한 부여
chmod +x scripts/*.sh scripts/*.py
```

### 3. macOS

```bash
# Homebrew 설치 (없는 경우)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 필수 패키지 설치
brew install git python3 pandoc wkhtmltopdf

# Python 패키지 설치
pip3 install markdown weasyprint reportlab

# 저장소 클론
git clone https://github.com/linuxsw/chrome_lecture_for_korean_teacher.git
cd chrome_lecture_for_korean_teacher

# 실행 권한 부여
chmod +x scripts/*.sh scripts/*.py
```

### 4. Windows

#### 4.1 WSL2 사용 (권장)
```powershell
# WSL2 설치 (PowerShell 관리자 권한)
wsl --install

# Ubuntu 설치 후 위의 Ubuntu 설치 방법 따라하기
```

#### 4.2 직접 설치
1. **Git 설치**: https://git-scm.com/download/win
2. **Python 설치**: https://www.python.org/downloads/windows/
3. **Pandoc 설치**: https://pandoc.org/installing.html
4. **wkhtmltopdf 설치**: https://wkhtmltopdf.org/downloads.html

```cmd
# Python 패키지 설치
pip install markdown weasyprint reportlab

# 저장소 클론
git clone https://github.com/linuxsw/chrome_lecture_for_korean_teacher.git
cd chrome_lecture_for_korean_teacher
```

## 🚀 실행 방법

### 1. 전체 자료 생성
```bash
# Bash 스크립트 실행
bash scripts/generate_materials.sh

# 또는 Python 스크립트 실행
python3 scripts/generate_slides.py
```

### 2. 결과물 확인
```bash
# 생성된 파일 목록 확인
ls -la output/

# 웹 브라우저에서 열기
# Linux/macOS
open output/index.html

# Windows
start output/index.html
```

### 3. 로컬 웹 서버 실행 (선택사항)
```bash
# Python 내장 웹 서버 사용
cd output
python3 -m http.server 8000

# 브라우저에서 http://localhost:8000 접속
```

## 🔧 문제 해결

### 일반적인 문제

#### 1. 권한 오류
```bash
# 스크립트 실행 권한 부여
chmod +x scripts/*.sh scripts/*.py
```

#### 2. Python 패키지 설치 오류
```bash
# pip 업그레이드
pip3 install --upgrade pip

# 가상환경 사용 (권장)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
pip install markdown weasyprint reportlab
```

#### 3. wkhtmltopdf 오류
```bash
# Ubuntu에서 추가 패키지 설치
sudo apt-get install -y xvfb

# 또는 다른 PDF 생성 도구 사용
pip install pdfkit
```

#### 4. 한글 폰트 문제
```bash
# Ubuntu에서 한글 폰트 설치
sudo apt-get install -y fonts-noto-cjk

# macOS에서 한글 폰트 설치
brew install --cask font-noto-sans-cjk-kr
```

### 플랫폼별 특이사항

#### Ubuntu 18.04
- Python 3.6 사용 시 일부 패키지 호환성 문제 가능
- `python3.8` 이상 설치 권장

#### macOS Big Sur 이상
- Apple Silicon (M1/M2) 칩에서 일부 패키지 설치 시 추가 설정 필요
- Rosetta 2 설치 권장

#### Windows
- 경로에 공백이 있으면 문제 발생 가능
- 짧은 경로 사용 권장

## 📋 설치 확인

설치가 완료되면 다음 명령어로 확인:

```bash
# 버전 확인
python3 --version
pandoc --version
wkhtmltopdf --version

# 테스트 실행
python3 scripts/generate_slides.py
```

성공적으로 실행되면 `output/` 디렉토리에 파일들이 생성됩니다.

## 🆘 추가 도움

설치 중 문제가 발생하면:

1. **GitHub Issues**: https://github.com/linuxsw/chrome_lecture_for_korean_teacher/issues
2. **이메일**: linuxsw@gmail.com
3. **문서**: 각 도구의 공식 문서 참조

## 🔄 업데이트

```bash
# 저장소 업데이트
git pull origin main

# 의존성 업데이트
pip3 install --upgrade markdown weasyprint reportlab

# 새로운 자료 생성
bash scripts/generate_materials.sh
```

---

설치가 완료되면 [README.md](README.md)를 참조하여 자료를 활용해 보세요! 🎉

