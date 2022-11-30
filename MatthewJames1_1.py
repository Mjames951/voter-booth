def main():
    john = 0
    jane = 0
    
    vote_option = vote_menu()
    
    while vote_option == 'v':
        candid = candidate_main()
        if candid == 0:
            john += 1
            print('Voted John')
        elif candid == 1:
            jane += 1
            print('Voted Jane')
        else:
            print('bruh this aint supposed to happen')
        print('--------------------')
        vote_option = vote_menu()
        
    print("--------------------")
    print("John = {}, Jane = {}, Total = {}".format(john, jane, john+jane))
    
def candidate_main():
    print("--------------------\nCANDIDATES\n--------------------\n0 - John\n1 - Jane")
    option = int(input("Candidate: ").strip())
    while option != 1 and option != 0:
        option = int(input("Invalid (0/1): ").strip())
    return option
            
def vote_menu():
    print("VOTE MENU\n--------------------\nv - vote\nx - exit")
    option = input("Option: ").lower().strip()
    while option != 'x' and option != 'v':
        option = input("Invalid (v/x): ").lower().strip()
    return option
        
main()
    