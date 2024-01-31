def main():
    count = 0

    n_2 = 1
    n_1 = 1
    for i in range(2, 400, 1):
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n

        if i >= 300 and n % 2 == 1:
            count += 1
        print(f"{i}: {n}")
    print(f"count: {count}")


if __name__ == "__main__":
    main()
