from importlib import util
from os.path import abspath

# Imports the module of file "5.dip.py" as the variable "_module":
_module_name = "5.dip"
_absolute_path = abspath(f"./{_module_name}.py")
_spec = util.spec_from_file_location(_module_name, _absolute_path)
_module = util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Player = _module.Player

def test_dip():
    player = Player("Índio do Sul")
    original_stats = ("\nOriginal player stats:"
            + f"\nname: {player.name()}"
            + f"\nhp: {player.hp()}")
    print(original_stats)
    print("\nReport:")
    player.stats.report()

if __name__ == "__main__":
    test_dip()

