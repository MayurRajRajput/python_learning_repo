def http_status(status):
    match status:
        
        case 200:
            return "OK" 
        case 404:
            return "Not Found" 
        case 500:
            return "Internal Server Error" 
        case _:
            return "Unkown status"
print(http_status(2007))