# 기여 가이드라인

한글학교 선생님을 위한 크롬 웹브라우저 활용 교육 자료에 기여해 주셔서 감사합니다! 이 문서는 프로젝트에 기여하는 방법을 안내합니다.

## 🤝 기여 방법

### 1. 이슈 제기
- 버그 발견 시 [Issues](https://github.com/linuxsw/chrome_lecture_for_korean_teacher/issues)에서 신고
- 새로운 기능 제안
- 교육 자료 개선 사항 제안

### 2. Pull Request
1. 저장소 Fork
2. 새 브랜치 생성 (`git checkout -b feature/amazing-feature`)
3. 변경 사항 커밋 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 푸시 (`git push origin feature/amazing-feature`)
5. Pull Request 생성

### 3. 교육 자료 개선
- 슬라이드 내용 개선
- 워크북 실습 시나리오 추가
- 새로운 도구 및 확장프로그램 소개

## 📝 코딩 스타일

### HTML/CSS
- 들여쓰기: 2 spaces
- 한글 폰트: Noto Sans KR 사용
- 반응형 디자인 고려
- 접근성 고려 (alt 텍스트, semantic HTML)

### Python
- PEP 8 스타일 가이드 준수
- 함수 및 클래스에 docstring 작성
- 타입 힌트 사용 권장

### Bash
- 에러 처리 (`set -e`)
- 명확한 변수명 사용
- 주석으로 각 단계 설명

## 🧪 테스트

### 로컬 테스트
```bash
# 자료 생성 테스트
bash scripts/generate_materials.sh

# Python 스크립트 테스트
python scripts/generate_slides.py

# 결과물 확인
open output/index.html
```

### 자동화 테스트
- GitHub Actions가 자동으로 빌드 테스트 실행
- Pull Request 시 자동 검증

## 📋 체크리스트

Pull Request 제출 전 확인사항:

- [ ] 로컬에서 정상 빌드 확인
- [ ] 새로운 파일의 한글 인코딩 확인 (UTF-8)
- [ ] 반응형 디자인 테스트 (모바일/데스크톱)
- [ ] 브라우저 호환성 확인
- [ ] 문서 업데이트 (필요시)

## 🎯 우선순위 기여 영역

1. **교육 내용 개선**
   - 최신 크롬 기능 반영
   - 새로운 교육용 확장프로그램 추가
   - 실습 시나리오 다양화

2. **사용성 개선**
   - 모바일 최적화
   - 접근성 향상
   - 로딩 속도 개선

3. **국제화**
   - 영어 버전 제작
   - 다른 언어 지원

## 💬 소통

- **GitHub Discussions**: 일반적인 질문 및 토론
- **GitHub Issues**: 구체적인 문제 신고
- **Email**: linuxsw@gmail.com (긴급한 사항)

## 🏆 기여자 인정

모든 기여자는 README.md의 기여자 섹션에 추가됩니다.

감사합니다! 🙏

