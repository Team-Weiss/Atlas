<template>
  <div class="alert">
    <div class="row" style="align-items: center;">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform; fill: #FFF; height: 2em;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M17 22v-9h-4v2h2v7h-3v2h8v-2h-3zM16 7a1.5 1.5 0 1 0 1.5 1.5A1.5 1.5 0 0 0 16 7z"></path><path d="M16 30a14 14 0 1 1 14-14 14 14 0 0 1-14 14zm0-26a12 12 0 1 0 12 12A12 12 0 0 0 16 4z"></path><title>Information</title></svg>
      <p style="font-size: 1.8em; margin-left: .5em;">Are you sure you want to proceed with this action</p>
    </div>
    <span class="row">
      <span class="cancel buttons" @click="$emit('cancel')">cancel</span>
      <span class="accept buttons" @click="$emit('accept')">accept</span>
    </span>
  </div>
</template>

<style lang="scss" scoped>
.alert {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  position: fixed;
  z-index: 1;
  height: min-content;
  width: max-content;
  color: #FFF;
  background-color: #131b22;

  div {
    margin: 2em;
  }
}

.buttons {
  width: 50%;
  text-align: center;
  padding: .5em 0;
  font-size: 2em;
  text-transform: capitalize;
  font-weight: 100;
  cursor: pointer;
  
  &:hover {
    filter: brightness(.9);
  }
}

.cancel {
  background-color: #0e98f4;
}
.accept {
  background: #fe4863;
}
</style>