def main():
    mar = [[False for _ in range(10)] for _ in range(10)]

    def validoBatalhaNaval(mar):
        for _ in range(int(input())):
            dados = list(map(int, input().split()))
            dados[2] -= 1
            dados[3] -= 1
            if dados[0] == 0:
                if dados[3] + dados[1] > 10:
                    return "N"
                
                for x in range(dados[1]):
                    if mar[dados[2]][dados[3]+x] == True:
                        return "N"
                        
                    mar[dados[2]][dados[3]+x] = True
            else:
                if dados[2] + dados[1] > 10:
                    return "N"
                
                for x in range(dados[1]):
                    if mar[dados[2]+x][dados[3]] == True:
                        return "N"
                    
                    mar[dados[2]+x][dados[3]] = True
                
        return "Y"
        
    print(validoBatalhaNaval(mar))

if __name__ == "__main__":
    main()
