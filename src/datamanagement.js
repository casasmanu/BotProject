/* functions to load the users info and to add-storage new users
*/

const fs = require("fs");
const todos = [{ user: "user1" }, { user: "user2" }, { user: "user3" }];
console.log(todos);
const myJSON = JSON.stringify(todos);

fs.writeFile("info.txt", myJSON, "utf-8", (err) => {
  console.log("File created");
});

console.log(todos[0]);
