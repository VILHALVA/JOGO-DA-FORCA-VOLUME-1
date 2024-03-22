from random import choice
import os

def get_wordlist():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'WORD.txt'), encoding='utf-8') as w:
            lines = w.readlines()
            words = [line.strip().upper() for line in lines]
            secret = choice(words)
            return secret
    except IOError:
        return "ERRO: Nenhum dicionário foi encontrado. Crie o arquivo chamado WORD.txt e coloque uma palavra em cada linha!"

def hide(word, masked, hack=False):
    for position, letter in enumerate(word):
        if masked[position] == letter:
            print(f'{letter}', end=' ')
        elif word[position] == ' ':
            masked[position] = letter
            print('', end='')
        else:
            print('_', end=' ')
    print('', end='')
    print()
    if hack:
        for letter in word:
            print(f'{letter.lower()}', end=' ')
        print()

def play(secret):
    hidden = ['_' for letter in secret]
    guessed_letters = []
    turns = 6
    while turns > 0:
        hide(secret, hidden)
        if ''.join(secret) == ''.join(hidden):
            print("😄Parabéns, você acertou!")
            break
        print()
        guess = input("😎Tente adivinhar qual é a palavra secreta! Digite uma letra:\n>>>").strip().upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("🤬Você já jogou esta letra!")
            else:
                if guess in secret:
                    for position, letter in enumerate(secret):
                        if guess == letter:
                            hidden[position] = letter
                else:
                    turns -= 1
                    print(f"😠Errado! {guess.upper()} não está na palavra.")
                guessed_letters.append(guess)
            if turns > 0:
                print(f"😎Letras jogadas: {' - '.join(guessed_letters)}")
                print(f"🤬Você tem {turns} chance(s) restantes.")
        else:
            print("🤬Você deve digitar uma letra.")
        print()
    else:
        print(f"🤬Você perdeu! A resposta correta era {secret}")

def main():
    word = get_wordlist()
    play(word)

if __name__ == '__main__':
    main()
