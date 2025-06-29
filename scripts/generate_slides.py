#!/usr/bin/env python3
"""
Chrome Education Slides Generator
한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 슬라이드 생성기
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

class ChromeEducationSlidesGenerator:
    def __init__(self, project_dir=None):
        if project_dir is None:
            project_dir = Path(__file__).parent.parent
        
        self.project_dir = Path(project_dir)
        self.slides_dir = self.project_dir / "slides"
        self.assets_dir = self.project_dir / "assets"
        self.output_dir = self.project_dir / "output"
        self.src_dir = self.project_dir / "src"
        
        # 디렉토리 생성
        self.output_dir.mkdir(exist_ok=True)
        self.src_dir.mkdir(exist_ok=True)
    
    def get_slide_config(self):
        """슬라이드 구성 정보 반환"""
        return {
            "title": "수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로 — 디지털 도구 완전정복",
            "subtitle": "한글학교 선생님을 위한 크롬 웹브라우저 활용 교육",
            "slides": [
                {
                    "id": "title_slide",
                    "title": "타이틀 슬라이드",
                    "type": "title",
                    "content": {
                        "main_title": "수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로",
                        "subtitle": "디지털 도구 완전정복",
                        "description": "한글학교 선생님을 위한 크롬 웹브라우저 활용 교육"
                    }
                },
                {
                    "id": "course_overview",
                    "title": "강의 개요",
                    "type": "content",
                    "content": {
                        "sections": [
                            "교육 목표 및 대상",
                            "기초-중급-고급 단계별 구성",
                            "실습 중심의 학습 방법",
                            "지속적인 학습을 위한 커뮤니티"
                        ]
                    }
                },
                {
                    "id": "basic_features",
                    "title": "기초 단계: 크롬 브라우저 기본 기능",
                    "type": "content",
                    "content": {
                        "features": [
                            "프로필 관리",
                            "북마크 활용",
                            "단축키 활용",
                            "기본 설정 최적화"
                        ]
                    }
                },
                {
                    "id": "extensions_intro",
                    "title": "중급 단계: 교육자를 위한 확장프로그램",
                    "type": "content",
                    "content": {
                        "extensions": [
                            "Fireshot - 웹페이지 캡처",
                            "Google Keep - 메모 및 스크랩",
                            "Video Speed Controller - 동영상 속도 조절",
                            "Mote - 음성 피드백"
                        ]
                    }
                },
                {
                    "id": "korean_edu_tools",
                    "title": "중급 단계: 한글교육 특화 웹도구",
                    "type": "content",
                    "content": {
                        "tools": [
                            "스터디코리안넷",
                            "한국어교수학습샘터",
                            "NAKS 온라인 자료실",
                            "한글또박또박"
                        ]
                    }
                },
                {
                    "id": "advanced_collab",
                    "title": "고급 단계: 구글 워크스페이스 연동",
                    "type": "content",
                    "content": {
                        "workspace_tools": [
                            "구글 클래스룸",
                            "구글 문서/슬라이드",
                            "구글 드라이브",
                            "구글 미트"
                        ]
                    }
                },
                {
                    "id": "ai_tools",
                    "title": "고급 단계: AI 도구 활용",
                    "type": "content",
                    "content": {
                        "ai_tools": [
                            "Brisk Teaching - AI 교사 어시스턴트",
                            "ChatGPT - 교육 자료 생성",
                            "Canva AI - 시각적 자료 제작",
                            "음성 인식/합성 도구"
                        ]
                    }
                },
                {
                    "id": "practice_scenarios",
                    "title": "실습 시나리오",
                    "type": "content",
                    "content": {
                        "scenarios": [
                            "새 학기 준비 (기초)",
                            "효율적인 수업 자료 준비 (중급)",
                            "온라인 수업 진행 (중급)",
                            "학급 관리 시스템 구축 (고급)"
                        ]
                    }
                },
                {
                    "id": "resources",
                    "title": "추가 자료 및 참고 링크",
                    "type": "content",
                    "content": {
                        "resources": [
                            "크롬 브라우저 공식 자료",
                            "한글교육 자료",
                            "디지털 교육 도구",
                            "교사 커뮤니티"
                        ]
                    }
                },
                {
                    "id": "qa_contact",
                    "title": "질문 및 연락처",
                    "type": "contact",
                    "content": {
                        "contact_info": [
                            "이메일: support@koreanedu.org",
                            "전화: 02-123-4567",
                            "웹사이트: www.koreanedu.org"
                        ]
                    }
                }
            ]
        }
    
    def generate_slide_config_file(self):
        """슬라이드 구성 파일 생성"""
        config = self.get_slide_config()
        config_file = self.src_dir / "slide_config.json"
        
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 슬라이드 구성 파일 생성: {config_file}")
        return config_file
    
    def copy_existing_slides(self):
        """기존 슬라이드 파일들을 output 디렉토리로 복사"""
        if self.slides_dir.exists():
            print("📋 기존 슬라이드 파일 복사 중...")
            
            # HTML 파일들 복사
            for html_file in self.slides_dir.glob("*.html"):
                shutil.copy2(html_file, self.output_dir)
                print(f"  ✅ {html_file.name} 복사 완료")
            
            # 이미지 디렉토리가 있다면 복사
            images_dir = self.slides_dir / "images"
            if images_dir.exists():
                output_images_dir = self.output_dir / "images"
                if output_images_dir.exists():
                    shutil.rmtree(output_images_dir)
                shutil.copytree(images_dir, output_images_dir)
                print("  ✅ 이미지 디렉토리 복사 완료")
    
    def generate_presentation_index(self):
        """프레젠테이션 인덱스 HTML 생성"""
        config = self.get_slide_config()
        
        html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config["title"]}</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Noto Sans KR', sans-serif; }}
        .slide-card:hover {{ transform: translateY(-4px); transition: all 0.3s ease; }}
        .chrome-colors {{ 
            background: linear-gradient(45deg, #4285F4, #EA4335, #FBBC05, #34A853);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
    </style>
</head>
<body class="bg-gray-50">
    <div class="container mx-auto px-4 py-8">
        <!-- 헤더 -->
        <div class="text-center mb-12">
            <div class="flex justify-center items-center mb-6">
                <i class="fab fa-chrome text-6xl text-blue-500 mr-4"></i>
                <div>
                    <h1 class="text-4xl font-bold chrome-colors mb-2">
                        {config["title"]}
                    </h1>
                    <p class="text-xl text-gray-600">{config["subtitle"]}</p>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md p-6 max-w-2xl mx-auto">
                <p class="text-gray-700">
                    한글학교 선생님들을 위한 크롬 웹브라우저 활용 교육 자료입니다. 
                    기초부터 고급까지 단계별로 구성되어 있으며, 실습 중심의 학습을 통해 
                    디지털 도구를 효과적으로 활용할 수 있도록 도와드립니다.
                </p>
            </div>
        </div>
        
        <!-- 슬라이드 목록 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
'''
        
        # 슬라이드 카드 생성
        for i, slide in enumerate(config["slides"]):
            level_colors = {
                "title": "bg-gradient-to-r from-blue-500 to-purple-500",
                "content": "bg-gradient-to-r from-green-500 to-blue-500",
                "contact": "bg-gradient-to-r from-orange-500 to-red-500"
            }
            
            card_color = level_colors.get(slide["type"], "bg-gradient-to-r from-gray-500 to-gray-600")
            
            html_content += f'''
            <div class="slide-card bg-white rounded-xl shadow-lg overflow-hidden">
                <div class="{card_color} p-4">
                    <div class="flex items-center justify-between">
                        <span class="text-white font-bold">슬라이드 {i+1:02d}</span>
                        <i class="fas fa-presentation text-white text-xl"></i>
                    </div>
                </div>
                <div class="p-6">
                    <h3 class="text-lg font-bold text-gray-800 mb-3">{slide["title"]}</h3>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-gray-500 capitalize">{slide["type"]}</span>
                        <a href="{slide["id"]}.html" target="_blank" 
                           class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition-colors inline-flex items-center">
                            <i class="fas fa-eye mr-2"></i>보기
                        </a>
                    </div>
                </div>
            </div>
'''
        
        html_content += '''
        </div>
        
        <!-- 추가 자료 섹션 -->
        <div class="bg-white rounded-xl shadow-lg p-8">
            <h2 class="text-2xl font-bold text-center text-gray-800 mb-8">
                <i class="fas fa-book-open mr-3 text-blue-500"></i>추가 자료
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <a href="../docs/chrome_edu_workbook.pdf" target="_blank" 
                   class="bg-gradient-to-r from-green-500 to-green-600 text-white p-6 rounded-lg hover:from-green-600 hover:to-green-700 transition-all transform hover:scale-105">
                    <div class="text-center">
                        <i class="fas fa-file-pdf text-3xl mb-3"></i>
                        <h3 class="font-bold text-lg mb-2">실습 워크북</h3>
                        <p class="text-sm opacity-90">단계별 실습 가이드 (PDF)</p>
                    </div>
                </a>
                
                <a href="../docs/chrome_education_research.md" target="_blank" 
                   class="bg-gradient-to-r from-purple-500 to-purple-600 text-white p-6 rounded-lg hover:from-purple-600 hover:to-purple-700 transition-all transform hover:scale-105">
                    <div class="text-center">
                        <i class="fas fa-search text-3xl mb-3"></i>
                        <h3 class="font-bold text-lg mb-2">조사 자료</h3>
                        <p class="text-sm opacity-90">교육 도구 조사 및 분석</p>
                    </div>
                </a>
                
                <a href="../docs/curriculum_design.md" target="_blank" 
                   class="bg-gradient-to-r from-orange-500 to-orange-600 text-white p-6 rounded-lg hover:from-orange-600 hover:to-orange-700 transition-all transform hover:scale-105">
                    <div class="text-center">
                        <i class="fas fa-graduation-cap text-3xl mb-3"></i>
                        <h3 class="font-bold text-lg mb-2">커리큘럼 설계</h3>
                        <p class="text-sm opacity-90">교육 과정 설계 문서</p>
                    </div>
                </a>
            </div>
        </div>
        
        <!-- 푸터 -->
        <div class="text-center mt-12 text-gray-600">
            <p class="mb-2">
                <i class="fas fa-calendar-alt mr-2"></i>
                생성일: {datetime.now().strftime("%Y년 %m월 %d일")}
            </p>
            <p>
                <i class="fas fa-heart text-red-500 mr-2"></i>
                한글교육의 디지털 혁신을 응원합니다
            </p>
        </div>
    </div>
</body>
</html>'''
        
        index_file = self.output_dir / "index.html"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ 프레젠테이션 인덱스 생성: {index_file}")
        return index_file
    
    def generate_build_info(self):
        """빌드 정보 파일 생성"""
        config = self.get_slide_config()
        
        build_info = {
            "build_date": datetime.now().isoformat(),
            "build_version": "1.0.0",
            "title": config["title"],
            "subtitle": config["subtitle"],
            "slides_count": len(config["slides"]),
            "slides": [slide["id"] for slide in config["slides"]],
            "generated_files": [
                "index.html",
                "slide_config.json",
                "chrome_edu_workbook.pdf"
            ] + [f"{slide['id']}.html" for slide in config["slides"]]
        }
        
        build_file = self.output_dir / "build_info.json"
        with open(build_file, 'w', encoding='utf-8') as f:
            json.dump(build_info, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 빌드 정보 생성: {build_file}")
        return build_file
    
    def run(self):
        """전체 생성 프로세스 실행"""
        print("🚀 Chrome Education Slides Generator 시작")
        print(f"📁 프로젝트 디렉토리: {self.project_dir}")
        
        # 1. 슬라이드 구성 파일 생성
        self.generate_slide_config_file()
        
        # 2. 기존 슬라이드 파일 복사
        self.copy_existing_slides()
        
        # 3. 프레젠테이션 인덱스 생성
        self.generate_presentation_index()
        
        # 4. 빌드 정보 생성
        self.generate_build_info()
        
        # 5. 결과 출력
        print("\n🎉 슬라이드 생성 완료!")
        print(f"📂 결과물 위치: {self.output_dir}")
        print(f"🌐 프레젠테이션 인덱스: {self.output_dir}/index.html")
        
        # 생성된 파일 목록
        print("\n📋 생성된 파일 목록:")
        for file_path in sorted(self.output_dir.iterdir()):
            if file_path.is_file():
                size = file_path.stat().st_size
                print(f"  📄 {file_path.name} ({size:,} bytes)")

if __name__ == "__main__":
    generator = ChromeEducationSlidesGenerator()
    generator.run()

