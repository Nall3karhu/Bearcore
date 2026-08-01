import subprocess


def safe_builder(args=None):
    print("🐻 Safe Builder käynnissä")

    print("🔨 Ajetaan testit...")

    try:
        result = subprocess.run(
            ["python", "-m", "pytest"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("✅ Testit läpi")
            return True

        else:
            print("❌ Testejä epäonnistui")
            print(result.stdout)
            print(result.stderr)
            return False

    except Exception as e:
        print("❌ Safe Builder virhe:")
        print(e)
        return False