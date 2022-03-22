from os import listdir as ls, path

class FolderFinder:
    def __init__(self, debug = False) -> None:
        self.items = []
        self.debug = debug

    def find_in_folder(self, directory:str) -> list:  # lista subdiretórios e retorna lista com arquivos encontrados
        if self.debug:
            print('Listando diretórios...')
        try:
            for item in ls(directory):
                d = path.join(directory, item)
                if path.isdir(d):
                    if self.debug:
                        print('Pasta encontrada')
                    self.find_in_folder(d)
                else:
                    if self.debug:
                        print('Arquivo Encontrado')
                    self.items.append(str(d))
            else:
                if len(self.items) == 0:
                    print('Não encontrados arquivos')
                    exit(3)
                    
        except PermissionError:
            if self.debug:
                print('Permissão Negada à Pasta')
            exit(1)
        except Exception as e:
            if self.debug:
                print('Erro não tratado list_sub_dir: '+str(e))
            exit(2)
        finally:
            return self.items
