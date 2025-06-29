#!/usr/bin/env python3
"""
HTML Pages 생성 스크립트 (Commit 3bbe342 기반)
타임스탬프 포함 및 GitHub Pages 최적화
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

class HTMLPagesGenerator:
    def __init__(self, project_dir=None):
        if project_dir is None:
            project_dir = Path(__file__).parent.parent
        
        self.project_dir = Path(project_dir)
        self.slides_source_dir = self.project_dir / "slides_3bbe342"
        self.output_dir = self.project_dir / "output"
        
        # 디렉토리 생성
        self.output_dir.mkdir(exist_ok=True)
    
    def copy_slides_and_images(self):
        """Commit 3bbe342의 슬라이드와 이미지 복사"""
        print("📋 Commit 3bbe342 슬라이드 및 이미지 복사 중...")
        
        if not self.slides_source_dir.exists():
            print(f"  ❌ 소스 슬라이드 디렉토리를 찾을 수 없습니다: {self.slides_source_dir}")
            return False
        
        # HTML 파일들 복사
        html_files = list(self.slides_source_dir.glob("*.html"))
        if not html_files:
            print(f"  ❌ HTML 파일을 찾을 수 없습니다: {self.slides_source_dir}")
            return False
        
        for html_file in html_files:
            dest_file = self.output_dir / html_file.name
            shutil.copy2(html_file, dest_file)
            print(f"  ✅ {html_file.name} 복사 완료")
        
        # 이미지 디렉토리 복사
        images_source_dir = self.slides_source_dir / "images"
        if images_source_dir.exists():
            output_images_dir = self.output_dir / "images"
            if output_images_dir.exists():
                shutil.rmtree(output_images_dir)
            shutil.copytree(images_source_dir, output_images_dir)
            print("  ✅ 이미지 디렉토리 복사 완료")
        
        return True
    
    def generate_enhanced_index(self):
        """타임스탬프가 포함된 향상된 인덱스 페이지 생성"""
        print("🌐 타임스탬프 포함 인덱스 페이지 생성 중...")
        
        # 현재 시간 정보
        now = datetime.now()
        build_time = now.strftime("%Y년 %m월 %d일 %H시 %M분")
        iso_time = now.isoformat()
        
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
        .timestamp-badge {{
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        }}
        .pulse {{
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.7; }}
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
            
            <!-- 타임스탬프 배지 -->
            <div class="mb-8">
                <div class="timestamp-badge">
                    <i class="fas fa-clock pulse"></i>
                    <span>최종 업데이트: {build_time}</span>
                </div>
            </div>
            
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
            <p class="text-center text-gray-600 mb-4 text-lg">
                각 슬라이드를 클릭하여 전체 화면으로 보실 수 있습니다
            </p>
            <p class="text-center text-sm text-gray-500 mb-12">
                <i class="fas fa-info-circle mr-1"></i>
                Commit 3bbe342 기반으로 복원된 원본 슬라이드
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
        
        html_content += f'''
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
                        <p class="text-sm opacity-90">Aspose.Slides로 생성된 PPTX 파일</p>
                        <div class="mt-3 text-xs bg-blue-400 bg-opacity-50 px-2 py-1 rounded">
                            10개 슬라이드 • Commit 3bbe342 이미지
                        </div>
                    </div>
                </a>
                
                <a href="chrome_edu_workbook.pdf" target="_blank" 
                   class="bg-gradient-to-r from-green-500 to-green-600 text-white p-6 rounded-xl hover:from-green-600 hover:to-green-700 transition-all transform hover:scale-105 group">
                    <div class="text-center">
                        <i class="fas fa-file-pdf text-4xl mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 class="font-bold text-lg mb-2">실습 워크북</h3>
                        <p class="text-sm opacity-90">WeasyPrint로 생성된 PDF (한글 지원)</p>
                        <div class="mt-3 text-xs bg-green-400 bg-opacity-50 px-2 py-1 rounded">
                            Commit 4a9b4e9 방법
                        </div>
                    </div>
                </a>
                
                <a href="https://github.com/linuxsw/chrome_lecture_for_korean_teacher" target="_blank" 
                   class="bg-gradient-to-r from-purple-500 to-purple-600 text-white p-6 rounded-xl hover:from-purple-600 hover:to-purple-700 transition-all transform hover:scale-105 group">
                    <div class="text-center">
                        <i class="fab fa-github text-4xl mb-4 group-hover:scale-110 transition-transform"></i>
                        <h3 class="font-bold text-lg mb-2">GitHub 저장소</h3>
                        <p class="text-sm opacity-90">소스 코드 및 자동 빌드 시스템</p>
                        <div class="mt-3 text-xs bg-purple-400 bg-opacity-50 px-2 py-1 rounded">
                            오픈소스
                        </div>
                    </div>
                </a>
            </div>
        </div>
        
        <!-- 빌드 정보 섹션 -->
        <div class="bg-gradient-to-r from-gray-50 to-gray-100 rounded-2xl shadow-lg p-8 mb-16">
            <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">
                <i class="fas fa-info-circle mr-3 text-blue-500"></i>빌드 정보
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
                <div class="bg-white rounded-lg p-4 shadow">
                    <div class="text-2xl font-bold text-blue-600 mb-2">{build_time}</div>
                    <div class="text-sm text-gray-600">최종 빌드 시간</div>
                </div>
                <div class="bg-white rounded-lg p-4 shadow">
                    <div class="text-2xl font-bold text-green-600 mb-2">3가지 형식</div>
                    <div class="text-sm text-gray-600">HTML • PDF • PPTX</div>
                </div>
                <div class="bg-white rounded-lg p-4 shadow">
                    <div class="text-2xl font-bold text-purple-600 mb-2">자동 생성</div>
                    <div class="text-sm text-gray-600">GitHub Actions</div>
                </div>
            </div>
            <div class="mt-6 text-center">
                <div class="text-xs text-gray-500 bg-gray-200 px-3 py-1 rounded-full inline-block">
                    <i class="fas fa-code-branch mr-1"></i>
                    HTML: Commit 3bbe342 • PDF: Commit 4a9b4e9 • PPTX: Aspose.Slides
                </div>
            </div>
        </div>
        
        <!-- 기능 소개 섹션 -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            <div class="bg-white rounded-xl shadow-lg p-6 text-center">
                <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-history text-blue-500 text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-800 mb-2">원본 복원</h3>
                <p class="text-gray-600">Commit 3bbe342의 원본 슬라이드와 이미지 완전 복원</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 text-center">
                <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-language text-green-500 text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-800 mb-2">한글 지원</h3>
                <p class="text-gray-600">모든 형식에서 한글 폰트 정상 표시 보장</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 text-center">
                <div class="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-clock text-purple-500 text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-gray-800 mb-2">실시간 업데이트</h3>
                <p class="text-gray-600">빌드 시간 표시로 최신 버전 확인 가능</p>
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
                생성일: {build_time}
            </p>
            <p class="mb-2 text-sm">
                <i class="fas fa-code mr-2"></i>
                빌드 ID: <code class="bg-gray-100 px-2 py-1 rounded text-xs">{iso_time}</code>
            </p>
            <p class="text-lg">
                <i class="fas fa-heart text-red-500 mr-2"></i>
                한글교육의 디지털 혁신을 응원합니다
            </p>
        </div>
    </div>
    
    <!-- 실시간 시계 스크립트 -->
    <script>
        // 페이지 로드 시간 표시
        document.addEventListener('DOMContentLoaded', function() {{
            const buildTime = new Date('{iso_time}');
            const now = new Date();
            const diffMinutes = Math.floor((now - buildTime) / (1000 * 60));
            
            if (diffMinutes < 60) {{
                const badge = document.querySelector('.timestamp-badge span');
                if (badge) {{
                    badge.innerHTML = `최종 업데이트: ${{diffMinutes}}분 전`;
                }}
            }}
        }});
    </script>
</body>
</html>'''
        
        index_file = self.output_dir / "index.html"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"  ✅ 타임스탬프 포함 인덱스 생성: {index_file}")
        return index_file
    
    def generate_build_info(self):
        """빌드 정보 JSON 파일 생성"""
        print("📊 빌드 정보 생성 중...")
        
        now = datetime.now()
        build_info = {
            "build_date": now.isoformat(),
            "build_date_kr": now.strftime("%Y년 %m월 %d일 %H시 %M분"),
            "build_version": "3.0.0",
            "commit_info": {
                "html_slides": "3bbe342",
                "pdf_method": "4a9b4e9", 
                "pptx_library": "Aspose.Slides"
            },
            "title": "수업을 쉽게, 자료를 예쁘게, 협업을 효율적으로 — 디지털 도구 완전정복",
            "subtitle": "한글학교 선생님을 위한 크롬 웹브라우저 활용 교육",
            "slides_count": 10,
            "features": [
                "Commit 3bbe342 원본 슬라이드 복원",
                "Commit 4a9b4e9 PDF 생성 방법 사용",
                "Aspose.Slides for Python PPTX 생성",
                "한글 폰트 완전 지원",
                "실시간 빌드 타임스탬프",
                "GitHub Actions 자동 빌드"
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
        print("🚀 HTML Pages Generator 시작 (Commit 3bbe342 기반)")
        print(f"📁 프로젝트 디렉토리: {self.project_dir}")
        
        success = True
        
        # 1. 슬라이드와 이미지 복사
        if not self.copy_slides_and_images():
            print("  ❌ 슬라이드 복사 실패")
            success = False
        
        # 2. 타임스탬프 포함 인덱스 생성
        self.generate_enhanced_index()
        
        # 3. 빌드 정보 생성
        self.generate_build_info()
        
        # 4. 결과 출력
        print("\n🎉 HTML Pages 생성 완료!")
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
    generator = HTMLPagesGenerator()
    generator.run()

