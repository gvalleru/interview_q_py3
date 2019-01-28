import find_battle_ships


b = [['x', '.', 'x', '.', 'x', '.', 'x'],
     ['x', '.', '.', '.', 'x', '.', 'x'],
     ['.', '.', 'x', '.', 'x', '.', 'x'],
     ['.', 'x', '.', '.', 'x', '.', 'x'],
     ['.', '.', '.', '.', 'x', '.', 'x'],
     ['x', 'x', 'x', '.', 'x', '.', '.']]

x = find_battle_ships.Solution()
print(x.countBattleships(b))
