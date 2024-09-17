

num = int(input('First: '))

modulo = num / 40

print(modulo)

def get_cargo(self):
        divi = self.max_capacity / 40

        if divi > 1:
            two_teu = divi
        elif divi < 1:
            modulo = divi % 40
            new_divi = modulo * 40
            one_teu = new_divi / 2

        teu_cargo = two_teu + one_teu

        return teu_cargo

    def get_draft(self):
