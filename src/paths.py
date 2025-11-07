from pathlib import Path

# define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# create necessary directories if they don't exist
TESTS_DIR = BASE_DIR / "tests"
TESTS_DIR.mkdir(parents=True, exist_ok=True)

RESULTS_DIR = BASE_DIR / "Asistentes"  
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

LOGGS_PATH = BASE_DIR / "loggs"
LOGGS_PATH.mkdir(parents=True, exist_ok=True)

LOGGS_PATH_FILE = LOGGS_PATH / "history.log"
LOGGS_PATH_FILE.touch(exist_ok= True)



