const { Deck } = require('./cards');
const { sum } = require('./utils');


class Character {
  constructor(money = 1000) {
    this.hand = [];
    this.money = money;
  }

  countCards() {
    const possibleValues = this.handToNumbers();
    const sumHands = [
      sum(possibleValues.map(x => x[0])),
      sum(possibleValues.map(x => x[1])),
    ];
    const under21 = sumHands.filter(x => x <= 21)[0];
    return under21 || sumHands.sort()[1];
  }

  handToNumbers() {
    return this.hand.map((card) => {
      if (['K', 'Q', 'J'].includes(card.rank)) {
        return [10, 10];
      } if (card.rank === 'A') {
        return [1, 11];
      }
      const num = Number(card.rank);
      return [num, num];
    });
  }

  // TODO: refactor
  seeHand(n = this.hand.length) {
    const selectedCards = this.hand.slice(0, n);
    const cardList = selectedCards.map(card => card.getImage(false));
    const cardLines = cardList[0].length;
    const multiCardList = [];
    for (let i = 0; i < cardLines; i++) {
      const multCardLine = cardList.map(x => x[i]).join(' ');
      multiCardList.push(multCardLine);
    }
    return multiCardList.join('\n');
  }
}


class Dealer extends Character {
  constructor() {
    super(1000000);
    this.deck = new Deck();
  }

  deal(player) {
    player.hand.push(this.deck.takeCard());
  }
}


module.exports = {
  Character,
  Dealer,
};
