import pyperclip

psw = {
    'roblox': 'federico2',
    'googleAccountCatli': 'Federico2',
}

print("quale password ti ineressa?")
for sito in psw:
    print(" -"+sito)
sito_scelto = input()
try:
    password_scelta = psw[sito_scelto]
    pyperclip.copy(password_scelta)
    print("\nPassword trovata! sei pronto ad incollarla")

    input()
except:
    print("il sito non esiste. riprova o scrivi mrglio.")

    
