<template>
  <div class="directory-explorer">
    <div v-for="(directory, index) in directories" :key="index">
      <directory-component :level="`level-1`" :type="directory.type" :pathname="directory.pathname" />
      <div class="children">
        <div v-for="(directory, index) in directory.directories" :key="index + directory.pathname">
          <directory-component :level="`level-2`" :type="directory.type" :pathname="directory.pathname" />
          <div class="children">
            <div v-for="(directory, index) in directory.directories" :key="index">
              <directory-component :level="`level-3`" :type="directory.type" :pathname="directory.pathname" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DirectoryComponent from './DirectoryComponent'
export default {
  components: {
    DirectoryComponent
  },
  data: () => {
    return {
      directories: [
        {
          pathname: 'Hakuten',
          type: 'host',
          directories: [
            {
              pathname: 'Accounts',
              type: 'schema',
              directories: [
                {
                  pathname: 'Login Accounts',
                  type: 'table'
                }
              ]
            }
          ]
        },
        {
          pathname: 'Heroku',
          type: 'host',
          directories: [
            {
              pathname: 'Accounts L4',
              type: 'schema',
              directories: [
                {
                  pathname: 'Login Accounts',
                  type: 'table'
                },
                {
                  pathname: 'Master Accounts',
                  type: 'table'
                }
              ]
            },
            {
              pathname: 'Accounts L3',
              type: 'schema',
              directories: [
                {
                  pathname: 'Login Accounts',
                  type: 'table'
                },
                {
                  pathname: 'Admin Accounts',
                  type: 'table'
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.directory-explorer {
  width: 100%;
  height: 100%;
  background: #FFF;
  border-radius: 2px;
  border: 1px solid #E4E3E8;
  overflow-y: scroll;
}

.children {
  display: none;
}

.active {
  display: flex;
  background-color: #F0F1FC;
  flex-direction: column;
}

</style>