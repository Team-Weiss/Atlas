<template>
  <div class="Panel flex flex-col conncetions">
    <span class="panel-header">Connection Directory</span>
    <Button>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M11.61 29.92a1 1 0 0 1-.6-1.07L12.83 17H8a1 1 0 0 1-1-1.23l3-13A1 1 0 0 1 11 2h10a1 1 0 0 1 .78.37 1 1 0 0 1 .2.85L20.25 11H25a1 1 0 0 1 .9.56 1 1 0 0 1-.11 1l-13 17A1 1 0 0 1 12 30a1.09 1.09 0 0 1-.39-.08z"></path></svg>
      <p>New Connection</p>
    </Button>
    <section-header>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M20.59 22L15 16.41V7h2v8.58l5 5.01L20.59 22z"></path><path d="M16 2A13.94 13.94 0 0 0 6 6.23V2H4v8h8V8H7.08A12 12 0 1 1 4 16H2A14 14 0 1 0 16 2z"></path></svg>
      <p>Recent Connections</p>
    </section-header>
    <span class="flex flex-row metadata">
      <span><p>{{ metadata.dbs }}</p> Databases</span>
      <div class="vr"></div>
      <!-- <span><p>{{ metadata.schemas }}</p> Schemas</span> -->
      <span><p>{{ metadata.connections }}</p> Connections</span>
      <div class="vr"></div>
      <span class="refresh">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M12 10H6.78A11 11 0 0 1 27 16h2A13 13 0 0 0 6 7.68V4H4v8h8zm8 12h5.22A11 11 0 0 1 5 16H3a13 13 0 0 0 23 8.32V28h2v-8h-8z"></path></svg>
      </span>
    </span>
    <Search/>
    <directory-explorer />
  </div>
</template>

<script>
import Button from '../../../common/button'
import SectionHeader from '../../../common/sectionHeader'
import Search from './Search'
import DirectoryExplorer from './DirectoryExplorer'

export default {
  components: {
    Button,
    SectionHeader,
    Search,
    DirectoryExplorer
  },
  data () {
    return {
      metadata: {
        dbs: 3,
        schemas: 3,
        connections: 2
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.conncetions {
  padding: 3em 2em;
}

.panel-header {
  font-size: 1.5em;
  font-family: sans-serif;
  color: #22243E;
  margin-bottom: 1.5em;
  font-weight: 700;
}

.metadata {
  padding: 1em 0;
  align-items: center;

  span {
    display: flex;
    flex-direction: row;
    justify-content: center;
    text-align: center;
    flex: 1 1 auto;
    font-family: sans-serif;
    font-size: 1.4em;

    p {
      font-weight: 700;
      margin-right: .25em;
    }
  }

  .vr {
    width: 1px;
    height: 1.5em;
    background-color: #22243E;
  }

  .refresh {
    svg {
      cursor: pointer;
      height: 1em;
    }
  }
}
</style>