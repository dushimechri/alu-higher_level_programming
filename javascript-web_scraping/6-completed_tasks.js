#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const userTasks = {};
    tasks.forEach(task => {
      if (task.completed) {
	if (userTasks[task.userId]) {
	  userTasks[task.userId] += 1;
	} else {
	   userTasks[task.userId] = 1;
	}
      }
    });
    console.log(userTasks);
  }
});
