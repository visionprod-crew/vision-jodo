# VISION 촬영 조감도 메이커

교회 영상 크루(VISION Production & Film Crew)용 촬영 조감도 + 장비 리스트 웹앱.
GitHub Pages로 배포: https://janyuck.github.io/vision-jodo/

## 파일 구조
- `src/app.html` — 원본 소스 (단일 HTML, CSS/JS 포함). 로고 자리는 `__LOGO__` 플레이스홀더.
- `src/logo.png` — 기본 워터마크/상단 로고 (VISION 오렌지 로고)
- `src/build.py` — `src/app.html` → `index.html` 빌드 (로고 base64 삽입 + PWA 태그 추가)
- `index.html` — 배포되는 결과물 (직접 수정하지 말 것, 항상 빌드로 생성)
- `manifest.webmanifest`, `icon-*.png` — 홈 화면에 추가(PWA)용
- `.nojekyll` — GitHub Pages의 Jekyll 처리 끄기

## 업데이트 절차 (사용자가 기능 수정/추가를 요청하면 항상 이 순서로)
1. `src/app.html` 수정
2. `python3 src/build.py` 실행
3. 헤드리스 크롬(playwright)으로 페이지 오류가 없는지 확인 — 데스크톱과 모바일 뷰포트 둘 다
4. `main` 브랜치에 커밋 후 푸시 → GitHub Pages가 1~2분 안에 자동 배포
5. 사용자에게 무엇이 바뀌었는지 한국어로 짧게 알리기

사용자는 업데이트가 GitHub에 자동으로 반영되기를 원함 — 별도 확인 없이 main에 바로 푸시해도 됨.

## 참고
- 사용자와의 대화는 한국어로.
- 데이터(조감도·장비 리스트)는 각 기기 브라우저 localStorage + 저장(.json) 파일로만 보관. 서버 없음.
- 조감도 장비 목록 ↔ 장비 리스트(엑셀형) ↔ 평면도 카메라 라벨이 서로 연동됨.
- 단축키는 조감도=일러스트레이터, 장비 리스트=엑셀 기준.

## 계정 · 클라우드 저장 (Firebase)
- `firebase-config.js` — Firebase 웹 설정. `null`이면 로그인 기능이 숨겨지고 기기 저장 모드로만 동작.
- `firestore.rules` — Firestore 보안 규칙 (Firebase 콘솔 → Firestore → 규칙에 붙여넣기). 관리자 = 이름 `admin`.
- 이름+비밀번호 로그인은 Firebase Auth 이메일/비밀번호를 사용: 이름을 UTF-8 hex로 바꿔 `u<hex>@vision-jodo.app` 이메일로 씀.
- 데이터: `users/{uid}` (이름·가입일·차단 여부), `users/{uid}/docs/{id}` (조감도 JSON), `users/{uid}/assets/{id}` (평면도 사진, 1MB 이하로 자동 압축).
- 빌드 후에는 `node --check`로 스크립트 문법 검사도 할 것.
