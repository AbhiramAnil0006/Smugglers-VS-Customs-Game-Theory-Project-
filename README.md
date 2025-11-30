# Smugglers-VS-Customs-Game-Theory-Project
## Game Rules:
---
1. The game has 3 lanes:
   - N  : North
   - C  : Center
   - S  : South

2. The game is played for 5 rounds.

3. In each round, BOTH players choose one lane:
      Smuggler : N / C / S
      Customs  : N / C / S

4. Round Outcome:
      If Smuggler lane == Customs lane:
            -> Smuggler is CAUGHT
      Else:
            -> Smuggler ESCAPES

5. Scoring:
      ESCAPED  -> Smuggler +1 point
      CAUGHT   -> Customs  +1 point

6. Final Result (after 5 rounds):
      If Smuggler score > Customs score:
            -> Smuggler WINS
      If Customs score > Smuggler score:
            -> Customs WINS
      Otherwise:
            -> MATCH TIED

7. Game Theory Interpretation:
      Each round corresponds to the same 3x3 payoff matrix.
      This is a repeated zero-sum game similar to
      a 3-action Matching Pennies structure.

============================================================
