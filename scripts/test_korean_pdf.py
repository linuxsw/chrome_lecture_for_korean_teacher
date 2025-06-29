#!/usr/bin/env python3
"""
한글 PDF 테스트 스크립트
다양한 방법으로 한글 표시 테스트
"""

import os
from pathlib import Path

def test_weasyprint_korean():
    """WeasyPrint 한글 테스트"""
    try:
        import weasyprint
        
        print("🧪 WeasyPrint 한글 테스트 중...")
        
        # 테스트 HTML 내용
        test_html = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <style>
        @font-face {
            font-family: 'NotoSansCJKKR';
            src: url('file:///usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc') format('truetype-collection');
            font-weight: normal;
            font-style: normal;
        }
        
        body {
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', sans-serif;
            font-size: 14pt;
            line-height: 1.8;
            margin: 2cm;
        }
        
        h1 {
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', sans-serif;
            color: #2c3e50;
            font-size: 20pt;
            font-weight: bold;
        }
        
        p {
            font-family: 'NotoSansCJKKR', 'Noto Sans CJK KR', 'Noto Sans KR', sans-serif;
            margin-bottom: 1em;
        }
    </style>
</head>
<body>
    <h1>한글 폰트 테스트</h1>
    <p>안녕하세요! 이것은 한글 폰트 테스트입니다.</p>
    <p>크롬 웹브라우저를 활용한 교육 자료입니다.</p>
    <p>한글학교 선생님들을 위한 디지털 도구 완전정복</p>
    <p>가나다라마바사아자차카타파하</p>
    <p>ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ</p>
    <p>ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ</p>
    <p>수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로</p>
</body>
</html>'''
        
        # 출력 디렉토리 생성
        os.makedirs('output', exist_ok=True)
        
        # WeasyPrint로 PDF 생성
        document = weasyprint.HTML(string=test_html)
        document.write_pdf('output/korean_test_weasyprint.pdf')
        
        # 파일 크기 확인
        size = os.path.getsize('output/korean_test_weasyprint.pdf')
        print(f"  ✅ WeasyPrint 테스트 PDF 생성: {size:,} bytes")
        
        return True
        
    except Exception as e:
        print(f"  ❌ WeasyPrint 테스트 실패: {e}")
        return False

def test_reportlab_korean():
    """ReportLab 한글 테스트"""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        
        print("🧪 ReportLab 한글 테스트 중...")
        
        # 한글 폰트 등록 시도
        font_paths = [
            "/usr/share/fonts/truetype/noto/NotoSansKR-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ]
        
        font_registered = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    pdfmetrics.registerFont(TTFont('TestKoreanFont', font_path))
                    font_registered = True
                    print(f"  ✅ 폰트 등록 성공: {font_path}")
                    break
                except Exception as e:
                    print(f"  ⚠️ 폰트 등록 실패 ({font_path}): {e}")
        
        # 출력 디렉토리 생성
        os.makedirs('output', exist_ok=True)
        
        # PDF 문서 생성
        doc = SimpleDocTemplate(
            'output/korean_test_reportlab.pdf',
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # 스타일 설정
        styles = getSampleStyleSheet()
        
        korean_style = ParagraphStyle(
            'Korean',
            parent=styles['Normal'],
            fontName='TestKoreanFont' if font_registered else 'Helvetica',
            fontSize=12,
            leading=18,
            spaceAfter=12
        )
        
        title_style = ParagraphStyle(
            'KoreanTitle',
            parent=styles['Title'],
            fontName='TestKoreanFont' if font_registered else 'Helvetica-Bold',
            fontSize=16,
            leading=20,
            spaceAfter=20,
            alignment=1
        )
        
        # 내용 구성
        story = []
        story.append(Paragraph("한글 폰트 테스트", title_style))
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("안녕하세요! 이것은 한글 폰트 테스트입니다.", korean_style))
        story.append(Paragraph("크롬 웹브라우저를 활용한 교육 자료입니다.", korean_style))
        story.append(Paragraph("한글학교 선생님들을 위한 디지털 도구 완전정복", korean_style))
        story.append(Paragraph("가나다라마바사아자차카타파하", korean_style))
        story.append(Paragraph("ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ", korean_style))
        story.append(Paragraph("ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ", korean_style))
        story.append(Paragraph("수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로", korean_style))
        
        # PDF 빌드
        doc.build(story)
        
        # 파일 크기 확인
        size = os.path.getsize('output/korean_test_reportlab.pdf')
        print(f"  ✅ ReportLab 테스트 PDF 생성: {size:,} bytes")
        
        return True
        
    except Exception as e:
        print(f"  ❌ ReportLab 테스트 실패: {e}")
        return False

def main():
    """메인 함수"""
    print("🚀 한글 PDF 테스트 시작")
    print("=" * 50)
    
    # WeasyPrint 테스트
    weasyprint_success = test_weasyprint_korean()
    
    # ReportLab 테스트
    reportlab_success = test_reportlab_korean()
    
    print("=" * 50)
    print("📊 테스트 결과:")
    print(f"  WeasyPrint: {'✅ 성공' if weasyprint_success else '❌ 실패'}")
    print(f"  ReportLab: {'✅ 성공' if reportlab_success else '❌ 실패'}")
    
    if weasyprint_success or reportlab_success:
        print("\n📁 생성된 테스트 파일:")
        if weasyprint_success:
            print("  - output/korean_test_weasyprint.pdf")
        if reportlab_success:
            print("  - output/korean_test_reportlab.pdf")
        
        print("\n📝 테스트 파일을 열어서 한글이 정상적으로 표시되는지 확인해주세요.")
    
    print("🎉 한글 PDF 테스트 완료!")

if __name__ == "__main__":
    main()

