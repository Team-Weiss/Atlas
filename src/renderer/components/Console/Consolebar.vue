<template>
  <div class="Consolebar flex flex-row items-center">
      <div class="flex flex-row items-center quick-access">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M26 4.01H6a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2v-20a2 2 0 0 0-2-2zm0 2v4H6v-4zm-20 20v-14h20v14z"></path><path d="M10.76 16.18l2.82 2.83-2.82 2.83 1.41 1.41 4.24-4.24-4.24-4.24-1.41 1.41z"></path></svg>
      <p>Terminal</p>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 2C8.2 2 2 8.2 2 16s6.2 14 14 14 14-6.2 14-14S23.8 2 16 2zm0 26C9.4 28 4 22.6 4 16S9.4 4 16 4s12 5.4 12 12-5.4 12-12 12z"></path><path d="M21.4 23L16 17.6 10.6 23 9 21.4l5.4-5.4L9 10.6 10.6 9l5.4 5.4L21.4 9l1.6 1.6-5.4 5.4 5.4 5.4z"></path></svg>
      <p>0</p>
      <!-- <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M2 16A14 14 0 1 0 16 2 14 14 0 0 0 2 16zm23.15 7.75L8.25 6.85a12 12 0 0 1 16.9 16.9zM8.24 25.16a12 12 0 0 1-1.4-16.89l16.89 16.89a12 12 0 0 1-15.49 0z"></path></svg> -->
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12 12 12 0 0 1-12 12z"></path><path d="M15 8h2v11h-2zm1 14a1.5 1.5 0 1 0 1.5 1.5A1.5 1.5 0 0 0 16 22z"></path></svg>
      <p>0</p>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.Consolebar {
  background-color: #1D2129;
  height: 4em;
  padding: 0 1em;
  border-top: 1px solid #191A25;

  .quick-access {
    padding: .25em .5em;
    cursor: pointer;
    border-radius: 25px;
    transition: .3s ease-in-out;
    padding-right: 1.35em;

    svg {
      height: 1.5em;
      fill: #787980;
    }

    p {
      font-size: 1.25em;
      color: #787980;
      font-family: sans-serif;
    }

    &:hover {
      background-color: #2e3440;
    }
  }
}
</style>