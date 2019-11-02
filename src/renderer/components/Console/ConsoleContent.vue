<template>
  <div class="ConsoleContent flex flex-col">
      <p>Lorem Ipsum is simply dummy text of the printing and <span class="success">Success</span> typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
      <p>Lorem Ipsum is simply dummy <span class="info">Some information</span> text of the printing and <span class="error">Error</span> typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.ConsoleContent {
  background-color: #1D2129;
  height: 4em;
  flex: 1;
  padding: 0 1em;
//   border-top: 1px solid #191A25;
  overflow-y: scroll;
  color: aliceblue;
  font-size: 1.5rem;
  .success {
      color: rgb(47, 255, 82);
  }
  .info {
      color: rgb(255, 241, 47);
  }
  .error {
      color: rgb(180, 12, 12);
  }
  
}
</style>