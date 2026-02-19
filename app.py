def static_gpa_app():
    # PRE-DEFINED DATA (No input needed)
    # Format: "Course Name": [Credits, Grade_Point]
    report_card = {
        "Mathematics": [4, 9.0],
        "Digital Marketing": [3, 10.0],
        "Web Development": [4, 8.5],
        "Graphic Design": [2, 9.5],
        "Entrepreneurship": [3, 10.0]
    }

    print("========================================")
    print("      AUTOMATIC SEMESTER REPORT         ")
    print("========================================")
    print(f"{'Course':<20} | {'Credits':<7} | {'Grade':<5}")
    print("-" * 40)

    total_points = 0
    total_credits = 0

    # Automatic Calculation Logic
    for course, data in report_card.items():
        credits = data[0]
        grade = data[1]
        
        print(f"{course:<20} | {credits:<7} | {grade:<5}")
        
        total_points += (credits * grade)
        total_credits += credits

    # The Result
    sgpa = total_points / total_credits

    print("-" * 40)
    print(f"TOTAL CREDITS: {total_credits}")
    print(f"FINAL SGPA:    {sgpa:.2f} / 10.0")
    print("========================================")

if __name__ == "__main__":
    static_gpa_app()