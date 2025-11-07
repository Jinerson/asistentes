import time
import sys
from openai import APIConnectionError
from openai import OpenAI
from src.config import API_KEY
from src.loggers import logger
from src.assistants import PersonalAssistant, AssistantManager
from src.config import REPO_URL_T
from src.paths import BASE_DIR, RESULTS_DIR
from src.functions import temp_file, config_git, git_commit_and_push, delete_temp_file

def main():

    try:
        logger.info("Iniciando ejecucion principal para monitoreo de asistentes OpenAI...")
       
        client = OpenAI(api_key=API_KEY) #definir el cliente usando la APY_KEY
        assistant_manager = AssistantManager(client= client) #crear un onjeto para manejar asistentes de OpenAI
        current_assistants = [key for key in assistant_manager.list_assistants()] #crear lista de asistentes actuales asociados al cliente
    
        for assistant_id in current_assistants: #iterar a traves de los asistentes
            assistant = PersonalAssistant() #inicializar objeto asistente
            assistant.attach_client(client= client) #asociar el asistente al cliente
            assistant.load_from_api(assistant_id= assistant_id) #cargar asistente desde la API
            logger.info(f"Cliente {assistant_id[0:5]}... cargado con exito.")
            assistant_config = assistant.get_assistant_config() #cargar la configuracion del asistente actual
            logger.info(f"Configuracion de {assistant_id[0:5]}... cargado con exito.")
            assistant_folder = RESULTS_DIR / f"{assistant_id}" # carpeta para guardar archivo config.json y prompt.md del asistente
            assistant_folder.mkdir(parents= True, exist_ok= True) #asegurar existencia de la carpeta.

            #crear archivos temporales oara comparar las configuraciones de los asistentes
            temp_file(assistant_folder /"config.json", 
                    assistant_folder / "prompt.md",
                    assistant_config)
            
            #iniciar cargado a github
            config_git(BASE_DIR, REPO_URL_T)
            git_commit_and_push(BASE_DIR, BASE_DIR, "Commit realizado")
            
    except APIConnectionError:
        logger.error("Verifique su conexion a internet.")
        sys.exit()
        
if __name__ == "__main__":
    main()
