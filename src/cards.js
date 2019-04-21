const { getRandomInt } = require('./utils.js');

class Card {
  constructor(suit, rank) {
    this.suit = suit;
    this.rank = rank;
  }

  getImage(str = true) {
    const image = [
      '┌─────────┐',
      `│${this.rank}        │`,
      '│         │',
      '│         │',
      `│    ${this.suit}    │`,
      '│         │',
      '│         │',
      `│        ${this.rank}│`,
      '└─────────┘',
    ];
    if (str) {
      return image.join('');
    }
    return image;
  }
}


class Deck {
  constructor() {
    this.cards = this.generateAllCards();
  }

  generateAllCards() {
    const suits = ['♥', '♠', '♣', '♦'];
    const ranks = [
      'A', '2', '3', '4', '5', '6',
      '7', '8', '9', '10', 'J', 'Q', 'K',
    ];
    const allCards = [];
    suits.forEach((suit) => {
      ranks.forEach((rank) => {
        allCards.push(new Card(suit, rank));
      });
    });
    return allCards;
  }

  takeCard() {
    const i = getRandomInt(this.cards.length);
    const card = this.cards[i];
    this.cards.splice(i, 1);
    return card;
  }

  checkCardCount() {
    if (this.cards.length < 5) {
      this.cards = this.generateAllCards;
    }
  }
}


module.exports = {
  Deck,
};
