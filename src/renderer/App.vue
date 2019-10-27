<template>
  <div class="container flex flex-col">
    <Titlebar />
    <div class="h-full flex flex-row">
      <Sidebar />
      <div class="main-content flex flex-col">
        <Editor />
        <console-bar />
      </div>
    </div>
  </div> 
</template>

<script>
import Sidebar from './components/Sidebar'
import Titlebar from './components/Titlebar'
import Editor from './components/Editor'
import ConsoleBar from './components/Console'

export default {
  components: {
    Sidebar,
    Titlebar,
    Editor,
    ConsoleBar
  }
}
</script>

<style lang="scss">
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
html {
  font-size: 10px;
}
.flex {
  display: flex;
}
.flex-row {
  flex-direction: row;
}
.flex-col {
  flex-direction: column;
}
.justify-center {
  justify-content: center;
}
.h-full {
  height: 100%;
}
.items-center {
  align-items: center;
}
</style>

<style lang="scss" scoped>
.container {
  height: 100vh;
  width: 100vw;
}

.main-content {
  flex: 1 1 auto;
  max-height: 100vh;
  background-color: #2e3440;

}
</style>