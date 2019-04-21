const sum = arr => arr.reduce((x, y) => (x + y));

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

module.exports = {
  getRandomInt,
  sum,
};
