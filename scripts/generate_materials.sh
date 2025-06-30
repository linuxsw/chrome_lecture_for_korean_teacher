#!/bin/bash

# Chrome Education Materials Generator
# 한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 자료 생성 스크립트

echo "🚀 Chrome Education Materials Generator 시작"

# 프로젝트 디렉토리 설정
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SLIDES_DIR="$PROJECT_DIR/slides"
DOCS_DIR="$PROJECT_DIR/docs"
OUTPUT_DIR="$PROJECT_DIR/output"
ASSETS_DIR="$PROJECT_DIR/assets"

# 출력 디렉토리 초기화
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"
echo "🗑️  출력 디렉토리 초기화 완료"

echo "📁 프로젝트 디렉토리: $PROJECT_DIR"

# 1. 슬라이드 HTML 파일들이 존재하는지 확인
echo "🔍 슬라이드 파일 확인 중..."
SLIDE_FILES=(
    "title_slide.html"
    "course_overview.html"
    "basic_features.html"
    "extensions_intro.html"
    "korean_edu_tools.html"
    "advanced_collab.html"
    "ai_tools.html"
    "practice_scenarios.html"
    "resources.html"
    "qa_contact.html"
)

for slide in "${SLIDE_FILES[@]}"; do
    if [[ ! -f "$SLIDES_DIR/$slide" ]]; then
        echo "❌ 슬라이드 파일이 없습니다: $slide"
        exit 1
    fi
done

echo "✅ 모든 슬라이드 파일이 존재합니다."

# 2. 슬라이드 인덱스 HTML 생성
echo "📄 슬라이드 인덱스 생성 중..."
cat > "$OUTPUT_DIR/slides_index.html" << 'EOF'
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>한글학교 선생님을 위한 크롬 웹브라우저 활용 교육</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Noto Sans KR', sans-serif; }
        .slide-card:hover { transform: translateY(-2px); transition: all 0.3s ease; }
    </style>
</head>
<body class="bg-gray-100">
    <div class="container mx-auto px-4 py-8">
        <h1 class="text-4xl font-bold text-center text-blue-600 mb-8">
            수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로<br>
            <span class="text-2xl text-gray-700">디지털 도구 완전정복</span>
        </h1>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
EOF

# 슬라이드 카드 생성
SLIDE_TITLES=(
    "타이틀 슬라이드"
    "강의 개요"
    "기초: 크롬 브라우저 기본 기능"
    "중급: 교육자를 위한 확장프로그램"
    "중급: 한글교육 특화 웹도구"
    "고급: 구글 워크스페이스 연동"
    "고급: AI 도구 활용"
    "실습 시나리오"
    "추가 자료 및 참고 링크"
    "질문 및 연락처"
)

for i in "${!SLIDE_FILES[@]}"; do
    cat >> "$OUTPUT_DIR/slides_index.html" << EOF
            <div class="slide-card bg-white rounded-lg shadow-md p-6 hover:shadow-lg">
                <h3 class="text-lg font-bold text-gray-800 mb-2">${SLIDE_TITLES[$i]}</h3>
                <p class="text-gray-600 mb-4">슬라이드 $(($i + 1))</p>
                <a href="$(printf "%02d" $((i+1)))_${SLIDE_FILES[$i]}" target="_blank" 
                   class="inline-block bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition-colors">
                    보기
                </a>
            </div>
EOF
done

cat >> "$OUTPUT_DIR/slides_index.html" << 'EOF'
        </div>
        
        <div class="mt-12 text-center">
            <h2 class="text-2xl font-bold text-gray-800 mb-4">추가 자료</h2>
            <div class="flex justify-center space-x-4">
                <a href="../docs/chrome_edu_workbook.pdf" target="_blank" 
                   class="bg-green-500 text-white px-6 py-3 rounded-lg hover:bg-green-600 transition-colors">
                    📚 실습 워크북 (PDF)
                </a>
                <a href="../docs/chrome_education_research.md" target="_blank" 
                   class="bg-purple-500 text-white px-6 py-3 rounded-lg hover:bg-purple-600 transition-colors">
                    📋 조사 자료
                </a>
                <a href="../docs/curriculum_design.md" target="_blank" 
                   class="bg-orange-500 text-white px-6 py-3 rounded-lg hover:bg-orange-600 transition-colors">
                    📖 커리큘럼 설계
                </a>
            </div>
        </div>
    </div>
</body>
</html>
EOF

echo "✅ 슬라이드 인덱스 생성 완료"

