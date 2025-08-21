from fastapi import APIRouter
from app.domains.users.router import router as users_router

api_router = APIRouter()

# "/users" 접두사와 "users" 태그와 함께 users_router를 포함시킵니다.
api_router.include_router(users_router, prefix="/users", tags=["users"])

# --- 예시: 새로운 "posts" 기능이 추가된다면 ---
# from app.domains.posts.router import router as posts_router
# api_router.include_router(posts_router, prefix="/posts", tags=["posts"])
