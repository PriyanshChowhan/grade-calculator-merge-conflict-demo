"""Student Grade Calculator CLI."""

from typing import List


def average(scores: List[float]) -> float:
    """Return the arithmetic mean of a list of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def percentage(scores: List[float], max_score_per_subject: float = 100.0) -> float:
    """Return the overall percentage across all subjects."""
    if not scores or max_score_per_subject <= 0:
        return 0.0
    total_possible = len(scores) * max_score_per_subject
    return (sum(scores) / total_possible) * 100.0


def grade_letter(pct: float) -> str:
    """Map a percentage score to a standard letter grade."""
    # Enhanced honors grading scale with A+ tier
    if pct >= 95:
        return "A+"
    elif pct >= 90:
        return "A"
    elif pct >= 80:
        return "B"
    elif pct >= 70:
        return "C"
    elif pct >= 60:
        return "D"
    return "F"


def pass_fail(pct: float, passing_threshold: float = 40.0) -> str:
    """Return 'PASS' if percentage meets threshold, else 'FAIL'."""
    return "PASS" if pct >= passing_threshold else "FAIL"


def main() -> None:
    print("=== Student Grade Calculator ===")
    raw = input("Enter subject scores separated by spaces (0-100): ").strip()
    if not raw:
        print("No scores entered.")
        return

    scores = [float(item) for item in raw.split()]
    avg = average(scores)
    pct = percentage(scores)
    grade = grade_letter(pct)
    status = pass_fail(pct)

    print(f"Average Score : {avg:.2f}")
    print(f"Percentage    : {pct:.2f}%")
    print(f"Letter Grade  : {grade}")
    print(f"Result        : {status}")


if __name__ == "__main__":
    main()
