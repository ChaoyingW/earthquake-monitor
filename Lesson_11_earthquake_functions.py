readings = []

while True:
    try:
        magnitude = float(input("Enter earthquake magnitude (or 0 to quit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if magnitude == 0:
        print("System shutting down. Goodbye!")
        if len(readings) > 0:
            print("Total readings recorded:", len(readings))
            print("Maximum magnitude recorded:", max(readings))
            average = sum(readings) / len(readings)
            print("Average magnitude recorded:", round(average, 2))
        else:
            print("No readings were recorded.")
        break

    if magnitude < 0:
        print("Invalid magnitude. Please enter a positive number.")
        continue

    readings.append(magnitude)

    if magnitude >= 6.0:
        print("ALERT: Major Earthquake!")
    elif magnitude >= 4.0:
        print("Warning: Moderate Earthquake!")
    else:
        print("Status: Safe.")
    print("-" * 30)

import math


def classify(magnitude):
    """根据震级返回对应的警报等级"""
    if magnitude >= 6.0:
        return "ALERT: Major Earthquake!"
    elif magnitude >= 4.0:
        return "Warning: Moderate Earthquake!"
    else:
        return "Status: Safe."


def print_summary(readings):
    """计算并打印地震数据的统计汇总"""
    print("System shutting down. Goodbye!")
    if len(readings) > 0:
        average = sum(readings) / len(readings)
        print("Total readings recorded:", len(readings))
        print("Maximum magnitude recorded:", max(readings))
        print("Average magnitude recorded:", round(average, 2))
    else:
        print("No readings were recorded.")


def main():
    readings = []

    while True:
        try:
            magnitude = float(input("Enter earthquake magnitude (or 0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # 拦截 nan 和 inf（无限大）
        if not math.isfinite(magnitude):
            print("Invalid input. Please enter a finite number.")
            continue

        if magnitude == 0:
            print_summary(readings)
            break

        if magnitude < 0:
            print("Invalid magnitude. Please enter a positive number.")
            continue

        readings.append(magnitude)
        print(classify(magnitude))
        print("-" * 30)
if __name__ == "__main__":
    main()
