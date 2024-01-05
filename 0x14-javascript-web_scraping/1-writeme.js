#!/usr/bin/node
const fs = require("fs")
console.log(process.argv[0], "\n\r", process.argv[1])
fs.writeFileSync(process.argv[2], process.argv[3], error=>{
    if (error) {
        console.log(error)
    }
});
