var TennisGame1 = function() {
    this.scorePlayer1 = 0;
    this.scorePlayer2 = 0;
    this.scoreboard = "";
};

TennisGame1.prototype.wonPoint = function(playerName) {
    if (playerName === "player1") {
        this.scorePlayer1 += 1;
    } else {
        this.scorePlayer2 += 1;
    }
};

TennisGame1.prototype.getScore = function() {
    var tempScore = 0;
    if (this.scorePlayer1 === this.scorePlayer2) {
        var options = ["Love-All", "Fifteen-All", "Thirty-All"];
        this.scoreBoard = (this.scorePlayer1 < 3) ? options[this.scorePlayer1] : "Deuce";

    } else TennisGame1.prototype.getScore2();
    console.log(this.scoreBoard);
};

TennisGame1.prototype.getScore2 = function() {
    if (this.scorePlayer1 >= 4 || this.scorePlayer2 >= 4) {
        var minusResult = this.scorePlayer1 - this.scorePlayer2;
        if (minusResult === 1) {
             this.scoreBoard = "Advantage player1";
         }
        else if (minusResult === -1) {
            this.scoreBoard = "Advantage player2";
        }
        else if (minusResult >= 2) {
            this.scoreBoard = "Win for player1";
        }
        else {
            this.scoreBoard = "Win for player2";
        }
    } else {
        for (var i = 1; i < 3; i++) {
            if (i === 1) {
                tempScore = this.scorePlayer1;
            }
            else {
                this.scoreBoard += "-";
                tempScore = this.scorePlayer2;
            }
            switch (tempScore) {
                case 0:
                    this.scoreBoard += "Love";
                    break;
                case 1:
                    this.scoreBoard += "Fifteen";
                    break;
                case 2:
                    this.scoreBoard += "Thirty";
                    break;
                case 3:
                    this.scoreBoard += "Forty";
                    break;
            }
        }
    }
    return this.scoreBoard;
};
