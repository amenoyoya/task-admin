const fs = require('fs')

/**
 * 指定パスがファイルか判定 
 */
const isFile = (path) => {
  try {
    return fs.statSync(path).isFile()
  } catch(err) {
    return false
  }
}

/**
 * タスクリスト取得: <= load from ./tasks.json
 */
const loadTasks = () => {
  if (!isFile('./tasks.json')) {
    return [[], [], [], []]
  }
  return JSON.parse(fs.readFileSync('./tasks.json', 'utf8'))
}

/**
 * タスクリスト保存: => save to ./tasks.json
 */
const saveTasks = (tasks) => {
  return fs.writeFileSync('./tasks.json', JSON.stringify(tasks, null, '  '))
}