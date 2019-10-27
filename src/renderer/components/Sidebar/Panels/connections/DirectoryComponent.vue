<template>
  <div ref="currentDirectoryComponent" @click="doubleclick" :class="`directory-component flex flex-row ${level}`">
    <svg v-if="level != 'level-1'" class="corner" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22"><path d="M28,9H14V6H6v8H9V28h2V14h3V11H28ZM12,12H8V8h4Z" transform="translate(-6 28) rotate(-90)"/></svg>
    <svg v-if="type == 'host'" focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M11.61 29.92a1 1 0 0 1-.6-1.07L12.83 17H8a1 1 0 0 1-1-1.23l3-13A1 1 0 0 1 11 2h10a1 1 0 0 1 .78.37 1 1 0 0 1 .2.85L20.25 11H25a1 1 0 0 1 .9.56 1 1 0 0 1-.11 1l-13 17A1 1 0 0 1 12 30a1.09 1.09 0 0 1-.39-.08zM17.75 13l2-9H11.8L9.26 15h5.91l-1.59 10.28L23 13z"></path></svg>
    <svg v-else-if="type == 'schema'" focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M8 30H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2zm-4-6v4h4v-4zm14 6h-4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2zm-4-6v4h4v-4zm14 6h-4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2zm-4-6v4h4v-4zm4-4H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h24a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2zM4 4v14h24V4z"></path></svg>
    <svg v-else-if="type == 'table'" focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M29 5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v22a2 2 0 0 0 2 2h22a2 2 0 0 0 2-2zm-2 0v4H5V5zm0 22H5v-4h22zm0-6H5v-4h22zm0-6H5v-4h22z"></path></svg>
    <p>{{ pathname }}</p>
  </div>
</template>

<script>
export default {
  props: ['type', 'pathname', 'level'],
  methods: {
    toggleChildren: function () {
      const el = this.$refs.currentDirectoryComponent.parentNode.querySelector('.children')
      if (el != null) {
        el.classList.toggle('active')
        console.log('Toggle Children')
      } else {
        this.expandObject()
      }
    },
    expandObject: () => console.log('Expand Object'),
    doubleclick: function (el, ondouble) {
      if (el.srcElement.getAttribute('data-dblclick') === null) {
        el.srcElement.setAttribute('data-dblclick', 1)
        const vm = this
        setTimeout(function () {
          if (el.srcElement.getAttribute('data-dblclick') === '1') {
            vm.toggleChildren()
          }
          el.srcElement.removeAttribute('data-dblclick')
        }, 200)
      } else {
        el.srcElement.removeAttribute('data-dblclick')
        this.expandObject()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.directory-component {
  padding: .5em 1em;
  height: 3em;
  align-items: center;
  position: relative;
  cursor: pointer;
  user-select: none;

  svg {
    height: 1.8em;
  }
  
  p {
    font-size: 1.5em;
    font-family: sans-serif;
  }

  &:hover {
    background: #E0E2F3;
    // border-bottom: 1px solid rgba(36,36,36,.3);
  }
}

.level-1 {
  // background: #eee;
}
.level-2 {
  padding-left: 4em;
  
  .corner {
    position: absolute;
    top: .25em;
    left: 2.25em;
    height: 1.5em;
  }
}
.level-3 {
  padding-left: 6em;
  
  .branch {
    position: absolute;
    top: .25em;
    left: 2.25em;
    height: 1.5em;
  }

  .corner {
    position: absolute;
    top: .25em;
    left: 4.25em;
    height: 1.5em;
  }
}
</style>