#!/usr/bin/env python3
"""
PowerPoint 프레젠테이션 생성 스크립트
"""

import os
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

def create_powerpoint():
    """PowerPoint 프레젠테이션 생성"""
    
    # 슬라이드 구성 정보
    slides_config = [
        {
            'title': '수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로',
            'subtitle': '디지털 도구 완전정복\n한글학교 선생님을 위한 크롬 웹브라우저 활용 교육'
        },
        {
            'title': '강의 개요',
            'content': [
                '교육 목표 및 대상',
                '기초-중급-고급 단계별 구성',
                '실습 중심의 학습 방법',
                '지속적인 학습을 위한 커뮤니티'
            ]
        },
        {
            'title': '기초 단계: 크롬 브라우저 기본 기능',
            'content': [
                '프로필 관리',
                '북마크 활용',
                '단축키 활용',
                '기본 설정 최적화'
            ]
        },
        {
            'title': '중급 단계: 교육자를 위한 확장프로그램',
            'content': [
                'Fireshot - 웹페이지 캡처',
                'Google Keep - 메모 및 스크랩',
                'Video Speed Controller - 동영상 속도 조절',
                'Mote - 음성 피드백'
            ]
        },
        {
            'title': '중급 단계: 한글교육 특화 웹도구',
            'content': [
                '스터디코리안넷',
                '한국어교수학습샘터',
                'NAKS 온라인 자료실',
                '한글또박또박'
            ]
        },
        {
            'title': '고급 단계: 구글 워크스페이스 연동',
            'content': [
                '구글 클래스룸',
                '구글 문서/슬라이드',
                '구글 드라이브',
                '구글 미트'
            ]
        },
        {
            'title': '고급 단계: AI 도구 활용',
            'content': [
                'Brisk Teaching - AI 교사 어시스턴트',
                'ChatGPT - 교육 자료 생성',
                'Canva AI - 시각적 자료 제작',
                '음성 인식/합성 도구'
            ]
        },
        {
            'title': '실습 시나리오',
            'content': [
                '새 학기 준비 (기초)',
                '효율적인 수업 자료 준비 (중급)',
                '온라인 수업 진행 (중급)',
                '학급 관리 시스템 구축 (고급)'
            ]
        },
        {
            'title': '추가 자료 및 참고 링크',
            'content': [
                '크롬 브라우저 공식 자료',
                '한글교육 자료',
                '디지털 교육 도구',
                '교사 커뮤니티'
            ]
        },
        {
            'title': '질문 및 연락처',
            'content': [
                '이메일: support@koreanedu.org',
                '전화: 02-123-4567',
                '웹사이트: www.koreanedu.org'
            ]
        }
    ]
    
    # 새 프레젠테이션 생성
    prs = Presentation()
    
    # 크롬 색상 정의
    chrome_blue = RGBColor(66, 133, 244)
    chrome_red = RGBColor(234, 67, 53)
    chrome_yellow = RGBColor(251, 188, 5)
    chrome_green = RGBColor(52, 168, 83)
    
    for i, slide_data in enumerate(slides_config):
        # 슬라이드 레이아웃 선택
        if i == 0:  # 타이틀 슬라이드
            slide_layout = prs.slide_layouts[0]  # Title Slide
        else:
            slide_layout = prs.slide_layouts[1]  # Title and Content
        
        slide = prs.slides.add_slide(slide_layout)
        
        # 제목 설정
        title = slide.shapes.title
        title.text = slide_data['title']
        title.text_frame.paragraphs[0].font.size = Pt(32)
        title.text_frame.paragraphs[0].font.color.rgb = chrome_blue
        
        if i == 0:  # 타이틀 슬라이드
            if len(slide.placeholders) > 1 and slide.placeholders[1]:  # 부제목
                subtitle = slide.placeholders[1]
                subtitle.text = slide_data['subtitle']
                subtitle.text_frame.paragraphs[0].font.size = Pt(20)
        else:  # 내용 슬라이드
            if 'content' in slide_data and len(slide.placeholders) > 1 and slide.placeholders[1]:
                content = slide.placeholders[1]
                content.text = '\n'.join([f'• {item}' for item in slide_data['content']])
                
                # 글꼴 크기 조정
                for paragraph in content.text_frame.paragraphs:
                    paragraph.font.size = Pt(18)
                    paragraph.space_after = Pt(12)
    
    return prs

def main():
    """메인 함수"""
    print('PowerPoint 프레젠테이션 생성 중...')
    
    # 출력 디렉토리 확인
    os.makedirs('output', exist_ok=True)
    
    try:
        # PowerPoint 생성
        prs = create_powerpoint()
        
        # 파일 저장
        output_path = 'output/chrome_education_slides.pptx'
        prs.save(output_path)
        
        print(f'✅ PowerPoint 파일 생성 완료: {output_path}')
        
    except Exception as e:
        print(f'❌ PowerPoint 생성 실패: {e}')
        return False
    
    return True

if __name__ == '__main__':
    main()

