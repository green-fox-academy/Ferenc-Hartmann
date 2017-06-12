'use strict'

var PokerFace = (function() {

  function init(firstList, secondList) {
    transformer(firstList, PokerFace.leftHand);
    transformer(secondList, PokerFace.rightHand);
    // straightFlush(PokerFace.leftHand);
    // straightFlush(PokerFace.rightHand);
    console.log(PokerFace.leftHand);
    console.log(PokerFace.rightHand);
    // console.log(straightFlush(PokerFace.leftHand));
    // console.log(straightFlush(PokerFace.rightHand));
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
      for (let i = 0; i < hand.length - 1; i++) {
          if (hand[i].cardColor === hand[i+1].cardColor){
            if (){
            }
          }
      }

        return
      else fourofakind()
      };

    return {
        init,
        leftHand: [],
        rightHand: []
    }

})();

PokerFace.init(['2H', '3D', '5S', '9C', 'KD'],['2C', '3H', '4S', '8C', 'AH'])
