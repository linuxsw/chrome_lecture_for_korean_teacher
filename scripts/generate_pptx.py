#!/usr/bin/env python3
"""
PowerPoint 프레젠테이션 생성 스크립트 (원본 형식 기반)
"""

import os
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

def create_powerpoint():
    """PowerPoint 프레젠테이션 생성 (원본 형식 기반)"""
    
    # 원본과 동일한 슬라이드 구성 정보
    slides_config = [
        {
            'title': '수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로',
            'subtitle': '디지털 도구 완전정복\n한글학교 선생님을 위한 크롬 웹브라우저 활용 교육',
            'content': [
                '한글학교 선생님들을 위한 실용적인 디지털 도구 활용법',
                '크롬 웹브라우저를 중심으로 한 통합 교육 환경 구축',
                '기초부터 고급까지 단계별 학습 과정',
                '실습 중심의 체계적인 교육 프로그램'
            ]
        },
        {
            'title': '강의 개요',
            'content': [
                '교육 목표',
                '• 크롬 웹브라우저의 교육적 활용 능력 향상',
                '• 디지털 도구를 활용한 효율적인 수업 준비',
                '• 온라인 교육 환경에서의 협업 능력 강화',
                '',
                '교육 대상',
                '• 한글학교 교사 및 교육 관계자',
                '• 디지털 도구 활용에 관심 있는 교육자',
                '• 온라인 수업 환경 구축이 필요한 교사',
                '',
                '교육 구성',
                '• 기초: 크롬 브라우저 기본 기능 및 설정',
                '• 중급: 교육용 확장프로그램 및 한글교육 도구',
                '• 고급: 구글 워크스페이스 연동 및 AI 도구 활용',
                '',
                '교사 팁',
                '이 강의는 실습 중심으로 진행됩니다. 크롬 브라우저가 설치된 컴퓨터를 준비해 주세요.'
            ]
        },
        {
            'title': '기초 단계: 크롬 브라우저 기본 기능',
            'content': [
                '프로필 관리',
                '• 교육용 전용 프로필 생성',
                '• 개인용과 업무용 프로필 분리',
                '• 프로필별 북마크 및 확장프로그램 관리',
                '',
                '북마크 활용',
                '• 한글교육 사이트 북마크 폴더 구성',
                '• 북마크 바 활용 및 동기화 설정',
                '• 자주 사용하는 사이트 빠른 접근',
                '',
                '단축키 활용',
                '• Ctrl+T: 새 탭 열기',
                '• Ctrl+Shift+T: 최근 닫은 탭 복원',
                '• Ctrl+L: 주소창 포커스',
                '• Ctrl+Shift+N: 시크릿 모드',
                '',
                '기본 설정 최적화',
                '• 시작 페이지 설정',
                '• 검색 엔진 설정',
                '• 개인정보 및 보안 설정',
                '',
                '교사 팁',
                '수업 전 관련 사이트를 모두 탭으로 열어두고 탭 그룹으로 저장하면 수업 준비 시간을 단축할 수 있습니다.'
            ]
        },
        {
            'title': '중급 단계: 교육자를 위한 확장프로그램',
            'content': [
                '수업 준비 및 자료 관리',
                '',
                'Fireshot',
                '• 전체 웹페이지 스크린샷 캡처 도구',
                '• 자료 수집, 이미지 저장',
                '',
                'Google Keep Chrome',
                '• 단축키로 웹페이지 스크랩 및 메모',
                '• 메모, 자료 정리',
                '',
                '온라인 수업 지원',
                '',
                'Video Speed Controller',
                '• 웹 비디오 속도 조절 (0.5배속~4배속)',
                '• 동영상, 학습 속도',
                '',
                'Mote',
                '• 음성 피드백 및 지시사항 전달',
                '• 음성 메모, 피드백',
                '',
                '교사들이 가장 많이 사용하는 확장프로그램',
                '',
                'Brisk Teaching',
                '• AI 기반 교사 어시스턴트',
                '• AI, 자동화, 평가',
                '',
                '교사 팁',
                '확장프로그램은 크롬 웹 스토어에서 무료로 설치할 수 있습니다. 프로필별로 다른 확장프로그램을 설정하면 용도에 맞게 브라우저를 최적화할 수 있습니다.'
            ]
        },
        {
            'title': '중급 단계: 한글교육 특화 웹도구',
            'content': [
                '정부 제공 한국어 교육 플랫폼',
                '',
                '스터디코리안넷',
                '• 재외동포 한글/문화/역사 교육 종합 플랫폼',
                '• 교수자료, 학습자료',
                '',
                '한국어교수학습샘터',
                '• 국립국어원 제공 교수 자료 및 학습 콘텐츠',
                '• 교재, 멀티미디어',
                '',
                '한글학교 전용 자료',
                '',
                'NAKS 온라인 수업자료실',
                '• 재미한국학교협의회 제공 교육 자료',
                '• 수업자료, 활동지',
                '',
                '한국어교재 전자책 뷰어',
                '• 해외 초중등학교 한국어교재 온라인 학습',
                '• e-book, 멀티미디어',
                '',
                '한글 학습 웹사이트',
                '• 아신나 한글: 한글 기초 학습 사이트',
                '• 한글또박또박: 한글 쓰기 연습 사이트',
                '• LearnKoreanTools: 한국어 학습 워크시트 생성',
                '• Dinolingo: 어린이 한국어 학습 사이트',
                '',
                '교사 팁',
                '크롬 북마크 폴더를 만들어 사이트들을 주제별로 정리하고, 크롬 동기화 기능을 활용하면 모든 기기에서 동일한 북마크를 사용할 수 있습니다.'
            ]
        },
        {
            'title': '고급 단계: 구글 워크스페이스 연동',
            'content': [
                '통합 교육 플랫폼 구축',
                '',
                '구글 클래스룸',
                '• 온라인 학급 관리 및 과제 배포/평가',
                '• 학급관리, 과제평가',
                '',
                '구글 문서/슬라이드',
                '• 실시간 협업 문서 및 프레젠테이션',
                '• 문서작성, 실시간협업',
                '',
                '구글 드라이브',
                '• 클라우드 저장소 및 파일 공유',
                '• 자료저장, 공유',
                '',
                '구글 미트',
                '• 화상 수업 및 회의',
                '• 화상수업, 화면공유',
                '',
                '한글학교 수업 워크플로우',
                '자료 업로드 → 학생 공유 → 실시간 협업 → 피드백/평가',
                '',
                '구글 워크스페이스 활용 이점',
                '• 실시간 동기화: 모든 기기에서 동일한 환경',
                '• 협업 강화: 교사-학생, 교사-교사 간 실시간 협업',
                '• 과제 관리: 배포, 제출, 평가 자동화',
                '• 학습 분석: 학생 참여도 및 성취도 추적',
                '',
                '교사 팁',
                '크롬 브라우저에서 구글 계정으로 로그인하면 모든 구글 워크스페이스 도구를 원활하게 연동하여 사용할 수 있습니다.'
            ]
        },
        {
            'title': '고급 단계: AI 도구 활용',
            'content': [
                'AI 기반 교육 도구',
                '',
                'Brisk Teaching',
                '• AI 기반 교사 어시스턴트, 맞춤형 피드백 제공',
                '• 퀴즈생성, 피드백',
                '',
                'ChatGPT',
                '• 한국어 교육 자료 생성 및 문화 콘텐츠 제작',
                '• 자료생성, 질의응답',
                '',
                'Canva AI',
                '• 시각적 교육 자료 및 프레젠테이션 제작',
                '• 디자인, 이미지생성',
                '',
                '음성 인식/합성 도구',
                '• 발음 평가 및 맞춤형 음성 피드백',
                '• 발음교정, 듣기자료',
                '',
                '한글교육 AI 활용 사례',
                '• 맞춤형 학습지 생성: 학생 수준에 맞는 한글 학습지를 AI로 자동 생성',
                '• 발음 교정 피드백: AI 음성 인식으로 학생 발음을 분석하고 교정 피드백 제공',
                '• 문화 콘텐츠 제작: 한국 문화 관련 이야기와 시각 자료를 AI로 생성',
                '• 자동 평가 및 분석: 학생 과제를 AI로 평가하고 학습 진도 분석',
                '',
                '교사 팁',
                'AI 도구는 교사의 창의성과 전문성을 대체하는 것이 아니라, 반복적인 업무를 자동화하고 개인화된 학습 경험을 제공하는 데 활용하세요.'
            ]
        },
        {
            'title': '실습 시나리오',
            'content': [
                '실제 상황 기반 실습',
                '',
                '새 학기 준비 (기초)',
                '• 새 학기를 맞아 온라인 수업 환경을 구축해야 하는 상황',
                '• 교육용 크롬 프로필 생성 및 설정',
                '• 한글교육 사이트 북마크 폴더 구성',
                '• 필수 확장프로그램 설치 및 설정',
                '',
                '효율적인 수업 자료 준비 (중급)',
                '• 다음 주 수업을 위한 자료를 빠르게 준비해야 하는 상황',
                '• Fireshot으로 웹 자료 스크랩',
                '• Brisk Teaching으로 AI 퀴즈 생성',
                '• Canva로 시각적 자료 제작',
                '',
                '온라인 수업 진행 (중급)',
                '• 실시간 온라인 수업을 진행해야 하는 상황',
                '• Google Cast로 화면 공유 설정',
                '• Mote로 음성 피드백 제공',
                '• 실시간 상호작용 도구 활용',
                '',
                '학급 관리 시스템 구축 (고급)',
                '• 여러 학급을 효율적으로 관리해야 하는 상황',
                '• 구글 클래스룸 학급별 설정',
                '• 학생 과제 제출/평가 시스템 구축',
                '• 학습 진도 추적 대시보드 설정',
                '',
                '워크북 활용 방법',
                '• 단계별 실습: 기초-중급-고급 순서로 진행',
                '• 페어 학습: 2인 1조로 실습하며 서로 도움',
                '• 체크리스트: 각 단계별 완료 항목 확인',
                '• 결과 공유: 완성된 결과물 공유 및 피드백',
                '',
                '교사 팁',
                '실습 시나리오는 자신의 교육 환경에 맞게 응용하여 활용하세요. 모든 단계를 한 번에 완료하려 하기보다 점진적으로 적용해 나가는 것이 효과적입니다.'
            ]
        },
        {
            'title': '추가 자료 및 참고 링크',
            'content': [
                '학습 자료 및 튜토리얼',
                '',
                '크롬 브라우저 공식 자료',
                '• Google Chrome 도움말 센터: support.google.com/chrome',
                '• Chrome 웹 스토어: chrome.google.com/webstore',
                '• Chrome 개발자 블로그: developer.chrome.com/blog',
                '',
                '한글교육 자료',
                '• 스터디코리안넷: study.korean.net',
                '• 국립국어원 한국어교수학습샘터: kcenter.korean.go.kr',
                '• 재미한국학교협의회 (NAKS): www.naks.org',
                '',
                '디지털 교육 도구',
                '• Brisk Teaching: www.briskteaching.com',
                '• Canva 교육자용: www.canva.com/education',
                '• Google Workspace for Education: edu.google.com',
                '',
                '커뮤니티 및 지속적 학습',
                '',
                '교사 커뮤니티',
                '• 한글학교 교사 네트워크: 전 세계 한글학교 교사들의 경험과 자료 공유',
                '• 교육 기술 포럼: 최신 교육 기술 트렌드와 디지털 도구 활용법 논의',
                '• 크롬 교육자 그룹: 크롬 브라우저와 구글 도구를 교육에 활용하는 교사 모임',
                '',
                '온라인 강좌',
                '• 티처빌 - 크롬 활용 강좌: www.teacherville.co.kr',
                '• 구글 교육자 센터: teachercenter.withgoogle.com',
                '• 한국어 교원 온라인 연수: www.sejonghakdang.org',
                '',
                '교사 팁',
                '디지털 도구와 교육 트렌드는 빠르게 변화합니다. 커뮤니티에 참여하고 정기적으로 새로운 도구와 방법을 탐색하는 것이 중요합니다.'
            ]
        },
        {
            'title': '질문 및 연락처',
            'content': [
                '문의 및 지원',
                '',
                '이메일: support@koreanedu.org',
                '전화: 02-123-4567',
                '채팅 지원: 평일 9:00-18:00',
                'FAQ: www.koreanedu.org/faq',
                '',
                '커뮤니티 참여',
                '',
                '웹사이트: www.koreanedu.org',
                '월간 웨비나: 매월 마지막 주 토요일',
                '뉴스레터: 월 2회 발행',
                '',
                '',
                '감사합니다!',
                '',
                '더 나은 한글교육을 위한',
                '여러분의 디지털 여정을 응원합니다.'
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
        
        # 내용 슬라이드
        if 'content' in slide_data and len(slide.placeholders) > 1 and slide.placeholders[1]:
            content = slide.placeholders[1]
            content.text = '\n'.join(slide_data['content'])
            
            # 글꼴 크기 조정
            for paragraph in content.text_frame.paragraphs:
                paragraph.font.size = Pt(14)  # 원본과 유사한 크기
                paragraph.space_after = Pt(6)
    
    return prs

def main():
    """메인 함수"""
    print('PowerPoint 프레젠테이션 생성 중... (원본 형식 기반)')
    
    # 출력 디렉토리 확인
    os.makedirs('output', exist_ok=True)
    
    try:
        # PowerPoint 생성
        prs = create_powerpoint()
        
        # 파일 저장
        output_path = 'output/chrome_education_slides.pptx'
        prs.save(output_path)
        
        print(f'✅ PowerPoint 파일 생성 완료: {output_path}')
        print('📊 10개 슬라이드, 원본과 동일한 상세 내용 포함')
        
    except Exception as e:
        print(f'❌ PowerPoint 생성 실패: {e}')
        return False
    
    return True

if __name__ == '__main__':
    main()

