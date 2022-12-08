namespace LibTest;
using Day2Lib;

public class RPSTests
{       
    [Fact]
    public void SingleRound_AXhasCorrectScore()
    {
      // Tie game
       GameScore score = RPSGame.PlayGame(new string[]{"A X"});
       Assert.Equal(4, score.playerScore);
       Assert.Equal(4, score.opponentScore);

    }

    [Fact]
    public void SingleRound_BYhasCorrectScore()
    {
       GameScore score = RPSGame.PlayGame(new string[]{"B Y"});
       Assert.Equal(5, score.opponentScore);
       Assert.Equal(5, score.playerScore);

    }

    [Fact]
    public void SingleRound_CZhasCorrectScore()
    {
       GameScore score = RPSGame.PlayGame(new string[]{"C Z"});
       Assert.Equal(6, score.opponentScore);
       Assert.Equal(6, score.playerScore);

    }

    [Fact]
    public void MultiRound_hasCorrectScore()
    {
       GameScore score = RPSGame.PlayGame(new string[]{"C Z", "A Z", "B Y"});
       // R1: 6, 6
       // R2: 7, 3
       // R3: 5, 5
       Assert.Equal(18, score.opponentScore);
       Assert.Equal(14, score.playerScore);

    }
}