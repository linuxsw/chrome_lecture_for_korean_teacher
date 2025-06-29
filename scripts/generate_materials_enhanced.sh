#!/bin/bash

# Enhanced Chrome Education Materials Generator
# 향상된 크롬 교육 자료 생성 스크립트

set -e  # 오류 발생 시 스크립트 중단

echo "🚀 Enhanced Chrome Education Materials Generator 시작"
echo "📅 $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 프로젝트 디렉토리 설정
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$PROJECT_DIR/output"
DOCS_DIR="$PROJECT_DIR/docs"

echo "📁 프로젝트 디렉토리: $PROJECT_DIR"
echo "📂 출력 디렉토리: $OUTPUT_DIR"
echo ""

# 출력 디렉토리 생성
mkdir -p "$OUTPUT_DIR"
mkdir -p "$DOCS_DIR"

# 1. 향상된 HTML 슬라이드 생성
echo "🌐 향상된 HTML 슬라이드 생성 중..."
cd "$PROJECT_DIR"
python3 scripts/generate_slides_enhanced.py
echo ""

# 2. 고급 PowerPoint 프레젠테이션 생성
echo "📊 고급 PowerPoint 프레젠테이션 생성 중..."
python3 scripts/generate_pptx_advanced.py
echo ""

# 3. PDF 워크북 생성 (한글 폰트 지원)
echo "📚 PDF 워크북 생성 중..."
if [ -f "$DOCS_DIR/chrome_edu_workbook.md" ]; then
    echo "  📝 Markdown 워크북 파일 발견"
    
    # WeasyPrint 우선 사용 (한글 지원 우수)
    if command -v weasyprint >/dev/null 2>&1; then
        echo "  🔧 WeasyPrint로 PDF 생성 중..."
        weasyprint "$DOCS_DIR/chrome_edu_workbook.md" "$OUTPUT_DIR/chrome_edu_workbook.pdf" \
            --stylesheet <(echo "
                body { 
                    font-family: 'Noto Sans KR', 'Noto Sans CJK KR', sans-serif; 
                    line-height: 1.6; 
                    margin: 2cm; 
                    font-size: 12pt; 
                }
                h1, h2, h3 { 
                    color: #4285F4; 
                    font-weight: bold; 
                }
                h1 { font-size: 24pt; margin-bottom: 1em; }
                h2 { font-size: 18pt; margin-bottom: 0.8em; }
                h3 { font-size: 14pt; margin-bottom: 0.6em; }
                p { margin-bottom: 0.5em; }
                ul, ol { margin-bottom: 1em; }
                li { margin-bottom: 0.3em; }
                code { 
                    background-color: #f5f5f5; 
                    padding: 2px 4px; 
                    border-radius: 3px; 
                    font-family: 'Courier New', monospace; 
                }
                blockquote { 
                    border-left: 4px solid #4285F4; 
                    padding-left: 1em; 
                    margin: 1em 0; 
                    font-style: italic; 
                }
            ") 2>/dev/null || echo "  ⚠️ WeasyPrint 실패, Pandoc으로 시도..."
    fi
    
    # WeasyPrint 실패 시 Pandoc 사용
    if [ ! -f "$OUTPUT_DIR/chrome_edu_workbook.pdf" ] && command -v pandoc >/dev/null 2>&1; then
        echo "  🔧 Pandoc으로 PDF 생성 중..."
        pandoc "$DOCS_DIR/chrome_edu_workbook.md" -o "$OUTPUT_DIR/chrome_edu_workbook.pdf" \
            --pdf-engine=wkhtmltopdf \
            -V margin-top=20mm \
            -V margin-bottom=20mm \
            -V margin-left=15mm \
            -V margin-right=15mm \
            -V mainfont="Noto Sans KR" \
            --variable fontsize=12pt \
            --variable linestretch=1.6 2>/dev/null || echo "  ⚠️ Pandoc도 실패"
    fi
    
    if [ -f "$OUTPUT_DIR/chrome_edu_workbook.pdf" ]; then
        echo "  ✅ PDF 워크북 생성 완료"
    else
        echo "  ❌ PDF 워크북 생성 실패"
    fi
else
    echo "  ⚠️ 워크북 Markdown 파일을 찾을 수 없습니다: $DOCS_DIR/chrome_edu_workbook.md"
fi
echo ""

# 4. 파일 크기 및 정보 출력
echo "📊 생성된 파일 정보:"
echo "----------------------------------------"
if [ -f "$OUTPUT_DIR/index.html" ]; then
    size=$(stat -f%z "$OUTPUT_DIR/index.html" 2>/dev/null || stat -c%s "$OUTPUT_DIR/index.html" 2>/dev/null || echo "0")
    echo "🌐 HTML 인덱스: $(printf "%'d" $size) bytes"
fi

if [ -f "$OUTPUT_DIR/chrome_education_slides.pptx" ]; then
    size=$(stat -f%z "$OUTPUT_DIR/chrome_education_slides.pptx" 2>/dev/null || stat -c%s "$OUTPUT_DIR/chrome_education_slides.pptx" 2>/dev/null || echo "0")
    mb=$(echo "scale=1; $size / 1024 / 1024" | bc -l 2>/dev/null || echo "0")
    echo "📊 PowerPoint: $(printf "%'d" $size) bytes (${mb} MB)"
fi

if [ -f "$OUTPUT_DIR/chrome_edu_workbook.pdf" ]; then
    size=$(stat -f%z "$OUTPUT_DIR/chrome_edu_workbook.pdf" 2>/dev/null || stat -c%s "$OUTPUT_DIR/chrome_edu_workbook.pdf" 2>/dev/null || echo "0")
    kb=$(echo "scale=1; $size / 1024" | bc -l 2>/dev/null || echo "0")
    echo "📚 PDF 워크북: $(printf "%'d" $size) bytes (${kb} KB)"
fi

# HTML 슬라이드 파일들 개수
html_count=$(find "$OUTPUT_DIR" -name "*.html" -not -name "index.html" | wc -l)
echo "🎯 HTML 슬라이드: ${html_count}개 파일"

echo "----------------------------------------"
echo ""

# 5. 성공 메시지
echo "🎉 모든 교육 자료 생성 완료!"
echo "📂 결과물 위치: $OUTPUT_DIR"
echo "🌐 온라인 보기: index.html"
echo "📊 오프라인 프레젠테이션: chrome_education_slides.pptx"
echo "📚 실습 가이드: chrome_edu_workbook.pdf"
echo ""
echo "💡 사용법:"
echo "  - 온라인 프레젠테이션: 웹브라우저에서 index.html 열기"
echo "  - 오프라인 프레젠테이션: PowerPoint에서 .pptx 파일 열기"
echo "  - 실습 가이드: PDF 뷰어에서 워크북 열기"
echo ""
echo "✨ 한글교육의 디지털 혁신을 응원합니다!"

