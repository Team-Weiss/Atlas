<template>
  <div class="search flex flex-row">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9 9 9 0 0 1-9-9z"></path></svg>
    <input placeholder="Filter" />
  </div>
</template>

<style lang="scss" scoped>
.search {
  min-height: 4em;
  background: #FFFFFF;
  border-radius: 2px;
  border: 1px solid #E4E3E8;
  align-items: center;
  margin: 1em 0;

  svg {
    margin: 0 .5em 0 1em;
    height: 1.75em;
    fill: #707070;
  }

  input {
    min-height: calc(3em - 2px);
    width: 100%;
    border: none;
    &:focus {
      outline: none;
    }
  }
}
</style>