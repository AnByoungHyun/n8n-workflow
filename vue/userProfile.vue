<template>
  <div v-if="user" class="profile-card">
    <h1>{{ user.name }}</h1>
    <p>{{ user.email }}</p>
  </div>
  <div v-else>
    <p>회원 정보를 불러오는 중입니다...</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: null,
    };
  },
  created() {
    // API 호출을 통해 사용자 정보를 비동기적으로 불러옴
    // 예시: 1초 후 데이터가 로드된다고 가정
    setTimeout(() => {
      this.user = {
        name: '홍길동',
        email: 'gildong@example.com',
      };
    }, 1000);
  },
};
</script>
