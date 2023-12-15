# The RPG experience, in Python.

## Concept and overall idea of the game
This game will be coded using OOP Python (which I usually hate) to make a terminal based RPG in the style of D&D (UX might come in later using Pygame, but this may require to rework a good chunk of the code).  
You will be able to play through chapters, that are unique stories told in D&D style, with infinite replayability.  
Because this is an RPG, you will have a character that can level-up, gather items and grow stronger the more you play!  

## Accounts
The game will require you to login to an account as the data of your characters will be saved onto your account.  
Username will be unique, letters and numbers only, with a size between 4 and 16 characters.  
Password will follow the same size restriction.  

## Character creation.  
Upon creating a new character, you will be able to choose which class you will play, setting you 50% of your base skill points. Another 30% will be given out randomly, and finally, you can decide how do you want to add the final 20% of skill points.  
The total amount of base skill point is 50 (25 Class dependant, 15 Rng, 10 self-given).  

## Stats (7)  
1 - Strength  
Buffs: Base damage, HP  

2 - Agility  
Buffs: Accuracy  

3 - Defense  
Buffs: Defence  

4 - Magic  
Buffs: Magic damage, Healing outpout  

5 - Holyness  
Buffs: Overall Stat boost

6 - Charisma  
Buffs: Resistance to debuff  

7 - Speed  
Buffs: Movement speed  

## Classes and associated stats  
| Class \ Stats | Strength | Agility | Defense | Magic | Holyness | Charisma | Speed |  
|---------------|----------|---------|---------|-------|----------|----------|-------|  
| Dragoon       | 12       | 2       | 4       | 2     | 2        | 2        | 1     |  
| Arbalist      | 6        | 9       | 3       | 3     | 0        | 1        | 3     |  
| Slaughterer   | 7        | 5       | 1       | 4     | 0        | 3        | 5     |  
| Guardian      | 4        | 0       | 10      | 1     | 4        | 6        | 0     |  
| Spellcaster   | 3        | 5       | 1       | 9     | 2        | 1        | 4     |  
| Angel         | 2        | 2       | 2       | 7     | 7        | 3        | 1     |  