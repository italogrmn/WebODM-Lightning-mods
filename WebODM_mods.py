import shutil
import os
import time

def dispath():
    #pega o caminho dos arquivos do instalador
    exec_dir = getattr(sys, '_MEIPASS', os.getcwd())
    package_dir = os.path.join(exec_dir, 'package')

    #pega o nome do usuário
    user_profile = os.environ['USERPROFILE']

    #pastas do webodm
    webodm_path = r'C:\Users' + "\\" + user_profile + "\\" + r'AppData\Local\Programs\WebODM Lightning'
    projects_path = user_profile + r'\resources\app\apps\WebODM\app\api'
    potree_build_path = user_profile + r'\resources\app\apps\WebODM\build\static\app\js\vendor\potree\build\potree'
    potree_app_path = user_profile + r'\resources\app\apps\WebODM\app\static\app\js\vendor\potree\build\potree'            

    if os.path.exists(r'C:\Plugin Revit'):
        print('O WebODM foi encontrado. Iniciando cópia...\n\n')

        #projects.py
        shutil.move(package_dir + r'\projects.py', projects_path)
        
        #potree mods em build
        shutil.move(package_dir + r'\potree.js', potree_build_path)
        shutil.move(package_dir + r'\sidebar.html', potree_build_path)
        
        #potree mods em app
        shutil.move(package_dir + r'\potree.js', potree_app_path)
        shutil.move(package_dir + r'\sidebar.html', potree_app_path)
        
        return 1
    
    else:
        print('O WebODM não foi encontrado')
        return 0

try:
    
    sucess = dispath()

    if (sucess == 1):
        print('\nInstalação das modificações concluida com sucesso!!')
        print('\n\nVocê pode fechar esse terminal ou ele fechará em 2 min')

except Exception as e:
    print(f'Ocorreu um erro na instalação, verifique se o WebODM está instalado corretamente.\n\nErro: {e}')
    print('\n\nVocê pode fechar esse terminal ou ele fechará em 2 min')

time.sleep(120)