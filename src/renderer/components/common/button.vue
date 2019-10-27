<template>
  <div class="button flex flex-row">
    <slot></slot>
  </div>
</template>

<style lang="scss" scoped>
.button {
  min-height: 4em;
  background-color: #4347FE;
  align-items: center;
  justify-content: center;
  border-radius: 2px;
  cursor: pointer;
  transition: .1s ease-in-out;

  svg {
    height: 1.5em;
    fill: #FFF;
  }

  p {
    font-family: sans-serif;
    font-size: 1.3em;
    font-weight: 400;
    color: #FFF;
  }

  &:hover {
    background-color: rgba(67, 71, 254, 0.8);
  }
}
</style>