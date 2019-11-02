const mysqlx = require('@mysql/xdevapi')

const config = {
  password: 'root',
  user: 'test',
  host: 'localhost',
  port: 33060
  // schema: 'mySchema'
}
exports.test = () => {
  mysqlx
    .getSession(config)
    .then(session => {
      // console.log(session.inspect());
      session.sql('show databases')
        .execute(data => {
          console.log(data)
        })
        .then(() => {
          return session.close()
        })
        // { user: 'root', host: 'localhost', port: 33060 }
    })
    .catch(err => {
      // eslint-disable-next-line no-undef
      return session.close()
        .then(() => {
          throw err
        })
        .catch(err => {
          throw err
        })
    })
}
