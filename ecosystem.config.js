module.exports = {
  apps : [
    {
      name: 'bay-extracts-node',
      cwd: 'C:\\iacon\\baymax-extracts-node',
      script: 'dist\\schedules\\server.js',
      cron_restart: "1 0 * * *",
      min_uptime: 5000,
	    max_restarts: 3,
	    restart_delay: 4000
    },
    {
      name: 'iacon-rest-api-pg',
      cwd: 'C:\\iacon\\iacon-rest-api-pg',
      script: 'dist\\server.js',
      cron_restart: "1 0 * * *",
      min_uptime: 5000,
	    max_restarts: 3,
	    restart_delay: 4000
    },
    {
      name: 'webscraping-nfe-go-s',
      cwd: 'C:\\iacon\\webscraping-nfe-nfce-go',
      script: 'dist\\schedules\\server.js',
      cron_restart: "1 0 * * *",
      min_uptime: 5000,
	    max_restarts: 3,
	    restart_delay: 4000
    },
    {
      name: 'webscraping-nfe-go-q',
      cwd: 'C:\\iacon\\webscraping-nfe-nfce-go',
      script: 'dist\\queues\\queue.js',
      cron_restart: "0 */1 * * *",
      min_uptime: 5000,
	    max_restarts: 3,
	    restart_delay: 4000
    },
    {
      name: 'webscraping-gyn-go-s',
      cwd: 'C:\\iacon\\webscraping-nfse-goiania',
      script: 'dist\\schedules\\server.js',
      cron_restart: "1 0 * * *",
      min_uptime: 5000,
	    max_restarts: 3,
	    restart_delay: 4000
    },
    {
      name: 'webscraping-gyn-go-q',
      cwd: 'C:\\iacon\\webscraping-nfse-goiania',
      script: 'dist\\queues\\queue.js',
      cron_restart: "1 0 * * *",
      min_uptime: 5000,
	    max_restarts: 3,
	    restart_delay: 4000
    }
  ],

  deploy : {
    production : {
      user : 'SSH_USERNAME',
      host : 'SSH_HOSTMACHINE',
      ref  : 'origin/master',
      repo : 'GIT_REPOSITORY',
      path : 'DESTINATION_PATH',
      'pre-deploy-local': '',
      'post-deploy' : 'npm install && pm2 reload ecosystem.config.js --env production',
      'pre-setup': ''
    }
  }
};
