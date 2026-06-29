# example program to understand use case of match case statement in python

while True:
    status_code = int(input("Enter HTTP status code: "))

    match status_code:
        case 200:
            print("OK")
        case 301:
            print("Moved Permanently")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case 502:
            print("Bad Gateway")
        case 503:
            print("Service Unavailable")
        case _:
            print("Unknown Status Code")
            break;

# End of Lession13_1.py


number = int(input("Enter a number between 1 and 10: "))

match number:
    case 1:
        print("you won a Eraser")
    case 3:
        print("you won a book")
    case 6:
        print("you won a pen")
    case _:
        print("you won nothing")