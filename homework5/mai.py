def shutdown():
    response = input("if you want to shut dwon press 'y' else press 'n'")
    if  response == 'y':
        print("System shutdown")
        exit()
    else:
        print("User rejected the shutdown request")

    shutdown()