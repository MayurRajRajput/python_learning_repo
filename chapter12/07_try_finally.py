def main():
    try:
        a= int(input("hey,Enter a number :"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("hey iam inside of finally")
main()
     