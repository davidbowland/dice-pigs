# dice-pigs.py

Calculate possible dice rolls based on <https://youtu.be/ULhRLGzoXQ0>

## Game Premise

Repeatedly, 2-6 is rolled on a die. That value is added to a running total of points.

Technically, if a 1 is rolled then the player should receive no points and the player can stop rolling at any time, but that isn't germane to the code.

## Questions

This project is intended to answer:

- How many ways can we roll a specific total point value?
- How many total points is it possible to have at each roll?

## Usage

```zsh
python3 dice-pigs.py [number of rolls to perform]
```

## Output

Executing this code will output the results in two files, named using the number of rolls performed:

- `breakdown-after-{number of rolls}-rolls.csv`
- `points-up-to-{number of rolls}-rolls.csv`

See the sample files for more information.
