const inquirer = require('inquirer');

function getPlayerMove() {
  const questions = [
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

// async retrivePlayerMove f() {
//   const answer = await getPlayerMove()
//   return answer
// }

module.exports = {
  getPlayerMove,
};
