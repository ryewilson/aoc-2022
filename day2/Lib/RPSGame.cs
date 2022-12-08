namespace Day2Lib;
public class RPSGame
{
    /*
        roc = 1 = A
        paper = 2 = B
        scissor = 3 = C

        0 = lose
        3 = draw
        6 = win

        x = lose
        y = draw
        z = win
    */

    public static GameScore PlayGame(string[] input)
    {
        int opponentScore = 0;
        int playerScore = 0;
        // for each line, read characters and score each person

        foreach(string round in input)
        {
            var plays = round.ToLower().Split(' ');
            RockPaperScissor opponent = ConvertToTypedScore(plays[0]);
            opponentScore += GetScoreValue(opponent);
            
            Outcome outcome = ConvertToOutcome(plays[1]);
            // Based on outcome and opponent play, get our play
            RockPaperScissor player = GetPlayerPlay(outcome, opponent);
            playerScore += GetScoreValue(player);
            
            (int opponentPoints, int playerPoints) = GetOutcomeScore(opponent, player);

            opponentScore += opponentPoints;
            playerScore += playerPoints;
        }

        return new GameScore(playerScore, opponentScore);
    }

    private static RockPaperScissor GetPlayerPlay(Outcome outcome, RockPaperScissor opponent) =>
     (outcome, opponent) switch
     {
        (Outcome.Draw, _) => opponent,
        (Outcome.Win, RockPaperScissor.Rock) => RockPaperScissor.Paper,
        (Outcome.Win, RockPaperScissor.Paper) => RockPaperScissor.Scissor,
        (Outcome.Win, RockPaperScissor.Scissor) => RockPaperScissor.Rock,
        // Lose
        (Outcome.Lose, RockPaperScissor.Rock) => RockPaperScissor.Scissor,
        (Outcome.Lose, RockPaperScissor.Paper) => RockPaperScissor.Rock,
        (Outcome.Lose, RockPaperScissor.Scissor) => RockPaperScissor.Paper,
        (_, _) => throw new ArgumentException($"Unhandled case: {outcome}, {opponent}"),
     };

    private static Outcome ConvertToOutcome(string choice) =>
        choice switch
        {
            "x" => Outcome.Lose,
            "y" => Outcome.Draw,
            "z" => Outcome.Win,
            _ => throw new ArgumentException("Unexpected input: " + choice),
        };

    private static RockPaperScissor ConvertToTypedScore(string play) =>
        play switch
        {
            "x" or "a" => RockPaperScissor.Rock,
            "y" or "b" => RockPaperScissor.Paper,
            "z" or "c" => RockPaperScissor.Scissor,
            _ => throw new ArgumentException("Unexpected input: " + play),
        };

    private static (int opponentPoints, int playerPoints) GetOutcomeScore(RockPaperScissor opponentPlay, RockPaperScissor playerPlay)
    {
        if(opponentPlay == playerPlay)
        {
            return (3,3);
        }

        if(opponentPlay == RockPaperScissor.Rock && playerPlay == RockPaperScissor.Paper)
        {
            return (0, 6);
        }

        if(opponentPlay == RockPaperScissor.Rock && playerPlay == RockPaperScissor.Scissor)
        {
            return (6, 0);
        }

        if(opponentPlay == RockPaperScissor.Scissor && playerPlay == RockPaperScissor.Rock)
        {
            return (0, 6);
        }

        if(opponentPlay == RockPaperScissor.Paper && playerPlay == RockPaperScissor.Rock)
        {
            return (6, 0);
        }

        if(opponentPlay == RockPaperScissor.Paper && playerPlay == RockPaperScissor.Scissor)
        {
            return (0, 6);
        }

        if(opponentPlay == RockPaperScissor.Scissor && playerPlay == RockPaperScissor.Paper)
        {
            return (6, 0);
        }

        throw new ArgumentException($"Unhandled case: opp = {opponentPlay.ToString()}, player = {playerPlay.ToString()}");
    }

    public static int GetScoreValue(RockPaperScissor singleScore)
    {
        return ((int)singleScore);
    }

}
