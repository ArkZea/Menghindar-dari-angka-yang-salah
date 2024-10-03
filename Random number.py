import random
import string

def rng(guess, jumlahBom):
    result = ""
    inputNumbers = range(1,5)
    angkaRandom = random.sample(inputNumbers, jumlahBom)
    if guess in angkaRandom:
        result = "Game Over, anda menebak angka yang memiliki bom"
    else:
        result = "Selamat anda berhasil menghindari angka yang memiliki bom"
    return result

def menu():
    while True:
        try:
            print("-- Selamat datang di tebak angka --")
            print("Cara bermain: Kamu harus menebak angka yang yang tidak memiliki bom dari 1-5 :")
            print("Pilih jumlah bom yang ingin anda tebak dari ")
            print('1. 1 Bom')
            print('2. 2 Bom')
            print('3. 3 Bom')
            print('4. 4 Bom')
            print('5. Exit')

            choice = input("Enter your choice (1/2/3/4/5): ").strip()
            match choice:
                case '1':
                    guess = int(input("Tebak angka yang tidak memiliki bom dari 1 - 5 : "))
                    bom = rng(guess, jumlahBom = 1)
                    print(bom)
                    break;
                case '2':
                    guess = int(input("Tebak angka yang tidak memiliki bom dari 1 - 5 : "))
                    bom = rng(guess, jumlahBom = 2)
                    print(bom)
                    break;
                case '3':
                    guess = int(input("Tebak angka yang tidak memiliki bom dari 1 - 5 : "))
                    bom = rng(guess, jumlahBom= 3)
                    print(bom)
                    break;
                case '4':
                    guess = int(input("Tebak angka yang tidak memiliki bom dari 1 - 5 : "))
                    bom = rng(guess, jumlahBom= 4)
                    print(bom)
                    break;
                case '5':
                    print("You have exited the game. Goodbye!")
                    break;
                case _ :
                    print("Invalid choice, please try again")
                    break;
        except ValueError:
            print("Err: Input tidak tepat")
        except Exception as e :
            print(f"An error has occured : {e}. Restarting")

if __name__ == '__main__':
    menu()