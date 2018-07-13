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


class NPC:

    def __init__(self, nome, dano, hp, mp):
        self.nome = nome
        self.dano = dano
        self.hp = hp
        self.mp = mp


class Cozinheiro(NPC):

    def __init__(self):
        super().__init__(
                         nome="",
                         dano=0,
                         hp=1,
                         mp=450)

    def esta_vivo(self):
        if self.hp <= 0:
            return False
        return True


class Samantha(NPC):

    def __init__(self):
        self.solta = False
        super().__init__(
                         nome="Samantha",
                         dano=0,
                         hp=1,
                         mp=0)


npcs = {
    "cozinheiro": {
        "nome": "Cozinheiro",
        "dano": 0,
        "hp": 1,
        "mp": 450
    },
    "samantha": {
        "nome": "Samantha",
        "dano": 0,
        "hp": 1,
        "mp": 0,
        "solta": False
    }
}
