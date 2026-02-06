import os
import sys

def list_categories():
    return sorted([d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()])

def list_files(category):
    return sorted([f for f in os.listdir(category) if f.endswith('.md')])

def clear_screen():
    print("\033[H\033[J", end="")

def view_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        print("\n" + "="*50)
        print(f"📄 VIEWING: {filepath}")
        print("="*50 + "\n")
        print(content)
        print("\n" + "="*50)
        input("Press Enter to return...")
    except Exception as e:
        print(f"Error reading file: {e}")
        input("Press Enter to return...")

def main():
    while True:
        clear_screen()
        print("🚀 AI EMPIRE 2025 - PROMPT LIBRARY 🚀")
        print("-------------------------------------")

        categories = list_categories()
        for i, cat in enumerate(categories):
            print(f"{i+1}. {cat}")

        print("\nQ. Quit")

        choice = input("\nSelect a category: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            sys.exit(0)

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                selected_cat = categories[idx]

                while True:
                    clear_screen()
                    print(f"📂 CATEGORY: {selected_cat}")
                    print("-------------------------------------")

                    files = list_files(selected_cat)
                    if not files:
                        print("No files found in this category.")

                    for i, f in enumerate(files):
                        print(f"{i+1}. {f}")

                    print("\nB. Back")

                    file_choice = input("\nSelect a file to view: ").strip().lower()

                    if file_choice == 'b':
                        break

                    try:
                        f_idx = int(file_choice) - 1
                        if 0 <= f_idx < len(files):
                            filepath = os.path.join(selected_cat, files[f_idx])
                            view_file(filepath)
                        else:
                            input("Invalid selection. Press Enter...")
                    except ValueError:
                        input("Invalid selection. Press Enter...")

            else:
                input("Invalid selection. Press Enter...")
        except ValueError:
            input("Invalid selection. Press Enter...")

if __name__ == "__main__":
    main()
