import os
import shutil

from core.project import project_path


TEMPLATE_FOLDER = project_path("templates")
MODULE_FOLDER = project_path("modules")


def create_from_template(
    template,
    module_name,
    category="general",
    version="1.0",
    author="BearCore",
    description=""
):

    template_path = os.path.join(
        TEMPLATE_FOLDER,
        template
    )

    module_path = os.path.join(
        MODULE_FOLDER,
        module_name
    )

    if not os.path.exists(template_path):

        print(f"❌ Template '{template}' ei löytynyt.")
        return False

    if os.path.exists(module_path):

        print(f"❌ Moduuli '{module_name}' on jo olemassa.")
        return False

    shutil.copytree(
        template_path,
        module_path
    )

    rename_files(
        module_path,
        module_name
    )

    placeholders = {

        "{{MODULE_NAME}}": module_name,
        "{{CATEGORY}}": category,
        "{{VERSION}}": version,
        "{{AUTHOR}}": author,
        "{{DESCRIPTION}}": description

    }

    replace_placeholders(
        module_path,
        placeholders
    )

    return True


def rename_files(folder, module_name):

    for root, _, files in os.walk(folder):

        for file in files:

            if file == "module.py":

                old = os.path.join(root, file)
                new = os.path.join(root, f"{module_name}.py")

                os.rename(old, new)


def replace_placeholders(folder, placeholders):

    for root, _, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = f.read()

                for key, value in placeholders.items():

                    data = data.replace(
                        key,
                        value
                    )

                with open(
                    path,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(data)

            except Exception:
                pass