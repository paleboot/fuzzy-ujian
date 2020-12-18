from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem

essay = FuzzyInputVariable('Essay', 0, 10, 100)
essay.add_triangular('Sedikit', 0, 0, 5)
essay.add_triangular('Sedang', 2.5, 5, 7.5)
essay.add_triangular('Banyak', 5, 10, 10)

pilgan = FuzzyInputVariable('Pilihan Ganda', 0, 20, 100)
pilgan.add_triangular('Sedikit', 0, 0, 10)
pilgan.add_triangular('Sedang', 5, 10, 15)
pilgan.add_triangular('Banyak', 10, 20, 20)


waktu = FuzzyOutputVariable('Waktu Pengerjaan', 0, 120, 100)
waktu.add_triangular('Cepat', 0, 0, 60)
waktu.add_triangular('Sedang', 30, 60, 90)
waktu.add_triangular('Lama', 60, 120, 120)

fuzzy_system = FuzzySystem()
fuzzy_system.add_input_variable(essay)
fuzzy_system.add_input_variable(pilgan)
fuzzy_system.add_output_variable(waktu)

fuzzy_system.add_rule(
		{ 'Essay':'Sedikit',
			'Pilihan Ganda':'Sedikit' },
		{ 'Waktu Pengerjaan':'Cepat'})

fuzzy_system.add_rule(
		{ 'Essay':'Sedang',
			'Pilihan Ganda':'Sedang' },
		{ 'Waktu Pengerjaan':'Sedang'})

fuzzy_system.add_rule(
		{ 'Essay':'Banyak',
			'Pilihan Ganda':'Banyak' },
		{ 'Waktu Pengerjaan':'Lama'})

output = fuzzy_system.evaluate_output({
				'Essay':6,
				'Pilihan Ganda':13
		})

print(output)

# fuzzy_system.plot_system()