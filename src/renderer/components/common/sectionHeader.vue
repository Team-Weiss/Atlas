<template>
  <div class="section-header flex flex-row">
    <slot></slot>
  </div>
</template>

<style lang="scss" scoped>
.section-header {
  margin: 2em 0 1em 0;
  align-items: center;

  svg {
    height: 1.5em;
    width: 2em;
    fill: #707070;
    margin-right: .5em;
  }

  p {
    font-family: sans-serif;
    font-size: 1.3em;
    font-weight: 400;
    color: #707070;
  }
}
</style>