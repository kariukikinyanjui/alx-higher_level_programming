# 0x14. JavaScript - Web scraping
`Scripting` `API` `JavaScript`

## Learning Objectives
* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module

## Requirements
* Allowed editors `vi` `vim` `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* Include a `README.md` file
* Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolon on top](https://github.com/standard/semistandard). Also reference: [AirBnB style](https://github.com/airbnb/javascript)
* Make your files executable `chmod u+x`
* Not allowed to use `var`

## More Info
### Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**Notes:** Request module has been deprecated since February 2020 - the team is considered alternative to replace this module - however, it's a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
