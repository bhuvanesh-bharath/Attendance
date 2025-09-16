def calculate_attendance(total, attended):
    percentage = (attended / total) * 100
    required = int((0.75 * total) + 0.9999) 
    extra_needed = max(0, required - attended)
    return percentage, extra_needed


def full_calculator():
    print("\n📊 Attendance Calculator ")
    print("----------------------------------")

    subjects = ["COA", "DS", "DBMS", "DELD", "ETHICS", "MATHS"]

    results = []
    for name in subjects:
        print(f"\n{name}:")
        total = int(input("  Total Hours Taken: "))
        attended = int(input("  Hours Attended: "))
        percentage, extra_needed = calculate_attendance(total, attended)
        results.append((name, total, attended, percentage, extra_needed))

    print("\n========== RESULTS ==========")
    overall_total = sum(r[1] for r in results)
    overall_attended = sum(r[2] for r in results)
    overall_percentage = (overall_attended / overall_total) * 100

    for name, total, attended, percentage, extra_needed in results:
        status = "✅ Safe" if percentage >= 75 else f"❌ Need {extra_needed} more hour(s)"
        print(f"{name}: {attended}/{total} → {percentage:.2f}% | {status}")

    print("\nOverall Attendance:", f"{overall_attended}/{overall_total} → {overall_percentage:.2f}%")


def extra_hours_mode():
    print("\n📊 Extra Hours Needed for 75% Attendance")
    print("----------------------------------------")

    n = int(input("Enter number of subjects below 75%: "))

    for i in range(1, n + 1):
        print(f"\nSubject {i}:")
        total = int(input("  Total Hours Taken: "))
        attended = int(input("  Hours Attended: "))
        _, extra = calculate_attendance(total, attended)
        print(f"  ➤ You need {extra} more hour(s) to reach 75%.")

    print("\n✅ Done. Now you know how many extra hours to attend!")


def main():
    while True:
        print("\n==============================")
        print("       Attendance Calculator")
        print("==============================")
        print("1. Full Attendance Calculator (all subjects)")
        print("2. Quick Extra Hours Needed (for <75%)")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            full_calculator()
        elif choice == "2":
            extra_hours_mode()
        elif choice == "3":
            print("👋 Exiting... Stay consistent with attendance!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

