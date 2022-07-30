class GPACalculator:
    def __init__(self, subjects: list):
        self.subjects: list = subjects

    def calculate_gpa(self):
        score_by_weight_list = self.calculate_score_by_weight()
        total_weight = self.get_total_weight()
        return sum(score_by_weight_list) / total_weight

    def calculate_score_by_weight(self):
        score_by_weight: list = []
        for subject in self.subjects:
            weight_score = float(subject.get('subject_score')) * float(subject.get('weight'))
            score_by_weight.append(weight_score)

        return score_by_weight

    def get_total_weight(self):
        total_weight = 0.0
        for subject in self.subjects:
            total_weight += float(subject.get('weight'))
        return total_weight

    @staticmethod
    def convert_base(gpa_value: float):
        return (gpa_value * 4) / 10


if __name__ == '__main__':
    information_system = [
        {
            'weight': 2,
            'subject_score': 8.80
        },
        {
            'weight': 2,
            'subject_score': 8.80
        },
        {
            'weight': 2,
            'subject_score': 6.40
        },
        {
            'weight': 2,
            'subject_score': 8.25
        },
        {
            'weight': 2,
            'subject_score': 7.50
        },
        {
            'weight': 4,
            'subject_score': 9.50
        },
        {
            'weight': 4,
            'subject_score': 9.75
        },
        {
            'weight': 4,
            'subject_score': 9.75
        },
        {
            'weight': 4,
            'subject_score': 9.75
        },
        {
            'weight': 4,
            'subject_score': 10.00
        },
        {
            'weight': 4,
            'subject_score': 9.50
        }, {
            'weight': 4,
            'subject_score': 7.50
        }, {
            'weight': 4,
            'subject_score': 9.75
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 9.75
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 9.00
        }, {
            'weight': 4,
            'subject_score': 9.50
        }, {
            'weight': 8,
            'subject_score': 9.00
        }, {
            'weight': 2,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 9.25
        }, {
            'weight': 4,
            'subject_score': 7.50
        }, {
            'weight': 4,
            'subject_score': 9.50
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 8,
            'subject_score': 9.00
        }, {
            'weight': 2,
            'subject_score': 10.00
        }, {
            'weight': 2,
            'subject_score': 7.50
        }, {
            'weight': 2,
            'subject_score': 8.25
        }, {
            'weight': 2,
            'subject_score': 8.75
        }, {
            'weight': 4,
            'subject_score': 7.50
        }, {
            'weight': 4,
            'subject_score': 7.00
        }, {
            'weight': 4,
            'subject_score': 8.25
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 2,
            'subject_score': 9.50
        },
        {
            'weight': 2,
            'subject_score': 9.50
        }, {
            'weight': 4,
            'subject_score': 7.00
        }, {
            'weight': 2,
            'subject_score': 9.00
        }, {
            'weight': 2,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 9.50
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 9.50
        }, {
            'weight': 2,
            'subject_score': 7.50
        }, {
            'weight': 2,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 8.50
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 7.75
        }, {
            'weight': 7,
            'subject_score': 10.00
        }, {
            'weight': 2,
            'subject_score': 9.00
        }, {
            'weight': 4,
            'subject_score': 10.00
        }, {
            'weight': 4,
            'subject_score': 7.00
        }, {
            'weight': 2,
            'subject_score': 7.50
        }

    ]
    gpa = GPACalculator(subjects=information_system)
    my_gpa = gpa.calculate_gpa()
    my_gpa_converted = gpa.convert_base(my_gpa)

    print(f'O GPA de 0 a 10: {format(my_gpa, ".2f")} pontos.\n'
          f'O GPA de 0 a 4: {format(my_gpa_converted, ".2f")} pontos.')
