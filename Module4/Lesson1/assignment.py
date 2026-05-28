def square_values(start, end):

    squares = []
    odd_squares = []
    even_squares = []

    for num in range(start, end + 1):
        square = num ** 2
        squares.append(square)

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Square values :", squares)
    print("Odd square values :", odd_squares)
    print("Even square values :", even_squares)


start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

square_values(start, end)