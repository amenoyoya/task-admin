const fs = require('fs');

const isFile = (path) => {
  try {
    return fs.statSync(path).isFile();
  } catch(err) {
    return false;
  }
}

/**
 * タスクリスト取得
 */
const loadTasks = () => {
  if (!isFile('./tasks.json')) {
    return [[], [], [], []];
  }
  return JSON.parse(fs.readFileSync('./tasks.json', 'utf8'));
}

/**
 * タスクリスト保存
 */
const saveTasks = (tasks) => {
  return fs.writeFile('./tasks.json', JSON.stringify(tasks));
}
