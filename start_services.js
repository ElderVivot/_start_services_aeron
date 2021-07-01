const { exec } = require('child_process')
const util = require('util')

const execAsync = util.promisify(exec)

async function start() {
    await execAsync(`pm2 start ecosystem.config.js`)
    await new Promise((resolve) => setTimeout(() => resolve(''), 5000))
}

start().then(_ => console.log(_))