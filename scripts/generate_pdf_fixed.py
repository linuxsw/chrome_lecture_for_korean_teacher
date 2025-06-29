#!/usr/bin/env python3
"""
PDF 생성 스크립트 (한글 폰트 문제 완전 해결)
시스템 폰트 경로 직접 지정 및 강화된 CSS 설정
"""

import os
import subprocess
import sys
from pathlib import Path

def generate_pdf_with_weasyprint_fixed():
    """WeasyPrint를 사용한 PDF 생성 (한글 폰트 강화)"""
    try:
        import weasyprint
        import markdown
        
        print("📚 WeasyPrint를 사용한 PDF 생성 중 (한글 폰트 강화)...")
        
        # 시스템 폰트 경로 확인
        font_paths = [
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
            "/usr/share/fonts/truetype/noto/NotoSansKR-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ]
        
        available_fonts = []
        for font_path in font_paths:
            if os.path.exists(font_path):
                available_fonts.append(font_path)
                print(f"  ✅ 폰트 발견: {font_path}")
        
        if not available_fonts:
            print("  ⚠️ 시스템 폰트를 찾을 수 없습니다.")
            return False
        
        # 강화된 CSS 스타일 정의 (시스템 폰트 경로 직접 지정)
        css_style = f'''
        @font-face {{
            font-family: 'NotoSansCJKKR';
            src: url('file:///usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc') format('truetype-collection');
            font-weight: normal;
            font-style: normal;
        }}
        
        @font-face {{
            font-family: 'NotoSansCJKKR';
            src: url('file:///usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc') format('truetype-collection');
            font-weight: bold;
            font-style: normal;
        }}
        
        * {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
        }}
        
        body {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            line-height: 1.8;
            margin: 2.5cm;
            font-size: 11pt;
            color: #333;
            word-break: keep-all;
            word-wrap: break-word;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            font-weight: bold !important;
            margin-top: 2em;
            margin-bottom: 0.8em;
            color: #2c3e50;
            word-break: keep-all;
        }}
        
        h1 {{ 
            font-size: 22pt !important; 
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.5em;
            page-break-before: auto;
        }}
        
        h2 {{ 
            font-size: 18pt !important; 
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 0.3em;
        }}
        
        h3 {{ 
            font-size: 14pt !important; 
            color: #e67e22;
        }}
        
        p {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            margin-bottom: 1.2em;
            text-align: justify;
            line-height: 1.8;
            word-break: keep-all;
        }}
        
        ul, ol {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            margin-bottom: 1.5em;
            padding-left: 2.5em;
        }}
        
        li {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            margin-bottom: 0.8em;
            line-height: 1.8;
            word-break: keep-all;
        }}
        
        code {{
            font-family: 'Courier New', 'DejaVu Sans Mono', monospace !important;
            background-color: #f8f9fa;
            padding: 3px 6px;
            border-radius: 4px;
            font-size: 10pt;
            border: 1px solid #e9ecef;
        }}
        
        pre {{
            font-family: 'Courier New', 'DejaVu Sans Mono', monospace !important;
            background-color: #f8f9fa;
            padding: 1.5em;
            border-radius: 6px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
            margin: 1.5em 0;
        }}
        
        blockquote {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            border-left: 4px solid #3498db;
            padding-left: 1.5em;
            margin: 1.5em 0;
            font-style: italic;
            background-color: #f8f9fa;
            padding: 1.5em;
            border-radius: 0 6px 6px 0;
            word-break: keep-all;
        }}
        
        table {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            border-collapse: collapse;
            width: 100%;
            margin: 1.5em 0;
        }}
        
        th, td {{
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif !important;
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
            word-break: keep-all;
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}
        
        @page {{
            margin: 2.5cm;
            @bottom-center {{
                content: counter(page);
                font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', sans-serif;
            }}
        }}
        '''
        
        # 워크북 파일 확인
        workbook_paths = [
            'docs/chrome_edu_workbook.md',
            'chrome_edu_workbook.md',
            '../chrome_edu_workbook.md'
        ]
        
        workbook_file = None
        for path in workbook_paths:
            if os.path.exists(path):
                workbook_file = path
                break
        
        if not workbook_file:
            print("  ⚠️ 워크북 Markdown 파일을 찾을 수 없습니다.")
            return False
        
        print(f"  📖 워크북 파일 발견: {workbook_file}")
        
        # Markdown을 HTML로 변환
        with open(workbook_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Markdown 확장 기능 사용
        html_body = markdown.markdown(
            md_content, 
            extensions=['tables', 'fenced_code', 'toc', 'codehilite'],
            extension_configs={
                'toc': {'title': '목차'},
                'codehilite': {'use_pygments': False}
            }
        )
        
        html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 워크북</title>
    <style>{css_style}</style>
</head>
<body>
    <div style="text-align: center; margin-bottom: 3em; padding: 2em; border-bottom: 2px solid #3498db;">
        <h1 style="font-size: 28pt; margin-bottom: 0.5em; border: none;">한글학교 선생님을 위한</h1>
        <h1 style="font-size: 24pt; margin-bottom: 0.5em; border: none; color: #3498db;">크롬 웹브라우저 활용 교육 워크북</h1>
        <p style="font-size: 14pt; color: #666; margin-top: 1em;">수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로</p>
        <p style="font-size: 12pt; color: #888;">— 디지털 도구 완전정복 —</p>
    </div>
{html_body}
</body>
</html>'''
        
        # 출력 디렉토리 생성
        os.makedirs('output', exist_ok=True)
        
        # WeasyPrint로 PDF 생성 (폰트 설정 강화)
        print("  🔧 WeasyPrint 설정 중...")
        
        # HTML 문서 생성
        document = weasyprint.HTML(string=html_content, base_url='.')
        
        # CSS 문서 생성
        css_document = weasyprint.CSS(string=css_style)
        
        # PDF 생성
        document.write_pdf('output/chrome_edu_workbook.pdf', stylesheets=[css_document])
        
        print("  ✅ WeasyPrint PDF 생성 완료")
        return True
        
    except ImportError:
        print("  ⚠️ WeasyPrint 모듈을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"  ❌ WeasyPrint PDF 생성 실패: {e}")
        return False

def generate_pdf_with_reportlab():
    """ReportLab을 사용한 PDF 생성 (대안)"""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        import markdown
        
        print("📚 ReportLab을 사용한 PDF 생성 중...")
        
        # 한글 폰트 등록
        font_paths = [
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/truetype/noto/NotoSansKR-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ]
        
        font_registered = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    if font_path.endswith('.ttc'):
                        # TTC 파일은 건너뛰기 (ReportLab에서 지원 제한)
                        continue
                    pdfmetrics.registerFont(TTFont('NotoSansKR', font_path))
                    font_registered = True
                    print(f"  ✅ 폰트 등록: {font_path}")
                    break
                except Exception as e:
                    print(f"  ⚠️ 폰트 등록 실패 ({font_path}): {e}")
        
        if not font_registered:
            print("  ⚠️ 한글 폰트 등록 실패, 기본 폰트 사용")
        
        # 워크북 파일 확인
        workbook_paths = [
            'docs/chrome_edu_workbook.md',
            'chrome_edu_workbook.md',
            '../chrome_edu_workbook.md'
        ]
        
        workbook_file = None
        for path in workbook_paths:
            if os.path.exists(path):
                workbook_file = path
                break
        
        if not workbook_file:
            print("  ⚠️ 워크북 Markdown 파일을 찾을 수 없습니다.")
            return False
        
        # Markdown 읽기
        with open(workbook_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 출력 디렉토리 생성
        os.makedirs('output', exist_ok=True)
        
        # PDF 문서 생성
        doc = SimpleDocTemplate(
            'output/chrome_edu_workbook.pdf',
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # 스타일 설정
        styles = getSampleStyleSheet()
        
        # 한글 스타일 정의
        korean_style = ParagraphStyle(
            'Korean',
            parent=styles['Normal'],
            fontName='NotoSansKR' if font_registered else 'Helvetica',
            fontSize=11,
            leading=16,
            spaceAfter=12,
            wordWrap='CJK'
        )
        
        title_style = ParagraphStyle(
            'KoreanTitle',
            parent=styles['Title'],
            fontName='NotoSansKR' if font_registered else 'Helvetica-Bold',
            fontSize=18,
            leading=22,
            spaceAfter=20,
            alignment=1  # 중앙 정렬
        )
        
        # 내용 구성
        story = []
        
        # 제목
        story.append(Paragraph("한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 워크북", title_style))
        story.append(Spacer(1, 0.5*inch))
        
        # Markdown을 간단한 텍스트로 변환 (ReportLab 호환)
        lines = md_content.split('\n')
        for line in lines:
            if line.strip():
                # 헤더 처리
                if line.startswith('#'):
                    level = len(line) - len(line.lstrip('#'))
                    text = line.lstrip('# ').strip()
                    if level == 1:
                        story.append(Paragraph(text, title_style))
                    else:
                        story.append(Paragraph(text, korean_style))
                else:
                    story.append(Paragraph(line, korean_style))
                story.append(Spacer(1, 6))
        
        # PDF 빌드
        doc.build(story)
        
        print("  ✅ ReportLab PDF 생성 완료")
        return True
        
    except ImportError:
        print("  ⚠️ ReportLab 모듈을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"  ❌ ReportLab PDF 생성 실패: {e}")
        return False

def generate_pdf_with_pandoc_enhanced():
    """Pandoc을 사용한 PDF 생성 (강화된 한글 설정)"""
    try:
        print("📚 Pandoc을 사용한 PDF 생성 중 (강화된 한글 설정)...")
        
        # 워크북 파일 확인
        workbook_paths = [
            'docs/chrome_edu_workbook.md',
            'chrome_edu_workbook.md',
            '../chrome_edu_workbook.md'
        ]
        
        workbook_file = None
        for path in workbook_paths:
            if os.path.exists(path):
                workbook_file = path
                break
        
        if not workbook_file:
            print("  ⚠️ 워크북 Markdown 파일을 찾을 수 없습니다.")
            return False
        
        print(f"  📖 워크북 파일 발견: {workbook_file}")
        
        # 출력 디렉토리 생성
        os.makedirs('output', exist_ok=True)
        
        # Pandoc 명령어 구성 (한글 설정 강화)
        pandoc_cmd = [
            'pandoc',
            workbook_file,
            '-o', 'output/chrome_edu_workbook.pdf',
            '--pdf-engine=wkhtmltopdf',
            '--variable', 'mainfont=Noto Sans CJK KR',
            '--variable', 'sansfont=Noto Sans CJK KR',
            '--variable', 'monofont=Courier New',
            '--variable', 'fontsize=11pt',
            '--variable', 'linestretch=1.6',
            '--variable', 'margin-top=25mm',
            '--variable', 'margin-bottom=25mm',
            '--variable', 'margin-left=20mm',
            '--variable', 'margin-right=20mm',
            '--variable', 'papersize=a4',
            '--variable', 'documentclass=article',
            '--variable', 'geometry=a4paper',
            '--table-of-contents',
            '--toc-depth=3',
            '--highlight-style=tango',
            '--standalone'
        ]
        
        # Pandoc 실행
        result = subprocess.run(pandoc_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("  ✅ Pandoc PDF 생성 완료")
            return True
        else:
            print(f"  ❌ Pandoc PDF 생성 실패: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("  ⚠️ Pandoc을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"  ❌ Pandoc PDF 생성 실패: {e}")
        return False

def main():
    """메인 함수"""
    print("🚀 PDF 워크북 생성 시작 (한글 폰트 문제 완전 해결)")
    
    success = False
    
    # 1. WeasyPrint 강화 버전 시도
    if generate_pdf_with_weasyprint_fixed():
        print("✅ WeasyPrint 강화 버전으로 PDF 생성 성공")
        success = True
    # 2. ReportLab 시도
    elif generate_pdf_with_reportlab():
        print("✅ ReportLab으로 PDF 생성 성공")
        success = True
    # 3. Pandoc 강화 버전 시도
    elif generate_pdf_with_pandoc_enhanced():
        print("✅ Pandoc 강화 버전으로 PDF 생성 성공")
        success = True
    else:
        print("❌ 모든 PDF 생성 방법 실패")
        sys.exit(1)
    
    # 파일 크기 확인
    pdf_file = 'output/chrome_edu_workbook.pdf'
    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        print(f"📊 생성된 PDF 크기: {size:,} bytes ({size/1024:.1f} KB)")
        
        # 한글 테스트를 위한 간단한 검증
        print("🔍 PDF 파일 생성 확인 완료")
        print("📝 한글 표시 확인을 위해 PDF 파일을 열어보세요.")
    
    print("🎉 PDF 워크북 생성 완료!")

if __name__ == "__main__":
    main()

