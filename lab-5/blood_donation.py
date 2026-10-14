"""Manage blood donors, blood stock, and donor eligibility."""

import tempfile
from datetime import date, timedelta

donors = []

stock = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "O+": 0,
    "O-": 0,
    "AB+": 0,
    "AB-": 0,
}

COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(stock),
}


def register_donor(
    donor_name,
    blood_group,
    age,
    last_donation=None,
    notes=None,
):
    """Register an eligible donor and record any age-related issue."""
    if notes is None:
        notes = []

    if blood_group not in stock:
        raise ValueError("Unknown blood group")

    if age < 18 or age > 65:
        notes.append(
            f"{donor_name} is not eligible because of age"
        )
        return False

    donors.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def can_donate(donor):
    """Return whether a donor is eligible to donate today."""
    if donor["last"] is None:
        return True

    return (
        date.today() - donor["last"]
        >= timedelta(days=90)
    )


def record_donation(donor_name, units=1):
    """Record a donation if the named donor is eligible."""
    for donor in donors:
        if (
            donor["name"] == donor_name
            and can_donate(donor)
        ):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True

    return False


def units_for(patient_group):
    """Return the available compatible blood units."""
    try:
        compatible_groups = COMPATIBLE[patient_group]
    except KeyError:
        return 0

    return sum(stock[group] for group in compatible_groups)


def is_universal(blood_group):
    """Return whether the group is a universal red-cell donor."""
    return blood_group == "O-"


def low_stock(threshold=2):
    """Return blood groups with stock below the threshold."""
    return [
        group
        for group, units in stock.items()
        if units < threshold
    ]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".csv",
        delete=False,
    ) as temp_file:
        return temp_file.name


def main():
    """Run the blood donation demonstration."""
    register_donor("Arjun", "O+", 25)
    register_donor(
        "Priya",
        "A+",
        30,
        date.today() - timedelta(days=30),
    )
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)

    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")

    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())  # Below 2 units

    eligible = [
        donor["name"]
        for donor in donors
        if can_donate(donor)
    ]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
