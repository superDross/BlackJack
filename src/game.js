const { Character, Dealer } = require('./player');
const { getPlayerMove } = require('./menu');


class BlackJack {
  constructor() {
    this.player = new Character();
    this.dealer = new Dealer();
    this.min = 10;
    this.max = Math.floor(this.min * 1.5);
    this.bet = 0;
  }

  clearHands() {
    this.dealer.hand = [];
    this.player.hand = [];
  }

  updateBetRange() {
    if (this.max < 500) {
      this.min *= 2;
      this.max *= 2;
    } else {
      this.min = 350;
      this.max = 500;
    }
  }

  dealCards(num = 1) {
    this.dealer.deal(this.dealer, num);
    this.dealer.deal(this.player, num);
  }

  async play() {
    const choices = await getPlayerMove();
    this.player.money -= choices.quantity;
    // if (choices.command)
  }
}
