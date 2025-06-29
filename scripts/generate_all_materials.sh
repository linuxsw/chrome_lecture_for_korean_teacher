#!/bin/bash

# 통합 교육 자료 생성 스크립트
# 3가지 다른 방법으로 PDF, HTML, PPTX 생성

set -e  # 오류 발생 시 스크립트 중단

echo "🚀 통합 교육 자료 생성 시스템 시작"
TIMESTAMP="$(date '+%Y%m%d_%H%M')"
echo "📅 $TIMESTAMP"
echo ""

# 프로젝트 디렉토리 설정
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$PROJECT_DIR/output"

echo "📁 프로젝트 디렉토리: $PROJECT_DIR"
echo "📂 출력 디렉토리: $OUTPUT_DIR"
echo ""

# 출력 디렉토리 생성
mkdir -p "$OUTPUT_DIR"
export TIMESTAMP

# 1. PDF 워크북 생성 (강화된 한글 폰트 지원)
echo "📚 PDF 워크북 생성 중 (Commit 4a9b4e9 방법)..."
cd "$PROJECT_DIR"
python3 scripts/generate_pdf.py
echo ""

# 2. HTML Pages 생성 (Commit 3bbe342 + 타임스탬프)
echo "🌐 HTML Pages 생성 중 (Commit 3bbe342 + 타임스탬프)..."
python3 scripts/generate_html_pages.py
echo ""

# 3. PPTX 프레젠테이션 생성 (Aspose 스타일 + Commit 3bbe342 이미지)
echo "📊 PPTX 프레젠테이션 생성 중 (Aspose 스타일)..."
python3 scripts/generate_pptx_aspose.py
echo ""

# 4. 생성 결과 검증
echo "🔍 생성 결과 검증 중..."
echo "----------------------------------------"

# 필수 파일들 확인
PPTX_FILE="output/chrome_education_slides_${TIMESTAMP}.pptx"
PDF_FILE="output/chrome_edu_workbook_${TIMESTAMP}.pdf"
REQUIRED_FILES=(
    "output/index.html"
    "$PPTX_FILE"
    "$PDF_FILE"
)

OPTIONAL_FILES=(
    "output/build_info.json"
)

ALL_GOOD=true

echo "📋 필수 파일 검증:"
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
        if [ "$size" -gt 0 ]; then
            echo "  ✅ $(basename $file): $(printf "%'d" $size) bytes"
        else
            echo "  ❌ $(basename $file): 파일이 비어있음"
            ALL_GOOD=false
        fi
    else
        echo "  ❌ $(basename $file): 파일 없음"
        ALL_GOOD=false
    fi
done

echo ""
echo "📋 선택적 파일 검증:"
for file in "${OPTIONAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
        echo "  ✅ $(basename $file): $(printf "%'d" $size) bytes"
    else
        echo "  ⚠️ $(basename $file): 파일 없음 (선택적)"
    fi
done

echo ""

# HTML 슬라이드 파일들 개수 확인
html_count=$(find "$OUTPUT_DIR" -name "*.html" -not -name "index.html" | wc -l)
echo "📄 HTML 슬라이드: ${html_count}개 파일"

# 이미지 파일들 확인
if [ -d "$OUTPUT_DIR/images" ]; then
    image_count=$(find "$OUTPUT_DIR/images" -type f | wc -l)
    echo "🖼️ 이미지 파일: ${image_count}개 파일"
fi

echo "----------------------------------------"

# 5. 상세 파일 정보 출력
echo "📊 상세 파일 정보:"
echo "----------------------------------------"

if [ -f "$OUTPUT_DIR/index.html" ]; then
    size=$(stat -c%s "$OUTPUT_DIR/index.html" 2>/dev/null || stat -f%z "$OUTPUT_DIR/index.html" 2>/dev/null || echo "0")
    kb=$(echo "scale=1; $size / 1024" | bc -l 2>/dev/null || echo "0")
    echo "🌐 HTML 인덱스: $(printf "%'d" $size) bytes (${kb} KB)"
    echo "   - Commit 3bbe342 기반 원본 슬라이드 복원"
    echo "   - 실시간 타임스탬프 표시"
    echo "   - 반응형 디자인"
fi

if [ -f "$PPTX_FILE" ]; then
    size=$(stat -c%s "$PPTX_FILE" 2>/dev/null || stat -f%z "$PPTX_FILE" 2>/dev/null || echo "0")
    mb=$(echo "scale=1; $size / 1024 / 1024" | bc -l 2>/dev/null || echo "0")
    echo "📊 PowerPoint: $(printf "%'d" $size) bytes (${mb} MB)"
    echo "   - Aspose 스타일 고급 기능"
    echo "   - Commit 3bbe342 이미지 사용"
    echo "   - 한글 폰트 지원"
fi

if [ -f "$PDF_FILE" ]; then
    size=$(stat -c%s "$PDF_FILE" 2>/dev/null || stat -f%z "$PDF_FILE" 2>/dev/null || echo "0")
    kb=$(echo "scale=1; $size / 1024" | bc -l 2>/dev/null || echo "0")
    echo "📚 PDF 워크북: $(printf "%'d" $size) bytes (${kb} KB)"
    echo "   - Commit 4a9b4e9 방법 사용"
    echo "   - WeasyPrint 우선, Pandoc 폴백"
    echo "   - 한글 폰트 완전 지원"
fi

echo "----------------------------------------"

# 6. 최종 결과
if [ "$ALL_GOOD" = true ]; then
    echo "🎉 모든 교육 자료 생성 성공!"
    echo ""
    echo "📂 결과물 위치: $OUTPUT_DIR"
    echo "🌐 온라인 프레젠테이션: index.html"
    echo "📊 오프라인 프레젠테이션: $(basename "$PPTX_FILE")"
    echo "📚 실습 워크북: $(basename "$PDF_FILE")"
    echo ""
    echo "💡 각 형식별 특징:"
    echo "  • HTML: Commit 3bbe342 원본 + 타임스탬프"
    echo "  • PPTX: Aspose 스타일 + Commit 3bbe342 이미지"
    echo "  • PDF: Commit 4a9b4e9 방법 + 한글 지원"
    echo ""
    echo "✨ 한글교육의 디지털 혁신을 응원합니다!"
    
    exit 0
else
    echo "❌ 일부 필수 파일 생성 실패"
    echo "위의 오류를 확인하고 다시 시도해주세요."
    
    exit 1
fi

