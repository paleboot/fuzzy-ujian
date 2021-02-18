import argparse
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyVariable:
    def __init__(self):
        self.essay = ctrl.Antecedent(np.arange(1, 6, 1), "essay")
        self.pilgan = ctrl.Antecedent(np.arange(1, 16, 1), "pilgan")
        self.waktu = ctrl.Consequent(np.arange(30, 121, 1), "waktu")

        self.essay["sedikit"] = fuzz.trimf(self.essay.universe, [1, 1, 2])
        self.essay["sedang"] = fuzz.trimf(self.essay.universe, [1, 3, 4])
        self.essay["banyak"] = fuzz.trimf(self.essay.universe, [3, 5, 5])

        self.pilgan["sedikit"] = fuzz.trimf(self.pilgan.universe, [1, 1, 6])
        self.pilgan["sedang"] = fuzz.trimf(self.pilgan.universe, [5, 8, 12])
        self.pilgan["banyak"] = fuzz.trimf(self.pilgan.universe, [8, 15, 15])

        self.waktu["sedikit"] = fuzz.trimf(self.waktu.universe, [30, 30, 60])
        self.waktu["sedang"] = fuzz.trimf(self.waktu.universe, [45, 90, 100])
        self.waktu["banyak"] = fuzz.trimf(self.waktu.universe, [90, 120, 120])


class FuzzyRule(FuzzyVariable):
    def __init__(self):
        super().__init__()
        self.r1 = ctrl.Rule(
            self.essay["sedikit"] & self.pilgan["sedikit"], self.waktu["sedikit"]
        )
        self.r2 = ctrl.Rule(
            self.essay["sedikit"] & self.pilgan["sedang"], self.waktu["sedang"]
        )
        self.r3 = ctrl.Rule(
            self.essay["sedikit"] & self.pilgan["banyak"], self.waktu["sedang"]
        )
        self.r4 = ctrl.Rule(
            self.essay["sedang"] & self.pilgan["sedikit"], self.waktu["sedang"]
        )
        self.r5 = ctrl.Rule(
            self.essay["sedang"] & self.pilgan["sedang"], self.waktu["banyak"]
        )
        self.r6 = ctrl.Rule(
            self.essay["sedang"] & self.pilgan["banyak"], self.waktu["banyak"]
        )
        self.r7 = ctrl.Rule(
            self.essay["banyak"] & self.pilgan["sedikit"], self.waktu["banyak"]
        )
        self.r8 = ctrl.Rule(
            self.essay["banyak"] & self.pilgan["sedang"], self.waktu["banyak"]
        )
        self.r9 = ctrl.Rule(
            self.essay["banyak"] & self.pilgan["banyak"], self.waktu["banyak"]
        )
        self.rules = [
            self.r1,
            self.r2,
            self.r3,
            self.r4,
            self.r5,
            self.r6,
            self.r7,
            self.r8,
            self.r9,
        ]


class FuzzySystem(FuzzyRule):
    def __init__(self, essay: int, pilgan: int):
        super().__init__()
        print("test CI")
        self.essay = essay
        self.pilgan = pilgan

        self.system = ctrl.ControlSystem(self.rules)
        self.system_sim = ctrl.ControlSystemSimulation(self.system)

    def compute(self, view=False):
        system_sim = self.system_sim
        system_sim.input["essay"] = self.essay
        system_sim.input["pilgan"] = self.pilgan
        system_sim.compute()
        if view:
            self.waktu.view(sim=system_sim)

        return int(system_sim.output["waktu"])


if __name__ == "__main__":
    fuzzy_parser = argparse.ArgumentParser()
    fuzzy_parser.add_argument(
        "essay", metavar="essay", type=int, help="banyaknya soal essay"
    )
    fuzzy_parser.add_argument(
        "pilihan_ganda",
        metavar="pilihan_ganda",
        type=int,
        help="banyaknya soal pilihan ganda",
    )

    args = fuzzy_parser.parse_args()
    fuzzy_system = FuzzySystem(args.essay, args.pilihan_ganda)
    time = fuzzy_system.compute()
    print(time)
    for i in fuzzy_system.system.rules:
        print(i)
    for i in fuzzy_system.system.fuzzy_variables:
        print(i)
