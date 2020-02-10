# task-admin

タスク管理アプリ

![screenshot1.png](./screenshot1.gif)

![screenshot2.png](./screenshot2.gif)

- Electron:
    - Local GUI application libarary for Node.js

***

## Environment

- OS:
    - Windows 10
    - Ubuntu 18.04
- Applications:
    - Node.js: `12.14.1`
        - yarn package manager: `1.21.1`

### Setup
```bash
# install node modules
$ yarn install

# global install: electron
$ yarn global add electron-prebuilt

# PATHが通っていないなら通しておく
## `yarn global bin` で表示されるPATHを通す

# start electron application
$ electron main.js
```
