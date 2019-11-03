<template>
  <div class="editor flex flex-col">
    <tabs
      :tabsData="tabsData"
      :selected="selected"
      @closeTab="removeTab"
      @switchTab="switchTab"
      @newTab="newTab"
    />
    <codemirror v-if="renderEditor" v-model="tabsData[selected].code" :options="cmOptions"></codemirror>
    <help v-else />
  </div>
</template>

<script>
import tabs from './tabs'
import help from './Help'
import { codemirror } from 'vue-codemirror'
// import mysql from '@/databases/mysql'

// Language
import 'codemirror/mode/sql/sql'

// Style
import 'codemirror/lib/codemirror.css'

// Theme
import 'codemirror/theme/nord.css'

// KeyMaps
import 'codemirror/mode/clike/clike.js'
import 'codemirror/addon/edit/matchbrackets.js'
import 'codemirror/addon/comment/comment.js'
import 'codemirror/addon/dialog/dialog.js'
import 'codemirror/addon/dialog/dialog.css'
import 'codemirror/addon/search/searchcursor.js'
import 'codemirror/addon/search/search.js'
import 'codemirror/keymap/sublime.js'

export default {
  components: {
    codemirror,
    tabs,
    help
  },
  data () {
    return {
      selected: 0,
      tabsData: [
        {
          filename: 'App.sql',
          code: 'select * from table;'
        }
      ],
      renderEditor: false,
      cmOptions: {
        tabSize: 4,
        autofocus: true,
        styleActiveLine: true,
        lineNumbers: true,
        lineWrapping: true,
        foldGutter: true,
        styleSelectedText: true,
        mode: 'text/x-sql',
        theme: 'nord',
        keyMap: 'sublime',
        matchBrackets: true,
        showCursorWhenSelecting: true,
        extraKeys: { 'Ctrl': 'autocomplete' },
        hintOptions: {
          completeSingle: true
        }
      }
    }
  },
  methods: {
    newTab () {
      this.tabsData.push({
        filename: 'Untitled.sql',
        code: ''
      })
    },
    switchTab (tabIndex) {
      this.selected = tabIndex
    },
    removeTab (tabIndex) {
      if (this.selected === tabIndex) {
        this.selected = (tabIndex - 1) > 0 ? tabIndex - 1 : 0
      }
      if (this.tabsData.length === 0) {
        this.renderEditor = false
      }
      this.tabsData.splice(tabIndex, 1)
    }
  },
  watch: {
    tabsData: function (n, o) {
      if (n.length > 0 && !this.renderEditor) {
        this.selected = n.length - 1
        this.renderEditor = true
      } else if (n.length === 0) {
        this.selected = 0
        this.renderEditor = false
      }
    }
  },
  mounted () {
    const vm = this
    if (this.tabsData.length > 0) {
      this.selected = 0
      this.renderEditor = true
    }
    document.addEventListener('keyup', function (event) {
      if (event.ctrlKey && (event.key === 'n' || event.key === 'N')) {
        event.preventDefault()
        vm.tabsData.push({
          filename: 'Untitled.sql',
          code: ''
        })
      }
      if (event.ctrlKey && event.shiftKey && event.key === 'Enter') {
        event.preventDefault()
        console.log(vm.tabsData[vm.selected].code.trim())
        // mysql.test()
      }
    })
  }
}
</script>

<style lang="scss">
.editor {
  width: 100%;
  font-size: 1.65em;
  overflow-y: scroll;
  flex: 1 1 auto;
}

.CodeMirror {
  height: auto;
}
</style>