def main():
    Msbc = 100
    sbcs = 100
    
    for _ in range(int(input())):
        sbcs += int(input())
        if Msbc < sbcs:
            Msbc = sbcs
    
    print(Msbc)

if __name__ == "__main__":
    main()
