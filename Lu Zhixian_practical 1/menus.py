def main():
    name = str(input("enter your name: "))
    choose = " "
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    while choose != "Q":
        choose = str(input(">>> ")).upper()

        while choose not in ["H", "G", "Q"]:
            print("Invalid choice")
            print("(H)ello")
            print("(G)oodbye")
            print("(Q)uit")
            break

        if choose == "H":
            print(f"Hello {name}")
            print("(H)ello")
            print("(G)oodbye")
            print("(Q)uit")
            choose = input(">>> ").upper()

        if choose == "G":
            print(f"Goodbye {name}")
            print("(H)ello")
            print("(G)oodbye")
            print("(Q)uit")
            choose = input(">>> ").upper()

        if choose == "Q":
            print("finish")

main()