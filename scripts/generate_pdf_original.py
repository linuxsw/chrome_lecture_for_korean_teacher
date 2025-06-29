#!/usr/bin/env python3
"""
PDF 생성 스크립트 (Commit 4a9b4e9 방법 복원)
WeasyPrint를 우선 사용하고, 실패 시 Pandoc으로 폴백
한글 폰트 지원 강화
"""

import os
import subprocess
import sys
from pathlib import Path

def generate_pdf_with_weasyprint():
    """WeasyPrint를 사용한 PDF 생성"""
    try:
        import weasyprint
        import markdown
        
        print("📚 WeasyPrint를 사용한 PDF 생성 중...")
        
        # CSS 스타일 정의 (한글 폰트 포함)
        css_style = '''
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
        body {
            font-family: 'Noto Sans KR', 'Noto Sans CJK KR', 'Malgun Gothic', sans-serif;
            line-height: 1.6;
            margin: 2cm;
            font-size: 12pt;
            color: #333;
        }
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #2c3e50;
        }
        h1 { 
            font-size: 24pt; 
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.3em;
        }
        h2 { 
            font-size: 20pt; 
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 0.2em;
        }
        h3 { 
            font-size: 16pt; 
            color: #e67e22;
        }
        p {
            margin-bottom: 1em;
            text-align: justify;
        }
        ul, ol {
            margin-bottom: 1em;
            padding-left: 2em;
        }
        li {
            margin-bottom: 0.5em;
        }
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 11pt;
        }
        pre {
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
        }
        blockquote {
            border-left: 4px solid #3498db;
            padding-left: 1em;
            margin: 1em 0;
            font-style: italic;
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 0 5px 5px 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #3498db;
            color: white;
            font-weight: 700;
        }
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
        
        html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 워크북</title>
    <style>{css_style}</style>
</head>
<body>
{markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'toc'])}
</body>
</html>'''
        
        # 출력 디렉토리 생성
        os.makedirs('output', exist_ok=True)
        
        # WeasyPrint로 PDF 생성
        document = weasyprint.HTML(string=html_content)
        document.write_pdf('output/chrome_edu_workbook.pdf')
        
        print("  ✅ WeasyPrint PDF 생성 완료")
        return True
        
    except ImportError:
        print("  ⚠️ WeasyPrint 모듈을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"  ❌ WeasyPrint PDF 생성 실패: {e}")
        return False

def generate_pdf_with_pandoc():
    """Pandoc을 사용한 PDF 생성 (폴백)"""
    try:
        print("📚 Pandoc을 사용한 PDF 생성 중...")
        
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
        
        # Pandoc 명령어 구성
        pandoc_cmd = [
            'pandoc',
            workbook_file,
            '-o', 'output/chrome_edu_workbook.pdf',
            '--pdf-engine=wkhtmltopdf',
            '--variable', 'mainfont=Noto Sans KR',
            '--variable', 'fontsize=12pt',
            '--variable', 'linestretch=1.6',
            '--variable', 'margin-top=20mm',
            '--variable', 'margin-bottom=20mm',
            '--variable', 'margin-left=15mm',
            '--variable', 'margin-right=15mm',
            '--variable', 'papersize=a4',
            '--table-of-contents',
            '--toc-depth=3'
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
    print("🚀 PDF 워크북 생성 시작 (Commit 4a9b4e9 방법)")
    
    # WeasyPrint 우선 시도
    if generate_pdf_with_weasyprint():
        print("✅ WeasyPrint로 PDF 생성 성공")
    elif generate_pdf_with_pandoc():
        print("✅ Pandoc으로 PDF 생성 성공")
    else:
        print("❌ 모든 PDF 생성 방법 실패")
        sys.exit(1)
    
    # 파일 크기 확인
    pdf_file = 'output/chrome_edu_workbook.pdf'
    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        print(f"📊 생성된 PDF 크기: {size:,} bytes ({size/1024:.1f} KB)")
    
    print("🎉 PDF 워크북 생성 완료!")

if __name__ == "__main__":
    main()

