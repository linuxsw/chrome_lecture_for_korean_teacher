#!/usr/bin/env python3
"""
PDF 생성 스크립트
WeasyPrint를 우선 사용하고, 실패 시 Pandoc으로 폴백
"""

import os
import subprocess
import sys
from datetime import datetime

OUTPUT_FILE = "output/chrome_edu_workbook.pdf"

def generate_pdf_with_weasyprint():
    """WeasyPrint를 사용한 PDF 생성"""
    try:
        import weasyprint
        import markdown
        
        print("Using WeasyPrint for PDF generation...")
        
        # CSS 스타일 정의 (한글 폰트 포함)
        css_style = '''
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
        body {
            font-family: 'Noto Sans KR', 'Noto Sans CJK KR', sans-serif;
            line-height: 1.6;
            margin: 2cm;
            font-size: 12pt;
        }
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }
        h1 { font-size: 24pt; }
        h2 { font-size: 20pt; }
        h3 { font-size: 16pt; }
        '''
        
        # Markdown을 HTML로 변환
        with open('docs/chrome_edu_workbook.md', 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = f'''
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <style>{css_style}</style>
        </head>
        <body>
        {markdown.markdown(md_content)}
        </body>
        </html>
        '''
        
        # PDF 생성
        weasyprint.HTML(string=html_content).write_pdf(OUTPUT_FILE)
        print('✅ PDF generated successfully with WeasyPrint')
        return True
        
    except ImportError:
        print("WeasyPrint not available")
        return False
    except Exception as e:
        print(f"WeasyPrint failed: {e}")
        return False

def generate_pdf_with_pandoc():
    """Pandoc을 사용한 PDF 생성"""
    try:
        print("Using Pandoc for PDF generation...")
        
        cmd = [
            'pandoc', 'docs/chrome_edu_workbook.md',
            '-o', OUTPUT_FILE,
            '--pdf-engine=wkhtmltopdf',
            '-V', 'margin-top=20mm',
            '-V', 'margin-bottom=20mm',
            '-V', 'margin-left=15mm',
            '-V', 'margin-right=15mm',
            '-V', 'mainfont=Noto Sans CJK KR'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print('✅ PDF generated successfully with Pandoc')
            return True
        else:
            print(f"Pandoc failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Pandoc failed: {e}")
        return False

def main():
    """메인 함수"""
    if not os.path.exists('docs/chrome_edu_workbook.md'):
        print("Workbook markdown file not found")
        return
    
    # 출력 디렉토리 확인 및 파일명 설정
    os.makedirs('output', exist_ok=True)
    timestamp = os.getenv('TIMESTAMP') or datetime.now().strftime('%Y%m%d_%H%M')
    global OUTPUT_FILE
    OUTPUT_FILE = f'output/chrome_edu_workbook_{timestamp}.pdf'
    
    # WeasyPrint 우선 시도
    if generate_pdf_with_weasyprint():
        return
    
    # Pandoc으로 폴백
    if generate_pdf_with_pandoc():
        return
    
    print("❌ All PDF generation methods failed")
    sys.exit(1)

if __name__ == '__main__':
    main()

