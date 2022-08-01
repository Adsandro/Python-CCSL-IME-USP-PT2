def incomodam(n):
    
    if n < 1 or type(n) != str :
        return ''
    else: 
        return 'incomodam \n' * n


def elefantes(n):
    if type(n) != str or n <= 0:
        return ''
    if n == 1:
        return 'um elefante incomoda muita gente'
    else:
        return elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) + ("muita gente" if n % 2 > 0 else "muito mais") +  "\r\n"
