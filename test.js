var path = require('path');
let json = require(path.join(process.cwd(), 'credentials.json'));
var username = json['username'];
var password = json['password'];
process.stdout.write('Local username env var:\t' + process.env.USER + '\n');
process.stdout.write('Local password env var:\t' + process.env.PASSWORD + '\n');
console.log('Var username from json:\t' + username + '\n');
console.log('Var password from json:\t' + password);
