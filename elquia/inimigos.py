"""
Natália Gama, Edison Neto, Pietro Gonçalves
This software is a text RPG.

Copyright (C) 2018 Pietro Gonçalves
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

class Inimigo:

    def __init__(self, nome, dano, hp):
        self.nome = nome
        self.dano = dano
        self.hp = hp

    def esta_vivo(self):
        if self.hp >= 0:
            return False
        return True

    def __str__(self):
        return "Nome: {}\nHP: {}\nDano: {}".format(self.nome, self.hp, self.dano)


class RatoGigante(Inimigo):

    def __init__(self):
        super().__init__(
                         nome="Rato gigante",
                         dano=9,
                         hp=100)


class CarrascoDoRei(Inimigo):

    def __init__(self):
        super().__init__(
                         nome="Carrasco do rei",
                         dano=13,
                         hp=150)


class Basilisco(Inimigo):

    def __init__(self):
        super().__init__(
                         nome="Basilisco",
                         dano=30,
                         hp=50)

rato = RatoGigante()

print(rato)

inimigos = {
    "rato_gigante": {
        'nome' : 'Rato gigante',
        'dano' : 8,
        'hp': 100
    },
    "rato_gigante_refeitorio": {
        'nome' : 'Rato gigante',
        'dano' : 9,
        'hp': 100
    },
    "carrasco_do_rei_1": {
        'nome' : 'Carrasco do rei',
        'dano' : 13,
        'hp' : 150
    },
    "carrasco_do_rei_2": {
        'nome' : 'Carrasco do rei',
        'dano' : 13,
        'hp' : 150
    },
    "basilisco": {
        'nome' : 'basilisco',
        'dano' : 30,
        'hp' : 50
    }
}