# 3. 워크북 PDF 생성 (한글 지원 개선)
if [[ -f "$DOCS_DIR/chrome_edu_workbook.md" ]]; then
    echo "📚 워크북 PDF 생성 중..."
    
    # 변수 초기화
    TIMESTAMP=$(date +"%Y%m%d_%H%M")
    PDF_FILENAME="chrome_edu_workbook_${TIMESTAMP}.pdf"
    
    # 필요한 도구 확인
    if ! command -v pandoc &> /dev/null || ! command -v xelatex &> /dev/null; then
        echo "⚠️  pandoc 또는 xelatex가 설치되어 있지 않습니다."
        echo "macOS의 경우: brew install pandoc && brew install --cask mactex"
        echo "Ubuntu의 경우: sudo apt-get install pandoc texlive-xetex"
        echo "PDF 생성을 건너뜁니다."
    else
        echo "🔧 pandoc + xelatex로 PDF 생성 중..."
        if pandoc "$DOCS_DIR/chrome_edu_workbook.md" \
            -o "$OUTPUT_DIR/$PDF_FILENAME" \
            --pdf-engine=xelatex \
            --variable mainfont="Noto Sans CJK KR" \
            --variable lang=ko \
            --toc \
            --metadata title="한글학교 선생님을 위한 크롬 웹브라우저 활용 실습 워크북" \
            --metadata author="Chrome Education Team" \
            --metadata date="$(date '+%Y년 %m월 %d일')"
        then
            echo "✅ PDF 생성 완료: $PDF_FILENAME"
        else
            echo "⚠️  PDF 생성 실패, 계속 진행합니다..."
        fi
    fi
fi

# 4. PPTX 프레젠테이션 생성
echo "📊 PowerPoint 프레젠테이션 생성 중..."
if command -v python3 &> /dev/null; then
    python3 "$PROJECT_DIR/scripts/generate_pptx.py"
    if [[ $? -eq 0 ]]; then
        echo "✅ PowerPoint 프레젠테이션 생성 완료"
    else
        echo "⚠️  PowerPoint 생성 중 오류 발생"
    fi
else
    echo "⚠️  Python3를 찾을 수 없습니다. PPTX 생성을 건너뜁니다."
fi

# 5. 슬라이드 파일들을 순서대로 output 디렉토리로 복사
echo "📋 슬라이드 파일 복사 중..."
for i in "${!SLIDE_FILES[@]}"; do
    src="$SLIDES_DIR/${SLIDE_FILES[$i]}"
    dst="$OUTPUT_DIR/$(printf "%02d" $((i+1)))_${SLIDE_FILES[$i]}"
    if [[ -f "$src" ]]; then
        cp "$src" "$dst"
        echo "  ✅ $(printf "%02d" $((i+1)))_${SLIDE_FILES[$i]} 복사 완료"
    else
        echo "  ❌ 소스 파일을 찾을 수 없습니다: $src"
    fi
done

# 이미지 폴더 복사
if [[ -d "$SLIDES_DIR/images" ]]; then
    echo "🖼️  이미지 폴더 복사 중..."
    rm -rf "$OUTPUT_DIR/images"  # 기존 이미지 폴더 제거
    cp -r "$SLIDES_DIR/images" "$OUTPUT_DIR/"
    echo "  ✅ 이미지 폴더 복사 완료"
else
    echo "⚠️  이미지 폴더를 찾을 수 없습니다: $SLIDES_DIR/images"
fi

# 문서 파일 복사
if [[ -d "$DOCS_DIR" ]]; then
    echo "📄 문서 파일 복사 중..."
    for doc in "$DOCS_DIR"/*.md; do
        if [[ -f "$doc" ]]; then
            cp "$doc" "$OUTPUT_DIR/"
            echo "  ✅ $(basename "$doc") 복사 완료"
        fi
    done
else
    echo "⚠️  문서 디렉토리를 찾을 수 없습니다: $DOCS_DIR"
fi

# 6. 슬라이드 인덱스 및 빌드 정보 생성
echo "ℹ️  슬라이드 인덱스 및 빌드 정보 생성 중..."
if command -v python3 &> /dev/null; then
    python3 "$PROJECT_DIR/scripts/generate_slides.py"
    if [[ $? -eq 0 ]]; then
        echo "✅ 슬라이드 인덱스 및 빌드 정보 생성 완료"
    else
        echo "⚠️  슬라이드 인덱스 생성 중 오류 발생"
    fi
else
    echo "⚠️  Python3를 찾을 수 없습니다. 슬라이드 인덱스 생성을 건너뜁니다."
fi

echo "🎉 교육 자료 생성 완료!"
echo "📂 결과물 위치: $OUTPUT_DIR"
echo "🌐 슬라이드 인덱스: $OUTPUT_DIR/slides_index.html"

# 7. 생성된 파일 목록 출력
echo ""
echo "📋 생성된 파일 목록:"
ls -la "$OUTPUT_DIR"
