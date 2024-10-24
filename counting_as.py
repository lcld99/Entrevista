def count_letter_a(s):
    count = s.lower().count('a') # Convert a string para lower case e usa a função count para contar os caracteres 'a'
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

string = "A raposa rápida saltou sobre o cachorro preguiçoso."
print(count_letter_a(string))
