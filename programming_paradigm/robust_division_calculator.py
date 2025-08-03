def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except(ValueError, TypeError):
        return "Error: Both inputs must be numeric."
    try:
        result = num / dem
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    import sys
    from robust_division_calculator import safe_divide

    def main():
        if len(sys.argv) != 3:
            print("Usage: python mail.py <numerator> <denominator>")
            sys.exit(1)
       numerator = sys.argv[1]
       denominator = sys.argv[2]

       result = safe_divide(numerator, denominator)
       print(result)

     if __name__ == "__main__":
         main()
   
    


