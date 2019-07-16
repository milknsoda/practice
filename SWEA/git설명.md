```bash
git init # 현재 폴더에 .git 폴더 생성. 이후에 git을 사용한 흔적이 다 들어가있음
git add a.txt # 커밋할 목록(INDEX, staging area)에 올림
git commit -m ' ' # 커밋할 목록(INDEX, staging area)에서 올림
git status # 현재 상태 확인
git log # 기록
vi a.txt # 문서 작업
git remote add origin https://github.com/milknsoda/gittest.git
git remote -v # 어떤 원격 저장소를 가졌는지 확인
git push -u origin master # 처음 올릴때
git push origin master # 그 이후에?
git clone # 올려져있는 파일들과 이력을 복사
git pull origin master # 올려져있는 파일 중에서 변경사항을 내려받음
```

Local (`git init`-> `(master)`)

WD(working directory) -> Staging area -> commit

작업공간						커밋대상파일목록	버전이력

