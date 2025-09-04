<template>
  <div class="profile-card">
    <h1>{{ user.name }}</h1>
    <p>{{ user.email }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: null, // 초기 상태가 null
    };
  },
  created() {
    // API를 통해 사용자 정보를 비동기적으로 불러옴
    fetchUserData().then(data => {
      this.user = data;
    });
  },
};
</script>
