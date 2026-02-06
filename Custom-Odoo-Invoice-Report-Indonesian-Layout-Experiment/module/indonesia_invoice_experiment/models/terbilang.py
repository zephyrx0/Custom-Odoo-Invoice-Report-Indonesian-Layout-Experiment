from odoo import models

class TerbilangMixin(models.AbstractModel):
    _name = "terbilang.mixin"
    _description = "Convert amount to Indonesian words"

    def amount_to_text_id(self, amount):
        amount = int(round(amount or 0))  # <-- kunci: jadi int

        angka = ["", "satu", "dua", "tiga", "empat", "lima", "enam",
                 "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"]

        def to_words(n):
            n = int(n)  # <-- pastiin int di setiap recursion
            if n < 12:
                return angka[n]
            elif n < 20:
                return to_words(n - 10) + " belas"
            elif n < 100:
                return to_words(n // 10) + " puluh " + to_words(n % 10)
            elif n < 200:
                return "seratus " + to_words(n - 100)
            elif n < 1000:
                return to_words(n // 100) + " ratus " + to_words(n % 100)
            elif n < 2000:
                return "seribu " + to_words(n - 1000)
            elif n < 1000000:
                return to_words(n // 1000) + " ribu " + to_words(n % 1000)
            else:
                return ""

        return ((to_words(amount).strip() or "nol") + " rupiah").title()
