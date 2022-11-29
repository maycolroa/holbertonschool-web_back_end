const express = require('express');

const app = express()
const PORT = process.env.PORT || 1245

app.get("/", (req, res) => {
  res.send("Hello Holberton School!")
})
app.listen(PORT, () => {
  console.log("server runing on port: ", PORT)
})
