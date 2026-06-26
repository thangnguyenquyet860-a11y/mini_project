import sys

def add(a, b):
    return float(a) + float(b)

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    print("Tổng:", add(a, b))