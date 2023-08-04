import random
import datetime
import pywhatkit as wp

class ScaleGenerator:
    def __init__(self, enterprises: list):
        self.eduardo_scale = []
        self.gabriel_scale = []
        self.enterprises = enterprises

    def generate(self):
        for item in self.enterprises:
            add_enterprise = self.enterprises[random.randint(0, len(self.enterprises) - 1)]

            while self.eduardo_scale.count(add_enterprise) > 0 or self.gabriel_scale.count(add_enterprise):
                add_enterprise = self.enterprises[random.randint(0, len(self.enterprises) - 1)]
            
            if(len(self.gabriel_scale) >= 3):
                self.eduardo_scale.append(add_enterprise)
            else:
                self.gabriel_scale.append(add_enterprise)

    def scale_date(self):
        today = datetime.datetime.now()
        day = f'{today.day}' if today.day > 10 else f'0{today.day}'
        month = f'{today.month}' if today.month > 10 else f'0{today.month}'
        year = f'{today.year}'
        return f'{day}-{month}-{year}'
    
    def send_message(self):
        message = f'*Escala de Atendimento do Suporte {self.scale_date()}*\n\nSegue abaixo a escala de atendimentos para o dia presente:\n\n*> Gabriel M. V. Braga:*\n- {self.gabriel_scale[0]}\n- {self.gabriel_scale[1]}\n- {self.gabriel_scale[2]}\n\n*> Eduardo J. Borges:*\n- {self.eduardo_scale[0]}\n- {self.eduardo_scale[1]}\n- {self.eduardo_scale[2]}'
        wp.sendwhatmsg_to_group("LXDMvaptOMp8EU9oVbw5ip", message, 15, 52, 35)


scale: ScaleGenerator = ScaleGenerator(['Agrisan', 'LFG Agro', 'Panarello', 'Santa Rita', 'Agrovence', 'PrimeFoods'])
scale.generate()
scale.send_message()