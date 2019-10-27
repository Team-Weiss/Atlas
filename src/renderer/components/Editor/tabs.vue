<template>
  <div class="flex flex-row tabs">
    <span 
      v-for="(tab, index) in tabsData" :key="index"
      :class="{'active': selected == index}" 
      class="tab flex flex-row"
      @click="$emit('switchTab', index)"
    >
      <span class="flex flex-row items-center">
        <img src="../../assets/icons/extensions/sql.svg" />
        <p>{{ tab.filename }}</p>
      </span>
      <svg @click="$emit('closeTab', index)" focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4l6.6 6.6L8 22.6 9.4 24l6.6-6.6 6.6 6.6 1.4-1.4-6.6-6.6L24 9.4z"></path></svg>
    </span>
    <span class="new-tab" @click="$emit('newTab')">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M17 15V7h-2v8H7v2h8v8h2v-8h8v-2h-8z"></path></svg>
    </span>
  </div>
</template>

<script>
export default {
  props: ['tabsData', 'selected']
}
</script>

<style lang="scss" scoped>
.tabs {
  width: 100%;
  height: 3em;
  color: #747681;
  background-color: #2B2F37;
}

.tab {
  min-width: 15em;
  padding: .5em 0;
  align-items: center;
  user-select: none;
  justify-content: space-between;
  cursor: pointer;

  img {
    height: 1.25em;
    margin-left: .75em;
  }

  p {
    font-family: sans-serif;
    margin-left: .75em;
    font-size: .85em;
  }

  svg {
    margin-left: .75em;
    fill: #FFF;
    height: 1.15em;
    opacity: 0;
  }

  &:hover {
    background-color: #3b4252;
    
    svg {
      opacity: 1;
    }
  }
}

.new-tab {
  width: 3em;;
  background-color: #2B2F37;
  position: relative;
  user-select: none;
  cursor: pointer;

  svg {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    margin: auto;
    fill: #747681;
    height: 1.25em;
  }
  
  &:hover {
    background: #3b4252;

    svg {
      fill: #FFF;
    }
  }
}

.active {
  background: #2e3440;
  color: #ddd;
}
</style>