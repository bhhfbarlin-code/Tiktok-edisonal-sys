import os
import textwrap
from datetime import datetime

TOOL_NAME = "TIKTOK REPORT SYSTEM"
AUTHOR = "KARLO X MARCO"
REPORT_FILE = "tiktok_privacy_reports.txt"

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
GRAY = "\033[90m"


def clear():
    os.system("clear")


def width():
    try:
        return max(45, min(os.get_terminal_size().columns, 72))
    except:
        return 60


def line():
    print(GRAY + "─" * width() + RESET)


def title(text):
    w = width()
    print(CYAN + "╔" + "═" * (w - 2) + "╗" + RESET)
    print(
        CYAN + "║" +
        BOLD + WHITE + text.center(w - 2) +
        RESET + CYAN + "║" + RESET
    )
    print(CYAN + "╚" + "═" * (w - 2) + "╝" + RESET)


def wrap(text):
    return textwrap.fill(
        text,
        width=max(35, width() - 4),
        break_long_words=False
    )


def pause():
    input(
        "\n" + GRAY +
        "Press ENTER to continue..." +
        RESET
    )


# ==========================================
# PRIVACY REPORT GENERATOR
# ==========================================

def privacy_report():

    clear()

    title("TIKTOK PRIVACY REPORT")

    print()
    print(
        CYAN +
        "Professional Privacy Additional Information" +
        RESET
    )

    print(
        GRAY +
        f"Author : {AUTHOR}" +
        RESET
    )

    line()

    print()
    print(
        WHITE +
        "Enter factual information about the content." +
        RESET
    )

    print(
        GRAY +
        "Do not add information that is not true." +
        RESET
    )

    # --------------------------------------
    # BASIC INFORMATION
    # --------------------------------------

    print()
    print(CYAN + "CONTENT INFORMATION" + RESET)
    line()

    video_url = input(
        "TikTok Video URL\n> "
    ).strip()

    print()

    identification = input(
        "How can we identify you in the content?\n> "
    ).strip()

    if not identification:
        print(
            RED +
            "\nIdentification information is required." +
            RESET
        )
        pause()
        return

    print()

    reason = input(
        "Why should this content be removed?\n> "
    ).strip()

    if not reason:
        print(
            RED +
            "\nRemoval reason is required." +
            RESET
        )
        pause()
        return

    # --------------------------------------
    # GENERATE ADDITIONAL 1
    # --------------------------------------

    additional_1 = (
        "I can be identified in the reported content because "
        + identification +
        ". The content contains or shows information that "
        "allows me to be identified. I am requesting a review "
        "of this content under TikTok's applicable privacy "
        "policies."
    )

    # --------------------------------------
    # GENERATE ADDITIONAL 2
    # --------------------------------------

    additional_2 = (
        "I am requesting removal of this content because "
        + reason +
        ". I believe the content creates a privacy concern "
        "and was shared without the necessary permission or "
        "authorization. Please review the reported content "
        "and take appropriate action if a policy violation "
        "is confirmed."
    )

    # --------------------------------------
    # SHOW RESULT
    # --------------------------------------

    clear()

    title("PRIVACY REPORT RESULT")

    print()
    print(
        GREEN +
        "✓ Two Additional Information fields generated" +
        RESET
    )

    print()

    # FIELD 1
    print(
        CYAN +
        "1️⃣ HOW CAN WE IDENTIFY YOU IN THE CONTENT?" +
        RESET
    )

    line()

    print()
    print(wrap(additional_1))

    print()
    line()

    # FIELD 2
    print(
        CYAN +
        "2️⃣ WHY SHOULD THIS CONTENT BE REMOVED?" +
        RESET
    )

    line()

    print()
    print(wrap(additional_2))

    print()
    line()

    # --------------------------------------
    # SAVE
    # --------------------------------------

    with open(
        REPORT_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write("\n")
        file.write("=" * 70 + "\n")
        file.write(
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write(
            f"Video URL: {video_url}\n\n"
        )

        file.write(
            "1. HOW CAN WE IDENTIFY YOU IN THE CONTENT?\n\n"
        )
        file.write(additional_1)
        file.write("\n\n")

        file.write(
            "2. WHY SHOULD THIS CONTENT BE REMOVED?\n\n"
        )
        file.write(additional_2)
        file.write("\n")

        file.write("=" * 70 + "\n")

    print()
    print(
        GREEN +
        f"✓ Saved: {REPORT_FILE}" +
        RESET
    )

    print()

    # --------------------------------------
    # COPY TEXT
    # --------------------------------------

    print(
        YELLOW +
        "COPY-PASTE TEXT" +
        RESET
    )

    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("FIELD 1:")
    print()
    print(additional_1)

    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("FIELD 2:")
    print()
    print(additional_2)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    pause()


# ==========================================
# ABOUT
# ==========================================

def about():

    clear()

    title("ABOUT TOOL")

    print()
    print(f"Tool   : {TOOL_NAME}")
    print(f"Author : {AUTHOR}")
    print("Mode   : Manual Privacy Report Assistant")
    print("Engine : Python")

    print()

    print(
        wrap(
            "This tool prepares two separate professional "
            "Additional Information texts for a TikTok "
            "Privacy Violation report. The generated text "
            "is based only on information provided by the "
            "reporter."
        )
    )

    print()
    print(
        YELLOW +
        "The tool does not automatically submit reports." +
        RESET
    )

    pause()


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        clear()

        title(TOOL_NAME)

        print()
        print(
            CYAN +
            "Professional TikTok Report Assistant" +
            RESET
        )

        print(
            GRAY +
            f"Author : {AUTHOR}" +
            RESET
        )

        line()

        print()

        print(
            f"{CYAN}[1]{RESET} "
            "Privacy Violation Report"
        )

        print(
            f"{CYAN}[2]{RESET} "
            "About Tool"
        )

        print(
            f"{RED}[3]{RESET} "
            "Exit"
        )

        line()

        choice = input(
            "\nSelect option > "
        ).strip()

        if choice == "1":

            privacy_report()

        elif choice == "2":

            about()

        elif choice == "3":

            clear()

            print(
                CYAN +
                TOOL_NAME +
                RESET
            )

            print(
                f"Author: {AUTHOR}"
            )

            print("\nGoodbye.")
            break

        else:

            print(
                RED +
                "\nInvalid option." +
                RESET
            )

            pause()


if __name__ == "__main__":
    main()