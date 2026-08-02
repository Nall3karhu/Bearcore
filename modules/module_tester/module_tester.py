from pathlib import Path
import subprocess



def find_bearcore():

    current = Path(__file__).resolve()

    for parent in current.parents:

        if parent.name == "BearCore":

            return parent

    return None



def module_tester(module_name=None):

    # Yhteensopivuus vanhojen testien kanssa

    if not module_name:

        print(
            "✅ module_tester-moduuli toimii!"
        )

        return True



    base = find_bearcore()


    if not base:

        return False



    tests_dir = (
        base /
        "tests"
    )


    if not tests_dir.exists():

        return False



    test_file = (
        tests_dir /
        f"test_{module_name}.py"
    )



    if not test_file.exists():

        return False



    try:

        result = subprocess.run(

            [
                "python",
                "-m",
                "pytest",
                str(test_file)
            ],

            capture_output=True,

            text=True

        )


        return result.returncode == 0



    except Exception as e:

        print(
            f"❌ Testivirhe: {e}"
        )

        return False