from pathlib import Path


# BearCore ulkoinen data-asema

DATA_DIR = Path(
    "D:/BearCore_Data"
)


KNOWLEDGE_DIR = DATA_DIR / "knowledge"

LEARNING_DIR = DATA_DIR / "learning"

RESEARCH_DIR = DATA_DIR / "research"

CONVERSATION_DIR = DATA_DIR / "conversations"

BACKUP_DIR = DATA_DIR / "backups"



def create_data_folders():

    folders = [

        KNOWLEDGE_DIR,

        LEARNING_DIR,

        RESEARCH_DIR,

        CONVERSATION_DIR,

        BACKUP_DIR

    ]


    for folder in folders:

        folder.mkdir(
            exist_ok=True
        )



def data_status():

    return {

        "data_path":
            str(DATA_DIR),

        "status":
            "ready"

    }