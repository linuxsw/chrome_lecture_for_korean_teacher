#!/usr/bin/env python3
"""
Enhanced Chrome Education Slides Generator
기존 HTML 슬라이드를 기반으로 향상된 슬라이드 생성기
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

class EnhancedChromeEducationSlidesGenerator:
    def __init__(self, project_dir=None):
        if project_dir is None:
            project_dir = Path(__file__).parent.parent
        
        self.project_dir = Path(project_dir)
        self.assets_dir = self.project_dir / "assets"
        self.output_dir = self.project_dir / "output"
        self.src_dir = self.project_dir / "src"
        
        # 기존 슬라이드 디렉토리 (원본 HTML 슬라이드들)
        self.original_slides_dir = Path("/home/ubuntu/chrome_edu_project")
        
        # 디렉토리 생성
        self.output_dir.mkdir(exist_ok=True)
        self.src_dir.mkdir(exist_ok=True)
    
    def copy_original_slides(self):
        """기존 HTML 슬라이드 파일들을 output 디렉토리로 복사"""
        print("📋 기존 HTML 슬라이드 파일 복사 중...")
        
        if not self.original_slides_dir.exists():
            print(f"  ⚠️ 원본 슬라이드 디렉토리를 찾을 수 없습니다: {self.original_slides_dir}")
            return False
        
        # HTML 파일들 복사
        html_files = list(self.original_slides_dir.glob("*.html"))
        if not html_files:
            print(f"  ⚠️ HTML 파일을 찾을 수 없습니다: {self.original_slides_dir}")
            return False
        
        for html_file in html_files:
            dest_file = self.output_dir / html_file.name
            shutil.copy2(html_file, dest_file)
            print(f"  ✅ {html_file.name} 복사 완료")
        
        # 이미지 디렉토리 복사
        images_dir = self.original_slides_dir / "images"
        if images_dir.exists():
            output_images_dir = self.output_dir / "images"
            if output_images_dir.exists():
                shutil.rmtree(output_images_dir)
            shutil.copytree(images_dir, output_images_dir)
            print("  ✅ 이미지 디렉토리 복사 완료")
        
        return True
    
    def copy_assets(self):
        """생성된 assets을 output 디렉토리로 복사"""
        print("📁 Assets 파일 복사 중...")
        
        if not self.assets_dir.exists():
            print(f"  ⚠️ Assets 디렉토리를 찾을 수 없습니다: {self.assets_dir}")
            return False
        
        # assets 디렉토리를 output으로 복사
        output_assets_dir = self.output_dir / "assets"
        if output_assets_dir.exists():
            shutil.rmtree(output_assets_dir)
        shutil.copytree(self.assets_dir, output_assets_dir)
        print("  ✅ Assets 디렉토리 복사 완료")
        
        return True
    
    def generate_enhanced_index(self):
        """향상된 프레젠테이션 인덱스 HTML 생성"""
        print("🌐 향상된 프레젠테이션 인덱스 생성 중...")
        
        # 슬라이드 정보
        slides_info = [
            ("title_slide.html", "타이틀 슬라이드", "수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로"),
            ("course_overview.html", "강의 개요", "교육 목표, 대상, 단계별 학습 내용"),
            ("basic_features.html", "기초 단계", "크롬 브라우저 기본 기능 마스터"),
            ("extensions_intro.html", "중급 단계 - 확장프로그램", "교육자를 위한 필수 확장프로그램"),
            ("korean_edu_tools.html", "중급 단계 - 한글교육 도구", "한글교육 특화 웹도구 활용"),
            ("advanced_collab.html", "고급 단계 - 워크스페이스", "구글 워크스페이스 연동 마스터"),
            ("ai_tools.html", "고급 단계 - AI 도구", "AI 기반 교육 도구 활용"),
            ("practice_scenarios.html", "실습 시나리오", "단계별 실습 가이드"),
            ("resources.html", "추가 자료", "참고 링크 및 학습 자료"),
            ("qa_contact.html", "질문 및 연락처", "문의 및 지원 정보")
        ]
        
        html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로 — 디지털 도구 완전정복</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ 
            font-family: 'Noto Sans KR', sans-serif; 
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }}
        .slide-card:hover {{ 
            transform: translateY(-8px) scale(1.02); 
            transition: all 0.4s ease; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }}
        .chrome-colors {{ 
            background: linear-gradient(45deg, #4285F4, #EA4335, #FBBC05, #34A853);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .hero-section {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            position: relative;
            overflow: hidden;
        }}
        .hero-section::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }}
        .floating-icon {{
            animation: float 3s ease-in-out infinite;
        }}
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}
        .gradient-border {{
            background: linear-gradient(45deg, #4285F4, #EA4335, #FBBC05, #34A853);
            padding: 2px;
            border-radius: 12px;
        }}
        .gradient-border > div {{
            background: white;
            border-radius: 10px;
        }}
    </style>
</head>
<body>
    <!-- Hero Section -->
    <div class="hero-section text-white py-20 relative">
        <div class="container mx-auto px-4 text-center relative z-10">
            <div class="flex justify-center items-center mb-8">
                <i class="fab fa-chrome text-8xl mr-6 floating-icon"></i>
                <div>
                    <h1 class="text-5xl font-bold mb-4">
                        수업을 쉽게, 자료를 예쁘게,<br>협업을 효율적으로
                    </h1>
                    <p class="text-2xl opacity-90">— 디지털 도구 완전정복</p>
                </div>
            </div>
            <p class="text-xl mb-8 max-w-3xl mx-auto opacity-90">
                한글학교 선생님들을 위한 크롬 웹브라우저 활용 교육 자료입니다. 
                기초부터 고급까지 단계별로 구성되어 있으며, 실습 중심의 학습을 통해 
                디지털 도구를 효과적으로 활용할 수 있도록 도와드립니다.
            </p>
            
            <!-- Chrome Color Dots -->
            <div class="flex justify-center space-x-4 mb-8">
                <div class="w-4 h-4 bg-blue-500 rounded-full floating-icon" style="animation-delay: 0s;"></div>
                <div class="w-4 h-4 bg-red-500 rounded-full floating-icon" style="animation-delay: 0.5s;"></div>
                <div class="w-4 h-4 bg-yellow-500 rounded-full floating-icon" style="animation-delay: 1s;"></div>
                <div class="w-4 h-4 bg-green-500 rounded-full floating-icon" style="animation-delay: 1.5s;"></div>
            </div>
        </div>
    </div>
    
    <!-- Main Content -->
    <div class="container mx-auto px-4 py-16">
        <!-- 슬라이드 목록 -->
        <div class="mb-16">
            <h2 class="text-4xl font-bold text-center text-gray-800 mb-4">
                <i class="fas fa-presentation mr-3 text-blue-500"></i>프레젠테이션 슬라이드
            </h2>
            <p class="text-center text-gray-600 mb-12 text-lg">
                각 슬라이드를 클릭하여 전체 화면으로 보실 수 있습니다
            </p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
        
        # 슬라이드 카드 생성
        level_colors = [
            "from-purple-500 to-blue-500",    # 타이틀
            "from-blue-500 to-indigo-500",    # 개요
            "from-green-500 to-teal-500",     # 기초
            "from-yellow-500 to-orange-500",  # 중급1
            "from-orange-500 to-red-500",     # 중급2
            "from-red-500 to-pink-500",       # 고급1
            "from-pink-500 to-purple-500",    # 고급2
            "from-indigo-500 to-blue-500",    # 실습
            "from-teal-500 to-green-500",     # 자료
            "from-gray-500 to-gray-600"       # 연락처
        ]
        
        for i, (filename, title, description) in enumerate(slides_info):
            gradient = level_colors[i % len(level_colors)]
            
            html_content += f'''
                <div class="gradient-border">
                    <div class="slide-card bg-white rounded-xl overflow-hidden h-full">
                        <div class="bg-gradient-to-r {gradient} p-6">
                            <div class="flex items-center justify-between">
                                <span class="text-white font-bold text-lg">슬라이드 {i+1:02d}</span>
                                <i class="fas fa-play-circle text-white text-2xl"></i>
                            </div>
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-bold text-gray-800 mb-3">{title}</h3>
                            <p class="text-gray-600 mb-4 text-sm leading-relaxed">{description}</p>
                            <div class="flex justify-between items-center">
                                <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded">
                                    HTML 슬라이드
                                </span>
                                <a href="{filename}" target="_blank" 
                                   class="bg-gradient-to-r {gradient} text-white px-6 py-2 rounded-lg hover:shadow-lg transition-all inline-flex items-center">
                                    <i class="fas fa-external-link-alt mr-2"></i>보기
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
'''
        
        html_content += '''
            </div>
        </div>
        
        <!-- 추가 자료 섹션 -->
        <div class="bg-white rounded-2xl shadow-xl p-8 mb-16">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-8">
                <i class="fas fa-download mr-3 text-green-500"></i>다운로드 자료
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="chrome_education_slides.pptx" target="_blank" 
                   class="bg-gradient-to-r from-blue-500 to-blue-600 text-white p-6 rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all transform hover:scale-105 group">
                    <div class="text-center">
                        <i class="fas fa-file-powerpoint text-4xl mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 class="font-bold text-lg mb-2">PowerPoint 프레젠테이션</h3>
                        <p class="text-sm opacity-90">시각적으로 완성도 높은 PPTX 파일</p>
                        <div class="mt-3 text-xs bg-blue-400 bg-opacity-50 px-2 py-1 rounded">
                            10개 슬라이드 • 6.7MB
                        </div>
                    </div>
                </a>
                
                <a href="../docs/chrome_edu_workbook.pdf" target="_blank" 
                   class="bg-gradient-to-r from-green-500 to-green-600 text-white p-6 rounded-xl hover:from-green-600 hover:to-green-700 transition-all transform hover:scale-105 group">
                    <div class="text-center">
                        <i class="fas fa-file-pdf text-4xl mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 class="font-bold text-lg mb-2">실습 워크북</h3>
                        <p class="text-sm opacity-90">단계별 실습 가이드 (PDF)</p>
                        <div class="mt-3 text-xs bg-green-400 bg-opacity-50 px-2 py-1 rounded">
                            한글 폰트 지원
                        </div>
                    </div>
                </a>
                
                <a href="../docs/chrome_education_research.md" target="_blank" 
                   class="bg-gradient-to-r from-purple-500 to-purple-600 text-white p-6 rounded-xl hover:from-purple-600 hover:to-purple-700 transition-all transform hover:scale-105 group">
                    <div class="text-center">
                        <i class="fas fa-search text-4xl mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 class="font-bold text-lg mb-2">조사 자료</h3>
                        <p class="text-sm opacity-90">교육 도구 조사 및 분석</p>
                        <div class="mt-3 text-xs bg-purple-400 bg-opacity-50 px-2 py-1 rounded">
                            Markdown 형식
                        </div>
                    </div>
                </a>
            </div>
        </div>
        
        <!-- 기능 소개 섹션 -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            <div class="bg-white rounded-xl shadow-lg p-6 text-center">
                <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-laptop-code text-blue-500 text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-800 mb-2">시각적 완성도</h3>
                <p class="text-gray-600">배경 이미지, 아이콘, 그래픽이 포함된 고품질 슬라이드</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 text-center">
                <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-users text-green-500 text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-800 mb-2">실습 중심</h3>
                <p class="text-gray-600">한글학교 현장에 바로 적용 가능한 실용적 내용</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 text-center">
                <div class="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-rocket text-purple-500 text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-800 mb-2">자동 생성</h3>
                <p class="text-gray-600">GitHub Actions로 자동 빌드 및 배포</p>
            </div>
        </div>
        
        <!-- 푸터 -->
        <div class="text-center text-gray-600 border-t pt-8">
            <div class="flex justify-center items-center mb-4">
                <i class="fab fa-github mr-2"></i>
                <a href="https://github.com/linuxsw/chrome_lecture_for_korean_teacher" 
                   class="text-blue-500 hover:text-blue-600 transition-colors">
                    GitHub 저장소
                </a>
            </div>
            <p class="mb-2">
                <i class="fas fa-calendar-alt mr-2"></i>
                생성일: {datetime.now().strftime("%Y년 %m월 %d일")}
            </p>
            <p class="text-lg">
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
        
        print(f"  ✅ 향상된 프레젠테이션 인덱스 생성: {index_file}")
        return index_file
    
    def generate_build_info(self):
        """빌드 정보 파일 생성"""
        print("📊 빌드 정보 생성 중...")
        
        build_info = {
            "build_date": datetime.now().isoformat(),
            "build_version": "2.0.0",
            "title": "수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로 — 디지털 도구 완전정복",
            "subtitle": "한글학교 선생님을 위한 크롬 웹브라우저 활용 교육",
            "slides_count": 10,
            "features": [
                "시각적으로 완성도 높은 HTML 슬라이드",
                "배경 이미지, 아이콘, 그래픽 포함",
                "고품질 PowerPoint 파일 (6.7MB)",
                "한글 폰트 지원 PDF 워크북",
                "자동 빌드 및 배포 시스템"
            ],
            "generated_files": [
                "index.html",
                "chrome_education_slides.pptx",
                "chrome_edu_workbook.pdf",
                "title_slide.html",
                "course_overview.html",
                "basic_features.html",
                "extensions_intro.html",
                "korean_edu_tools.html",
                "advanced_collab.html",
                "ai_tools.html",
                "practice_scenarios.html",
                "resources.html",
                "qa_contact.html"
            ]
        }
        
        build_file = self.output_dir / "build_info.json"
        with open(build_file, 'w', encoding='utf-8') as f:
            json.dump(build_info, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ 빌드 정보 생성: {build_file}")
        return build_file
    
    def run(self):
        """전체 생성 프로세스 실행"""
        print("🚀 Enhanced Chrome Education Slides Generator 시작")
        print(f"📁 프로젝트 디렉토리: {self.project_dir}")
        
        success = True
        
        # 1. 기존 HTML 슬라이드 복사
        if not self.copy_original_slides():
            print("  ⚠️ 기존 슬라이드 복사 실패, 계속 진행...")
        
        # 2. Assets 복사
        if not self.copy_assets():
            print("  ⚠️ Assets 복사 실패, 계속 진행...")
        
        # 3. 향상된 프레젠테이션 인덱스 생성
        self.generate_enhanced_index()
        
        # 4. 빌드 정보 생성
        self.generate_build_info()
        
        # 5. 결과 출력
        print("\n🎉 향상된 슬라이드 생성 완료!")
        print(f"📂 결과물 위치: {self.output_dir}")
        print(f"🌐 프레젠테이션 인덱스: {self.output_dir}/index.html")
        
        # 생성된 파일 목록
        print("\n📋 생성된 파일 목록:")
        for file_path in sorted(self.output_dir.iterdir()):
            if file_path.is_file():
                size = file_path.stat().st_size
                print(f"  📄 {file_path.name} ({size:,} bytes)")
        
        return success

if __name__ == "__main__":
    generator = EnhancedChromeEducationSlidesGenerator()
    generator.run()

