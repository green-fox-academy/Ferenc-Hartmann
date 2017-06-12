'use strict'

var PokerFace = (function() {

  function transformer(firstList, secondList) {
    looper(firstList, PokerFace.leftHand);
    looper(secondList, PokerFace.rightHand);
    // console.log(PokerFace.leftHand[0].cardNumber);
  };

  function looper(list, hand) {
    for (let i = 0; i < list.length; i++) {
        hand.push({
          cardNumber: list[i][0],
          cardColor: list[i][1],
          });
      }
    };

    return {
        transformer: transformer,
        leftHand: [],
        rightHand: [],
    }

})();

PokerFace.transformer(['2H', '3D', '5S', '9C', 'KD'],['2C', '3H', '4S', '8C', 'AH'])
