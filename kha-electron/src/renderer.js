const $ = selector => document.querySelector(selector)

const sqlite = require('sqlite3').verbose()
const db = new sqlite.Database('src/db/kha.db', sqlite.OPEN_READWRITE, (err) => {
  if (err) return console.error(err)
})