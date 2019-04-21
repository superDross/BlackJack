const inquirer = require('inquirer');

function getPlayerMove(min, max) {
  const questions = [
    {
      type: 'input',
      name: 'quantity',
      message: 'How much do you want to bet?',
      validate(value) {
        if (isNaN(parseFloat(value))) {
          return 'Please enter a number';
        } if (min > Number(value) || Number(value) > max) {
          return `$${value} is out of the betting range $${min} - $${max}`;
        }
        return true;
      },
      filter: Number,
    },
    {
      type: 'list',
      name: 'command',
      message: 'Your move.',
      choices: ['Stand', 'Hit'],
      when(answers) {
        return answers.comments !== 'Nope, all good!';
      },
    },
  ];

  return inquirer.prompt(questions).then(answers => answers);
}

// async function retrivePlayerMove() {
//   console.log('CARDS');
//   const answer = await getPlayerMove(10, 100);
//   return answer;
// }
// 
// retrivePlayerMove();

module.exports = {
  getPlayerMove,
};
