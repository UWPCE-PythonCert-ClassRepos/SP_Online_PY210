"""
Christine Kim
Lesson 9
test mailroom
"""

from donor_models import Giver
from donor_models import GiverCollection

def test_giver_init():
    g1 = Giver("Solona Amell", [50, 20])
    g2 = Giver("Zevran Arainai", [10])

    assert g1.name == "Solona Amell"
    assert g1.donations == [50, 20]

    assert g2.name == "Zevran Arainai"
    assert g2.donations == [10]

def test_compare():
    g1 = Giver("Solona Amell", [50, 20])
    g2 = Giver("Zevran Arainai", [10])
    g3 = Giver("Cullen Rutherford", [5, 3, 2])

    assert g1 > g2
    assert g2 > g3

def test_num():
    g1 = Giver("Solona Amell", [50, 20])

    assert g1.num_give() == 2

def test_total():
    g1 = Giver("Solona Amell", [50, 20])

    assert g1.total_v() == 70

def test_avg():
    g1 = Giver("Solona Amell", [50, 20])

    assert g1.avg() == 35

def test_summary():
    g1 = Giver("Solona Amell", [50, 20])

    assert g1.summary() == "{:<30}${:>15.2f}{:>10} ${:>15.2f}\n".format(g1.name, g1.total_v(), g1.num_give(), g1.avg())

def test_email():
    g1 = Giver("Solona Amell", [50, 20])

    assert g1.gratitude(70) == (f"\nDear Ser {g1.name},\n"
                    f"Thank you for your generous donation of ${70:,d}\n"
                    "We will make certain your goodwill is directed to aid those affected by the Fifth Blight.\n"
                    "With regards,\n"
                    "The Blight Orphans Charity,\n") 

def test_GiverCollection():
    givetree = GiverCollection({"Cullen Rutherford": Giver("Cullen Rutherford", [1500, 4200, 50000]),
                            "Alistair Theirin": Giver("Alistair Theirin", [200, 80000, 1500000]),
                            "Zevran Arainai": Giver("Zevran Arainai", [50]),
                            "Solona Amell": Giver("Solona Amell", [2, 500000, 2000000]),
                            "Soufehla Lavellan": Giver("Soufehla Lavellan", [70, 600])})

    assert givetree.dict_givers() == {"Cullen Rutherford": Giver("Cullen Rutherford", [1500, 4200, 50000]),
                            "Alistair Theirin": Giver("Alistair Theirin", [200, 80000, 1500000]),
                            "Zevran Arainai": Giver("Zevran Arainai", [50]),
                            "Solona Amell": Giver("Solona Amell", [2, 500000, 2000000]),
                            "Soufehla Lavellan": Giver("Soufehla Lavellan", [70, 600])}

    assert givetree.num_givers() == 5

def test_names():
    givetree = GiverCollection({"Cullen Rutherford": Giver("Cullen Rutherford", [1500, 4200, 50000]),
                            "Alistair Theirin": Giver("Alistair Theirin", [200, 80000, 1500000]),
                            "Zevran Arainai": Giver("Zevran Arainai", [50]),
                            "Solona Amell": Giver("Solona Amell", [2, 500000, 2000000]),
                            "Soufehla Lavellan": Giver("Soufehla Lavellan", [70, 600])})

    assert givetree.names() == ("\nCullen Rutherford\nAlistair Theirin\nZevran Arainai\nSolona Amell\nSoufehla Lavellan")