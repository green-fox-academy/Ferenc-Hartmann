'use strict'

var PokerFace = (function() {

  function init(firstList, secondList) {
    transformer(firstList, PokerFace.leftHand);
    transformer(secondList, PokerFace.rightHand);
    PokerFace.leftHandValue = straightFlush(PokerFace.leftHand);
    PokerFace.rightHandValue = straightFlush(PokerFace.rightHand);
    console.log(PokerFace.leftHandValue);
    console.log(PokerFace.rightHandValue);
  };

  function transformer(list, hand) {
    for (let i = 0; i < list.length; i++) {
        hand.push({
          cardNumber: list[i][0],
          cardColor: list[i][1],
          });

        if (hand[i].cardNumber === 'J') {
          hand[i].cardNumber = '11';
        }
        if (hand[i].cardNumber === 'Q') {
          hand[i].cardNumber = '12';
        }
        if (hand[i].cardNumber === 'K') {
          hand[i].cardNumber = '13';
        }
        if (hand[i].cardNumber === 'A') {
          hand[i].cardNumber = '14';
        }
      };

      hand.sort(function (a, b) {
        return a.cardNumber - b.cardNumber;
      });
    };

    function straightFlush(hand) {
      let checker = 0;

      for (let i = 0; i < hand.length - 1; i++) {
        if (hand[i].cardColor === hand[i+1].cardColor) {
          if (hand[i].cardNumber == (hand[i+1].cardNumber - 1)) {
            checker++;
          }
        }
      };

      if (checker === hand.length - 1) {
        return 9;
      } else {
        return forofaKind(hand);
      }
    };

    function forofaKind(hand) {
      let checker = 0;

      return 8;
    }

    return {
        init,
        leftHand: [],
        rightHand: [],
        leftHandValue: 0,
        rightHandValue: 0
    }

})();

// PokerFace.init(['2H', '3D', '5S', '9C', 'KD'],['2C', '3H', '4S', '8C', 'AH'])
PokerFace.init(['2H', '3H', '4H', '5H', '6H'],['2C', '3H', '4S', '8C', 'AH'])
