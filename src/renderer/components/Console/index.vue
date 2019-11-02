<template>
  <div class="Console flex flex-col">
    <Consolebar />
    <console-content />
  </div>
</template>
<script>
import Consolebar from './Consolebar'
import ConsoleContent from './ConsoleContent'
export default {
  components: {
    Consolebar,
    ConsoleContent
  }
}
</script>
<style lang="scss" scoped>
.Console {
  background-color: #1D2129;
  width: 100%;
  // font-size: 1.65em;
  overflow: hidden;
  // flex: 1 1 auto;
  flex-basis: 200px;
}
</style>