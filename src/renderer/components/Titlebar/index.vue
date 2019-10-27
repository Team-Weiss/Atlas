<template>
  <div class="titlebar flex flex-row">
    <p @click="menu">ATLAS</p>
    <span class="fileinfo">index.sql - Atlas - Atlas</span>
    <span class="title-bar-buttons flex flex-row">
      <span class="title-bar-button minimize" @click="minimize">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M7 15h18v2H7z"></path></svg>
      </span>
      <span class="title-bar-button scale" @click="minmax" >
        <svg v-if="scaled" xmlns="http://www.w3.org/2000/svg" width="11.67" height="11.67" viewBox="0 0 11.67 11.67">
          <path id="Path_22" data-name="Path 22" d="M11.253,0H.417A.417.417,0,0,0,0,.417V11.253a.417.417,0,0,0,.417.417H11.253a.417.417,0,0,0,.417-.417V.417A.417.417,0,0,0,11.253,0Zm-.417,10.836h-10v-10h10v10Z"/>
        </svg>
        <svg v-else id="Group_22" data-name="Group 22" xmlns="http://www.w3.org/2000/svg" width="11.866" height="11.866" viewBox="0 0 11.866 11.866">
          <path id="Path_23" data-name="Path 23" d="M51.371,0H41.654a.242.242,0,0,0-.241.241v.7a.241.241,0,0,0,.483,0V.483h9.233V9.716h-.459a.241.241,0,1,0,0,.483h.7a.242.242,0,0,0,.241-.241V.241A.242.242,0,0,0,51.371,0Z" transform="translate(-39.746)"/>
          <path id="Path_24" data-name="Path 24" d="M9.958,41.413H.241A.242.242,0,0,0,0,41.654v9.716a.242.242,0,0,0,.241.241H9.958a.242.242,0,0,0,.241-.241V41.654A.242.242,0,0,0,9.958,41.413Zm-.241,9.716H.483V41.9H9.716Z" transform="translate(0 -39.746)"/>
        </svg>
      </span>
      <span class="title-bar-button close" @click="close">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4l6.6 6.6L8 22.6 9.4 24l6.6-6.6 6.6 6.6 1.4-1.4-6.6-6.6L24 9.4z"></path></svg>
      </span>
    </span>
  </div>
</template>

<script>
import { remote, ipcRenderer } from 'electron'

export default {
  data () {
    return {
      scaled: false
    }
  },
  methods: {
    menu: () => ipcRenderer.send('display-app-menu', {
      x: event.x,
      y: event.y
    }),
    minimize: () => remote.getCurrentWindow().minimize(),
    minmax: function () {
      this.scaled = !this.scaled
      const currentWindow = remote.getCurrentWindow()
      if (currentWindow.isMaximized()) currentWindow.unmaximize()
      else currentWindow.maximize()
    },
    close: () => remote.app.quit()
  }
}
</script>

<style lang="scss" scoped>
.titlebar {
  -webkit-app-region: drag;
  --dimesion: 3.5em;
  height: var(--dimesion);
  background-color: #E0E2F3;
  justify-content: space-between;
  
  .fileinfo {
    font-family: sans-serif;
    font-size: 1.2em;
    color: #707070;
    margin: auto 0;
    padding: 0 1em;
  }

  .title-bar-buttons {
    -webkit-app-region: no-drag;
    height: var(--dimesion);
  }

  .title-bar-button {
    position: relative;
    max-height: calc(var(--dimesion) - 1.5px);
    width: calc(var(--dimesion) * 1.35);
    
    svg {
      height: 2em;
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      margin: auto;
      fill: #B4B6C3;
    }
  }

  .close {
    &:hover {
      background-color: #e53935;

      svg {
        fill: #FFF;
      }
    }
  }

  .minimize {
    &:hover {
      background-color: #EEEFF8;
      svg {
        fill: #2B2F37;
      }
    }
  }

  .scale {
    & {
      svg {
        stroke: none;
      }
    }

    &:hover {
      background-color: #EEEFF8;
      svg {
        // stroke: #2B2F37;
        fill: #2B2F37;
      }
    }
  }

  p {
    letter-spacing: 1px;
    font-weight: 700;
    font-family: sans-serif;
    text-transform: uppercase;
    font-size: 1.2em;
    color: #707070;
    margin: auto 0;
    padding: 0 1em;
  }
}
</style>