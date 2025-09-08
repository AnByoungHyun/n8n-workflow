# FastAPI + Alembic 프로젝트

이 프로젝트는 FastAPI와 Alembic을 사용한 데이터베이스 스키마 관리 시스템입니다. Alembic을 통해 안전하고 체계적인 데이터베이스 마이그레이션을 수행할 수 있습니다.

## 사전 요구사항 (Prerequisites)

프로젝트를 실행하기 전에 다음 소프트웨어가 설치되어 있어야 합니다.

  * **Python**: `3.8` 버전 이상을 권장합니다. 터미널에서 다음 명령어로 버전을 확인할 수 있습니다.
    ```bash
    python --version
    ```
  * **pip**: Python 패키지 관리자입니다. Python 3.4 이상 버전에는 기본적으로 포함되어 있습니다. 터미널에서 다음 명령어로 설치 여부 및 버전을 확인할 수 있습니다.
    ```bash
    pip --version
    ```

-----

## 설치 방법 (Installation)

1.  **프로젝트 저장소 복제 (Clone the repository):**
    먼저, Git을 사용하여 이 프로젝트 저장소를 로컬 컴퓨터로 복제합니다.

    ```bash
    git clone [저장소 URL]
    cd [프로젝트 폴더명]
    ```

2.  **(선택사항) 가상 환경 생성 및 활성화 (Create and activate a virtual environment):**
    프로젝트별로 독립된 개발 환경을 유지하기 위해 가상 환경 사용을 강력히 권장합니다.

    ```bash
    # 가상 환경 생성 (Windows)
    python -m venv venv

    # 가상 환경 활성화 (Windows)
    .\venv\Scripts\activate

    # 가상 환경 생성 (macOS/Linux)
    python3 -m venv venv

    # 가상 환경 활성화 (macOS/Linux)
    source venv/bin/activate
    ```

3.  **의존성 패키지 설치 (Install dependencies):**
    프로젝트에 필요한 모든 라이브러리와 패키지는 `requirements.txt` 파일에 명시되어 있습니다. 다음 명령어를 실행하여 한 번에 설치할 수 있습니다.

    ```bash
    pip install -r requirements.txt
    ```

    이제 프로젝트 실행에 필요한 모든 준비가 완료되었습니다. 🚀

-----

## 데이터베이스 마이그레이션 (Database Migration)

이 프로젝트는 Alembic을 사용하여 데이터베이스 스키마를 관리합니다.

### 초기 데이터베이스 설정

```bash
# 데이터베이스 마이그레이션 실행
alembic upgrade head
```

### 새로운 마이그레이션 생성

모델을 변경한 후에는 다음 명령어로 마이그레이션을 생성합니다:

```bash
# 자동으로 변경사항을 감지하여 마이그레이션 생성
alembic revision --autogenerate -m "설명"

# 마이그레이션 적용
alembic upgrade head
```

### 마이그레이션 히스토리 확인

```bash
# 현재 마이그레이션 상태 확인
alembic current

# 마이그레이션 히스토리 확인
alembic history
```

### 마이그레이션 롤백

```bash
# 이전 버전으로 롤백
alembic downgrade -1

# 특정 리비전으로 롤백
alembic downgrade <revision_id>
```

## 실행 방법 (Running the app)

의존성 패키지 설치가 완료되었다면, 다음 명령어를 터미널에 입력하여 애플리케이션을 실행할 수 있습니다.

```bash
# 데이터베이스 마이그레이션 먼저 실행
alembic upgrade head

# FastAPI 애플리케이션 실행
uvicorn app.main:app --reload
```

애플리케이션이 성공적으로 실행되면, 터미널에 `서버가 http://127.0.0.1:8000 에서 실행 중입니다.` 와 같은 메시지가 나타납니다. 웹 브라우저를 열고 해당 주소로 접속하여 애플리케이션을 확인할 수 있습니다.

-----

### 추가 정보 (Additional Information)

  * **코드 기여:** 프로젝트에 기여하고 싶다면, `CONTRIBUTING.md` 파일을 참고해주세요.
  * **문의:** 질문이나 문제가 발생하면 언제든지 [담당자 이름]에게 문의해주세요.
