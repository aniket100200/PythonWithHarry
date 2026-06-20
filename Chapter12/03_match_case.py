def httpStatus(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case 429:
            return "Rate limit Exceeded"
        
        case _:
            return "Unknown status"
        

print(httpStatus(404))