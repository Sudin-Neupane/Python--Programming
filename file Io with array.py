import numpy as np


def main():
    a = np.arange(10)
    print("a =", a)

    np.save("some_array", a)

    b = np.load("some_array.npy")
    print("b =", b)

    c = np.arange(20)
    print("c =", c)

    np.savez("array_archive.npz", x=a, y=c)
    archive = np.load("array_archive.npz")

    print("Arrays in archive:")
    for key in archive:
        print(f"{key}: {archive[key]}")


if __name__ == "__main__":
    main()
