const { all } = require('./2018-9');

// Examples
let ex=[`9 players; last marble is worth 25 points`,
        `10 players; last marble is worth 1618 points`,
        `13 players; last marble is worth 7999 points`];
ex.forEach(e => console.log(all(e)));


// Real input
let input=`459 players; last marble is worth 71790 points`;

console.log(all(input));
