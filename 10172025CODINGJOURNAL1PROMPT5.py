import math


def main():
    print("x\t\t sin(x)")
    print("-" * 25)

    # Generate 1000 points between 0 and 2
    num_points = 1000
    for i in range(num_points + 1):
        x = 2 * i / num_points  # even spacing between 0 and 2
        y = math.sin(x)
        print(f"{x:.5f}\t {y:.5f}")


if __name__ == "__main__":
    main()
