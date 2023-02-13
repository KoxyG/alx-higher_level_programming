#!/usr/bin/node

// A scripts that computes the number of tasks completed by user id
// Only prints users with completed task
// must use the request module

const require = request('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode == 200) {
    const taskComplete = {};
    const tasks = JSON.parse(body);
    if (task.completed) {
      if (!tasksComplete[todo.userId]) {
        tasksComplete[tasks.userId] = 1;
      } else {
        tasksComplete[tasks.userId] += 1;
      }
    }
  });
  console.log(tasksComplete);
});
